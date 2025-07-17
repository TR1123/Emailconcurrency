@echo off
setlocal enabledelayedexpansion


set "SCRIPT_NAME=Emailconcurrency.py"
set "OUTPUT_DIR=bin"
set "ICON_FILE=starry.sky.ico"


if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"


if exist "%ICON_FILE%" (
    set "ICON_OPTION=--icon "%ICON_FILE%""
) else (
    echo [WARNING] ico: %ICON_FILE%
    set "ICON_OPTION="
)


echo [INFO]  %SCRIPT_NAME%...
pyinstaller --onefile --distpath "%OUTPUT_DIR%" !ICON_OPTION! "%SCRIPT_NAME%"


if !errorlevel! neq 0 (
    echo [ERROR] 
    exit /b 1
)

echo [SUCCESS] 打包完成（保留控制台窗口）
echo 可执行文件路径: %CD%\%OUTPUT_DIR%\
endlocal
pause
