# Disconnect / Connect the Simulator Bridge repeatedly (fast and slow) and check the app never freezes.
# The Apr 20 app froze once on Disconnect with the v1 box (18:37:33, 2 Nov). Offline only: never touches
# "Launch Machine Simulator".
param([int]$Cycles = 4)
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes
$AE = [System.Windows.Automation.AutomationElement]; $TS = [System.Windows.Automation.TreeScope]

function Get-Button([string]$id) {
    $p = Get-Process "Online - Display and CommandARM Simulator" -ErrorAction Stop | Select-Object -First 1
    $cond = New-Object System.Windows.Automation.PropertyCondition($AE::ProcessIdProperty, $p.Id)
    foreach ($w in $AE::RootElement.FindAll($TS::Children, $cond)) {
        foreach ($e in $w.FindAll($TS::Descendants, [System.Windows.Automation.Condition]::TrueCondition)) {
            if ($e.Current.AutomationId -eq $id) { return $e }
        }
    }
    $null
}
function Click([string]$id) {
    $b = Get-Button $id
    $pat = $b.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern); $pat.Invoke()
}
function Arm([string]$cmd) {
    $c = New-Object System.Net.Sockets.TcpClient("127.0.0.1", 47800); $s = $c.GetStream()
    $w = New-Object System.IO.StreamWriter($s); $w.NewLine = "`n"; $w.AutoFlush = $true; $r = New-Object System.IO.StreamReader($s)
    $w.WriteLine($cmd); $line = $r.ReadLine(); $c.Close(); $line
}
function Responding { (Get-Process "Online - Display and CommandARM Simulator" | Select-Object -First 1).Responding }
function Connected { (Arm "state") -match '"connected":true' }

$results = @()
foreach ($gap in @(3000, 1500, 500)) {
    for ($i = 1; $i -le $Cycles; $i++) {
        Click "BtnconnectSimBridge"; Start-Sleep -Milliseconds $gap        # disconnect
        $afterOff = @{ responding = Responding; connected = Connected }
        Click "BtnconnectSimBridge"; Start-Sleep -Milliseconds $gap        # connect
        $afterOn = @{ responding = Responding; connected = Connected }
        $ok = $afterOff.responding -and -not $afterOff.connected -and $afterOn.responding -and $afterOn.connected
        $results += [pscustomobject]@{ gapMs = $gap; cycle = $i; offResponding = $afterOff.responding; offLinkDown = -not $afterOff.connected;
                                       onResponding = $afterOn.responding; onLinkUp = $afterOn.connected; ok = $ok }
        if (-not ($afterOff.responding -and $afterOn.responding)) { break }
    }
}
$results | Format-Table -AutoSize | Out-String -Width 200
"final: app responding=$(Responding), armrest connected=$(Connected)"
"armrest state: " + (Arm "state")
