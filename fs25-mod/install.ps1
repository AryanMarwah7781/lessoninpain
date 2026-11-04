# Deploy the Deere Vehicle Control spike into FS25 and (optionally) give savegame 1 a Patriot.
#   powershell -ExecutionPolicy Bypass -File install.ps1             copy the mod files only
#   powershell -ExecutionPolicy Bypass -File install.ps1 -PatchSave  also add the mod + a Patriot 4450 to savegame 1
# The game must be closed for -PatchSave (it rewrites the savegame when it saves).
# The app's own files in mods\DeereVehicleControl\src (VehicleInfo.xml, gameToSim.xml) are never touched.
param([switch]$PatchSave, [int]$Savegame = 1)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$src = Join-Path $here "DeereVehicleControl"
$profileDir = Join-Path $env:USERPROFILE "Documents\My Games\FarmingSimulator2025"
$dst = Join-Path $profileDir "mods\DeereVehicleControl"

New-Item -ItemType Directory -Force (Join-Path $dst "scripts"), (Join-Path $dst "src") | Out-Null
foreach ($f in "modDesc.xml", "icon.dds", "config.xml", "scripts\DeereVehicleControl.lua") {
    Copy-Item (Join-Path $src $f) (Join-Path $dst $f) -Force
}
"mod copied to $dst"

if (-not $PatchSave) { return }
if (Get-Process FarmingSimulator2025* -ErrorAction SilentlyContinue) { throw "close Farming Simulator first: it overwrites the savegame when it saves" }

$sg = Join-Path $profileDir "savegame$Savegame"
$backup = Join-Path $here ("backups\savegame$Savegame-" + (Get-Date -Format "yyyyMMdd-HHmmss"))
New-Item -ItemType Directory -Force $backup | Out-Null
Copy-Item (Join-Path $sg "*") $backup -Recurse -Force
"savegame backed up to $backup"

$settings = New-Object System.Xml.XmlWriterSettings
$settings.Encoding = New-Object System.Text.UTF8Encoding($false)
$settings.Indent = $true
function Save-Xml($doc, $path) { $w = [System.Xml.XmlWriter]::Create($path, $settings); $doc.Save($w); $w.Close() }

# 1. the savegame loads the mod
$careerPath = Join-Path $sg "careerSavegame.xml"
$career = New-Object System.Xml.XmlDocument; $career.Load($careerPath)
if (-not $career.SelectSingleNode("//mod[@modName='DeereVehicleControl']")) {
    $m = $career.CreateElement("mod")
    foreach ($kv in @(@("modName", "DeereVehicleControl"), @("title", "Deere Vehicle Control (spike)"), @("version", "0.1.0.0"), @("required", "false"), @("fileHash", ""))) { $m.SetAttribute($kv[0], $kv[1]) }
    $last = $career.SelectNodes("//mod") | Select-Object -Last 1
    [void]$last.ParentNode.InsertAfter($m, $last)
    Save-Xml $career $careerPath
    "mod added to careerSavegame.xml"
} else { "mod already in careerSavegame.xml" }

# 2. a Patriot 4450 on flat ground south-east of the HelloMap farm (terrain 37.88 m there), facing north
$vehPath = Join-Path $sg "vehicles.xml"
$veh = New-Object System.Xml.XmlDocument; $veh.Load($vehPath)
$file = "data/vehicles/caseIH/patriot50/patriot50.xml"
if (-not $veh.SelectSingleNode("//vehicle[@filename='$file']")) {
    $v = $veh.CreateElement("vehicle")
    $id = "vehicle" + ([guid]::NewGuid().ToString("N"))
    foreach ($kv in @(@("filename", $file), @("uniqueId", $id), @("age", "0.000000"), @("price", "0.000000"), @("farmId", "1"), @("propertyState", "OWNED"), @("operatingTime", "0.000000"))) { $v.SetAttribute($kv[0], $kv[1]) }
    $c = $veh.CreateElement("component")
    $c.SetAttribute("index", "1"); $c.SetAttribute("position", "20.000 38.300 40.000"); $c.SetAttribute("rotation", "0.00 180.00 0.00")
    [void]$v.AppendChild($c)
    [void]$veh.DocumentElement.AppendChild($v)
    Save-Xml $veh $vehPath
    "Patriot 4450 added to vehicles.xml ($id)"
} else { "a Patriot is already in vehicles.xml" }
