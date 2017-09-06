# -*- coding: utf-8 -*-

from qgis.gui import *
from qgis.core import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys, os

# app.setPrefixPath("C:\Program Files\QGIS 2.18\apps\qgis")

class myWnd(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX_PATH'], True)
        QgsApplication.initQgis()






        self.canvas = QgsMapCanvas()

        self.canvas.setCanvasColor(Qt.white)
        self.lyr = QgsVectorLayer(r"D:\ahlopez\Escritorio\Control de expedientes\BF CONTROL\EXP\27900A03400053.DXF|layername=entities|geometrytype=Line", "Mississippi", "ogr", True)

        print "nombre:" + self.lyr.name()
        print self.lyr.isValid()
        QgsMapLayerRegistry.instance().addMapLayer(self.lyr)

        self.canvas.setExtent(self.lyr.extent())

        self.canvas.setLayerSet([QgsMapCanvasLayer(self.lyr)])

        self.setCentralWidget(self.canvas)

        actionZoomIn = QAction('Zoom in', self)

        actionZoomOut = QAction('Zoom out', self)

        actionPan = QAction('Pan', self)

        actionZoomIn.setCheckable(True)

        actionZoomOut.setCheckable(True)

        actionPan.setCheckable(True)

        actionZoomIn.triggered.connect(self.zoomIn)

        actionZoomOut.triggered.connect(self.zoomOut)

        actionPan.triggered.connect(self.pan)

        self.toolbar = self.addToolBar('Canvas actions')

        self.toolbar.addAction(actionZoomIn)

        self.toolbar.addAction(actionZoomOut)

        self.toolbar.addAction(actionPan)

        self.toolPan = QgsMapToolPan(self.canvas)

        self.toolPan.setAction(actionPan)

        self.toolZoomIn = QgsMapToolZoom(self.canvas, False)  # false = in

        self.toolZoomIn.setAction(actionZoomIn)

        self.toolZoomOut = QgsMapToolZoom(self.canvas, True)  # true = out

        self.toolZoomOut.setAction(actionZoomOut)

        self.pan()

        print QgsMapLayerRegistry.instance().mapLayers()


    def zoomIn(self):

        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self):

        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):

        self.canvas.setMapTool(self.toolPan)

class MainApp(QApplication):

    def __init__(self):

        QApplication.__init__(self,[],True)

        wdg = myWnd()

        wdg.show()

        self.exec_()

if __name__ == '__main__':

    import sys

    app = MainApp()