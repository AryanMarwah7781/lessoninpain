-- Deere Vehicle Control (Lesson Studio spike, 3 Nov 2026). Throwaway: proves the game <-> Connections app loop.
--
-- The Connections app (Apr 20 build) talks to the game through two files in this mod's src folder:
--   src/VehicleInfo.xml  app -> game, rewritten every 80 ms: wheelAngle, wheelSpeed, hydroHandlePosition,
--                        nozzleOnOffStatus, boomUnfolded, boomHeight, cameraView, ladderRaised
--   src/gameToSim.xml    game -> app, read every 150 ms: <lat> <long> <speed> <heading>, all four required
--                        (SBMCommnHandler.cs:300-330); the app sends them to the cloud as GPS signals.
-- This script drives the sprayer you are sitting in from the first file and reports it in the second.
-- Every status line in the game log starts with "DVC:".

DeereVehicleControl = {}
local DVC = DeereVehicleControl

DVC.modDir = g_currentModDirectory
DVC.inPath = DVC.modDir .. "src/VehicleInfo.xml"
DVC.outPath = DVC.modDir .. "src/gameToSim.xml"
DVC.cfgPath = DVC.modDir .. "config.xml"

DVC.cfg = {
    lat0 = 41.6, lon0 = -93.6,
    neutral = 125, deadband = 6, fullForwardKmh = 20,
    fullLockDeg = 35, invertSteer = false,
    readMs = 100, writeMs = 150, logMs = 2000,
}
DVC.t = { read = 0, write = 0, log = 0 }
DVC.info = nil            -- last good read of VehicleInfo.xml
DVC.applied = {}          -- last values acted on (fold, spray, camera act on change only)
DVC.seen = {}             -- one-time log keys
DVC.targetKmh = 0
DVC.reads, DVC.badReads, DVC.writes = 0, 0, 0

local function log(fmt, ...)
    print(string.format("DVC: " .. fmt, ...))
end

local function once(key, fmt, ...)
    if not DVC.seen[key] then
        DVC.seen[key] = true
        log(fmt, ...)
    end
end

local function clamp(v, lo, hi) return math.max(lo, math.min(hi, v)) end

function DVC:loadConfig()
    if not fileExists(self.cfgPath) then return end
    local x = loadXMLFile("dvcCfg", self.cfgPath)
    if x == nil or x == 0 then return end
    local c = self.cfg
    c.lat0 = getXMLFloat(x, "config.origin#lat") or c.lat0
    c.lon0 = getXMLFloat(x, "config.origin#lon") or c.lon0
    c.neutral = getXMLFloat(x, "config.lever#neutral") or c.neutral
    c.deadband = getXMLFloat(x, "config.lever#deadband") or c.deadband
    c.fullForwardKmh = getXMLFloat(x, "config.lever#fullForwardKmh") or c.fullForwardKmh
    c.fullLockDeg = getXMLFloat(x, "config.steering#fullLockDeg") or c.fullLockDeg
    local inv = getXMLBool(x, "config.steering#invert")
    if inv ~= nil then c.invertSteer = inv end
    c.readMs = getXMLInt(x, "config.timing#readMs") or c.readMs
    c.writeMs = getXMLInt(x, "config.timing#writeMs") or c.writeMs
    c.logMs = getXMLInt(x, "config.timing#logMs") or c.logMs
    delete(x)
end

function DVC:loadMap(name)
    self:loadConfig()
    log("loaded on map %s. in=%s out=%s origin=%.6f,%.6f fullForward=%.0f km/h",
        tostring(name), self.inPath, self.outPath, self.cfg.lat0, self.cfg.lon0, self.cfg.fullForwardKmh)
end

function DVC:deleteMap()
    log("unloaded after %d reads (%d bad), %d writes", self.reads, self.badReads, self.writes)
end

-- ---------------------------------------------------------------- input: VehicleInfo.xml
local FIELDS = { "wheelAngle", "wheelSpeed", "hydroHandlePosition", "nozzleOnOffStatus",
                 "boomUnfolded", "boomHeight", "cameraView", "ladderRaised" }

function DVC:readVehicleInfo()
    if not fileExists(self.inPath) then
        once("noin", "waiting for %s (the app writes it once the bridge is connected)", self.inPath)
        return
    end
    local x = loadXMLFile("dvcIn", self.inPath)
    if x == nil or x == 0 then
        self.badReads = self.badReads + 1          -- the app rewrites the file every 80 ms; caught mid-write
        return
    end
    local s = {}
    for _, k in ipairs(FIELDS) do
        s[k] = getXMLFloat(x, "VehicleInfo." .. k)
    end
    delete(x)
    if s.hydroHandlePosition == nil then
        self.badReads = self.badReads + 1
        return
    end
    self.reads = self.reads + 1
    if self.info == nil then
        log("first VehicleInfo: lever=%s wheelAngle=%s wheelSpeed=%s boomUnfolded=%s nozzles=%s camera=%s",
            tostring(s.hydroHandlePosition), tostring(s.wheelAngle), tostring(s.wheelSpeed),
            tostring(s.boomUnfolded), tostring(s.nozzleOnOffStatus), tostring(s.cameraView))
    end
    self.info = s
