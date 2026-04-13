#!/usr/bin/env python
"""
Registrar Chatbot - Setup Validation Script

This script validates that your system is properly configured to build the
executable. Run this BEFORE attempting to build the .exe file.

Usage:
  python validate_setup.py

"""

import sys
import subprocess
import os

print("=" * 70)
print("Registrar ML AI Chatbot - Setup Validator")
print("=" * 70)
print()

# Check Python version
print("[1/6] Checking Python version...")
try:
    python_version = sys.version.split()[0]
    major, minor, patch = map(int, python_version.split('.'))
    if major >= 3 and minor >= 8:
        print(f"  ✓ Python {python_version} - OK")
    else:
        print(f"  ✗ Python {python_version} - OUTDATED (need 3.8+)")
        sys.exit(1)
except Exception as e:
    print(f"  ✗ Error checking Python: {e}")
    sys.exit(1)

# Check required packages
print()
print("[2/6] Checking required packages...")
required_packages = {
    'flask': 'Flask',
    'flask_cors': 'Flask-CORS',
    'sklearn': 'scikit-learn',
    'numpy': 'numpy',
    'scipy': 'scipy',
}

missing_packages = []
for import_name, display_name in required_packages.items():
    try:
        __import__(import_name)
        print(f"  ✓ {display_name}")
    except ImportError:
        print(f"  ✗ {display_name} - MISSING")
        missing_packages.append(display_name)

if missing_packages:
    print()
    print("MISSING PACKAGES!")
    print("Install them with:")
    print("  pip install -r requirements.txt")
    sys.exit(1)

# Check PyInstaller
print()
print("[3/6] Checking PyInstaller...")
try:
    import PyInstaller
    print(f"  ✓ PyInstaller {PyInstaller.__version__}")
except ImportError:
    print("  ✗ PyInstaller - NOT INSTALLED")
    print("Install with: pip install PyInstaller")
    sys.exit(1)

# Check required files
print()
print("[4/6] Checking project files...")
required_files = [
    'app.py',
    'chatbot.py',
    'faq_item.py',
    'index.html',
    'style.css',
    'script.js',
    'requirements.txt',
    'RegistrarChatbot.spec',
]

missing_files = []
for filename in required_files:
    if os.path.exists(filename):
        print(f"  ✓ {filename}")
    else:
        print(f"  ✗ {filename} - MISSING")
        missing_files.append(filename)

if missing_files:
    print()
    print(f"MISSING FILES: {', '.join(missing_files)}")
    print("Make sure you're in the correct project directory")
    sys.exit(1)

# Check if app.py runs without errors
print()
print("[5/6] Checking if chatbot module loads...")
try:
    from chatbot import RegistrarChatbot
    bot = RegistrarChatbot()
    bot.load_faq_data()
    print("  ✓ Chatbot module loads successfully")
except Exception as e:
    print(f"  ✗ Error loading chatbot: {e}")
    sys.exit(1)

# Check ML model training
print()
print("[6/6] Checking ML model training...")
try:
    # Test if ML model was trained
    if bot._ml_enabled:
        print("  ✓ ML model trained successfully")
        # Test a query
        response = bot.get_response("What are enrollment requirements?")
        print("  ✓ Test query successful")
    else:
        print("  ✗ ML model training failed")
        sys.exit(1)
except Exception as e:
    print(f"  ✗ Error testing ML model: {e}")
    sys.exit(1)

# All checks passed
print()
print("=" * 70)
print("VALIDATION SUCCESSFUL!")
print("=" * 70)
print()
print("Your system is properly configured. You can now build the executable:")
print()
print("  Option 1 (Automated): build_exe.bat")
print("  Option 2 (Manual):    pyinstaller RegistrarChatbot.spec")
print()
print("Next step: Run 'build_exe.bat' or 'pyinstaller RegistrarChatbot.spec'")
print()
