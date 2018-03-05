# -*- mode: python -*-

block_cipher = None


a = Analysis(['naver_blog.py'],
             pathex=['C:\\Users\\นฺวüมุ\\Desktop\\naver-today'],
             binaries=[],
             datas=[],
             hiddenimports=['bs4','selenium','time','requests','urllib','re'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='naver_blog',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='favi.ico')