end

-- ---------------------------------------------------------------- which vehicle
function DVC:getVehicle()
    if g_localPlayer ~= nil and g_localPlayer.getCurrentVehicle ~= nil then
        local v = g_localPlayer:getCurrentVehicle()
        if v ~= nil then return v, "entered (g_localPlayer)" end
    end
    if g_currentMission ~= nil and g_currentMission.controlledVehicle ~= nil then
        return g_currentMission.controlledVehicle, "entered (controlledVehicle)"
    end
    return nil, "on foot"
end

function DVC:probe(v)
    local names = { "setCruiseControlState", "setCruiseControlMaxSpeed", "getCruiseControlState", "setSteeringInput",
                    "setAccelerationPedalInput", "getIsUnfolded", "setFoldState", "getToggledFoldDirection",
                    "setIsTurnedOn", "getIsTurnedOn", "getCanBeTurnedOn", "setActiveCameraIndex", "getLastSpeed",
                    "getRootVehicle", "getIsMotorStarted", "startMotor" }
    local have, miss = {}, {}
    for _, n in ipairs(names) do
        if type(v[n]) == "function" then table.insert(have, n) else table.insert(miss, n) end
    end
    log("vehicle '%s' (%s). has: %s. missing: %s", tostring(v.getName and v:getName() or "?"),
        tostring(v.configFileName), table.concat(have, ","), table.concat(miss, ","))
    log("specs: drivable=%s foldable=%s sprayer=%s enterable=%s turnOn=%s",
        tostring(v.spec_drivable ~= nil), tostring(v.spec_foldable ~= nil), tostring(v.spec_sprayer ~= nil),
        tostring(v.spec_enterable ~= nil), tostring(v.spec_turnOnVehicle ~= nil))
end

-- ---------------------------------------------------------------- output to the vehicle
function DVC:applyDrive(v, s)
    local c = self.cfg
    local lever = s.hydroHandlePosition
    local target = 0
    if lever > c.neutral + c.deadband then
        target = (lever - c.neutral) / (250 - c.neutral) * c.fullForwardKmh
    elseif lever < c.neutral - c.deadband then
        once("reverse", "lever below neutral (%.0f): reverse is not in the spike, holding still", lever)
    end
    self.targetKmh = target
    if v.setCruiseControlState == nil or v.setCruiseControlMaxSpeed == nil then
        once("nocruise", "no cruise control functions on this vehicle; cannot drive it from the lever")
        return
    end
    local state = v.getCruiseControlState ~= nil and v:getCruiseControlState() or nil
    if target >= 1 then
        if v.getIsMotorStarted ~= nil and not v:getIsMotorStarted() and v.startMotor ~= nil then
            v:startMotor()
        end
        local cc = v.spec_drivable ~= nil and v.spec_drivable.cruiseControl or nil
        if cc == nil or math.abs((cc.speed or 0) - target) > 0.25 then
            v:setCruiseControlMaxSpeed(target, cc ~= nil and cc.speedReverse or nil)
        end
        if state ~= Drivable.CRUISECONTROL_STATE_ACTIVE then
            v:setCruiseControlState(Drivable.CRUISECONTROL_STATE_ACTIVE)
        end
    elseif state ~= nil and state ~= Drivable.CRUISECONTROL_STATE_OFF then
        v:setCruiseControlState(Drivable.CRUISECONTROL_STATE_OFF)
    end
end

function DVC:applySteering(v, s)
    if v.setSteeringInput == nil or s.wheelAngle == nil then return end
    local val = clamp(s.wheelAngle / self.cfg.fullLockDeg, -1, 1)
    if self.cfg.invertSteer then val = -val end
    -- Drivable clears its steering input after each update, so this is set every frame.
    v:setSteeringInput(val, true, InputDevice.CATEGORY.WHEEL)
end

function DVC:applyFold(v, s)
    local spec = v.spec_foldable
    if spec == nil or s.boomUnfolded == nil or v.getIsUnfolded == nil or v.setFoldState == nil then return end
    local want = s.boomUnfolded >= 0.5
    if self.applied.unfold == want then return end          -- act on changes only (and once at start)
    if (spec.foldMoveDirection or 0) ~= 0 then return end   -- still moving; try again next frame
    if v:getIsUnfolded() ~= want then
        local dir = spec.turnOnFoldDirection or -1
        if not want then dir = -dir end
        v:setFoldState(dir, false)
        log("boom %s (game file boomUnfolded=%d)", want and "unfolding" or "folding", s.boomUnfolded)
    end
    self.applied.unfold = want
