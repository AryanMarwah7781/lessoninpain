<#
Lesson Studio setup: README steps 1-4 in one go. Safe to run again; what is already done is only checked.

  Setup.cmd                          the rig: real armrest box
  Setup.cmd -Armrest virtual         practising without hardware (virtual armrest)
  Setup.cmd -AppFolder "D:\x\net8.0-windows"   if the Connections app is somewhere unusual
  Setup.cmd -SkipMods                don't offer to install the Farming Simulator mods
  Setup.cmd -NoShortcut              don't put a Lesson Studio shortcut on the desktop

Windows PowerShell 5.1 compatible, ASCII only. Never signs in to anything.
#>
param(
    [ValidateSet('real', 'virtual')][string]$Armrest = 'real',
    [string]$AppFolder = '',
    [switch]$SkipMods,
    [switch]$NoShortcut
)

$RepoUrl = 'https://github.com/AryanMarwah7781/lessoninpain.git'
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Docs = [Environment]::GetFolderPath('MyDocuments')
$todo = New-Object System.Collections.Generic.List[string]

function Step($n, $text) { Write-Host ''; Write-Host "[$n/5] $text" -ForegroundColor Green }
function Ok($text) { Write-Host "    ok    $text" }
function Info($text) { Write-Host "          $text" -ForegroundColor Gray }
function Todo($text) { Write-Host "    TODO  $text" -ForegroundColor Yellow; $script:todo.Add($text) }
function Refresh-Path {
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
}

# A Python 3.10+ to run the API with, as an array: the exe plus any arguments (py launcher needs -3).
function Find-Python {
    $cands = @(
        ,@("$env:LOCALAPPDATA\Programs\Python\Python312\python.exe")
        ,@('py', '-3')
        ,@('python')
    )
    foreach ($c in $cands) {
        $exe = $c[0]
        if (-not ((Test-Path $exe) -or (Get-Command $exe -ErrorAction SilentlyContinue))) { continue }
        $rest = @(); if ($c.Count -gt 1) { $rest = $c[1..($c.Count - 1)] }
        try {
            $v = & $exe @rest -c "import sys; print('%d.%d' % sys.version_info[:2])" 2>$null
            if ($LASTEXITCODE -eq 0 -and $v -and [version]$v -ge [version]'3.10') { return ,$c }
        } catch { }
    }
    return $null
}

function Test-DesktopRuntime {
    $roots = @("$env:ProgramFiles\dotnet\shared\Microsoft.WindowsDesktop.App", "${env:ProgramFiles(x86)}\dotnet\shared\Microsoft.WindowsDesktop.App")
    foreach ($r in $roots) { if (Test-Path $r) { if (Get-ChildItem $r -Directory -Filter '8.*' -ErrorAction SilentlyContinue) { return $true } } }
    return $false
}

$haveWinget = [bool](Get-Command winget -ErrorAction SilentlyContinue)
function Ensure-Tool($name, [scriptblock]$test, $wingetId) {
    if (& $test) { Ok $name; return }
    if (-not $haveWinget) { Todo "$name is missing and winget isn't available: install it by hand"; return }
    Info "installing $name with winget (Windows may ask for permission) ..."
    winget install --id $wingetId -e --accept-source-agreements --accept-package-agreements | Out-Host
    Refresh-Path
    if (& $test) { Ok "$name (installed)" } else { Todo "$name didn't finish installing: open a new window and run Setup again" }
}

Write-Host 'Lesson Studio setup' -ForegroundColor Cyan
Refresh-Path    # see tools installed since this window opened

# ---------------------------------------------------------------------------------------------- 1. tools
Step 1 'Tools: Git, Python, .NET 8 Desktop Runtime'
Ensure-Tool 'Git' { [bool](Get-Command git -ErrorAction SilentlyContinue) } 'Git.Git'
Ensure-Tool 'Python 3.12' { [bool](Find-Python) } 'Python.Python.3.12'
Ensure-Tool '.NET 8 Desktop Runtime' { Test-DesktopRuntime } 'Microsoft.DotNet.DesktopRuntime.8'

