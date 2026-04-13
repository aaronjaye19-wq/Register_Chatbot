@echo off
REM =============================================================================
REM Registrar ML AI Chatbot - EXE Build Script
REM =============================================================================
REM This script automates the PyInstaller build process with all necessary
REM hidden imports for scikit-learn and scipy modules.
REM
REM Requirements:
REM   - Python 3.8+ installed
REM   - All dependencies from requirements.txt installed
REM   - PyInstaller installed
REM =============================================================================

echo.
echo ============================================================
echo  Registrar ML AI Chatbot - Building EXE
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Step 1: Checking dependencies...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo WARNING: PyInstaller not found. Installing...
    pip install PyInstaller==6.1.0
)

pip show scikit-learn >nul 2>&1
if errorlevel 1 (
    echo ERROR: scikit-learn not installed
    echo Run: pip install -r requirements.txt
    pause
    exit /b 1
)

echo Step 1: [DONE] Dependencies verified
echo.

echo Step 2: Cleaning previous builds...
if exist dist (
    rmdir /s /q dist
    echo Deleted dist folder
)
if exist build (
    rmdir /s /q build
    echo Deleted build folder
)
if exist RegistrarChatbot.spec (
    del /q RegistrarChatbot.spec
    echo Deleted old spec file
)

echo Step 2: [DONE] Previous builds cleaned
echo.

echo Step 3: Building EXE using RegistrarChatbot.spec...
echo This may take 2-5 minutes. Please wait...
echo.

REM Run PyInstaller with the spec file
pyinstaller RegistrarChatbot.spec

if errorlevel 1 (
    echo.
    echo ERROR: PyInstaller build failed!
    echo.
    echo Troubleshooting:
    echo 1. Make sure all dependencies are installed: pip install -r requirements.txt
    echo 2. Try the alternative build command:
    echo    pyinstaller --onefile --console --hidden-import=sklearn --hidden-import=scipy --hidden-import=numpy app.py
    echo 3. Check the error messages above
    echo.
    pause
    exit /b 1
)

echo.
echo Step 3: [DONE] EXE built successfully
echo.

echo Step 4: Verifying build...
if exist dist\RegistrarChatbot.exe (
    echo SUCCESS: RegistrarChatbot.exe created!
    echo.
    echo Location: %cd%\dist\RegistrarChatbot.exe
    echo File size: 
    for %%A in (dist\RegistrarChatbot.exe) do echo   %%~zA bytes
    echo.
) else (
    echo ERROR: RegistrarChatbot.exe not found in dist folder!
    pause
    exit /b 1
)

echo Step 4: [DONE] Build verified
echo.

echo ============================================================
echo BUILD COMPLETE!
echo ============================================================
echo.
echo Your executable is ready to use:
echo   Location: dist\RegistrarChatbot.exe
echo.
echo Next steps:
echo 1. Copy dist\RegistrarChatbot.exe to any location
echo 2. Double-click to run the chatbot
echo 3. The app will open in your default browser
echo.
echo To share with others:
echo   - Send only the RegistrarChatbot.exe file
echo   - No Python installation needed on their computer
echo.
echo Optional: Create a shortcut
echo   1. Right-click RegistrarChatbot.exe
echo   2. Select "Create shortcut"
echo   3. Place on Desktop
echo.
echo For troubleshooting, see BUILD_EXE_GUIDE.txt
echo.
pause
