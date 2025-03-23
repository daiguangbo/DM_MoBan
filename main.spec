# -*- mode: python ; coding: utf-8 -*-

py_list = ['main.py','tools.py','source/DMClient.py','source/dm_tools.py']
list = [
    ('resource/img', 'resource/img'),
    ('resource/font', 'resource/font'),
    ('resource/mp3', 'resource/mp3')
]


a = Analysis(
    py_list,
    pathex=[],
    binaries=[],
    datas=list,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
