# -*- mode: python -*-
block_cipher = None
a = Analysis(['start.py'],
         pathex=['c:\\Almacen\\Python\\Gis'],
         binaries=None,
         datas=[('C:/Program Files (x86)/QGIS 2.18/apps/qgis/plugins/*.dll','qgis_plugins')],
         hiddenimports=['PyQt4.QtSql','PyQt4.QtNetwork','PyQt4.QtXml','PyQt4.Qsci'],
         hookspath=None,
         runtime_hooks=None,
         excludes=None,
         win_no_prefer_redirects=None,
         win_private_assemblies=None,
         cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='gttGIS',
      debug=False,
      strip=None,
      upx=True,
      console=False)