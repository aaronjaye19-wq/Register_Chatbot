"""
Build script to create app.exe using PyInstaller
Run this script with: python build.py
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required packages"""
    packages = ['flask', 'flask-cors', 'pywebview', 'pyinstaller']
    print("Installing dependencies...")
    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    print("Dependencies installed!")

def build_exe():
    """Build the executable"""
    print("\nBuilding app.exe...")
    
    # PyInstaller command to create a single executable
    # On Windows, use semicolon (;) as separator for --add-data
    command = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--name=chatbot',
        '--icon=my_icon.ico',
        '--add-data=index.html;.',
        '--add-data=style.css;.',
        '--add-data=script.js;.',
        '--hidden-import=webview',
        'app.py'
    ]
    
    try:
        subprocess.check_call(command)
        print("\nBuild successful!")
        print(f"Executable location: {os.path.abspath('dist/chatbot.exe')}")
        print("\nYou can now run: dist\\chatbot.exe")
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    print("=" * 50)
    print("Registrar AI Chatbot - EXE Builder")
    print("=" * 50)
    
    # Install dependencies
    install_dependencies()
    
    # Build executable
    build_exe()
    
    print("\nYou can now run the chatbot with: dist/chatbot.exe")