end

function DVC:applySpray(v, s)
    if v.setIsTurnedOn == nil or v.getIsTurnedOn == nil or s.nozzleOnOffStatus == nil then return end
    local want = s.nozzleOnOffStatus >= 0.5
    if self.applied.spray == want then return end
    if v:getIsTurnedOn() ~= want then
        if want and v.getCanBeTurnedOn ~= nil and not v:getCanBeTurnedOn() then
            once("cantspray", "nozzles on, but the sprayer can't be turned on yet (boom folded or tank empty?)")
            return
        end
        v:setIsTurnedOn(want)
        log("sprayer %s", want and "on" or "off")
    end
    self.applied.spray = want
end

function DVC:applyCamera(v, s)
    if v.setActiveCameraIndex == nil or s.cameraView == nil then return end
    local idx = math.floor(s.cameraView + 0.5)
    if self.applied.camera == idx then return end
    local cams = v.spec_enterable ~= nil and v.spec_enterable.cameras or nil
    if cams ~= nil and cams[idx] ~= nil then
        v:setActiveCameraIndex(idx)
        log("camera %d", idx)
    end
    self.applied.camera = idx
end

-- ---------------------------------------------------------------- output to the app: gameToSim.xml
function DVC:writeGameToSim(v)
    local root = v.rootNode
    if root == nil then return end
    local c = self.cfg
    local x, _, z = getWorldTranslation(root)
    local dx, _, dz = localDirectionToWorld(root, 0, 0, 1)
    local heading = (math.deg(math.atan2(dx, -dz)) + 360) % 360        -- 0 = north (map top is -z)
    local kmh = v.getLastSpeed ~= nil and v:getLastSpeed() or 0
    if (v.movingDirection or 1) < 0 then kmh = -kmh end
    local lat = c.lat0 + (-z) / 111320
    local lon = c.lon0 + x / (111320 * math.cos(math.rad(c.lat0)))
    local h = createXMLFile("dvcOut", self.outPath, "gameToSim")
    if h == nil or h == 0 then
        once("noout", "cannot create %s", self.outPath)
        return
    end
    setXMLString(h, "gameToSim.lat", string.format("%.7f", lat))
    setXMLString(h, "gameToSim.long", string.format("%.7f", lon))
    setXMLString(h, "gameToSim.speed", string.format("%.2f", kmh))
    setXMLString(h, "gameToSim.heading", string.format("%.1f", heading))
    saveXMLFile(h)
    delete(h)
    self.writes = self.writes + 1
    self.out = { x = x, z = z, kmh = kmh, heading = heading }
end

-- ---------------------------------------------------------------- frame loop
function DVC:tick(dt)
    local t = self.t
    t.read, t.write, t.log = t.read + dt, t.write + dt, t.log + dt
    if t.read >= self.cfg.readMs then
        t.read = 0
        self:readVehicleInfo()
    end
    local v, how = self:getVehicle()
    if v ~= self.lastVehicle then
        self.lastVehicle = v
        self.applied = {}
        if v ~= nil then self:probe(v) else log("no vehicle entered (%s)", how) end
    end
    if v ~= nil and self.info ~= nil then
        self:applyDrive(v, self.info)
        self:applySteering(v, self.info)
        self:applyFold(v, self.info)
        self:applySpray(v, self.info)
        self:applyCamera(v, self.info)
    end
    if v ~= nil and t.write >= self.cfg.writeMs then
        t.write = 0
        self:writeGameToSim(v)
    end
    if t.log >= self.cfg.logMs then
        t.log = 0
        local s, o = self.info or {}, self.out or {}
        log("%s | lever=%s target=%.1f km/h speed=%.1f | wheel=%s | unfold=%s nozzles=%s cam=%s | pos=%.1f,%.1f hdg=%.0f | reads=%d bad=%d writes=%d",
            how, tostring(s.hydroHandlePosition), self.targetKmh, o.kmh or 0, tostring(s.wheelAngle),
            tostring(s.boomUnfolded), tostring(s.nozzleOnOffStatus), tostring(s.cameraView),
            o.x or 0, o.z or 0, o.heading or 0, self.reads, self.badReads, self.writes)
    end
end

function DVC:update(dt)
    local ok, err = pcall(self.tick, self, dt)
    if not ok then once("err:" .. tostring(err), "error (shown once): %s", tostring(err)) end
end

addModEventListener(DeereVehicleControl)
