# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['MrPlayer.py'],
             pathex=['D:\\Github-Projects\\MrPlayer-project\\MrPlayer'],
             binaries=[],
             datas=[],
             hiddenimports=['sys'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='MrPlayer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='assets\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='MrPlayer')