# ---------------------------------------------------------------------------------------------- 2. the files
Step 2 'Lesson Studio files'
$Studio = $null
if (Test-Path (Join-Path $Here '.git')) { $Studio = $Here }
else {
    $target = Join-Path $Docs 'lesson-studio'
    if (Test-Path (Join-Path $target '.git')) { $Studio = $target }
    elseif (Get-Command git -ErrorAction SilentlyContinue) {
        Info "cloning into $target (GitHub may ask you to sign in) ..."
        git clone $RepoUrl $target | Out-Host
        if (Test-Path (Join-Path $target '.git')) { $Studio = $target }
    }
}
if (-not $Studio) { Todo "Couldn't get the Lesson Studio files: git clone $RepoUrl" }
else {
    if (Get-Command git -ErrorAction SilentlyContinue) {
        $before = git -C $Studio rev-parse --short HEAD 2>$null
        git -C $Studio pull --ff-only 2>&1 | Out-Null
        $after = git -C $Studio rev-parse --short HEAD 2>$null
        if ($before -ne $after) { Ok "updated to $after ($Studio)" } else { Ok "up to date at $after ($Studio)" }
    } else { Ok $Studio }
}

# ---------------------------------------------------------------------------------------------- 3. Connections app
Step 3 'Connections app (Aug 26 build, SimulatorConnections.exe)'
$app = $null
if ($AppFolder) {
    foreach ($c in @($AppFolder, (Join-Path $AppFolder 'net8.0-windows'))) {
        if (Test-Path (Join-Path $c 'SimulatorConnections.exe')) { $app = $c; break }
    }
    if (-not $app) { Todo "No SimulatorConnections.exe in $AppFolder" }
}
if (-not $app) {
    # A rig can hold many builds (and run another one, e.g. the combine): the lessons are for the Aug 26 v4 612R
    # build, so prefer it, then a running Aug 26 copy, then the newest copy found.
    Info 'searching for the app ...'
    $roots = @((Join-Path $Docs 'jd_resources'), $Docs, "$env:USERPROFILE\Desktop", "$env:USERPROFILE\Downloads", 'C:\Simulator', 'C:\JD', 'D:\') | Where-Object { Test-Path $_ }
    $found = @()
    foreach ($r in $roots) { $found += @(Get-ChildItem $r -Recurse -Depth 4 -Filter 'SimulatorConnections.exe' -ErrorAction SilentlyContinue) }
    $v4 = $found | Where-Object { $_.FullName -match 'Aug26_Sprayer612R_TestBuild_v4' } | Select-Object -First 1
    $p = Get-Process SimulatorConnections -ErrorAction SilentlyContinue | Where-Object { $_.Path -match 'Aug26' } | Select-Object -First 1
    if ($v4) { $app = $v4.DirectoryName }
    elseif ($p -and $p.Path) { $app = Split-Path -Parent $p.Path; Info 'found the running copy' }
    elseif ($found) { $app = ($found | Sort-Object LastWriteTime -Descending | Select-Object -First 1).DirectoryName; Info 'no Aug 26 v4 build found: using the newest copy' }
}
if (-not $app) {
    $zip = @((Join-Path $Docs 'jd_resources'), $Docs, "$env:USERPROFILE\Downloads", "$env:USERPROFILE\Desktop") | Where-Object { Test-Path $_ } |
        ForEach-Object { Get-ChildItem $_ -Filter 'Aug26_Sprayer612R_TestBuild*.zip' -ErrorAction SilentlyContinue } | Select-Object -First 1
    if ($zip) {
        $dest = Join-Path (Join-Path $Docs 'jd_resources') $zip.BaseName
        Info "extracting $($zip.Name) to $dest ..."
        Expand-Archive -Path $zip.FullName -DestinationPath $dest -Force
        $hit = Get-ChildItem $dest -Recurse -Filter 'SimulatorConnections.exe' -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($hit) { $app = $hit.DirectoryName }
    }
}
if (-not $app) { Todo 'Connections app not found: copy the Aug 26 build (Aug26_Sprayer612R_TestBuild_v4.zip) to Documents\jd_resources and run Setup again, or use -AppFolder' }
else {
    Ok $app
    $py = Find-Python
    if ($py -and $Studio) {
        $exe = $py[0]; $rest = @(); if ($py.Count -gt 1) { $rest = $py[1..($py.Count - 1)] }
        if ($Armrest -eq 'real') { Stop-Process -Name SBMEmulator -ErrorAction SilentlyContinue }
        $out = & $exe @rest -I (Join-Path $Studio 'tools\armrest_mode.py') $Armrest $app 2>&1
        if ($LASTEXITCODE -eq 0) { Ok ("armrest: " + ($out | Select-String 'armrest:' | ForEach-Object { $_.Line.Trim() -replace '^armrest:\s*', '' })) }
        else { Todo "Couldn't set the armrest: $out" }
        # the 612R lessons in the app's own Operations panel (the app's page is kept as OperatingProcedure.orig.html)
        $out = & $exe @rest -I (Join-Path $Studio 'tools\operations_panel.py') install $app 2>&1
        if ($LASTEXITCODE -eq 0) { Ok 'Operations panel: the 612R lessons (live while Lesson Studio runs)' }
        else { Todo "Couldn't put the lessons in the Operations panel: $out" }
        if ($Armrest -eq 'virtual' -and -not (Get-Process SBMEmulator -ErrorAction SilentlyContinue)) {
            $emu = Join-Path $Studio 'virtual-commandarm\SBMEmulator.exe'
            Start-Process -FilePath $emu -WorkingDirectory (Split-Path $emu); Ok 'virtual armrest started'
        }
        if (Get-Process SimulatorConnections -ErrorAction SilentlyContinue) { Todo 'Restart the Connections app so it picks up the armrest setting' }
    }
}

# ---------------------------------------------------------------------------------------------- 4. Farming Simulator 22
Step 4 'Farming Simulator 22'
$fsDefault = "${env:ProgramFiles(x86)}\Farming Simulator 2022\FarmingSimulator2022.exe"
$fs = $null
if (Test-Path $fsDefault) { $fs = $fsDefault }
else {
    $libs = @("${env:ProgramFiles(x86)}\Steam")
    $vdf = "${env:ProgramFiles(x86)}\Steam\steamapps\libraryfolders.vdf"
    if (Test-Path $vdf) { Select-String -Path $vdf -Pattern '"path"\s+"([^"]+)"' | ForEach-Object { $libs += ($_.Matches[0].Groups[1].Value -replace '\\\\', '\') } }
    foreach ($l in $libs) {
        $c = Join-Path $l 'steamapps\common\Farming Simulator 22\FarmingSimulator2022.exe'
        if (Test-Path $c) { $fs = $c; break }
    }
}
if (-not $fs) { Todo 'Farming Simulator 22 not found: install it (standard edition is enough)' }
elseif ($fs -eq $fsDefault) { Ok "$fs (where the app looks by default)" }
else {
    Set-Clipboard -Value $fs
    Ok $fs
    Todo "In the Connections app: Settings > 'Path to where Farming Simulator is installed' > paste (the path is on the clipboard)"
}

$fsData = Join-Path $Docs 'My Games\FarmingSimulator2022'
if ($fs -and -not (Test-Path (Join-Path $fsData 'game.xml'))) { Todo 'Start Farming Simulator 22 once on its own (product key, first-run screens), then quit' }
elseif ($fs) { Ok 'first run done' }

# the LTTS sprayer mods + savegame, exactly as the app's own installer copies them
$src = $null
if ($app) { $src = Join-Path $app 'UI\FarmingSim\ModFiles\Sprayer' }
if (-not $SkipMods -and $src -and (Test-Path (Join-Path $src 'savegame1\careerSavegame.xml'))) {
    [xml]$sg = Get-Content (Join-Path $src 'savegame1\careerSavegame.xml')
    $mods = Join-Path $fsData 'mods'
    $need = @()
    foreach ($m in $sg.careerSavegame.mod) {
        $have = $null
        $f = Join-Path $mods $m.modName; $z = Join-Path $mods ($m.modName + '.zip')
        if (Test-Path (Join-Path $f 'modDesc.xml')) { $have = ([xml](Get-Content (Join-Path $f 'modDesc.xml'))).modDesc.version }
        elseif (Test-Path $z) {
            Add-Type -AssemblyName System.IO.Compression.FileSystem
            $zf = [IO.Compression.ZipFile]::OpenRead($z)
            try { $e = $zf.GetEntry('modDesc.xml'); $r = New-Object IO.StreamReader($e.Open()); $have = ([xml]$r.ReadToEnd()).modDesc.version; $r.Close() } finally { $zf.Dispose() }
        }
        if ("$have".Trim() -ne "$($m.version)".Trim()) { $need += $m.modName }
    }
    $sgInstalled = Join-Path $fsData 'savegame1\careerSavegame.xml'
    $sgSame = (Test-Path $sgInstalled) -and ((Get-Content $sgInstalled -Raw) -match 'DeereSprayerMapLF02')
    if ($need.Count -eq 0 -and $sgSame) { Ok 'LTTS sprayer mods and savegame installed and up to date' }
    else {
        Info ('to install: ' + (($need + $(if (-not $sgSame) { 'savegame1' } else { @() })) -join ', '))
        $ans = Read-Host '    Install the LTTS sprayer mods now? Savegame slot 1 is backed up first, then replaced [Y/n]'
        if ($ans -eq '' -or $ans -match '^[Yy]') {
            New-Item -ItemType Directory -Force $mods | Out-Null
            foreach ($n in $need) {
                $f = Join-Path $mods $n; $z = Join-Path $mods ($n + '.zip')
                if (Test-Path $f) { Remove-Item $f -Recurse -Force }
                if (Test-Path $z) { Remove-Item $z -Force }
                if (Test-Path (Join-Path $src $n)) { Copy-Item (Join-Path $src $n) $f -Recurse }
                elseif (Test-Path (Join-Path $src ($n + '.zip'))) { Copy-Item (Join-Path $src ($n + '.zip')) $z }
            }
            if (-not $sgSame) {
                $sgDir = Join-Path $fsData 'savegame1'
                if (Test-Path $sgDir) {
                    $bak = "$sgDir.backup-" + (Get-Date -Format 'yyyyMMdd-HHmmss')
                    Move-Item $sgDir $bak; Info "your old savegame 1 is in $bak"
                }
                Copy-Item (Join-Path $src 'savegame1') $sgDir -Recurse
            }
            Ok 'LTTS sprayer mods and savegame installed'
        } else { Info 'skipped: the app offers the same when you press Launch Farming Simulator' }
    }
}

# ---------------------------------------------------------------------------------------------- 5. shortcut + check
Step 5 'Shortcut and a quick check'
if ($Studio -and -not $NoShortcut) {
    $lnk = Join-Path ([Environment]::GetFolderPath('Desktop')) 'Lesson Studio.lnk'
    $ws = New-Object -ComObject WScript.Shell
    $s = $ws.CreateShortcut($lnk)
    $s.TargetPath = Join-Path $Studio 'Start Lesson Studio.cmd'
    $s.WorkingDirectory = $Studio
    $ico = Join-Path $Studio 'dist\LessonStudio\LessonStudio.exe'
    if (Test-Path $ico) { $s.IconLocation = "$ico,0" }
    $s.Save()
    Ok "desktop shortcut: $lnk"
}
$py = Find-Python
if ($Studio -and $py) {
    $exe = $py[0]; $rest = @(); if ($py.Count -gt 1) { $rest = $py[1..($py.Count - 1)] }
    $started = $null
    try { $h = Invoke-RestMethod http://127.0.0.1:47900/api/health -TimeoutSec 2 } catch { $h = $null }
    if (-not $h) {
        $argList = @($rest) + @('-I', (Join-Path $Studio 'run_simapi.py'), '--build', 'aug26')
        $started = Start-Process -FilePath $exe -ArgumentList $argList -WorkingDirectory $Studio -WindowStyle Hidden -PassThru
        for ($i = 0; $i -lt 20 -and -not $h; $i++) { Start-Sleep -Milliseconds 500; try { $h = Invoke-RestMethod http://127.0.0.1:47900/api/health -TimeoutSec 2 } catch { } }
    }
    if ($h) { Ok ("simulator API starts (build: " + $h.build + ")") } else { Todo 'The simulator API did not start: run Start Lesson Studio.cmd and read its window' }
    if ($started) { Stop-Process -Id $started.Id -ErrorAction SilentlyContinue }
    if (-not (Test-Path (Join-Path $Studio 'dist\LessonStudio\LessonStudio.exe'))) { Todo 'dist\LessonStudio\LessonStudio.exe is missing: git pull' }
}

# ---------------------------------------------------------------------------------------------- summary
Write-Host ''
if ($todo.Count -eq 0) { Write-Host 'All set.' -ForegroundColor Cyan }
else {
    Write-Host 'Still to do:' -ForegroundColor Yellow
    $i = 1; foreach ($t in $todo) { Write-Host "  $i. $t" -ForegroundColor Yellow; $i++ }
}
Write-Host ''
Write-Host 'Every session (README section 5):' -ForegroundColor Cyan
Write-Host '  1. Connections app: sign in; Settings > VNC Streaming Mode: Physical Display (rig displays wired) or HTML.'
Write-Host '  2. Sprayer Operator Experience > Desktop.'
if ($Armrest -eq 'real') { Write-Host '  3. Tick Message Replay Logger, THEN Connect Simulator Bridge.' }
else { Write-Host '  3. Connect Simulator Bridge (the virtual armrest window shows connected).' }
Write-Host '  4. Launch Machine Simulator, then Launch Farming Simulator.'
Write-Host '  5. Double-click Lesson Studio on the desktop; choose 612R or R4045, then a lesson.'
