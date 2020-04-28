@echo off

:: Weird time shit I forgot why it's like this but there's probably a good reason so lets just keep it this way nice mate
date /t > date.txt
set date=<date.txt
set date=%date:/=.%
del date.txt
time /t > time.txt
set time=<time.txt
set time=%time::=.%
del time.txt

:: Make the directory if it doesn't exist
mkdir "backups\%date% %time%"

:: actually backup the stuff
xcopy /q /e /i "worlds\world" "backups\%date% %time%\world\"
xcopy /q /e /i "log.txt" "backups\%date% %time%\log.txt"

echo.
echo %date% %time%: Backup Completed!
echo.