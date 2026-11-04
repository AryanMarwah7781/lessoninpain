@echo off
rem Builds SBMEmulator.exe (the app looks for a process with exactly this name).
rem Uses the C# compiler that ships with Windows (.NET Framework 4); nothing to install.
cd /d "%~dp0"
"%WINDIR%\Microsoft.NET\Framework64\v4.0.30319\csc.exe" /nologo /codepage:65001 /target:winexe /out:SBMEmulator.exe ^
  /r:System.Windows.Forms.dll /r:System.Drawing.dll /r:System.Core.dll /r:System.Xml.dll /r:System.Web.Extensions.dll ^
  VirtualCommandArm.cs
