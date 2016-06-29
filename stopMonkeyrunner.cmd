@echo off
tasklist | find "java.exe" > C:\screenshot\java.txt
tasklist | find "cmd.exe" | find /v "hk" > C:\screenshot\cmd.txt

for /f "delims=" %%t in (C:\screenshot\java.txt) do set str=%%t
echo %str%

for /f " tokens=2 delims= " %%i in (C:\screenshot\java.txt) do set id=%%i
taskkill /f /pid %id%

for /f " tokens=2 delims= " %%i in (C:\screenshot\cmd.txt) do taskkill /f /pid %%i


DEL /F C:\screenshot\java.txt
DEL /F C:\screenshot\cmd.txt