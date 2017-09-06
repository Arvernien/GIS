# -*- encoding=utf-8 -*-
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# A setup script showing how to extend py2exe for QGISLite.
#
# In this case, the py2exe command is subclassed to create an installation
# script for InnoSetup, which can be compiled with the InnoSetup compiler
# to a single file windows installer.
#
# By default, the installer will be created as dist\Output\setup.exe.
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# 
# QGISLite - An Open Source GIS tool based on the QGIS core libraries
# and written in Python
# 
# Copyright (C) 2008  Aaron Racicot, Z-Pulley Inc.
# 
# EMAIL: aaronr (at) z-pulley.com
# WEB  : http://www.reprojected.com
# TRAC : http://trac.reprojected.com/qgislite
# SVN  : http://svn.reprojected.com/qgislite
# 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# 
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
#--------------------------------------------------------------------------

from distutils.core import setup
import py2exe
import os

# Build tree of files given a dir (for appending to py2exe data_files)
# Taken from http://osdir.com/ml/python.py2exe/2006-02/msg00085.html
def tree(src):
    list = [(root, map(lambda f: os.path.join(root, f), files)) for (root, dirs, files) in os.walk(os.path.normpath(src))]
    new_list = []
    for (root, files) in list:	
        if len(files) > 0 and root.count('.svn') == 0:
            new_list.append((root, files))
    return new_list 

################################################################
class InnoScript:
    def __init__(self,
                 name,
                 lib_dir,
                 dist_dir,
                 windows_exe_files = [],
                 lib_files = [],
                 version = "1.0"):
        self.lib_dir = lib_dir
        self.dist_dir = dist_dir
        if not self.dist_dir[-1] in "\\/":
            self.dist_dir += "\\"
        self.name = name
        self.version = version
        self.windows_exe_files = [self.chop(p) for p in windows_exe_files]
        self.lib_files = [self.chop(p) for p in lib_files]

    def chop(self, pathname):
        assert pathname.startswith(self.dist_dir)
        return pathname[len(self.dist_dir):]
    
    def create(self, pathname="dist\\gttsig.iss"):
        self.pathname = pathname
        ofi = self.file = open(pathname, "w")
        print >> ofi, "; WARNING: This script has been created by py2exe. Changes to this script"
        print >> ofi, "; will be overwritten the next time py2exe is run!"
        print >> ofi, r"[Setup]"
        print >> ofi, r"AppName=%s %s" % (self.name, self.version)
        print >> ofi, r"AppVerName=%s %s" % (self.name, self.version)
        print >> ofi, r"DefaultDirName={pf}\%s" % self.name
        print >> ofi, r"DefaultGroupName=%s" % self.name
        print >> ofi, r"VersionInfoVersion=%s" % self.version
        print >> ofi, r"VersionInfoCompany=GeoTux"
        print >> ofi, r"VersionInfoDescription=Visor Geogr�fico"
        print >> ofi, r"VersionInfoCopyright=GeoTux"
        print >> ofi, r"AppCopyright=Germ�n Carrillo - 2009"
        print >> ofi, r"AppSupportURL=http://geotux.tuxfamily.org"
        print >> ofi, r"OutputBaseFilename=Visor_Geografico_GeoTux_Installer"
        print >> ofi, r"LicenseFile=d:\trabajos\dllo\qgis_python\visor_instalador\licencia.txt"
        print >> ofi, r"WizardImageBackColor=clBlack"
        print >> ofi
        print >> ofi, r"[Languages]"
        print >> ofi, r'Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"'
        print >> ofi
        
        print >> ofi, r"[Tasks]"
        print >> ofi, r'Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"'
        print >> ofi, r'Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"'
        print >> ofi

        print >> ofi, r"[Files]"
        for path in self.windows_exe_files + self.lib_files:
            print >> ofi, r'Source: "%s"; DestDir: "{app}\%s"; Flags: ignoreversion' % (path, os.path.dirname(path))
        print >> ofi, r'Source: lib\gdal16.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi, r'Source: lib\QtSvg4.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi, r'Source: lib\proj.dll; DestDir: {app}\lib; Flags: ignoreversion'

        print >> ofi, r"[Icons]"
        print >> ofi, r'Name: "{group}\{cm:ProgramOnTheWeb,%s}"; Filename: "http://geotux.tuxfamily.org"' % \
              self.name
              
        for path in self.windows_exe_files:
            print >> ofi, r'Name: "{group}\%s"; Filename: "{app}\%s"; WorkingDir: {app}' % \
                  (self.name, path)
                  
        print >> ofi, 'Name: "{group}\Uninstall %s"; Filename: "{uninstallexe}"' % self.name
        print >> ofi, 'Name: "{commondesktop}\%s"; Filename: "{app}\%s"; Tasks: desktopicon; WorkingDir: "{app}"' % \
              (self.name, path)
        print >> ofi, 'Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\%s"; Filename: "{app}\%s"; Tasks: quicklaunchicon; WorkingDir: "{app}"' % \
              (self.name, path)
    def compile(self):
        try:
            import ctypes2
        except ImportError:
            try:
                import win32api
            except ImportError:
                import os
                os.startfile(self.pathname)
            else:
                print "Ok, using win32api."
                win32api.ShellExecute(0, "compile",
                                                self.pathname,
                                                None,
                                                None,
                                                0)
        else:
            print "Cool, you have ctypes installed."
            res = ctypes.windll.shell32.ShellExecuteA(0, "compile",
                                                      self.pathname,
                                                      None,
                                                      None,
                                                      0)
            if res < 32:
                raise RuntimeError, "ShellExecute failed, error %d" % res


################################################################

from py2exe.build_exe import py2exe

class build_installer(py2exe):
    # This class first builds the exe file(s), then creates a Windows installer.
    # You need InnoSetup for it.
    def run(self):
        # First, let py2exe do it's work.
        py2exe.run(self)

        lib_dir = self.lib_dir
        dist_dir = self.dist_dir
        
        # create the Installer, using the files py2exe has created.
        script = InnoScript("gttSIG",
                            lib_dir,
                            dist_dir,
                            self.windows_exe_files,
                            self.lib_files)
        print "*** creating the inno setup script***"
        script.create()
        print "*** compiling the inno setup script***"
        script.compile()
        # Note: By default the final setup.exe will be in an Output subdirectory.

######################## py2exe setup options ########################################

zipfile = r"lib\shardlib"

options = {
    "py2exe": {
        "compressed": 1,
        "optimize": 2,
        "includes": ['sip'],
        "excludes": ['backend_gtkagg', 'backend_wxagg', 'tcl', 'tcl.tcl8.4', 'Tkinter' ],
        "dll_excludes": ['libgdk_pixbuf-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk-win32-2.0-0.dll', 'phonon4.dll', 'MSVCR80.dll', 'QtScriptTools4.dll', 'tcl84.dll', 'tk84.dll' ],
        "packages": ["qgis", "PyQt4"],
        "dist_dir": "dist",
    }
}


data_files = tree('plugins') + tree('resources') + [ ( ".", [ "msvcp71.dll", "licencia.txt" ] ) ]

setup(
    options = options,
    # The lib directory contains everything except the executables and the python dll.
    zipfile = zipfile,
    windows=[{"script": "siggtt.py"}],
    # use out build_installer class as extended py2exe build command
    cmdclass = {"py2exe": build_installer},
    data_files = data_files
)
