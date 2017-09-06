# -*- coding: utf-8 -*-

from qgis.gui import *
from qgis.core import *

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *



import sys
import os
import gttgis


# app.setPrefixPath(".")


class Principal(QtGui.QMainWindow, gttgis.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX_PATH'], True)
        QgsApplication.initQgis()
        self.canvas = QgsMapCanvas()
        self.layout.addWidget(self.canvas)
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.setDestinationCrs(QgsCoordinateReferenceSystem('25830'))
        self.canvas.setMapUnits(0)
        self.canvas.setObjectName("marco")
        self.jar = []
        self.CargaCapa("masa")
        self.CargaCapa("parcela")
        self.CargaCapa("constru")
        self.canvas.setLayerSet(self.jar)
        self.jar1.hide()
        self.jar2.hide()



    def CargaCapa(self, nombre):
        sql = ""
        uri = QgsDataSourceURI()
        uri.setConnection("9.56.3.159", "5432", "oliva", "postgres", "123456", QgsDataSourceURI.SSLdisable)
        uri.setDataSource("cartografia", nombre, "geom", sql, "gid")
        uri.setSrid("25830")
        vlayer = QgsVectorLayer(uri.uri(), nombre, "postgres")
        # label = QgsPalLayerSettings()
        # label.readFromLayer(vlayer)
        # label.enabled = True
        # label.fieldName = 'constru'
        # label.placement = QgsPalLayerSettings.AroundPoint
        # label.setDataDefinedProperty(QgsPalLayerSettings.Size, True, True, '8', '')
        # label.writeToLayer(vlayer)


        QgsMapLayerRegistry.instance().addMapLayer(vlayer)
        self.canvas.setExtent(vlayer.extent())
        self.jar.append(QgsMapCanvasLayer(vlayer))

    def actTitulo(self):
        self.statusBar.showMessage("Escala: 1:" + str(int(self.canvas.scale())))

    def showSeleccion(self):
        if self.c_seleccion.isChecked():
            self.jar1.show()
        else:
            self.jar1.hide()

    def showBusquedas(self):
        if self.c_Busquedas.isChecked():
            self.jar2.show()
        else:
            self.jar2.hide()

def main():
    app = QApplication(sys.argv)
    form = Principal()
    form.canvas.mapCanvasRefreshed.connect(form.actTitulo)
    form.c_seleccion.clicked.connect(form.showSeleccion)
    form.c_Busquedas.clicked.connect(form.showBusquedas)
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()
