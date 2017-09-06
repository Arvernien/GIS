#!/usr/bin/python

from distutils.core import setup
import py2exe
import zipfile
import shutil
import matplotlib
import sys
import os
path_lib = 'D:\\Almacen\\Python\\GIS\\dist\Library'
path_js   = 'C:\\Program Files (x86)\\QGIS 2.18\\apps\\Python27\\Lib\\site-packages\\plotly\\package_data\\'
path_temp = 'c:\\temp\\extract'

sys.setrecursionlimit(10000)
setup(windows=[
{
"script": "start.py"
}
],
 data_files=matplotlib.get_py2exe_datafiles(), options={"py2exe": {"includes": ["PyQt4.QtSql", "PyQt4.QtNetwork", "PyQt4.QtXml", "PyQt4.Qsci", "PyQt4.QtWebKit", "plotly"],
"packages": ["plotly"]}})

with zipfile.ZipFile(path_lib + '.zip', 'r') as z: z.extractall(path_temp)

#ADD PLOTLY.MIN.JS TO EXTRACT
if not os.path.exists(path_temp + '\\plotly\\package_data'):
	os.mkdir(path_temp + '\\plotly\\package_data')

shutil.copyfile(path_js + 'plotly.min.js', path_temp + '\\plotly\\package_data\\plotly.min.js')
shutil.copyfile(path_js + 'default-schema.json', path_temp + '\\plotly\\package_data\\default-schema.json')
shutil.copyfile(path_js + 'graphWidget.js', path_temp + '\\plotly\\package_data\\graphWidget.js')

#REZIP FILE
shutil.make_archive(path_lib, 'zip', path_temp)

#KILL TEMP FILE
shutil.rmtree(path_temp, ignore_errors=True)