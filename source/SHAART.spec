# -*- mode: python -*-

block_cipher = None


a = Analysis(['SHAART.py'],
             pathex=['/Users/shawley/github/SHAART/source'],
             binaries=[],
             datas=[],
             hiddenimports=['sklearn.utils._cython_blas', 'sklearn.neighbors.typedefs', 'sklearn.tree._utils', 'librosa', 'sklearn.neighbors.quad_tree', 'sklearn.tree', 'scipy._lib.messagestream'],
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
          name='SHAART',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='shaart_logo_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='SHAART')
app = BUNDLE(coll,
             name='SHAART.app',
             icon='shaart_logo_icon.ico',
             bundle_identifier=None)
