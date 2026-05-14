# -*- mode: python ; coding: utf-8 -*-
import os

# --- AUTOMATIC BINARY COLLECTOR ---
def collect_interpreter_binaries():
    binaries = []
    # Directories to scan for .pyd files
    folders_to_scan = ['.', 'ictl_builtins', 'handlers'] 
    
    for folder in folders_to_scan:
        for root, dirs, files in os.walk(folder):
            # Skip build/dist folders
            if 'build' in root or 'dist' in root:
                continue
            for f in files:
                if f.endswith('.pyd'):
                    source_path = os.path.join(root, f)
                    # Destination is the relative path (e.g., 'handlers')
                    dest_dir = os.path.relpath(root, '.')
                    binaries.append((source_path, dest_dir))
    return binaries

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=collect_interpreter_binaries(), # <--- MAGIC HAPPENS HERE
    datas=[],
    hiddenimports=[
        'app', # Ensure app.py is included since it's not cythonized
        'ictl_builtins',
        'handlers'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[], # Keep app.py included as source as requested
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Basic ICTL v1.2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ictl_icon.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Basic ICTL v1.2',
)
