# Building the Chatbot EXE

This guide explains how to create the `app.exe` executable from the Python application.

## Method 1: Automatic Build (Recommended)

Simply run the build script:

```bash
python build.py
```

This will:
1. Install all required dependencies
2. Build the executable automatically
3. Create `dist/chatbot.exe`

You can then run it directly by double-clicking `dist/chatbot.exe`.

## Method 2: Manual Build with PyInstaller

If you prefer to do it manually:

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Create the Executable
```bash
pyinstaller --onefile --windowed --name=chatbot ^
    --add-data "index.html:." ^
    --add-data "style.css:." ^
    --add-data "script.js:." ^
    app.py
```

The executable will be created in the `dist/` folder.

## Running the Application

### From Development
```bash
python app.py
```

### From Compiled EXE
Simply double-click `dist/chatbot.exe` and the desktop application will launch automatically.

## What Happens When You Run the EXE?

1. The Flask server starts in the background
2. A desktop window opens automatically
3. The chatbot interface is displayed in the window
4. The application is fully functional and self-contained

## Troubleshooting

### "pywebview not installed" message
Run: `pip install pywebview`

### Application doesn't start
Make sure all files are in the same directory:
- `app.py`
- `chatbot.py`
- `faq_item.py`
- `index.html`
- `style.css`
- `script.js`

### Port 5000 already in use
Close other applications using port 5000, or modify the port number in `app.py`

## Optional: Add a Custom Icon

To add a custom icon to your executable:

1. Create or download a `.ico` file (e.g., `chatbot.ico`)
2. Place it in the same directory as `app.py`
3. The build script will automatically use it

Without an icon, the application will use the default Python icon.