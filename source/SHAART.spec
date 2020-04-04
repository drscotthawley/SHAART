# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

def get_librosa_path():
     import librosa
     librosa_path = librosa.__path__[0]
     print("librosa_path = ",librosa_path)
     return librosa_path

a = Analysis(['SHAART.py'],
             pathex=['/home/shawley/github/SHAART/source'],
             binaries=[],
             datas=[],
             hiddenimports=['librosa', 'scipy._lib.messagestream', 'sklearn.tree', 'sklearn.neighbors.typedefs', 'sklearn.neighbors.quad_tree', 'sklearn.tree._utils', 'sklearn.utils._cython_blas'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

dict_tree = Tree(get_librosa_path(), prefix='librosa', excludes=["*.pyc"])
a.datas += dict_tree
a.binaries = filter(lambda x: 'librosa' not in x[0], a.binaries)


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='SHAART',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
