@echo off
setlocal enabledelayedexpansion

:: 基本配置
set "SCRIPT_NAME=Emailconcurrency.py"
set "OUTPUT_DIR=bin"
set "ICON_FILE=config\starry.sky.ico"

:: 确保输出目录存在
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

:: 图标参数处理
if exist "%ICON_FILE%" (
    set "ICON_OPTION=--icon "%ICON_FILE%""
) else (
    echo [WARNING] 图标文件不存在: %ICON_FILE%
    set "ICON_OPTION="
)

:: 关键修改：移除了 -w 参数以保留控制台
echo [INFO] 正在打包 %SCRIPT_NAME%...
pyinstaller --onefile --distpath "%OUTPUT_DIR%" !ICON_OPTION! "%SCRIPT_NAME%"

:: 结果检查
if !errorlevel! neq 0 (
    echo [ERROR] 打包失败
    exit /b 1
)

echo [SUCCESS] 打包完成（保留控制台窗口）
echo 可执行文件路径: %CD%\%OUTPUT_DIR%\
endlocal
pause