# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Spec File for Registrar ML AI Chatbot
This spec file includes all necessary hidden imports for scikit-learn and scipy
to work properly when packaged as a standalone executable.

Usage:
  pyinstaller RegistrarChatbot.spec
"""

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('index.html', '.'),
        ('style.css', '.'),
        ('script.js', '.'),
    ],
    hiddenimports=[
        # NumPy and core dependencies
        'numpy',
        'numpy.core._multiarray_umath',
        
        # SciPy core modules
        'scipy',
        'scipy.sparse',
        'scipy.sparse._base',
        'scipy.sparse._sputils',
        'scipy._lib',
        'scipy._lib._util',
        'scipy._lib._array_api',
        'scipy._lib.array_api_compat',
        'scipy._lib.array_api_compat.numpy',
        'scipy._lib.array_api_compat.numpy.fft',
        'scipy._lib.array_api_compat.numpy.linalg',
        'scipy._lib.array_api_compat.numpy.random',
        'scipy._lib.array_api_compat.numpy.lib.stride_tricks',
        
        # scikit-learn core modules
        'sklearn',
        'sklearn.base',
        'sklearn.utils',
        'sklearn.utils._cython_blas',
        'sklearn.utils._typedefs',
        'sklearn.feature_extraction',
        'sklearn.feature_extraction.text',
        'sklearn.metrics',
        'sklearn.metrics.pairwise',
        'sklearn.preprocessing',
        'sklearn.linear_model',
        'sklearn.tree',
        'sklearn.ensemble',
        'sklearn.pipeline',
        
        # Flask and web modules
        'flask',
        'flask.json',
        'flask_cors',
        
        # Standard library modules
        'json',
        'logging',
        'sys',
        'os',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='RegistrarChatbot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to True to see console output for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
