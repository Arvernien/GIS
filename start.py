# -*- coding: utf-8 -*-
# encoding: utf-8
import os
os.environ["GDAL_DATA"] = os.getcwd() + "\\gdal"
from qgis.gui import *
from qgis.core import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from math import sqrt, cos, sin, pi
from osgeo import gdal
import sys
import psycopg2
import gttgis
import valor
import criterio
import desconocido
import selector
import satelite
import colorlover as cl
import titular
import confirmacion
import plotly
import pythoncom
import osgeo.ogr
import wload
import vdesc
import inm
import contGraf
from threading import Thread
from win32com.client import Dispatch
from Queue import Queue
from plotly.graph_objs import Pie, Layout




global dbname

class ventanaDesconocidos(QWidget, vdesc.Ui_Form):
    def __init__(self, form, parent):
        super(ventanaDesconocidos, self).__init__(parent)
        self.setupUi(self)
        self.canvas = QgsMapCanvas()
        self.canvas.mapRenderer().setProjectionsEnabled(True)
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)
        self.canvas.mapRenderer().setDestinationCrs(QgsCoordinateReferenceSystem(25830), True, True)
        self.canvas.setMapUnits(0)
        self.canvas.setObjectName("mapa")
        self.marco.addWidget(self.canvas)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.parent = parent
        margenleft = (self.parent.width() / 2) - 550
        margentop = (self.parent.height() / 2) - 375
        self.setGeometry(QRect(margenleft, margentop, self.width(), self.height()))
        self.setGraphicsEffect(sombra())
        self.form = form
        self.minimizar.clicked.connect(self.minimiza)
        self.salir.clicked.connect(self.cierra)
        self.ldesc.setSpacing(2)
        self.lcand.setSpacing(3)
        self.CargaCapa()
        self.jar = []
        ly = QgsMapLayerRegistry.instance().mapLayersByName("Parcelas")[0]
        style = ly.getStyleFromDatabase("2", "parcela")
        self.fincas = QgsVectorLayer("MultiPolygon?crs=EPSG:25830", "fincas", "memory")
        QgsMapLayerRegistry.instance().addMapLayer(self.fincas)
        layer = QgsMapLayerRegistry.instance().mapLayersByName("fincas")[0]
        layer.applyNamedStyle(style)
        self.jar.append(QgsMapCanvasLayer(layer))
        ly = QgsMapLayerRegistry.instance().mapLayersByName("Construcciones")[0]
        style = ly.getStyleFromDatabase("5", "constru")
        self.constru = QgsVectorLayer("MultiPolygon?crs=EPSG:25830", "constru_desc", "memory")
        QgsMapLayerRegistry.instance().addMapLayer(self.constru)
        layer = QgsMapLayerRegistry.instance().mapLayersByName("constru_desc")[0]
        layer.applyNamedStyle(style)
        self.jar.append(QgsMapCanvasLayer(layer))
        ly = QgsMapLayerRegistry.instance().mapLayersByName("puntos_base")[0]
        style = ly.getStyleFromDatabase("11", "puntos_desc")
        self.puntos = QgsVectorLayer("MultiPoint?crs=EPSG:25830", "puntos_desc", "memory")
        QgsMapLayerRegistry.instance().addMapLayer(self.puntos)
        layer = QgsMapLayerRegistry.instance().mapLayersByName("puntos_desc")[0]
        layer.applyNamedStyle(style)
        self.jar.append(QgsMapCanvasLayer(layer))
        self.canvas.setLayerSet(self.jar)
        self.canvas.setExtent(self.fincas.extent())
        self.ldesc.itemSelectionChanged.connect(self.selecciona)
        self.lcand.itemSelectionChanged.connect(self.seleccand)
        self.lcand.itemDoubleClicked.connect(self.actCandidato)
        self.tfin.setText("")
        self.nfin.setText("")
        self.tcand.setText("")
        self.ncand.setText("")
        self.rubberBand = QgsRubberBand(self.canvas, False)
        self.rubberBand.setBorderColor(QColor(143, 212, 0, 255))
        self.rubberBand.setFillColor(QColor(143, 212, 0, 100))
        self.rubberBand.setWidth(1)
        self.rbContador = QgsRubberBand(self.canvas, False)
        self.rbContador.setBorderColor(QColor(148, 0, 211, 255))
        self.rbContador.setFillColor(QColor(148, 0, 211, 100))
        self.rbContador.setWidth(1)

    def actCandidato(self):
        sel = self.lcand.itemWidget(self.lcand.selectedItems()[0])
        dest = self.ldesc.itemWidget(self.ldesc.selectedItems()[0])
        ref = self.inmueble.text()
        nif = sel.getNif()
        nombre = sel.getTitular()
        ok = confirma("Actualizar titular", u"¿Utilizar " + unicode(nombre) + " con NIF " + nif + " como"
                                                                                                  u" titular candidato para este inmueble?",
                      u"Sí", "No", self)
        if ok.exec_() == QDialog.Accepted:
            psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
            psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
            conn = psycopg2.connect(
                "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
            cur = conn.cursor()
            sql = """UPDATE public.fin SET nif_candidato=%(nif)s, nombre_candidato=%(nombre)s WHERE ref_completa=%(ref)s;"""
            cur.execute(sql, {"ref": ref, "nif": nif, "nombre": nombre})
            conn.commit()
            cur.close()
            dest.candtit = nombre
            dest.candnif = nif
            self.ncand.setText(nif)
            self.tcand.setText(nombre)

    def CargaCapa(self):
        sql = ""
        uri = QgsDataSourceURI()
        uri.setConnection("9.56.3.159", "5432", dbname, "postgres", "123456", QgsDataSourceURI.SSLdisable)
        uri.setDataSource("cartografia", "puntos_desc", "geom", sql, "gid")
        uri.setSrid("25830")
        vlayer = QgsVectorLayer(uri.uri(), "puntos_base", "postgres")
        vlayer.setLayerName("puntos_base")
        QgsMapLayerRegistry.instance().addMapLayer(vlayer)

    def seleccand(self):
        if self.lcand.count() > 0:
            sel = self.lcand.itemWidget(self.lcand.selectedItems()[0])
            self.resaltaContador(sel.buffer())

    def selecciona(self):
        sel = self.ldesc.itemWidget(self.ldesc.selectedItems()[0])
        self.inmueble.setText(sel.inmueble)
        self.tfin.setText(sel.titular)
        self.nfin.setText(sel.nif)
        print sel.getCandNif(), sel.getCandTit()
        self.ncand.setText(sel.getCandNif())
        self.tcand.setText(sel.getCandTit())
        self.limpiaMapa()
        self.cargaFincas([sel.finca])
        self.cargaFincas(sel.getColindantes())
        self.canvas.setExtent(self.fincas.extent())
        self.fincas.removeSelection()
        self.constru.removeSelection()
        self.resalta(sel.finca)
        self.lcand.clear()
        if len(sel.getContadores()) > 0:
            contadores = sel.getContadores()
            ordcontadores = sorted(contadores, key=lambda contador: contador[7])
            for contador in ordcontadores:
                self.addContador(contador[0], QgsGeometry.fromWkt(contador[2]).centroid().exportToWkt())
                b = contadorGraf(contador)
                qlwi = QListWidgetItem()
                qlwi.setSizeHint(b.size())
                self.lcand.addItem(qlwi)
                self.lcand.setItemWidget(qlwi, b)
        for candidato in sel.getCandidato():
            self.addContador(candidato[0], QgsGeometry.fromWkt(candidato[2]).centroid().exportToWkt())
            b = contadorGraf(candidato)
            qlwi = QListWidgetItem()
            qlwi.setSizeHint(b.size())
            self.lcand.insertItem(0, qlwi)
            self.lcand.setItemWidget(qlwi, b)
        # c = self.ldesc.item(i)
        # if self.finnombre.text().upper() not in self.tabla.itemWidget(c).refcat()

    def addContador(self, gid, geom):
        self.puntos.startEditing()
        pr = self.puntos.dataProvider()
        pr.addAttributes([QgsField("gid", QVariant.Int)])
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromWkt(geom))
        feature.setAttributes([gid])
        self.puntos.addFeature(feature, True)
        self.puntos.commitChanges()

    def resalta(self, finca):
        self.rubberBand.reset(QGis.Polygon)
        for f in self.fincas.getFeatures():
            if f.attribute("refcat") == finca:
                g = f.geometry().exportToWkt()
                self.rubberBand.addGeometry(QgsGeometry.fromWkt(g), None)
                self.rubberBand.show()

    def resaltaContador(self, geom):
        self.rbContador.reset(QGis.Polygon)
        self.rbContador.addGeometry(QgsGeometry.fromWkt(geom), None)
        self.rbContador.show()

    def limpiaMapa(self):
        self.rbContador.reset(QGis.Polygon)
        self.rubberBand.reset(QGis.Polygon)
        self.fincas.startEditing()
        for feat in self.fincas.getFeatures():
            self.fincas.deleteFeature(feat.id())
        self.fincas.commitChanges()
        self.constru.startEditing()
        for feat in self.constru.getFeatures():
            self.constru.deleteFeature(feat.id())
        self.constru.commitChanges()
        self.puntos.startEditing()
        for feat in self.puntos.getFeatures():
            self.puntos.deleteFeature(feat.id())

    def cargaFincas(self, lfincas):
        conn = psycopg2.connect(
            "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
        cur = conn.cursor()
        for finca in lfincas:
            sql = "SELECT ST_AsText(geom) as geom, parcela FROM cartografia.parcela WHERE refcat=%(refcat)s;"
            cur.execute(sql, {"refcat": finca})
            geom = cur.fetchall()
            self.fincas.startEditing()
            features = []
            for g in geom:
                pr = self.fincas.dataProvider()
                pr.addAttributes([QgsField("parcela", QVariant.String), QgsField("refcat", QVariant.String)])
                feature = QgsFeature()
                feature.setGeometry(QgsGeometry.fromWkt(g[0]))
                feature.setAttributes([g[1], finca])
                features.append(feature)
            self.fincas.addFeatures(features, True)
            self.fincas.commitChanges()
            sql = "SELECT ST_AsText(geom) as geom, constru FROM cartografia.constru WHERE refcat=%(refcat)s;"
            cur.execute(sql, {"refcat": finca})
            geom = cur.fetchall()
            self.constru.startEditing()
            i = 0
            features = []
            for g in geom:
                i += 1
                pr = self.constru.dataProvider()
                pr.addAttributes([QgsField("constru", QVariant.String)])
                feature = QgsFeature()
                feature.setGeometry(QgsGeometry.fromWkt(g[0]))
                feature.setAttributes([g[1]])
                features.append(feature)
            self.constru.addFeatures(features, True)
            self.constru.commitChanges()


    def minimiza(self):
        self.hide()
        ventana(self, self.form.ventanas, "Contadores")

    def cierra(self):
        self.form.titWindowActive = False
        self.close()

    def paintEvent(self, event):
        margenleft = (self.parent.width() / 2) - 550
        margentop = (self.parent.height() / 2) - 375
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class openshp(QWidget, wload.Ui_Form):
    def __init__(self, form, parent):
        super(openshp, self).__init__(parent)
        self.setupUi(self)
        self.form = form
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry((parent.width() / 2) - 271, (parent.height() / 2) - 133, 542, 266)
        self.setGraphicsEffect(sombra())
        self.abrir.clicked.connect(self.loadShp)
        self.salir.clicked.connect(self.close)
        self.cargar.clicked.connect(self.carga)

    def carga(self):
        conn = psycopg2.connect(
            "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
        crsr = conn.cursor()
        try:
            sql = "DROP TABLE IF EXISTS cartografia.puntos_desc"
            crsr.execute(sql)
            conn.commit()
        except:
            pass
        sql = "CREATE TABLE cartografia.puntos_desc (" \
              "gid SERIAL PRIMARY KEY," \
              "geom Geometry(Point, 25830)," \
              "inmueble VARCHAR(20)," \
              "titular VARCHAR(80)," \
              "dni VARCHAR(20)" \
              ")"
        crsr.execute(sql)
        conn.commit()
        ctitular = str(self.titular.currentText())
        cdni = str(self.dni.currentText())
        cinmueble = str(self.inmueble.currentText())
        shp = osgeo.ogr.Open(self.ruta.text())
        lyr = shp.GetLayer(0)
        for i in range(lyr.GetFeatureCount()):
            feature = lyr.GetFeature(i)
            titular = feature.GetField(ctitular).decode("Latin-1")
            inmueble = feature.GetField(cinmueble).decode("Latin-1")
            dni = feature.GetField(cdni).decode("Latin-1")
            wkt = feature.GetGeometryRef().ExportToWkt()
            sql = "INSERT INTO cartografia.puntos_desc (geom, titular, dni, inmueble) " \
                  "VALUES (ST_GeomFromText(%(g)s, 25830), %(t)s, %(d)s, %(i)s);"
            crsr.execute(sql, {"g": wkt, "t": titular, "d": dni, "i": inmueble})
        conn.commit()
        self.form.CargaCapa("puntos_desc", "25830", "Contadores")
        c = self.form.l_capa("Contadores", self.form)
        # qlwi = QListWidgetItem(self.form.listCapas)
        qlwi = QListWidgetItem()
        qlwi.setSizeHint(c.sizeHint())
        self.form.listCapas.insertItem(0, qlwi)
        self.form.listCapas.setItemWidget(qlwi, c)
        self.form.visualizaCapa()
        self.close()
        self.form.layer = QgsMapLayerRegistry.instance().mapLayersByName("Contadores")[0]
        #self.form.createMapTips()

    def loadShp(self):
        ruta = QFileDialog.getOpenFileName(self, "Cargar fichero Shapefile", "",
                                           "Ficheros SHP (*.shp)")
        try:
            self.ruta.setText(ruta)
            shp = osgeo.ogr.Open(ruta)
            layer = shp.GetLayer(0)
            schema = []
            layerdef = layer.GetLayerDefn()
            for n in range(layerdef.GetFieldCount()):
                fdefn = layerdef.GetFieldDefn(n)
                schema.append(fdefn.name)
            for i in range(layer.GetFeatureCount()):
                feature = layer.GetFeature(i)
                wkt = feature.GetGeometryRef().ExportToWkt()
            self.inmueble.addItems(schema)
            self.titular.addItems(schema)
            self.dni.addItems(schema)
            self.cargar.setEnabled(True)
            self.groupBox.setEnabled(True)
        except:
            Mensaje("Ha ocurrido un error")



    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        qp.begin(self)
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(3)
        pen.setStyle(Qt.SolidLine)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()


class orgselector(QDialog, selector.Ui_Dialog):

    def __init__(self):
        super(orgselector, self).__init__(parent=None)
        self.setupUi(self)
        self.organismos.addItems(["Ayuntamiento de Oliva", "Murcia AMT"])
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowModality(Qt.WindowModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.aceptar.clicked.connect(self.openPrincipal)
        self.organismos.doubleClicked.connect(self.openPrincipal)
        self.setGraphicsEffect(sombra())

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(QColor(qRgb(143, 212, 0)))
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

    def openPrincipal(self):

        global dbname
        self.close()
        if self.organismos.currentRow() == 0:
            dbname = "oliva"
        else:
            dbname = "murcia"

class confirma(QDialog, confirmacion.Ui_Dialog):
    def __init__(self, titulo, mensaje, yes, no, parent):
        super(confirma, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.texto.setText(mensaje)
        self.setWindowTitle(titulo)
        self.ok.setText(yes)
        self.cancel.setText(no)
        self.ok.clicked.connect(self.acepta)
        self.cancel.clicked.connect(self.rechaza)
        self.setGraphicsEffect(sombra())

    def acepta(self):
        self.accept()

    def rechaza(self):
        self.reject()

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(4)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class clase_desconocido(QWidget, desconocido.Ui_Form):
    def __init__(self, ref_completa, nombre, dni, nif_candidato, nombre_candidato, origen, form):
        super(clase_desconocido, self).__init__(parent=None)
        self.setupUi(self)
        self.form = form
        self.ref_completa = ref_completa
        self.cambiaIcono(origen)
        self.finnif.setText(dni)
        self.finnombre.setText(nombre)
        self.candnif.setText(nif_candidato)
        self.candnombre.setText(nombre_candidato)
        self.ref.setText(ref_completa)
        self.borra.setEnabled(False)
        self.icono.raise_()
        self.evalua()
        self.icono.clicked.connect(self.localizaDesc)
        self.borra.clicked.connect(self.borraCandidato)

    def refcat(self):
        return self.ref.text()

    def localizaDesc(self):
        sql = """SELECT \
                            ST_AsText(ST_Centroid((g.geom))) AS geom,
                            CONCAT(p.numerocargo, ' // ', p.valorcatastral) as campo2,
                            COUNT(p.numerocargo) AS cuenta
                            FROM public.fin p INNER JOIN cartografia.parcela g USING(refcat)
                            WHERE p.ref_completa='""" + self.ref_completa + """' GROUP BY g.geom, p.refcat,
                             p.numerocargo, p.valorcatastral;"""
        Consulta(self.form, sql, "public.fin")

    def evalua(self):
        if self.candnif.text() != "":
            self.fondo.setStyleSheet("QLabel#fondo {border: 2px solid rgb(143,212,0);"
                                     "border-radius: 30px;"
                                     "background-color: rgba(143,212,0,100);}")
            self.borra.setEnabled(True)
        else:
            self.fondo.setStyleSheet("QLabel#fondo {border: 2px solid rgb(143,212,0);"
                                     "border-radius: 30px;"
                                     "background-color: rgba(255,255,255,255);}")
            self.borra.setEnabled(False)

    def borraCandidato(self):
        ok = confirma(u"Eliminar candidato", u"¿Eliminar titular candidato para el inmueble " + self.ref_completa + u"?",
                      u"Sí", "No", self)
        if ok.exec_() == QDialog.Accepted:
            psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
            psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
            conn = psycopg2.connect(
                "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
            cur = conn.cursor()
            sql = """UPDATE public.fin SET nif_candidato=NULL, nombre_candidato=NULL WHERE ref_completa=%(ref)s;"""
            cur.execute(sql, {"ref": self.ref_completa})
            conn.commit()
            self.candnif.setText("")
            self.candnombre.setText("")
            self.evalua()

    def cambiaIcono(self, origen):
        if origen == "BASURAS":
            self.icono.setIcon(QIcon(QPixmap(":/icons/basura.png")))
            self.icono.setIconSize(QSize(25, 25))
        if origen == "AGUAS":
            self.icono.setIcon(QIcon(QPixmap(":/icons/grifo.png")))
            self.icono.setIconSize(QSize(25, 25))

class clase_titular(QWidget, titular.Ui_Form):
    def __init__(self, ref_completa, origen, nombre, nif, form):
        super(clase_titular, self).__init__(parent=None)
        self.setupUi(self)
        self.form = form
        self.ref_completa = ref_completa
        self.nombre.setText(nombre)
        self.nif.setText(nif)
        self.cambiaIcono(origen)
        self.icono.clicked.connect(self.actTitularCandidato)

    def actTitularCandidato(self):
        ref = self.ref_completa
        nif = self.nif.text()
        nombre = self.nombre.text()
        ok = confirma("Actualizar titular", u"¿Utilizar " + unicode(nombre) + " con NIF " + nif + " como"
                                        u" titular candidato para este inmueble?", u"Sí", "No", self)
        if ok.exec_() == QDialog.Accepted:
            psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
            psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
            conn = psycopg2.connect(
                    "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
            cur = conn.cursor()
            sql = """UPDATE public.fin SET nif_candidato=%(nif)s, nombre_candidato=%(nombre)s WHERE ref_completa=%(ref)s;"""
            cur.execute(sql, {"ref": ref, "nif": nif, "nombre": nombre})
            conn.commit()
            cur.close()
            datosFin(ref[:14], self.form)


    def cambiaIcono(self, origen):
        if origen == "BASURAS":
            self.icono.setIcon(QIcon(QPixmap(":/icons/basura.png")))
            self.icono.setIconSize(QSize(25, 25))
        if origen == "AGUAS":
            self.icono.setIcon(QIcon(QPixmap(":/icons/grifo.png")))
            self.icono.setIconSize(QSize(25, 25))

class clase_criterio(QWidget, criterio.Ui_Form):
    def __init__(self, operador, tabla, campo, campo2, icono, unico, tipologia, nombre):
        super(clase_criterio, self).__init__(parent=None)
        self.setupUi(self)
        self.cambiaIcono(icono)
        self.setUnico(unico)
        self.tipo(tipologia)
        self.cambiaNombre(nombre)
        self.cambiaOperador(operador)
        self.setGeometry(QRect(0, 0, 260, 40))
        self.tabla = tabla
        self.campo = campo
        self.campo2 = campo2


    def cambiaOperador(self, operador):
        self.operador = operador

    def cambiaIcono(self, icon):
        self.icono.setPixmap(QPixmap(icon))
        self.icono.setScaledContents(True)
        self.icono.setMargin(6)

    def setUnico(self, estado):
        self.campounico = estado

    def cambiaNombre(self, nombre):
        self.n_criterio.setText(nombre)

    def tipo(self, valor):
        self.tipol = valor
        if valor == 1:
            x = self.criterio.x()
            y = self.criterio.y()
            w = self.criterio.width()
            h = self.criterio.height()
            self.criterio.setParent(None)
            self.criterio = QComboBox()
            self.criterio.setGeometry(QRect(46, 16, 190, 20))
            self.criterio.setParent(self)
            # self.gridLayout.addWidget(self.criterio)
        if valor == 0:
            return



class listBusquedas(QListWidget):
    def __init__(self, parent):
        super(listBusquedas, self).__init__(parent)
        parent.layout().addWidget(self)
        self.setDragDropMode(QAbstractItemView.DropOnly)
        self.setDefaultDropAction(Qt.CopyAction)
        self.setFrameShape(QFrame.NoFrame)
        self.setSpacing(3)


    def dropEvent(self, event):
        index = event.source()._drag_info[1]
        print index
        itm = event.source().item(index)
        obj = event.source().itemWidget(itm)

        valores = []

        if obj.tipol == 1:
            print obj.criterio.currentIndex()
            for i in range(0, obj.criterio.count()):
                valores.append(obj.criterio.itemText(i))

        j = clase_criterio(obj.operador, obj.tabla, obj.campo, obj.campo2, obj.icono.pixmap(), obj.campounico, obj.tipol, obj.n_criterio.text())
        if obj.tipol == 1:
            j.criterio.addItems(valores)
            j.criterio.setCurrentIndex(obj.criterio.currentIndex())


        qlwi = QListWidgetItem(self)
        qlwi.setSizeHint(QSize(150, 40))
        self.addItem(qlwi)
        self.setItemWidget(qlwi, j)










class ValorWidget(QWidget, valor.Ui_Form):
    advierte = pyqtSignal(QObject, QObject, str)
    def __init__(self, cargo, dni, titular, ref_completa, form, desconocido, nif_candidato, nombre_candidato, contenedor, parent=None):
        super(ValorWidget, self).__init__(parent)

        self.form = form
        self.contenedor = contenedor
        self.ref_completa = ref_completa
        self.setupUi(self)
        if nombre_candidato is None:
            self.nif.setText(unicode(dni))
            self.titular.setText(unicode(titular))
        else:
            self.nif.setText(unicode(nif_candidato))
            self.titular.setText(unicode(nombre_candidato))
            font = self.nif.font()
            font.setItalic(True)
            self.nif.setFont(font)
            self.titular.setFont(font)
            self.nif.setStyleSheet("QLabel { color: rgb(255,69,0);}")
            self.titular.setStyleSheet("QLabel { color: rgb(255,69,0);}")
        self.cargo.setText(cargo)

        self.info_ot.hide()
        self.showinfo.clicked.connect(self.presionado)
        self.advierte.connect(resizeResultado)
        self.mastit.clicked.connect(self.mastitulares)
        self.mastit.setVisible(False)
        titulares = 0
        if desconocido:
            titulares += self.refcatcoincide(ref_completa, "public.basuras")
            titulares += self.refcatcoincide(ref_completa, "public.aguas")
            if titulares > 0:
                self.ot.setStyleSheet("QWidget#ot {background-image: url(:/img/descon_back.png); \
                                      background-repeat: no-repeat; \
                                      background-position:center;}")
                self.mastit.setText(str(titulares))
                self.mastit.setMinimumWidth(19)
                self.mastit.setVisible(True)
            else:
                self.mastit.setVisible(False)

    def mastitulares(self):
        self.form.titWindow = TitularesWindow(self.ref_completa, self.titular.text(), self.nif.text(), self.form,
                                              self.form.canvas)
        self.form.titWindow.show()
        self.form.titWindowActive = True
        rellenamastitulares(self.ref_completa, self.form.titWindow, self.form)

    def refcatcoincide(self, ref_completa, tabla):
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
        conn = psycopg2.connect(
            "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
        cur = conn.cursor()
        sql = """SELECT COUNT(*) FROM """ + tabla + """ WHERE ref_completa=%(ref)s;"""
        cur.execute(sql, {"ref": ref_completa})
        rows = cur.fetchone()
        return rows[0]

    def presionado(self):
        print "emitiendo"
        self.advierte.emit(self, self.form, self.contenedor)

    def getRefCompleta(self):
        return self.ref_completa



class customAsk(QInputDialog):
    def __init__(self, parent, texto):
        QInputDialog.__init__(self, parent, QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setLabelText(texto)
        self.setOkButtonText("Aceptar")
        self.setCancelButtonText("Cancelar")
        self.setGraphicsEffect(sombra())
        self.show()

    def devuelve(self):
        return self.textValue()

    def reubica(self, canvas):

        x = canvas.width() - 160
        y = 10
        self.move(x, y)

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class listCriterios(QListWidget):
    _drag_info = []
    def __init__(self, parent):
        super(listCriterios,self).__init__(parent)
        self.setGeometry(20, 20, parent.width() - 40, parent.height() - 40)
        self.setViewMode(QListView.IconMode)
        self.setSpacing(5)

    def startDrag(self, actions):
        self._drag_info[:] = [str(self.objectName())]
        for item in self.selectedItems():
            self._drag_info.append(self.row(item))
        super(listCriterios, self).startDrag(actions)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(listCriterios, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            super(listCriterios, self).dragMoveEvent(event)

    def dropEvent(self, event):
        event.ignore()

    def reubica(self):
        self.setGeometry(20, 20, self.parent().width() - 40, self.parent().height() - 40)

class TablaDesconocidos(QWidget):
    def __init__(self, form, parent):
        super(TablaDesconocidos, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setMaximumWidth(630)
        self.form = form
        margen = (parent.width() - 620) / 2
        self.setGeometry(QRect(margen, 100, parent.width()-100, parent.height()-200))
        self.layout = QGridLayout(self)
        self.setLayout = self.layout
        self.tabla = QListWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ref = QLabel(self)
        self.ref.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ref.setFont(font)
        self.ref.setAlignment(Qt.AlignCenter)
        self.ref.setMaximumHeight(19)
        self.labelnombre = QLabel(self)
        self.labelnombre.setMaximumSize(QSize(60, 19))
        font.setPointSize(8)
        self.labelnombre.setFont(font)
        self.finnombre = QLineEdit(self)
        self.finnombre.setMaximumHeight(19)
        self.finnombre.setAlignment(Qt.AlignLeft)
        self.labelnombre.setText("INMUEBLE:")
        self.ref.setText("REF")
        self.cerrar = QPushButton(self)
        self.cerrar.setMaximumSize(QSize(50, 25))
        self.cerrar.setText("Salir")
        self.minimizar = QPushButton(self)
        self.minimizar.setMaximumSize(QSize(50, 25))
        self.minimizar.setText("Minimizar")
        self.layout.addWidget(self.ref, 0, 0, 1, 5)
        self.layout.addWidget(self.labelnombre, 1, 0, 1, 1)
        self.layout.addWidget(self.finnombre, 1, 1, 1, 4)
        self.layout.addWidget(self.tabla, 2, 0, 1, 5)
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.cerrar)
        self.hlayout.addWidget(self.minimizar)
        self.layout.addLayout(self.hlayout, 3, 0, 1, 5)
        self.ref.setText("LISTADO DE DESCONOCIDOS")
        self.tabla.setSpacing(3)
        self.cerrar.clicked.connect(self.cierra)
        self.minimizar.clicked.connect(self.minimiza)
        self.setGraphicsEffect(sombra())
        self.setCursor(Qt.ArrowCursor)
        self.finnombre.textChanged.connect(self.filtra)

    def filtra(self):
        if self.finnombre.text() == "":
            for i in range(0, self.tabla.count()):
                c = self.tabla.item(i)
                self.tabla.setItemHidden(c, False)
        else:
            for i in range(0, self.tabla.count()):
                c = self.tabla.item(i)
                if self.finnombre.text().upper() not in self.tabla.itemWidget(c).refcat():
                    self.tabla.setItemHidden(c, True)
                else:
                    self.tabla.setItemHidden(c, False)

    def minimiza(self):
        self.hide()
        ventana(self, self.form.ventanas, "Desconocidos")

    def cierra(self):
        self.form.titWindowActive = False
        self.close()

    def reubica(self, canvas):
        margen = (canvas.width() - 620) / 2
        self.setGeometry(margen, 100, canvas.width()-100, canvas.height()-200)

    def paintEvent(self, event):
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class TitularesWindow(QWidget):
    def __init__(self, ref_completa, nombre, nif, form, parent):
        super(TitularesWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setMaximumWidth(620)
        self.form = form
        margen = (parent.width() - 620) / 2
        self.setGeometry(QRect(margen, 100, parent.width()-100, parent.height()-200))
        self.layout = QGridLayout(self)
        self.setLayout = self.layout
        self.tabla = QListWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ref = QLabel(self)
        self.ref.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ref.setFont(font)
        self.ref.setAlignment(Qt.AlignCenter)
        self.ref.setMaximumHeight(19)
        self.labelnombre = QLabel(self)
        self.labelnombre.setMaximumSize(QSize(60, 19))
        font.setPointSize(8)
        self.labelnombre.setFont(font)
        self.labelnif = QLabel(self)
        self.labelnif.setMaximumSize(QSize(30, 19))
        self.labelnif.setFont(font)
        self.finnombre = QLabel(self)
        self.finnombre.setMaximumHeight(19)
        self.finnombre.setAlignment(Qt.AlignLeft)
        self.finnif = QLabel(self)
        self.finnif.setMaximumHeight(19)
        self.finnif.setAlignment(Qt.AlignRight)
        self.finnombre.setText("LABELNOMBRE")
        self.finnif.setText("LABELNIF")
        self.labelnif.setText("NIF:")
        self.labelnombre.setText("NOMBRE:")
        self.ref.setText("REF")
        self.cerrar = QPushButton(self)
        self.cerrar.setMaximumSize(QSize(50, 25))
        self.cerrar.setText("Salir")
        self.minimizar = QPushButton(self)
        self.minimizar.setMaximumSize(QSize(50, 25))
        self.minimizar.setText("Minimizar")
        self.layout.addWidget(self.ref, 0, 0, 1, 5)
        self.layout.addWidget(self.labelnombre, 1, 0, 1, 1)
        self.layout.addWidget(self.finnombre, 1, 1, 1, 2)
        self.layout.addWidget(self.labelnif, 1, 3, 1, 1)
        self.layout.addWidget(self.finnif, 1, 4, 1, 1)
        self.layout.addWidget(self.tabla, 2, 0, 1, 5)
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.cerrar)
        self.hlayout.addWidget(self.minimizar)
        self.layout.addLayout(self.hlayout, 3, 0, 1, 5)
        self.finnif.setText(nif)
        self.finnombre.setText(nombre)
        self.ref.setText(ref_completa)
        self.tabla.setSpacing(3)
        self.cerrar.clicked.connect(self.cierra)
        self.setGraphicsEffect(sombra())
        self.minimizar.clicked.connect(self.minimiza)
        self.setCursor(Qt.ArrowCursor)

    def cierra(self):
        self.form.titWindowActive = False
        self.close()

    def minimiza(self):
        self.hide()
        ventana(self, self.form.ventanas, "Titulares")





    def reubica(self, canvas):
        margen = (canvas.width() - 620) / 2
        self.setGeometry(margen, 100, canvas.width()-100, canvas.height()-200)


    def paintEvent(self, event):
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class Graficos(QWidget):
    def __init__(self, parent):
        super(Graficos, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setMaximumWidth(800)
        margen = (parent.width() - 800) / 2
        self.setGeometry(QRect(margen, 100, parent.width()-100, parent.height()-200))
        self.lytest = QVBoxLayout()
        self.lytest.setAlignment(Qt.AlignHCenter)
        self.setLayout(self.lytest)


    def reubica(self, canvas):
        margen = (canvas.width() - 620) / 2
        self.setGeometry(margen, 100, canvas.width()-100, canvas.height()-200)


    def paintEvent(self, event):
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class pool_Window(QWidget):
    def __init__(self, parent):
        super(pool_Window, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(QRect(50, 50, parent.width()-100, parent.height()-100))
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.layout = QGridLayout(self)
        self.setLayout = self.layout
        self.tabWidget = QTabWidget(self)
        #self.tabWidget.setGeometry(QRect(10, 10, self.tabWidget.parent().width()-20, self.tabWidget.parent().height()-20))
        self.tabWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.listIBI = listCriterios(self)
        self.listIBI.setViewMode(QListView.IconMode)
        self.listBASURA = listCriterios(self)
        self.listVADOS = listCriterios(self)
        self.listEXPEDIENTES = listCriterios(self)
        self.listAGUAS = listCriterios(self)
        self.listICIO = listCriterios(self)
        self.listPLUSVALIAS = listCriterios(self)
        self.listMULTAS = listCriterios(self)
        self.listDESCONOCIDOS = listCriterios(self)
        self.tabWidget.addTab(self.listIBI, QIcon(":/icons/25694.png"), "IBI",)
        self.tabWidget.addTab(self.listVADOS, QIcon(":/icons/vados.png"), "VADOS")
        self.tabWidget.addTab(self.listBASURA, QIcon(":/icons/basura.png"), "BASURAS")
        self.tabWidget.addTab(self.listAGUAS, QIcon(":/icons/grifo.png"), "AGUAS")
        self.tabWidget.addTab(self.listPLUSVALIAS, QIcon(":/icons/plusvalias.png"), "PLUSVALIAS")
        self.tabWidget.addTab(self.listICIO, QIcon(":/icons/gancho.png"), "ICIO")
        self.tabWidget.addTab(self.listEXPEDIENTES, QIcon(":/icons/expediente.png"), "EXPEDIENTES")
        self.tabWidget.addTab(self.listMULTAS, QIcon(":/icons/policia.png"), "MULTAS")
        self.tabWidget.addTab(self.listDESCONOCIDOS, QIcon(":/icons/desconocido.png"), "DESCONOCIDOS")
        self.layout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setGraphicsEffect(sombra())


    def reubica(self, canvas):

        self.setGeometry(50, 50, canvas.width()-100, canvas.height()-100)
        #self.tabWidget.reubica()

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class sat(QWidget, satelite.Ui_Form):
    def __init__(self, parent, form):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setCursor(Qt.PointingHandCursor)
        self.satelite.clicked.connect(form.visualizaCapa)
        self.satelite.setCheckState(Qt.Checked)
        self.setGraphicsEffect(sombra())

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(3)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

    def reubica(self, canvas):
        x = 10
        y = canvas.height() - 89
        self.move(x, y)
        print canvas.height()

class ventanas(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.layout = QVBoxLayout()
        self.setGeometry(5, 5, 150, 200)
        self.lista = QListWidget()
        self.lista.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addWidget(self.lista)
        self.setLayout(self.layout)
        self.lista.setSpacing(5)
        self.lista.setStyleSheet("QListWidget { border: 0px;"
                                 "background: rgba(0,0,0,0);"
                                 "}")




class panel_id(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        x = parent.width() - 160
        y = 10

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.layout = QVBoxLayout()
        self.setGeometry(x, y, 150, 30)
        self.finca = QLabel()
        self.finca.setAlignment(Qt.AlignCenter)
        self.finca.setText(u"Sin selección")
        self.finca.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addWidget(self.finca)
        self.setLayout(self.layout)


    def reubica(self, canvas):

        x = canvas.width() - 160
        y = 10
        self.move(x, y)

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        pen = QPen()
        pen.setBrush(QColor(qRgb(143, 212, 0)))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(pen)
        qp.setBrush(QColor(qRgb(255, 255, 255)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()



class loading(QWidget):
    def __init__(self, texto, parent):
        QWidget.__init__(self, parent=None)
        self.movie = QMovie(":/img/loading.gif", QByteArray(), self)
        self.movie.setScaledSize(QSize(25, 25))
        size = self.movie.scaledSize()
        self.titulo = QLabel()
        self.titulo.setText(texto)
        self.titulo.setAlignment(Qt.AlignHCenter)
        self.titulo.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setObjectName("principal")
        #self.setStyleSheet("QWidget {border: 2px rgb(143,212,0);}")
        center = parent.mapToGlobal(parent.frameGeometry().center())
        x = center.x() - 75
        y = center.y() - 25
        self.setGeometry(x, y, 150, 50)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.titulo)
        main_layout.addWidget(self.movie_screen)
        self.setLayout(main_layout)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.setGraphicsEffect(sombra())

    def __del__(self):
        print "Cerrado"

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(QColor(qRgb(143, 212, 0)))
        qp.setBrush(QColor(qRgb(211, 211, 211)))
        qp.drawRoundedRect(0, 0, s.width(), s.height(), 10, 10)
        qp.end()

class contadorGraf(QWidget, contGraf.Ui_Form):
    def __init__(self, contador):
        super(contadorGraf, self).__init__(parent=None)
        self.setupUi(self)
        self.gid = contador[0]
        self.dist = contador[1]
        self.buff = contador[2]
        self.area = contador[3]
        self.prob = contador[4]
        self.inter = contador[5]
        self.tit = contador[6]
        self.nif = contador[7]
        self.valido = contador[8]
        self.titular.setText(self.tit)
        self.dni.setText(self.nif)
        self.porc.setText(str(int(self.prob)) + "%")
        decena = int(self.prob / 10)
        if decena == 10:
            decena = 9
        color = cl.scales['10']['div']['RdYlGn'][decena]
        style = 'QLabel { border: 2px solid rgb(143,212,0); border-radius: 15px;background-color: ' + color + ';})'
        self.porc.setStyleSheet(style)

    def buffer(self):
        return self.buff

    def getGid(self):
        return self.gid

    def getTitular(self):
        return self.tit

    def getNif(self):
        return self.nif



class invDescGraf(QWidget, inm.Ui_Form):
    def __init__(self, invDesc):
        super(invDescGraf, self).__init__(parent=None)
        self.setupUi(self)
        self.ref.setText(invDesc.inmueble)
        self.finca = invDesc.finca
        self.geometria = ""
        self.inmueble = invDesc.inmueble
        self.titular = invDesc.titular
        self.nif = invDesc.nif
        self.candtit = ""
        self.candnif = ""
        self.tcand = invDesc.tcand
        self.lcont = invDesc.lcont
        self.colindantes = invDesc.colindantes

    def getCandTit(self):
        return self.candtit

    def getCandNif(self):
        return self.candnif

    def addCandidato(self, cand):
        self.tcand.append(cand)

    def addContador(self, contador):
        self.lcont.append(contador)

    def addGeometria(self, geom):
        self.geometria = geom

    def addColindante(self, geom):
        self.colindantes.append(geom)

    def getColindantes(self):
        return self.colindantes

    def getGeometria(self):
        return self.geometria

    def getContadores(self):
        return self.lcont

    def getCandidato(self):
        return self.tcand


class invDesc():
    def __init__(self, finca, inmueble, titular, nif):
        self.geometria = ""
        self.finca = finca
        self.inmueble = inmueble
        self.titular = titular
        self.nif = nif
        self.tcand = []
        self.lcont = []
        self.colindantes = []

    def addCandidato(self, cand):
        self.tcand.append(cand)

    def addContador(self, contador):
        self.lcont.append(contador)

    def addGeometria(self, geom):
        self.geometria = geom

    def addColindante(self, geom):
        self.colindantes.append(geom)

    def getColindantes(self):
        return self.colindantes

    def getGeometria(self):
        return self.geometria




class w(QPushButton):
    advierte = pyqtSignal(QObject, QObject)
    def __init__(self, window, texto, parent):
        super(w, self).__init__(parent)
        self.window = window
        self.parent = parent
        self.clicked.connect(self.muestra)
        self.setGeometry(0, 0, 90, 20)
        self.setText(texto)
        self.advierte.connect(eliminaVentana)
        self.setGraphicsEffect(sombra())
        self.setCursor(Qt.ArrowCursor)
        self.setMouseTracking(True)

    def muestra(self):
        self.window.show()
        self.advierte.emit(self.parent, self)


    def enterEvent(self, *args, **kwargs):
        pass

    def leaveEvent(self, *args, **kwargs):
        pass





class Principal(QMainWindow, gttgis.Ui_MainWindow):
    visibleCriterios = False

    class BufferLineal(QgsMapToolEmitPoint):
        def __init__(self, canvas, form):
            self.form = form
            self.canvas = canvas
            QgsMapToolEmitPoint.__init__(self, self.canvas)
            self.form.panel_resultados.show()
            self.rubberBand = QgsRubberBand(self.canvas, QgsWKBTypes.LineString)
            self.rubberBand.setBorderColor(QColor(143, 212, 0, 255))
            self.rubberBand.setWidth(2)
            self.isEmitting = False
            self.reset()
            self.puntos = []

        def canvasMoveEvent(self, e):
            if not self.isEmitting:
                return
            self.endPoint = self.toMapCoordinates(e.pos())
            self.previo = []
            self.previo = list(self.puntos)
            self.previo.append(self.endPoint)
            #print len(self.previo), len(self.puntos)
            self.showRect(self.previo)

        def canvasDoubleClickEvent(self, e):
            self.isEmitting = False
            self.showRect(self.puntos)
            #print len(self.puntos)
            radio_buffer = customAsk(self.canvas, "Introduzca distancia de buffer:")
            radio_buffer.exec_()
            if radio_buffer.result() == 1:
                #print radio_buffer.devuelve(), self.rubberBand.asGeometry()
                self.getgeom(self.rubberBand.asGeometry(), radio_buffer.devuelve())
            #getRefs(self.canvas, self.rubberBand.asGeometry(), self.form)
            self.reset()


        def getgeom(self, g, radio):
            p = loading("Representando parcelas seleccionadas", self.canvas)
            p.show()
            conn = psycopg2.connect("dbname='oliva' user='postgres' password='123456' host='9.56.3.159' port='5432'")
            cur = conn.cursor()
            geometria = g.exportToWkt()
            sql = """SELECT ST_AsText(p.geom), p.refcat FROM cartografia.parcela p \
                                    WHERE ST_DWithin(p.geom, ST_GeomFromText(%(geom)s, 25830), %(radio)s);"""
            cur.execute(sql, {"geom": geometria, "radio": radio})
            rows = cur.fetchall()
            self.canvas.freeze()
            geometrias = []
            fincas = []
            for row in rows:
                geometrias.append(row[0])
                fincas.append(row[1])
            self.form.panel_resultados.finca.setText(str(cur.rowcount) + " fincas seleccionadas.")
            Resaltador(self.canvas, geometrias, self.form)
            muestraFincas(fincas, self.form)
            self.canvas.freeze(False)
            self.canvas.refresh()
            p.close()

        def reset(self):
            self.puntos = []
            self.isEmittingPoint = False
            self.rubberBand.reset(QGis.Line)

        def canvasPressEvent(self, e):
            if self.isEmitting == False:
                limpiar(self.canvas, self.form)
            self.startPoint = self.toMapCoordinates(e.pos())
            self.isEmitting = True
            self.puntos.append(self.startPoint)
            self.showRect(self.puntos)

        def showRect(self, puntos):
            self.rubberBand.reset(QGis.Line)
            if len(puntos) == 1:
                return
            for pt in puntos:
                self.rubberBand.addPoint(pt, True)
            self.rubberBand.show()

    class IdTool(QgsMapToolEmitPoint):
        def __init__(self, canvas, form):
            self.form = form
            self.canvas = canvas
            QgsMapToolEmitPoint.__init__(self, self.canvas)
            self.form.panel_resultados.show()
            self.deactivated.connect(self.quita)

        def canvasPressEvent(self, e):
            limpiar(self.canvas, self.form)
            p = self.toMapCoordinates(e.pos())
            punto = QgsPoint(p.x(), p.y())
            getReferencia(self.canvas, QgsGeometry.fromPoint(punto), self.form)

        def quita(self):
            self.form.panel_resultados.hide()

    class bufferradial(QgsMapToolEmitPoint):
        def __init__(self, canvas, form):
            self.form = form
            self.canvas = canvas
            QgsMapToolEmitPoint.__init__(self, self.canvas)
            form.panel_resultados.show()

        def canvasPressEvent(self, e):
            limpiar(self.canvas, self.form)
            self.startPoint = self.toMapCoordinates(e.pos())
            self.punto = QgsPoint(self.startPoint.x(), self.startPoint.y())
            radio_buffer = customAsk(self.canvas, "Introduzca radio en metros:")
            radio_buffer.exec_()
            if radio_buffer.result() == 1:
                self.getgeom(self.punto, radio_buffer.devuelve())
                self.form.panel_resultados.show()
            else:
                print "No hay radio"

        def getgeom(self, punto, radio):
            p = loading("Representando parcelas seleccionadas", self.canvas)
            p.show()
            conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
            cur = conn.cursor()
            geometria = punto.wellKnownText()
            sql = """SELECT ST_AsText(p.geom), p.refcat FROM cartografia.parcela p \
                        WHERE ST_DWithin(ST_Centroid(p.geom), ST_GeomFromText(%(geom)s, 25830), %(radio)s);"""
            cur.execute(sql, {"geom": geometria, "radio": radio})
            rows = cur.fetchall()
            self.canvas.freeze()
            geometrias = []
            fincas = []
            for row in rows:
                geometrias.append(row[0])
                fincas.append(row[1])
            self.form.panel_resultados.finca.setText(str(cur.rowcount) + " fincas seleccionadas.")
            Resaltador(self.canvas, geometrias, self.form)
            muestraFincas(fincas, self.form)
            self.canvas.freeze(False)
            self.canvas.refresh()
            p.close()



    class Circulo(QgsMapToolEmitPoint):
        def __init__(self, canvas, form):
            self.form = form
            self.canvas = canvas
            QgsMapToolEmitPoint.__init__(self, self.canvas)
            self.form.panel_resultados.show()
            self.rubberBand = QgsRubberBand(self.canvas, QGis.Polygon)
            self.rubberBand.setBorderColor(QColor(143, 212, 0, 255))
            self.rubberBand.setFillColor(QColor(143, 212, 0, 100))
            self.rubberBand.setWidth(1)
            self.reset()

        def reset(self):
            self.startPoint = self.endPoint = None
            self.isEmittingPoint = False
            self.rubberBand.reset(QGis.Polygon)

        def canvasPressEvent(self, e):
            limpiar(self.canvas, self.form)
            self.startPoint = self.toMapCoordinates(e.pos())
            self.endPoint = self.startPoint
            self.isEmittingPoint = True
            self.showRect(self.startPoint, self.endPoint)

        def canvasReleaseEvent(self, e):
            self.isEmittingPoint = False
            r = self.rubberBand.asGeometry()
            getRefs(self.canvas, r, self.form)
            self.reset()

        def canvasMoveEvent(self, e):
            if not self.isEmittingPoint:
                return
            self.endPoint = self.toMapCoordinates(e.pos())
            self.showRect(self.startPoint, self.endPoint)

        def circle(self):
            a = self.calcirc(self.startPoint, self.endPoint)
            print a
            return QgsGeometry.fromPolygon(a)

        def calcirc(self, startPoint, endPoint):
            segments = 100
            radio = sqrt((startPoint.x() - endPoint.x()) ** 2 + (startPoint.y() - endPoint.y()) ** 2)
            print radio
            pts = []
            for i in range(segments):
                a = i * (2.0 * pi / segments)
                p = QgsPoint(startPoint.x() + radio * cos(a), startPoint.y() + radio * sin(a))
                pts.append(p)
            return pts

        def showRect(self, startPoint, endPoint):
            self.rubberBand.reset(QGis.Polygon)
            if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
                return

            puntos = self.calcirc(startPoint, endPoint)
            for pt in puntos:
                self.rubberBand.addPoint(pt, True)

            self.rubberBand.show()

    class SelLibre(QgsMapToolEmitPoint):
        def __init__(self, canvas, form):
            self.form = form
            self.canvas = canvas
            QgsMapToolEmitPoint.__init__(self, self.canvas)
            self.form.panel_resultados.show()
            self.rubberBand = QgsRubberBand(self.canvas, QGis.Polygon)
            self.rubberBand.setBorderColor(QColor(143, 212, 0, 255))
            self.rubberBand.setFillColor(QColor(143, 212, 0, 100))
            self.rubberBand.setWidth(1)
            self.acero()
            self.reset()

        def acero(self):
            self.puntos = []
            self.previo = []

        def reset(self):
            self.previo = []
            self.puntos = []
            self.startPoint = self.endPoint = None
            self.isEmittingPoint = False
            self.rubberBand.reset(QGis.Polygon)

        def canvasPressEvent(self, e):
            if self.isEmittingPoint == False:
                limpiar(self.canvas, self.form)
            self.startPoint = self.toMapCoordinates(e.pos())
            self.isEmittingPoint = True
            self.puntos.append(self.startPoint)

        def canvasDoubleClickEvent(self, e):
            self.isEmittingPoint = False
            self.showRect(self.puntos)
            print len(self.puntos)
            getRefs(self.canvas, self.rubberBand.asGeometry(), self.form)
            self.reset()

        def canvasReleaseEvent(self, e):
            return

        def canvasMoveEvent(self, e):
            if not self.isEmittingPoint:
                return
            self.endPoint = self.toMapCoordinates(e.pos())
            self.previo = []
            self.previo = list(self.puntos)
            self.previo.append(self.endPoint)
            print len(self.previo), len(self.puntos)
            self.showRect(self.previo)

        def showRect(self, puntos):
            self.rubberBand.reset(QGis.Polygon)
            if len(puntos) == 1:
                return
            for pt in puntos:
                self.rubberBand.addPoint(pt, True)
            self.rubberBand.show()

    class RectangleMapTool(QgsMapToolEmitPoint):
        def __init__(self, canvas, form):
            self.form = form
            self.canvas = canvas
            QgsMapToolEmitPoint.__init__(self, self.canvas)
            self.form.panel_resultados.show()
            self.rubberBand = QgsRubberBand(self.canvas, False)
            self.rubberBand.setBorderColor(QColor(143, 212, 0, 255))
            self.rubberBand.setFillColor(QColor(143, 212, 0, 100))
            self.rubberBand.setWidth(1)
            self.reset()

        def reset(self):
            self.startPoint = self.endPoint = None
            self.isEmittingPoint = False
            self.rubberBand.reset(QGis.Polygon)

        def canvasPressEvent(self, e):
            limpiar(self.canvas, self.form)
            self.startPoint = self.toMapCoordinates(e.pos())
            self.endPoint = self.startPoint
            self.isEmittingPoint = True
            self.showRect(self.startPoint, self.endPoint)

        def canvasReleaseEvent(self, e):
            self.isEmittingPoint = False
            r = self.rectangle()
            if r is not None:
                print "Rectangle:", r.xMinimum(), r.yMinimum(), r.xMaximum(), r.yMaximum()
                getRefs(self.canvas, QgsGeometry.fromRect(r), self.form)
            self.reset()



        def canvasMoveEvent(self, e):
            if not self.isEmittingPoint:
                return

            self.endPoint = self.toMapCoordinates(e.pos())
            self.showRect(self.startPoint, self.endPoint)

        def showRect(self, startPoint, endPoint):
            self.rubberBand.reset(QGis.Polygon)
            if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
                return

            point1 = QgsPoint(startPoint.x(), startPoint.y())
            point2 = QgsPoint(startPoint.x(), endPoint.y())
            point3 = QgsPoint(endPoint.x(), endPoint.y())
            point4 = QgsPoint(endPoint.x(), startPoint.y())

            self.rubberBand.addPoint(point1, False)
            self.rubberBand.addPoint(point2, False)
            self.rubberBand.addPoint(point3, False)
            self.rubberBand.addPoint(point4, True)  # true to update canvas
            self.rubberBand.show()

        def rectangle(self):
            if self.startPoint is None or self.endPoint is None:
                return None
            elif self.startPoint.x() == self.endPoint.x() or self.startPoint.y() == self.endPoint.y():
                return None

            return QgsRectangle(self.startPoint, self.endPoint)

    class l_capa(QWidget):
        def __init__(self, param, parent):
            super(Principal.l_capa, self).__init__(parent)
            self.layout = QFormLayout()
            self.check = QCheckBox()
            self.check.setMaximumHeight(13)
            self.layout.addWidget(self.check)
            self.setLayout(self.layout)
            self.check.setTristate(False)
            self.check.setChecked(True)
            self.check.setText(param)
            self.check.setStyleSheet("QCheckBox::indicator:unchecked {image: url(:/img/eyegray.png);}\
                        QCheckBox::indicator:checked {image: url(:/img/eye.png);}")
            self.check.clicked.connect(lambda: parent.visualizaCapa())



    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        QgsApplication.setPrefixPath('.', True)
        QgsApplication.initQgis()
        gdal.SetConfigOption("GDAL_DATA", os.getcwd() + "\\gdal")
        self.canvas = QgsMapCanvas()
        self.canvas.mapRenderer().setProjectionsEnabled(True)
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)
        self.canvas.mapRenderer().setDestinationCrs(QgsCoordinateReferenceSystem(25830), True, True)
        self.canvas.setMapUnits(0)
        self.canvas.setObjectName("marco")
        self.layout.addWidget(self.canvas)
        self.activateWindow()
        self.lBusquedas = listBusquedas(self.g_busquedas)
        self.runSQL = QPushButton(self.g_busquedas)
        self.g_busquedas.layout().addWidget(self.runSQL)
        self.runSQL.setText("Ejecutar")
        self.runDel = QPushButton(self.g_busquedas)
        self.g_busquedas.layout().addWidget(self.runDel)
        self.runDel.setText(u"Delimitar búsqueda")
        self.escala = QLabel()
        self.coord = QLabel()
        self.escala.setAlignment(Qt.AlignLeft)
        self.statusBar.addWidget(self.escala)
        self.resultados_ibi.setViewMode(QListView.ListMode)
        self.rubberBand = QgsRubberBand(self.canvas, False)
        self.rubberBand.setBorderColor(QColor(143, 212, 0, 255))
        self.rubberBand.setFillColor(QColor(143, 212, 0, 100))
        self.rubberBand.setWidth(1)
        self.rb = QgsRubberBand(self.canvas, False)
        self.rb.reset(QGis.Polygon)
        self.rb.setBorderColor(QColor(255, 0, 0, 255))
        self.rb.setWidth(3)
        self.titWindowActive = False
        self.ventanas = ventanas(self.canvas)
        self.jar = []
        self.tempcapa()
        layer = QgsMapLayerRegistry.instance().mapLayersByName("temp")[0]
        self.jar.append(QgsMapCanvasLayer(layer))
        self.CargaCapa("masa", "25830", "Manzanas")
        self.CargaCapa("parcela", "25830", "Parcelas")
        self.CargaCapa("constru", "25830", "Construcciones")
        self.CargaCapa("calles", "25830", "Lineales")
        self.CargaCapa("landuse", "25830", "Terreno")
        self.PNOA()
        self.canvas.setLayerSet(self.jar)
        self.g_busquedas.hide()
        self.g_seleccion.hide()
        self.g_capas.hide()
        self.g_resultados.hide()
        self.g_estadisticas.hide()
        self.sel_rect.clicked.connect(self.f_sel_Rect)
        self.sel_custom.clicked.connect(self.f_sel_libre)
        self.sel_circ.clicked.connect(self.f_sel_circ)
        self.sel_idtool.clicked.connect(self.f_id_tool)
        self.canvas.mapCanvasRefreshed.connect(self.actTitulo)
        self.c_seleccion.clicked.connect(self.showSeleccion)
        self.c_Busquedas.clicked.connect(self.showBusquedas)
        self.c_estadisticas.clicked.connect(self.showEstadisticas)
        self.lshp.clicked.connect(self.cargaShp)
        self.statDesc.clicked.connect(lambda: self.showStats(self.cb_stats.currentText()))
        self.statExport.clicked.connect(lambda: GenBet(self))
        self.c_resultados.clicked.connect(self.showResultados)
        self.fincas.currentIndexChanged.connect(lambda: getInfo(self.fincas.currentText(), self))
        self.c_capas.clicked.connect(self.showCapas)
        self.sel_Del.clicked.connect(lambda: limpiar(self.canvas, self))
        self.sel_buf_point.clicked.connect(self.f_buf_rad)
        self.self_buf_line.clicked.connect(self.f_buf_lin)
        self.c_criterios.clicked.connect(self.showCriterios)
        self.panel_resultados = panel_id(self.canvas)
        self.csat = sat(self.canvas, self)
        self.runSQL.clicked.connect(lambda: montaSQL(self))
        #self.tablaDesc.clicked.connect(self.abretabladesc)
        self.tablaDesc.clicked.connect(self.abretabladesc)
        self.AnaDesc.clicked.connect(lambda: lanzaDesc(self, self.canvas))
        self.panel_resultados.hide()
        self.showMaximized()
        self.show()

        for lyr in ['Construcciones', 'Parcelas', 'Manzanas', 'Terreno', 'Lineales']:
            c = self.l_capa(lyr, self)
            qlwi = QListWidgetItem(self.listCapas)
            qlwi.setSizeHint(c.sizeHint())
            self.listCapas.addItem(qlwi)
            self.listCapas.setItemWidget(qlwi, c)

        vl = QgsMapLayerRegistry.instance().mapLayersByName("Construcciones")[0]
        self.canvas.setExtent(vl.extent())
        self.csat.reubica(self.canvas)


    def createMapTips(self):
        """ Create MapTips on the map """
        self.timerMapTips = QTimer(self.canvas)
        self.mapTip = QgsMapTip()
        self.connect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint&)"),
                     self.mapTipXYChanged)
        self.connect(self.timerMapTips, SIGNAL("timeout()"),
                     self.showMapTip)

    def mapTipXYChanged(self, p):
        """" SLOT. Initialize the Timer to show MapTips on the map """
        if self.canvas.underMouse():  # Only if mouse is over the map
            # Here you could check if your custom MapTips button is active or sth
            self.lastMapPosition = QgsPoint(p.x(), p.y())
            self.mapTip.clear(self.canvas)
            self.timerMapTips.start(750)  # time in milliseconds

    def showMapTip(self):
        """ SLOT. Show  MapTips on the map """
        self.timerMapTips.stop()

        if self.canvas.underMouse():
            # Here you could check if your custom MapTips button is active or sth
            pointQgs = self.lastMapPosition
            pointQt = self.canvas.mouseLastXY()
            self.mapTip.showMapTip(self.layer, pointQgs, pointQt,
                                   self.canvas)

    def abretabladesc(self):
        self.tdesc = TablaDesconocidos(self, self.canvas)
        self.tdesc.show()
        rellenadesconocidos(self.tdesc, self)

    def bufferpoint(self):
        input = customAsk(self.canvas, "Introduzca radio del buffer en metros:")
        input.exec_()
        if input.result() == 1:
            print input.devuelve()
        else:
            print "No"

    def cargaShp(self):
        a = openshp(self, self.canvas)
        a.show()

    def f_buf_rad(self):
        self.h_buf_rad = self.bufferradial(self.canvas, self)
        self.canvas.setMapTool(self.h_buf_rad)
        pixmap = QPixmap(":/icons/bufferpunto.png").scaled(QSize(20, 20), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        cursor = QCursor(pixmap, 0, 0)
        self.canvas.setCursor(cursor)

    def f_buf_lin(self):
        self.h_buf_lin = self.BufferLineal(self.canvas, self)
        self.canvas.setMapTool(self.h_buf_lin)
        pixmap = QPixmap(":/icons/bufferlineal.png").scaled(QSize(20, 20), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        cursor = QCursor(pixmap, 0, 0)
        self.canvas.setCursor(cursor)

    def f_sel_Rect(self):
        self.h_rectangulo = self.RectangleMapTool(self.canvas, self)
        self.canvas.setMapTool(self.h_rectangulo)
        pixmap = QPixmap(":/icons/rectangulo.png").scaled(QSize(20, 20), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        cursor = QCursor(pixmap, 0, 0)
        self.canvas.setCursor(cursor)

    def f_sel_libre(self):
        self.h_selLibre = self.SelLibre(self.canvas, self)
        self.canvas.setMapTool(self.h_selLibre)
        pixmap = QPixmap(":/icons/custom.png").scaled(QSize(20, 20), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        cursor = QCursor(pixmap, 0, 0)
        self.canvas.setCursor(cursor)

    def f_sel_circ(self):
        self.h_selCirc = self.Circulo(self.canvas, self)
        self.canvas.setMapTool(self.h_selCirc)
        pixmap = QPixmap(":/icons/circulo.png").scaled(QSize(20, 20), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        cursor = QCursor(pixmap, 0, 0)
        self.canvas.setCursor(cursor)

    def f_id_tool(self):
        self.jare = self.IdTool(self.canvas, self)
        self.canvas.setMapTool(self.jare)
        pixmap = QPixmap(":/icons/info.png").scaled(QSize(20, 20), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        cursor = QCursor(pixmap, 0, 0)
        self.canvas.setCursor(cursor)

    def changeSymbol(self, icon):
        vl = QgsMapLayerRegistry.instance().mapLayersByName("temp")[0]
        symbolLayer = QgsSvgMarkerSymbolLayerV2()
        symbolLayer.setPath("./" + icon)
        symbolLayer.setColor(QColor(qRgb(143, 212, 0)))
        symbolLayer.setFillColor(QColor(qRgb(143, 212, 0)))
        symbolLayer.setOutlineWidth(0.2)
        symbolLayer.setSize(6)
        vl.rendererV2().symbols()[0].changeSymbolLayer(0, symbolLayer)


    def tempcapa(self):
        symbolLayer = QgsSvgMarkerSymbolLayerV2()
        symbolLayer.setPath("./mas.svg")
        symbolLayer.setColor(QColor(qRgb(143, 212, 0)))
        symbolLayer.setFillColor(QColor(qRgb(143, 212, 0)))
        symbolLayer.setOutlineWidth(0.2)
        symbolLayer.setSize(6)
        vl = QgsVectorLayer("Point?crs=EPSG:25830", "temp", "memory")
        vl.startEditing()
        pr = vl.dataProvider()
        pr.addAttributes([QgsField("info", QVariant.String)])
        vl.setCustomProperty("embeddedWidgets/count", "0")
        vl.setCustomProperty("labeling", "pal")
        vl.setCustomProperty("labeling/addDirectionSymbol", "false")
        vl.setCustomProperty("labeling/angleOffset", "0")
        vl.setCustomProperty("labeling/blendMode", "0")
        vl.setCustomProperty("labeling/bufferBlendMode", "0")
        vl.setCustomProperty("labeling/bufferColorA", "255")
        vl.setCustomProperty("labeling/bufferColorB", "255")
        vl.setCustomProperty("labeling/bufferColorG", "255")
        vl.setCustomProperty("labeling/bufferColorR", "255")
        vl.setCustomProperty("labeling/bufferDraw", "false")
        vl.setCustomProperty("labeling/bufferJoinStyle", "128")
        vl.setCustomProperty("labeling/bufferNoFill", "false")
        vl.setCustomProperty("labeling/bufferSize", "1")
        vl.setCustomProperty("labeling/bufferSizeInMapUnits", "false")
        vl.setCustomProperty("labeling/bufferSizeMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/bufferTransp", "0")
        vl.setCustomProperty("labeling/centroidInside", "false")
        vl.setCustomProperty("labeling/centroidWhole", "false")
        vl.setCustomProperty("labeling/decimals", "3")
        vl.setCustomProperty("labeling/displayAll", "true")
        vl.setCustomProperty("labeling/dist", "0")
        vl.setCustomProperty("labeling/distInMapUnits", "false")
        vl.setCustomProperty("labeling/distMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/drawLabels", "true")
        vl.setCustomProperty("labeling/enabled", "true")
        vl.setCustomProperty("labeling/fieldName", "info")
        vl.setCustomProperty("labeling/fitInPolygonOnly", "false")
        vl.setCustomProperty("labeling/fontCapitals", "0")
        vl.setCustomProperty("labeling/fontFamily", "MS Shell Dlg 2")
        vl.setCustomProperty("labeling/fontItalic", "false")
        vl.setCustomProperty("labeling/fontLetterSpacing", "0")
        vl.setCustomProperty("labeling/fontLimitPixelSize", "false")
        vl.setCustomProperty("labeling/fontMaxPixelSize", "10000")
        vl.setCustomProperty("labeling/fontMinPixelSize", "3")
        vl.setCustomProperty("labeling/fontSize", "8.25")
        vl.setCustomProperty("labeling/fontSizeInMapUnits", "false")
        vl.setCustomProperty("labeling/fontSizeMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/fontStrikeout", "false")
        vl.setCustomProperty("labeling/fontUnderline", "false")
        vl.setCustomProperty("labeling/fontWeight", "50")
        vl.setCustomProperty("labeling/fontWordSpacing", "0")
        vl.setCustomProperty("labeling/formatNumbers", "false")
        vl.setCustomProperty("labeling/isExpression", "false")
        vl.setCustomProperty("labeling/labelOffsetInMapUnits", "false")
        vl.setCustomProperty("labeling/labelOffsetMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/labelPerPart", "false")
        vl.setCustomProperty("labeling/leftDirectionSymbol", "&lt;")
        vl.setCustomProperty("labeling/limitNumLabels", "false")
        vl.setCustomProperty("labeling/maxCurvedCharAngleIn", "25")
        vl.setCustomProperty("labeling/maxCurvedCharAngleOut", "-25")
        vl.setCustomProperty("labeling/maxNumLabels", "2000")
        vl.setCustomProperty("labeling/mergeLines", "false")
        vl.setCustomProperty("labeling/minFeatureSize", "0")
        vl.setCustomProperty("labeling/multilineAlign", "3")
        vl.setCustomProperty("labeling/multilineHeight", "1")
        vl.setCustomProperty("labeling/namedStyle", "Normal")
        vl.setCustomProperty("labeling/obstacle", "true")
        vl.setCustomProperty("labeling/obstacleFactor", "1")
        vl.setCustomProperty("labeling/obstacleType", "0")
        vl.setCustomProperty("labeling/offsetType", "0")
        vl.setCustomProperty("labeling/placeDirectionSymbol", "0")
        vl.setCustomProperty("labeling/placement", "1")
        vl.setCustomProperty("labeling/placementFlags", "10")
        vl.setCustomProperty("labeling/plussign", "false")
        vl.setCustomProperty("labeling/predefinedPositionOrder", "TR,TL,BR,BL,R,L,TSR,BSR")
        vl.setCustomProperty("labeling/preserveRotation", "true")
        vl.setCustomProperty("labeling/previewBkgrdColor", "#ffffff")
        vl.setCustomProperty("labeling/priority", "5")
        vl.setCustomProperty("labeling/quadOffset", "4")
        vl.setCustomProperty("labeling/repeatDistance", "0")
        vl.setCustomProperty("labeling/repeatDistanceMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/repeatDistanceUnit", "1")
        vl.setCustomProperty("labeling/reverseDirectionSymbol", "false")
        vl.setCustomProperty("labeling/rightDirectionSymbol", ">")
        vl.setCustomProperty("labeling/scaleMax", "10000000")
        vl.setCustomProperty("labeling/scaleMin", "1")
        vl.setCustomProperty("labeling/scaleVisibility", "false")
        vl.setCustomProperty("labeling/shadowBlendMode", "6")
        vl.setCustomProperty("labeling/shadowColorB", "0")
        vl.setCustomProperty("labeling/shadowColorG", "0")
        vl.setCustomProperty("labeling/shadowColorR", "0")
        vl.setCustomProperty("labeling/shadowDraw", "false")
        vl.setCustomProperty("labeling/shadowOffsetAngle", "135")
        vl.setCustomProperty("labeling/shadowOffsetDist", "1")
        vl.setCustomProperty("labeling/shadowOffsetGlobal", "true")
        vl.setCustomProperty("labeling/shadowOffsetMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/shadowOffsetUnits", "1")
        vl.setCustomProperty("labeling/shadowRadius", "1.5")
        vl.setCustomProperty("labeling/shadowRadiusAlphaOnly", "false")
        vl.setCustomProperty("labeling/shadowRadiusMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/shadowRadiusUnits", "1")
        vl.setCustomProperty("labeling/shadowScale", "100")
        vl.setCustomProperty("labeling/shadowTransparency", "30")
        vl.setCustomProperty("labeling/shadowUnder", "0")
        vl.setCustomProperty("labeling/shapeBlendMode", "0")
        vl.setCustomProperty("labeling/shapeBorderColorA", "255")
        vl.setCustomProperty("labeling/shapeBorderColorB", "0")
        vl.setCustomProperty("labeling/shapeBorderColorG", "212")
        vl.setCustomProperty("labeling/shapeBorderColorR", "143")
        vl.setCustomProperty("labeling/shapeBorderWidth", "1")
        vl.setCustomProperty("labeling/shapeBorderWidthMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/shapeBorderWidthUnits", "1")
        vl.setCustomProperty("labeling/shapeDraw", "true")
        vl.setCustomProperty("labeling/shapeFillColorA", "255")
        vl.setCustomProperty("labeling/shapeFillColorB", "255")
        vl.setCustomProperty("labeling/shapeFillColorG", "255")
        vl.setCustomProperty("labeling/shapeFillColorR", "255")
        vl.setCustomProperty("labeling/shapeJoinStyle", "64")
        vl.setCustomProperty("labeling/shapeOffsetMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/shapeOffsetUnits", "1")
        vl.setCustomProperty("labeling/shapeOffsetX", "0")
        vl.setCustomProperty("labeling/shapeOffsetY", "0")
        vl.setCustomProperty("labeling/shapeRadiiMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/shapeRadiiUnits", "1")
        vl.setCustomProperty("labeling/shapeRadiiX", "0")
        vl.setCustomProperty("labeling/shapeRadiiY", "0")
        vl.setCustomProperty("labeling/shapeRotation", "0")
        vl.setCustomProperty("labeling/shapeRotationType", "0")
        vl.setCustomProperty("labeling/shapeSVGFile", "")
        vl.setCustomProperty("labeling/shapeSizeMapUnitScale", "0,0,0,0,0,0")
        vl.setCustomProperty("labeling/shapeSizeType", "0")
        vl.setCustomProperty("labeling/shapeSizeUnits", "1")
        vl.setCustomProperty("labeling/shapeSizeX", "0")
        vl.setCustomProperty("labeling/shapeSizeY", "0")
        vl.setCustomProperty("labeling/shapeTransparency", "0")
        vl.setCustomProperty("labeling/shapeType", "2")
        vl.setCustomProperty("labeling/substitutions", "&lt;substitutions)")
        vl.setCustomProperty("labeling/textColorA", "255")
        vl.setCustomProperty("labeling/textColorB", "0")
        vl.setCustomProperty("labeling/textColorG", "0")
        vl.setCustomProperty("labeling/textColorR", "0")
        vl.setCustomProperty("labeling/textTransp", "0")
        vl.setCustomProperty("labeling/upsidedownLabels", "0")
        vl.setCustomProperty("labeling/useSubstitutions", "false")
        vl.setCustomProperty("labeling/wrapChar", "")
        vl.setCustomProperty("labeling/xOffset", "0")
        vl.setCustomProperty("labeling/yOffset", "-7")
        vl.setCustomProperty("labeling/zIndex", "10")
        vl.commitChanges()
        vl.rendererV2().symbols()[0].changeSymbolLayer(0, symbolLayer)
        QgsMapLayerRegistry.instance().addMapLayer(vl)


    def CargaCapa(self, nombre, crs, label):
        sql = ""
        uri = QgsDataSourceURI()
        uri.setConnection("9.56.3.159", "5432", dbname, "postgres", "123456", QgsDataSourceURI.SSLdisable)
        uri.setDataSource("cartografia", nombre, "geom", sql, "gid")
        uri.setSrid(crs)
        vlayer = QgsVectorLayer(uri.uri(), nombre, "postgres")
        vlayer.setLayerName(label)
        QgsMapLayerRegistry.instance().addMapLayer(vlayer)
        self.canvas.setExtent(vlayer.extent())
        self.jar.append(QgsMapCanvasLayer(vlayer))


    def PNOA(self):
        # url = "contextualWMSLegend=0&crs=EPSG:25830&dpiMode=7&featureCount=10&format=image/png&layers=OI.OrthoimageCoverage&password=admin&styles=default&url=http://www.ign.es/wms-inspire/pnoa-ma&username=admin"
        #url = "contextualWMSLegend=0&crs=EPSG:4258&dpiMode=7&featureCount=10&format=image/jpeg&layers=OI.OrthoimageCoverage&styles=default&tileMatrixSet=EPSG:4258&url=http://www.ign.es/wmts/pnoa-ma"
        #layer = QgsRasterLayer(url, "PNOA", "wms")
        # url = os.getcwd().replace("\\", "/")
        # url = url + "/a.xml"
        # print url
        # layer = QgsRasterLayer(url, "PNOA", "gdal")
        # layer.setLayerName("PNOA")
        # QgsMapLayerRegistry.instance().addMapLayer(layer)
        # self.jar.append(QgsMapCanvasLayer(layer))
        # print "PNOA", layer.isValid(), layer.crs().authid()
        #----
        xml = """<GDAL_WMS>
<Service name="TMS">
<ServerUrl>http://mt.google.com/vt/lyrs=s&amp;x=${x}&amp;y=${y}&amp;z=${z}</ServerUrl>
<CRS>EPSG:3857</CRS>
</Service>
<DataWindow>
<UpperLeftX>-20037508.34</UpperLeftX>
<UpperLeftY>20037508.34</UpperLeftY>
<LowerRightX>20037508.34</LowerRightX>
<LowerRightY>-20037508.34</LowerRightY>
<TileLevel>20</TileLevel>
<TileCountX>1</TileCountX>
<TileCountY>1</TileCountY>
<YOrigin>top</YOrigin>
</DataWindow>
<Projection>EPSG:3857</Projection>
<BlockSizeX>256</BlockSizeX>
<BlockSizeY>256</BlockSizeY>
<BandsCount>3</BandsCount>
<MaxConnections>5</MaxConnections>
<Cache/>
<ZeroBlockHttpCodes>204,404,403</ZeroBlockHttpCodes>
</GDAL_WMS>"""
#         xml = """<GDAL_WMS>
#         <Service name="VirtualEarth">
#         <ServerUrl>
#         http://a${server_num}.ortho.tiles.virtualearth.net/tiles/a${quadkey}.jpeg?g=90
#         </ServerUrl>
#         <CRS>EPSG:3857</CRS>
#         </Service>
#         <Projection>EPSG:3857</Projection>
#         <MaxConnections>4</MaxConnections>
#         <Cache/>
#         </GDAL_WMS>"""
        vfn = "/vsimem/osm.xml"
        gdal.FileFromMemBuffer(vfn, xml)
        layer = QgsRasterLayer(vfn, "PNOA", "gdal")
        layer.setLayerName("PNOA")
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        #self.jar.append(QgsMapCanvasLayer(layer))
        print "PNOA", layer.isValid(), layer.crs().description()

    def actTitulo(self):
        #
        self.escala.setText("Escala: 1:" + str(int(self.canvas.scale())))


    def showSeleccion(self):
        if self.c_seleccion.isChecked():
            self.g_seleccion.show()
            print self.sel_rect.toolTip()
        else:
            self.g_seleccion.hide()

    def showCriterios(self):
        try:
            if self.c_criterios.isChecked():
                self.criterios = pool_Window(self.canvas)
                cargacriterios(self.criterios)
                self.criterios.show()
                self.visibleCriterios = True
            else:
                self.criterios.close()
                self.visibleCriterios = False
        except:
            pass

    def showBusquedas(self):
        if self.c_Busquedas.isChecked():
            self.g_busquedas.show()
        else:
            self.g_busquedas.hide()
            borraTemp()

    def showEstadisticas(self):
        if self.c_estadisticas.isChecked():
            self.g_estadisticas.show()
            self.cb_stats.clear()
            self.cb_stats.addItems(['Desconocidos'])
            #actEstadisticas(self)
        else:
            self.g_estadisticas.hide()

    def showCapas(self):
        if self.c_capas.isChecked():
            self.g_capas.show()
        else:
            self.g_capas.hide()

    def showResultados(self):
        if self.c_resultados.isChecked():
            self.g_resultados.show()
        else:
            self.g_resultados.hide()

    def visualizaCapa(self):
        capas = []
        capas.append(QgsMapCanvasLayer(QgsMapLayerRegistry.instance().mapLayersByName("temp")[0]))
        pnoa = False
        for jar in range(self.listCapas.count()):
            if self.listCapas.itemWidget(self.listCapas.item(jar)).check.isChecked() == True:
                c = self.listCapas.itemWidget(self.listCapas.item(jar)).check.text()
                if c == "PNOA":
                    pnoa = True

                try:
                    capas.append(QgsMapCanvasLayer(QgsMapLayerRegistry.instance().mapLayersByName(c)[0]))
                except:
                    Mensaje("Capa " + c + "no figura en QgsMapLayerRegistry")
        if not self.csat.satelite.isChecked():
            capas.append(QgsMapCanvasLayer(QgsMapLayerRegistry.instance().mapLayersByName("PNOA")[0]))
            pnoa = True

        self.canvas.setLayerSet(capas)
        if pnoa:
            layer = QgsMapLayerRegistry.instance().mapLayersByName("Construcciones")[0]
            style = layer.getStyleFromDatabase("10", "constru_pnoa")
            layer.applyNamedStyle(style)
        else:
            layer = QgsMapLayerRegistry.instance().mapLayersByName("Construcciones")[0]
            style = layer.getStyleFromDatabase("5", "constru")
            layer.applyNamedStyle(style)

        self.canvas.refresh()

    def showStats(self, tipo):

        labels = []
        values = []
        colors = []
        if tipo == 'Desconocidos':
             datos = actDesc()
             for dato, valor, color in datos:
                labels.append(dato)
                values.append(valor)
                colors.append(color)


        plotly.offline.plot({
            "data": [Pie(labels=labels, values=values, hoverinfo='label+percent', textinfo='value',
                         marker=dict(colors=colors, line=dict(color='#000000', width=0.5)))],
            "layout": Layout(title="Operativo de desconocidos")
        }, filename="desconocidos.html", include_plotlyjs=True)

    def resizeEvent(self, event):
        self.panel_resultados.reubica(self.canvas)
        self.csat.reubica(self.canvas)
        if self.visibleCriterios:
            self.criterios.reubica(self.canvas)
        if self.titWindowActive:
            self.titWindow.reubica(self.canvas)

def lanzaDesc(form, canvas):
    w = ventanaDesconocidos(form, canvas)
    q = Queue()
    thread = Thread(target=depuraDesconocidos, args=(q,))
    p = loading("Realizando consulta espacial", canvas)
    p.show()
    thread.start()
    while thread.isAlive():
        QApplication.processEvents()
    p.close()
    jar = q.get()
    for a in jar:
        b = invDescGraf(a)
        qlwi = QListWidgetItem()
        qlwi.setSizeHint(b.size())
        w.ldesc.addItem(qlwi)
        w.ldesc.setItemWidget(qlwi, b)
    w.show()

def depuraDesconocidos(q):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    # SELECCIONAMOS LAS FINCAS CON DESCONOCIDO Y UN ÚNICO CARGO
    sql = "SELECT * FROM (" \
          "SELECT " \
          "f.refcat," \
          "f.ref_completa, " \
          "f.nombre, " \
          "f.dni," \
          "COUNT(f.refcat) as cuenta " \
          "FROM fin f INNER JOIN cartografia.parcela p USING(refcat) " \
          "WHERE desconocido=TRUE " \
          "GROUP BY ref_completa, refcat, nombre, dni) as t " \
          "WHERE cuenta=1"
    cur.execute(sql)
    fincas = cur.fetchall()
    listacandidatos = []
    # REALIZAMOS LA CONSULTA ESPACIAL PARA CADA FINCA CRUZANDO CON LOS CONTADORES
    for finca in fincas:
        sql = "WITH total AS ( " \
        "SELECT " \
	    "CASE WHEN SUM(ST_Area(ST_Intersection(ST_Buffer(d.geom, 5), p.geom))) > 0 " \
              "THEN SUM(ST_Area(ST_Intersection(ST_Buffer(d.geom, 5), p.geom))) " \
              "ELSE 1 " \
              "END as suma " \
        "FROM " \
	    "cartografia.parcela p, cartografia.puntos_desc d " \
        "WHERE " \
	    "p.refcat=%(refcat)s) " \
        "SELECT " \
        "d.gid, " \
        "ST_Distance(d.geom, p.geom) as distancia, " \
        "ST_AsText(ST_Buffer(d.geom, 5)) as buff, " \
        "ST_Area(ST_Intersection(ST_Buffer(d.geom, 5), p.geom)) as area_interseccion, " \
        "CASE WHEN ST_Distance(d.geom, p.geom) = 0 THEN 100 " \
        "ELSE ST_Area(ST_Intersection(ST_Buffer(d.geom, 5), p.geom))/t.suma * 100 " \
        "END as probabilidad, " \
        "STX_Extract(ST_Intersection(ST_Buffer(d.geom, 5), p.geom),2)::geometry(MultiPolygon, 25830) as ngeom, " \
        "d.titular, " \
        "d.dni " \
        "FROM " \
        "cartografia.parcela p, cartografia.puntos_desc d, total t " \
        "WHERE p.refcat = %(refcat)s AND ST_Area(ST_Intersection(ST_Buffer(d.geom, 5), p.geom)) > 0 " \
        "ORDER BY " \
        "probabilidad"
        cur.execute(sql, {"refcat": finca[0]})
        analisis = cur.fetchall()
        probabilidad = 0
        candidato = []
        contadores = []
        valido = False
        for gid, dist, buff, area, prob, inter, titular, dni in analisis:
            # print "GID:" + str(a[0]), "DISTANCIA:" + str(a[1]), "INTERSECCION:" + str(a[3]), "PROBABILIDAD:" + str(a[4])\
            #     , "NOMBRE:" + str(a[6]), "DNI:" + str(a[7]), "FINCA:" + finca[0]
            # SELECCIONAMOS EL DE MAYOR PROBABILIDAD
            if prob > probabilidad:
                probabilidad = prob
                candidato = [gid, dist, buff, area, prob, inter, titular, dni, valido]
        if candidato != []:
            # COMPROBAMOS SI EL CONTADOR ESTÁ DENTRO DE LA FINCA ANTES DE COMPROBAR EL MARGEN
            if candidato[4] == 100:
                candidato[8] = True
            else:
                for gid, dist, buff, area, prob, inter, titular, dni in analisis:
                    if gid != candidato[0]:
                        contador = [gid, dist, buff, area, prob, inter, titular, dni, valido]
                        contadores.append(contador)
                        if candidato[4] - prob < 10:
                            candidato[8] = False
                        else:
                            candidato[8] = True
        if probabilidad > 0:
            i = invDesc(finca[0], finca[1], finca[2], finca[3])
            i.addCandidato(candidato)
            for contador in contadores:
                i.addContador(contador)
            sql = "WITH temp as (SELECT ST_Buffer(geom, 0.1) as geom FROM cartografia.parcela WHERE refcat=%(refcat)s) " \
                  "SELECT refcat FROM cartografia.parcela p, temp t WHERE ST_Intersects(p.geom, t.geom);"
            cur.execute(sql, {"refcat": finca[0]})
            col = cur.fetchall()
            for colindante in col:
                i.addColindante(colindante[0])
            listacandidatos.append(i)
    conn.close()
    q.put(listacandidatos)

def ventana(window, lista, texto):
    j = w(window, texto, lista.lista)
    qlwi = QListWidgetItem(lista.lista)
    qlwi.setSizeHint(j.size())
    lista.lista.addItem(qlwi)
    lista.lista.setItemWidget(qlwi, j)

def sombra():
    s = QGraphicsDropShadowEffect()
    s.setBlurRadius(9.0)
    s.setColor(QColor(0, 0, 0, 160))
    s.setOffset(4.0)
    return s


def getRefs(canvas, g, form):
    p = loading("Representando parcelas seleccionadas", canvas)
    p.show()
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    geometria = g.exportToWkt()
    sql = """SELECT ST_AsText(p.geom), p.refcat FROM cartografia.parcela p \
            WHERE ST_Within(ST_Centroid(p.geom), ST_GeomFromText(%(geom)s, 25830)) ORDER BY p.refcat;"""
    cur.execute(sql, {"geom": geometria})
    rows = cur.fetchall()
    canvas.freeze()
    geometrias = []
    fincas = []
    for row in rows:
        geometrias.append(row[0])
        fincas.append(row[1])
    form.panel_resultados.finca.setText(str(cur.rowcount) + " fincas seleccionadas.")
    Resaltador(canvas, geometrias, form)
    muestraFincas(fincas, form)
    canvas.freeze(False)
    canvas.refresh()
    p.close()


def Resaltador(canvas, geometrias, form):
    # rb = QgsRubberBand(canvas, False)
    # rb.reset(QGis.Polygon)
    # rb.setBorderColor(QColor(143, 212, 0, 255))
    # rb.setFillColor(QColor(143, 212, 0, 200))
    # rb.setWidth(1)
    # rb.hide()
    rb = form.rubberBand
    for geometria in geometrias:
        rb.addGeometry(QgsGeometry.fromWkt(geometria), None)
        QApplication.processEvents()
    rb.show()

def getReferencia(canvas, g, form):
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    geometria = g.exportToWkt()
    sql = """SELECT refcat, ST_AsText(geom) FROM cartografia.parcela p WHERE ST_Within(ST_GeomFromText(%(geom)s, 25830), geom);"""
    cur.execute(sql, {"geom": geometria})
    rows = cur.fetchall()
    geometrias = []
    fincas = []
    for row in rows:
        geometrias.append(row[1])
        fincas.append(row[0])
    Resaltador(canvas, geometrias, form)
    muestraFincas(fincas, form)
    form.panel_resultados.finca.setText("Finca: " + row[0])

def limpiar(canvas, form):
    for item in canvas.scene().items():
        if issubclass(type(item), QgsRubberBand):
            print item
            item.reset(QGis.Polygon)
    form.panel_resultados.finca.setText(u"Sin selección")
    #form.fincas.clear()
    #form.direccion.setText("")
    #form.resultados_ibi.clear()
    #form.resultados_vados.clear()
    #form.resultados_basuras.clear()
    #form.resultados_agua.clear()
    #form.resultados_expedientes.clear()


def muestraFincas(fincas, form):
    form.fincas.clear()
    for finca in fincas:
        form.fincas.addItem(finca)

def datosFin(refcat, form):
    form.resultados_ibi.clear()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT CONCAT(siglavia, ' ', nombrevia, ' ', numeropolicia) AS direccion, numerocargo,
    CONCAT(dni, letradni) AS dni, nombre, ref_completa, desconocido, nif_candidato, nombre_candidato FROM public.fin
    WHERE refcat=%(ref)s ORDER BY numerocargo;"""
    cur.execute(sql, {"ref": refcat})
    rows = cur.fetchall()

    direccion = ""
    for row in rows:
        direccion = row[0]
        c = ValorWidget(row[1], row[2], row[3], row[4], form, row[5], row[6], row[7], "IBI")
        qlwi = QListWidgetItem(form.resultados_ibi)
        qlwi.setSizeHint(QSize(250, 65))
        form.resultados_ibi.addItem(qlwi)
        form.resultados_ibi.setItemWidget(qlwi, c)
    form.direccion.setText(direccion)

def datosVados(refcat, form):
    form.resultados_vados.clear()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT n_fijo, desc_ot, importe_sub_1, ref_completa FROM public.vados WHERE refcat=%(ref)s;"""
    cur.execute(sql, {"ref": refcat})
    rows = cur.fetchall()
    for row in rows:
        c = ValorWidget(row[0], str(row[2])+u" €", row[1], row[3], form, False, None, None, "VADOS")
        c.dato1.setText("Placa:")
        c.dato2.setText("Importe:")
        c.dato3.setText("OT:")
        c.titulo.setText("Datos del vado")
        c.l_info_1.setText("Tarifa:")
        c.l_info_2.setText("Metros:")
        c.l_info_3.setText("S.P:")


        qlwi = QListWidgetItem(form.resultados_vados)
        qlwi.setSizeHint(QSize(250, 65))
        form.resultados_vados.addItem(qlwi)
        form.resultados_vados.setItemWidget(qlwi, c)

def datosBasura(refcat, form):
    form.resultados_basuras.clear()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT n_fijo, desc_ot, nif_sp_ot, ref_completa FROM public.basuras WHERE refcat=%(ref)s GROUP BY n_fijo, desc_ot, nif_sp_ot, ref_completa;"""
    cur.execute(sql, {"ref": refcat})
    rows = cur.fetchall()
    for row in rows:
        c = ValorWidget(row[0], str(row[2]), row[1], row[3], form, False, None, None, "BASURA")
        c.dato1.setText(u"Nº Fijo:")
        c.dato2.setText("NIF:")
        c.dato3.setText("OT:")
        c.titulo.setText("Recogida de residuos")
        c.l_info_1.setText("Tarifa:")
        c.l_info_2.setText("Importe:")
        c.l_info_3.setText("S.P:")


        qlwi = QListWidgetItem(form.resultados_basuras)
        qlwi.setSizeHint(QSize(250, 65))
        form.resultados_basuras.addItem(qlwi)
        form.resultados_basuras.setItemWidget(qlwi, c)

def datosAguas(refcat, form):
    form.resultados_agua.clear()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT numfijo, nombre, nif, ref_completa FROM public.aguas WHERE refcat=%(ref)s;"""
    cur.execute(sql, {"ref": refcat})
    rows = cur.fetchall()
    for row in rows:
        c = ValorWidget(row[0], str(row[2]), row[1], row[3], form, False, None, None, "AGUAS")
        c.dato1.setText(u"Nº Fijo:")
        c.dato2.setText("NIF:")
        c.dato3.setText("S.P:")
        c.titulo.setText("Aguas")
        c.l_info_1.setText("L. Anterior:")
        c.l_info_2.setText("L.Actual:")
        c.l_info_3.setText("Importe:")


        qlwi = QListWidgetItem(form.resultados_agua)
        qlwi.setSizeHint(QSize(250, 65))
        form.resultados_agua.addItem(qlwi)
        form.resultados_agua.setItemWidget(qlwi, c)

def datosExpedientes(refcat, form):
    form.resultados_expedientes.clear()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT numero_rege, CONCAT(cod_tdoc, '-', cod_sdoc) AS tipo, fecha_rege, ref_completa FROM public.expedientes WHERE refcat=%(ref)s;"""
    cur.execute(sql, {"ref": refcat})
    rows = cur.fetchall()
    for row in rows:
        c = ValorWidget(str(row[2].date().strftime("%d/%m/%Y")), row[1], row[0], row[3], form, False, None, None, "EXPEDIENTES")
        c.dato1.setText("Registro:")
        c.dato2.setText("Tipo:")
        c.dato3.setText(u"Nº Exp:")
        c.titulo.setText("Expediente")
        #c.l_info_1.setText("L. Anterior:")
        #c.l_info_2.setText("L.Actual:")
        #c.l_info_3.setText("Importe:")
        QWidget().setLayout(c.info_ot.layout())
        c.nLayout = QVBoxLayout()
        c.nDato = QTextEdit()
        c.nDato.setMaximumWidth(235)
        c.nLayout.addWidget(c.nDato)
        c.info_ot.setLayout(c.nLayout)




        qlwi = QListWidgetItem(form.resultados_expedientes)
        qlwi.setSizeHint(QSize(250, 65))
        form.resultados_expedientes.addItem(qlwi)
        form.resultados_expedientes.setItemWidget(qlwi, c)

def datosPlusvalias(refcat, form):
    form.resultados_plusvalias.clear()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT numero_cargo, obj_trib_valo, importe_valo, id_valor FROM public.plusvalia WHERE refcat=%(ref)s;"""
    cur.execute(sql, {"ref": refcat})
    rows = cur.fetchall()
    for row in rows:
        c = ValorWidget(row[0], str(row[2]/100) + u" €", row[1], row[3], form, False, None, None, "PLUSVALIAS")
        c.dato1.setText("Cargo:")
        c.dato2.setText("Importe:")
        c.dato3.setText("OT:")
        c.titulo.setText("Detalle del valor")
        c.l_info_1.setText("NIF:")
        c.l_info_2.setText("Nombre:")
        c.l_info_3.setText("Estado:")
        qlwi = QListWidgetItem(form.resultados_plusvalias)
        qlwi.setSizeHint(QSize(250, 65))
        form.resultados_plusvalias.addItem(qlwi)
        form.resultados_plusvalias.setItemWidget(qlwi, c)

def datosIcio(refcat, form):
    form.resultados_icio.clear()
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT ejercicio, direccion, nif_perg, id_valor FROM public.icio WHERE refcat=%(ref)s AND \
    descr_conc='IMPUESTO SOBRE CONST.INST.OBRA';"""
    cur.execute(sql, {"ref": refcat})
    rows = cur.fetchall()
    for row in rows:
        c = ValorWidget(row[0], row[2], row[1], row[3], form, False, None, None, "ICIO")
        c.dato1.setText("Ejercicio:")
        c.dato2.setText("NIF:")
        c.dato3.setText("OT:")
        c.titulo.setText("Detalle del valor")
        c.l_info_1.setText("Importe:")
        c.l_info_2.setText("S.P:")
        c.l_info_3.setText("Estado:")
        qlwi = QListWidgetItem(form.resultados_icio)
        qlwi.setSizeHint(QSize(250, 65))
        form.resultados_icio.addItem(qlwi)
        form.resultados_icio.setItemWidget(qlwi, c)

def getDatosIbi(obj):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT estado, importe, nombre FROM public.datos WHERE ref_completa=%(ref)s;"""
    cur.execute(sql, {"ref": obj.getRefCompleta()})
    rows = cur.fetchall()
    for row in rows:
        obj.e_info_1.setText(str(row[1]/100)+u" €")
        obj.e_info_2.setText(row[0])
        obj.l_info_3.setText("S.P:")
        obj.e_info_3.setText(row[2])


def getDatosVados(obj):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT nombre_sp, descripcion_tarifa_sub_1, n_unidades_sub_1 FROM public.vados WHERE ref_completa=%(ref)s;"""
    cur.execute(sql, {"ref": obj.getRefCompleta()})
    rows = cur.fetchall()
    for row in rows:
        obj.e_info_1.setText(row[1])
        obj.e_info_2.setText(str(row[2])+ " m.")
        obj.e_info_3.setText(row[0])

def getDatosBasura(obj):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT nombre_sp, descripcion_tarifa_sub_1, importe_conc FROM public.basuras WHERE ref_completa=%(ref)s;"""
    cur.execute(sql, {"ref": obj.getRefCompleta()})
    rows = cur.fetchall()
    for row in rows:
        obj.e_info_1.setText(row[1])
        obj.e_info_2.setText(str(row[2]) + u" €")
        obj.e_info_3.setText(row[0])

def getDatosAguas(obj):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT lectant, lectact, importe FROM public.aguas WHERE ref_completa=%(ref)s;"""
    cur.execute(sql, {"ref": obj.getRefCompleta()})
    rows = cur.fetchall()
    for row in rows:
        obj.e_info_1.setText(str(row[0]))
        obj.e_info_2.setText(str(row[1]))
        obj.e_info_3.setText(str(row[2]/100)+ u" €")

def getDatosExpediente(obj):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT extracto_rege FROM public.expedientes WHERE ref_completa=%(ref)s;"""
    cur.execute(sql, {"ref": obj.getRefCompleta()})
    rows = cur.fetchall()
    for row in rows:
        obj.nDato.setText(row[0])

def getDatosPlusvalia(obj):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT nif_perg, nombre_perg, cod_descrp_trad FROM public.plusvalia WHERE id_valor=%(ref)s;"""
    cur.execute(sql, {"ref": obj.getRefCompleta()})
    rows = cur.fetchall()
    for row in rows:
        obj.e_info_1.setText(str(row[0]))
        obj.e_info_2.setText(str(row[1]))
        obj.e_info_3.setText(str(row[2]))

def getDatosIcio(obj):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT importe, nombre_perg, estado FROM public.icio WHERE id_valor=%(ref)s;"""
    cur.execute(sql, {"ref": obj.getRefCompleta()})
    rows = cur.fetchall()
    for row in rows:
        obj.e_info_1.setText(str(row[0])+u" €")
        obj.e_info_2.setText(str(row[1]))
        obj.e_info_3.setText(str(row[2]))

def getCentroid(refcat, form):
    if refcat != "":
        #borraTemp()
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
        conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
        cur = conn.cursor()
        sql = """SELECT ST_AsText(p.geom) AS geom FROM cartografia.parcela p WHERE refcat=%(ref)s;"""
        cur.execute(sql, {"ref": refcat})
        rows = cur.fetchall()
        form.rb.reset()
        print "asde", refcat
        for row in rows:
            geom = row[0]
            form.rb.addGeometry(QgsGeometry.fromWkt(geom), None)

def addTempPoint(geom, info):
    layer = QgsMapLayerRegistry.instance().mapLayersByName("temp")[0]
    layer.startEditing()
    pr = layer.dataProvider()
    campos = layer.fields()
    fet = QgsFeature()
    fet.setGeometry(QgsGeometry.fromWkt(geom))
    fet.setFields(campos)
    fet['info'] = info
    pr.addFeatures([fet])
    layer.updateExtents()
    layer.commitChanges()

def borraTemp():
    layer = QgsMapLayerRegistry.instance().mapLayersByName("temp")[0]
    layer.startEditing()
    for feature in layer.getFeatures():
        layer.deleteFeature(feature.id())
    layer.commitChanges()






@pyqtSlot()
def eliminaVentana(lista, contenedor):
    for i in range(0, lista.count()):
        c = lista.item(i)
        if lista.itemWidget(c) == contenedor:
            lista.takeItem(i)




@pyqtSlot()
def resizeResultado(self, form, contenedor):
    if contenedor == "IBI":
        for i in range(0, form.resultados_ibi.count(), 1):
            c = form.resultados_ibi.item(i)
            if form.resultados_ibi.itemWidget(c) == self.sender():
                print c
                if self.sender().info_ot.isVisible():
                    self.sender().info_ot.hide()
                    c.setSizeHint(self.sender().sizeHint())

                else:
                    self.sender().info_ot.show()
                    getDatosIbi(self.sender())
                    c.setSizeHint(self.sender().sizeHint())
    elif contenedor == "VADOS":
        for i in range(0, form.resultados_vados.count(), 1):
            c = form.resultados_vados.item(i)
            if form.resultados_vados.itemWidget(c) == self.sender():
                print c
                if self.sender().info_ot.isVisible():
                    self.sender().info_ot.hide()
                    c.setSizeHint(self.sender().sizeHint())

                else:
                    self.sender().info_ot.show()
                    getDatosVados(self.sender())
                    c.setSizeHint(self.sender().sizeHint())
    elif contenedor == "BASURA":
        for i in range(0, form.resultados_basuras.count(), 1):
            c = form.resultados_basuras.item(i)
            if form.resultados_basuras.itemWidget(c) == self.sender():
                print c
                if self.sender().info_ot.isVisible():
                    self.sender().info_ot.hide()
                    c.setSizeHint(self.sender().sizeHint())

                else:
                    self.sender().info_ot.show()
                    getDatosBasura(self.sender())
                    c.setSizeHint(self.sender().sizeHint())
    elif contenedor == "AGUAS":
        for i in range(0, form.resultados_agua.count(), 1):
            c = form.resultados_agua.item(i)
            if form.resultados_agua.itemWidget(c) == self.sender():
                print c
                if self.sender().info_ot.isVisible():
                    self.sender().info_ot.hide()
                    c.setSizeHint(self.sender().sizeHint())

                else:
                    self.sender().info_ot.show()
                    getDatosAguas(self.sender())
                    c.setSizeHint(self.sender().sizeHint())

    elif contenedor == "EXPEDIENTES":
        for i in range(0, form.resultados_expedientes.count(), 1):
            c = form.resultados_expedientes.item(i)
            if form.resultados_expedientes.itemWidget(c) == self.sender():
                print c
                if self.sender().info_ot.isVisible():
                    self.sender().info_ot.hide()
                    c.setSizeHint(self.sender().sizeHint())

                else:
                    self.sender().info_ot.show()
                    getDatosExpediente(self.sender())
                    c.setSizeHint(self.sender().sizeHint())

    elif contenedor == "PLUSVALIAS":
        for i in range(0, form.resultados_plusvalias.count(), 1):
            c = form.resultados_plusvalias.item(i)
            if form.resultados_plusvalias.itemWidget(c) == self.sender():
                print c
                if self.sender().info_ot.isVisible():
                    self.sender().info_ot.hide()
                    c.setSizeHint(self.sender().sizeHint())

                else:
                    self.sender().info_ot.show()
                    getDatosPlusvalia(self.sender())
                    c.setSizeHint(self.sender().sizeHint())

    elif contenedor == "ICIO":
        for i in range(0, form.resultados_icio.count(), 1):
            c = form.resultados_icio.item(i)
            if form.resultados_icio.itemWidget(c) == self.sender():
                print c
                if self.sender().info_ot.isVisible():
                    self.sender().info_ot.hide()
                    c.setSizeHint(self.sender().sizeHint())

                else:
                    self.sender().info_ot.show()
                    getDatosIcio(self.sender())
                    c.setSizeHint(self.sender().sizeHint())

def getInfo(refcat, form):
    print getCentroid(refcat, form)
    datosFin(refcat, form)
    datosVados(refcat, form)
    datosBasura(refcat, form)
    datosAguas(refcat, form)
    datosExpedientes(refcat, form)
    datosPlusvalias(refcat, form)
    datosIcio(refcat, form)

def montaSQL(form):
    for i in range(0, form.lBusquedas.count()):
        crt = form.lBusquedas.itemWidget(form.lBusquedas.item(i))
        if type(crt.criterio) == QComboBox:
            if crt.operador == "=":
                criterio = crt.campo + " " + crt.operador + "'" + crt.criterio.currentText().upper() + "'"
            else:
                criterio = crt.campo + " " + crt.operador + u"'%" + crt.criterio.currentText().upper() + u"%'"
            print criterio
        else:
            if crt.operador == "=":
                criterio = crt.campo + " " + crt.operador + "'" + crt.criterio.text().upper() + "'"
            else:
                criterio = crt.campo + " " + crt.operador + u"'%" + crt.criterio.text().upper() + u"%'"
            print criterio
        # sql = """SELECT \
        #          ST_AsText(ST_Centroid((p.geom))) AS geom, \
        #          d.""" + crt.campo2 + """ as importe \
        #          FROM cartografia.parcela p INNER JOIN """ + crt.tabla + """ d \
        #          USING(refcat) \
        #          WHERE """ + criterio + """GROUP BY p.geom, d.""" + crt.campo2 + """;"""
        if crt.tabla == "public.datos":
            sql = """SELECT \
                             ST_AsText(ST_Centroid((p.geom))) AS geom, \
                             """ + crt.campo2 + """ as importe \
                             FROM cartografia.parcela p INNER JOIN """ + crt.tabla + """ \
                             USING(refcat) \
                             WHERE """ + criterio + """GROUP BY p.geom, public.datos.refcat;"""
        elif crt.tabla == "public.basuras":
            sql = """SELECT \
                                         ST_AsText(ST_Centroid((p.geom))) AS geom, \
                                         """ + crt.campo2 + """ as importe \
                                         FROM cartografia.parcela p INNER JOIN """ + crt.tabla + """ \
                                         USING(refcat) \
                                         WHERE """ + criterio + """GROUP BY p.geom, public.basuras.refcat;"""
        elif crt.tabla == "public.vados":
            sql = """SELECT \
                                         ST_AsText(ST_Centroid((p.geom))) AS geom, \
                                         """ + crt.campo2 + """ as importe \
                                         FROM cartografia.parcela p INNER JOIN """ + crt.tabla + """ \
                                         USING(refcat) \
                                         WHERE """ + criterio + """GROUP BY p.geom, public.vados.refcat;"""

        if crt.campo == "*" and crt.tabla =="cartografia.multas":
            sql = """SELECT \
                             ST_AsText(ST_Centroid((p.geom))) AS geom, \
                             CONCAT(p.infraccion, ' // ', p.objeto) as campo2 \
                             FROM cartografia.multas p;"""
        if crt.campo == "res" and crt.tabla =="public.fin":
            sql = """SELECT geom,
            MIN(origen)
            FROM cartografia.v_desc
            GROUP BY geom;"""
        if crt.tabla == "public.fin" and crt.campo!= "res":
            a = crt.criterio.currentIndex()
            if a == 0:
                criterio = u"desconocido=TRUE "
            elif a == 1:
                criterio = u"desconocido=TRUE AND nombre NOT LIKE '%INVESTIG%' "
            elif a ==2:
                criterio = u"desconocido=TRUE AND nombre LIKE '%INVESTIG%'"

            sql = """SELECT \
                            ST_AsText(ST_Centroid((g.geom))) AS geom,
                            CONCAT(p.numerocargo, ' // ', p.valorcatastral) as campo2,
                            COUNT(p.numerocargo) AS cuenta
                            FROM public.fin p INNER JOIN cartografia.parcela g USING(refcat)
                            WHERE """ + criterio + """GROUP BY g.geom, p.refcat, p.numerocargo, p.valorcatastral;"""

    Consulta(form, sql, crt.tabla)

def Consulta(form, sql, tabla):
    conn = psycopg2.connect("dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    # sql = """SELECT \
    #     ST_AsText(ST_Centroid((p.geom))) AS geom, \
    #     d.numero_rege \
    #     FROM cartografia.parcela p INNER JOIN public.expedientes d \
    #     USING(refcat) \
    #     WHERE d.cod_tdoc=1 GROUP BY d.numero_rege, p.geom;"""

    cur.execute(sql)
    rows = cur.fetchall()
    borraTemp()
    for row in rows:
        #print row[1], row[0]
        addTempPoint(row[0], str(row[1]))
    if tabla == "public.datos":
        form.changeSymbol("ibi.svg")
    elif tabla == "public.basuras":
        form.changeSymbol("basura.svg")
    elif tabla == "public.vados":
        form.changeSymbol("vados.svg")
    elif tabla == "cartografia.multas":
        form.changeSymbol("policia.svg")
    elif tabla == "public.fin":
        form.changeSymbol("desc.svg")
    form.panel_resultados.finca.setText(str(len(rows)) + " resultados.")
    form.panel_resultados.show()


    form.canvas.refresh()
    form.lBusquedas.clear()
    form.c_criterios.setChecked(False)
    form.showCriterios()
    print sql




def cargacriterios(widget):
    listacriterios = [
        (" LIKE ", "public.datos", "refcat", "CONCAT(public.datos.refcat, ' // ', SUM(public.datos.importe)/100)", ":/icons/25694.png", True, 0, "REFERENCIA CATASTRAL", "ibi", []),
        (" LIKE ", "public.datos", "estado", "CONCAT(public.datos.refcat, ' // ', SUM(public.datos.importe)/100)", ":/icons/25694.png", False, 1, "ESTADO", "ibi", ["Voluntaria", "Ejecutiva", "Fraccionado", "Pendiente"]),
        ("=", "public.datos", "nif", "CONCAT(public.datos.refcat, ' // ', SUM(public.datos.importe)/100)", ":/icons/25694.png", False, 0, "NIF", "ibi", []),
        (" LIKE ", "public.datos", "nombre", "CONCAT(public.datos.refcat, ' // ', SUM(public.datos.importe)/100)", ":/icons/25694.png", False, 0, "TITULAR", "ibi", []),
        ("=", "public.vados", "n_fijo", "CONCAT(public.vados.refcat, ' // ', SUM(public.vados.importe_sub_1))", ":/icons/vados.png", True, 0, "PLACA", "vados", []),
        ("=", "public.vados", "nif_sp_ot", "CONCAT(public.vados.refcat, ' // ', SUM(public.vados.importe_sub_1))", ":/icons/vados.png", False, 0, "NIF", "vados", []),
        ("=", "public.vados", "descripcion_tarifa_sub_1", "CONCAT(public.vados.refcat, ' // ', SUM(public.vados.importe_sub_1))", ":/icons/vados.png", False, 1, "TARIFA", "vados", ["RESTO CIUDAD HASTA 5 PLAZAS",
                                                            "POLIGONOS INDUSTRIALES HASTA 5 PLAZAS",
                                                            "PLAYAS HASTA 5 PLAZAS",
                                                            "NUCLEO ANTIGUO",
                                                            "POLIGONOS INDUSTRIALES MAS DE 6 PLAZAS",
                                                            "RESTA DE LA CIUTAT",
                                                            "RESTO CIUDAD MAS DE 6 PLAZAS",
                                                            "PLAYAS MAS DE 6 PLAZAS"]),
        ("=", "public.basuras", "nif_sp_ot", "CONCAT(public.basuras.refcat, ' // ', SUM(public.basuras.importe_conc::real))", ":/icons/basura.png", False, 0, "NIF", "basura", []),
        ("=", "public.basuras", "descripcion_tarifa_sub_1", "CONCAT(public.basuras.refcat, ' // ', SUM(public.basuras.importe_conc::real))", ":/icons/basura.png", False, 1, "TARIFA", "basura", ["1.VIVIENDAS",
                                                              "2.DESPACHOS, CONSULTAS MDICAS, ACTIV PROFESIONALES.",
                                                              "3.CLINICAS, FARMACIAS Y DESPACHOS (ARQUIT E INGEN)",
                                                              "4.NOTARIAS, REGISTRO PROPIEDAD",
                                                              "5. OFIC. ESTABLEC.Y LOCALES NO COMPRENDIDOS EN OTRO EPIGR.",
                                                              "6. COMERCIO",
                                                              "8. BARES, RESTAURANTES O CAFETERIAS",
                                                              "9. HOTELES, MOTELES Y APART DE MENOS DE 3 ESTRELLAS.",
                                                              "10. HOTELES, MOTELES Y APART DE 3 ESTRELLAS",
                                                              "11. HOTELES, MOTELES Y APART DE MµS DE 3 ESTRELLAS",
                                                              "12. CAMPING",
                                                              "16. OFICINAS DE BANCOS Y CAJAS DE AHORROS",
                                                              "18. LOCALES ASOCIACIONES/ENTIDADES SIN µNIMO DE LUCRO",
                                                              "17.2. GASOLINERAS SIN TIENDA",
                                                              "17.1. GASOLINERA CON TIENDA PRODUCTOS DIVERSOS"]),
        ("=", "cartografia.multas", "*", "refcat", ":/icons/policia.png", False, 0, "Todas", "multas", []),
        ("=", "public.fin", "*", "refcat", ":/icons/desconocido.png", False, 1, "TIPO", "Desconocidos",
         [u'TODOS', u'DNI FICTICIO', u'EN INVESTIGACIÓN']),
        ("=", "public.fin", "res", "refcat", ":/icons/desconocido.png", False, 1, "TIPO", "Desconocidos",
         [u'RESOLUBLES'])
         ]
    for operador, tabla, campo, campo2, icono, unico, tipo, nombre, destino, valores in listacriterios:
        if destino == "ibi":
            j = clase_criterio(operador, tabla, campo, campo2, icono, unico, tipo, nombre)
            if tipo == 1:
                j.criterio.addItems(valores)
            qlwi = QListWidgetItem(widget.listIBI)
            qlwi.setSizeHint(j.size())
            widget.listIBI.addItem(qlwi)
            widget.listIBI.setItemWidget(qlwi, j)
        if destino == "vados":
            j = clase_criterio(operador, tabla, campo, campo2, icono, unico, tipo, nombre)
            if tipo == 1:
                j.criterio.addItems(valores)
            qlwi = QListWidgetItem(widget.listVADOS)
            qlwi.setSizeHint(j.size())
            widget.listVADOS.addItem(qlwi)
            widget.listVADOS.setItemWidget(qlwi, j)
        if destino == "basura":
            j = clase_criterio(operador, tabla, campo, campo2, icono, unico, tipo, nombre)
            if tipo == 1:
                j.criterio.addItems(valores)
            qlwi = QListWidgetItem(widget.listBASURA)
            qlwi.setSizeHint(j.size())
            widget.listBASURA.addItem(qlwi)
            widget.listBASURA.setItemWidget(qlwi, j)
        if destino == "multas":
            j = clase_criterio(operador, tabla, campo, campo2, icono, unico, tipo, nombre)
            if tipo == 1:
                j.criterio.addItems(valores)
            qlwi = QListWidgetItem(widget.listMULTAS)
            qlwi.setSizeHint(j.size())
            widget.listMULTAS.addItem(qlwi)
            widget.listMULTAS.setItemWidget(qlwi, j)
        if destino == "Desconocidos":
            j = clase_criterio(operador, tabla, campo, campo2, icono, unico, tipo, nombre)
            if tipo == 1:
                j.criterio.addItems(valores)
            qlwi = QListWidgetItem(widget.listDESCONOCIDOS)
            qlwi.setSizeHint(j.size())
            widget.listDESCONOCIDOS.addItem(qlwi)
            widget.listDESCONOCIDOS.setItemWidget(qlwi, j)


def Mensaje(texto):
    a = QMessageBox()
    a.setText(texto)
    a.exec_()

def rellenadesconocidos(ventana, form):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect(
        "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT ref_completa, nombre, dni, nif_candidato, nombre_candidato FROM fin INNER JOIN
    cartografia.parcela USING(refcat) WHERE desconocido=TRUE;"""
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        j = clase_desconocido(row[0], row[1], row[2], row[3], row[4], "FIN", form)
        qlwi = QListWidgetItem(ventana.tabla)
        qlwi.setSizeHint(j.size())
        ventana.tabla.addItem(qlwi)
        ventana.tabla.setItemWidget(qlwi, j)

def rellenamastitulares(ref_completa, ventana, form):
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect(
        "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    sql = """SELECT nombre_sp, nif_sp_ot FROM public.basuras WHERE ref_completa=%(ref)s;"""
    cur.execute(sql, {"ref": ref_completa})
    rows = cur.fetchall()
    for row in rows:
        j = clase_titular(ref_completa, "BASURAS", row[0], row[1], form)
        qlwi = QListWidgetItem(ventana.tabla)
        qlwi.setSizeHint(j.size())
        ventana.tabla.addItem(qlwi)
        ventana.tabla.setItemWidget(qlwi, j)
    sql = """SELECT nombre, nif FROM public.aguas WHERE ref_completa=%(ref)s;"""
    cur.execute(sql, {"ref": ref_completa})
    rows = cur.fetchall()
    for row in rows:
        j = clase_titular(ref_completa, "AGUAS", row[0], row[1], form)
        qlwi = QListWidgetItem(ventana.tabla)
        qlwi.setSizeHint(j.size())
        ventana.tabla.addItem(qlwi)
        ventana.tabla.setItemWidget(qlwi, j)

def actDesc():
    datos = []
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
    conn = psycopg2.connect(
        "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
    cur = conn.cursor()
    #EN INVESTIGACIÓN
    sql = """SELECT COUNT(*)
    FROM fin INNER JOIN cartografia.parcela USING(refcat)
    WHERE desconocido=True
    AND nombre LIKE '%INVESTIG%'
    AND nombre_candidato IS NULL;"""
    cur.execute(sql)
    row = cur.fetchone()
    #print row[0]
    datos.append((u'EN INVESTIGACIÓN', row[0], '#FF6347'))
    # DNI FICTICIO
    sql = """SELECT COUNT(*)
    FROM fin INNER JOIN cartografia.parcela USING(refcat)
    WHERE desconocido=True
    AND dni IS NULL
    AND nombre_candidato IS NULL;"""
    cur.execute(sql)
    row = cur.fetchone()
    datos.append((u'DNI FICTICIO', row[0], '#FFD700'))
    # EN INVESTIGACIÓN TITULAR CANDIDATO
    sql = """SELECT COUNT(*)
        FROM fin INNER JOIN cartografia.parcela USING(refcat)
        WHERE desconocido=True
        AND nombre LIKE '%INVESTIG%'
        AND nombre_candidato IS NOT NULL;"""
    cur.execute(sql)
    row = cur.fetchone()
    datos.append((u'EN INVESTIGACIÓN (Con candidato)', row[0], '#8FD400'))
    # DNI FICTICIO TITULAR CANDIDATO
    sql = """SELECT COUNT(*)
        FROM fin INNER JOIN cartografia.parcela USING(refcat)
        WHERE desconocido=True
        AND dni IS NULL
        AND nombre_candidato IS NOT NULL;"""
    cur.execute(sql)
    row = cur.fetchone()
    datos.append((u'DNI FICTICIO (Con candidato)', row[0], '#ADFF2F'))
    return datos

def GenBet(form):
    pythoncom.CoInitialize()
    acc = Dispatch('Access.Application')
    acc_id = pythoncom.CoMarshalInterThreadInterfaceInStream(pythoncom.IID_IDispatch, acc)
    ruta = QFileDialog.getSaveFileName(form, u"Fichero access a exportar", "",
                                       "Base de datos de Access (*.accdb)")

    if ruta != "":
        ruta = unicode(ruta)
        if os.path.isfile(ruta):
            os.remove(ruta)
        q = Queue()
        thread = Thread(target=BuildAcces, args=(form, acc_id, ruta, q))
        p = loading("Exportando desconocidos", form.canvas)
        p.show()
        thread.start()
        while thread.isAlive():
            QApplication.processEvents()
        p.close()
        jar = q.get()
        if jar == "No":
            QMessageBox.information(form, "Guardado", u"Guardado correctamente")
        else:
            QMessageBox.critical(form, "Error", "Ha ocurrido un error:\n" + str(jar))


def BuildAcces(form, acc_id, expdb, q):
    try:
        pythoncom.CoInitialize()
        acc = Dispatch(pythoncom.CoGetInterfaceAndReleaseStream(acc_id, pythoncom.IID_IDispatch))
        dbEngine = acc.DBEngine
        workspace = dbEngine.Workspaces(0)
        dbLangGeneral = ';LANGID=0x0409;CP=1252;COUNTRY=0'
        newdb = workspace.CreateDatabase(expdb, dbLangGeneral, 64)
        sql = """CREATE TABLE DESCONOCIDOS (ID autoincrement,
        TIPO VARCHAR(40),
        [REFERENCIA CATASTRAL] varchar(20),
        TITULAR_FIN VARCHAR(80),
        NIF_FIN VARCHAR(10),
        TITULAR_CANDIDATO VARCHAR(80),
        NIF_CANDIDATO VARCHAR(10));"""

        newdb.Execute(sql.encode('latin-1'))
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
        conn = psycopg2.connect(
            "dbname='" + dbname + "' user='postgres' password='123456' host='9.56.3.159' port='5432'")
        cur = conn.cursor()
        sql = """SELECT nombre, dni, ref_completa, nif_candidato, nombre_candidato FROM fin INNER JOIN cartografia.parcela
        USING(refcat) WHERE desconocido=TRUE;"""
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            #print row[0], row[1], row[2], row[3], row[4]
            if 'INVESTIG' in row[0]:
                if row[3] == None:
                    tipo = u"EN INVESTIGACIÓN"
                else:
                    tipo = u"EN INVESTIGACIÓN CON CANDIDATO"
            else:
                if row[3] == None:
                    tipo = str("DNI FICTICIO")
                else:
                    tipo = str("DNI FICTICIO CON CANDIDATO")
            refcat = row[2]
            titular_fin = row[0]
            if row[1] == None:
                nif_fin = 'NULL'
            else:
                nif_fin = "'" + str(row[1]) + "'"
            if row[4] == None:
                titular_candidato = 'NULL'
            else:
                titular_candidato = "'" + str(row[4]).replace("'", "''") + "'"
            if row[3] == None:
                nif_candidato = 'NULL'
            else:
                nif_candidato = "'" + str(row[3]) + "'"
            titular_fin = titular_fin.replace("'", "''")



            sql = """INSERT INTO DESCONOCIDOS (TIPO, [REFERENCIA CATASTRAL], TITULAR_FIN, NIF_FIN, TITULAR_CANDIDATO,
            NIF_CANDIDATO) VALUES ('""" +\
                  tipo + """','""" + refcat + """','""" + titular_fin + """',""" + nif_fin + """,
                  """ + titular_candidato + """,""" + nif_candidato + """);"""

            newdb.Execute(sql.encode('latin-1'))
            q.put("No")

    except Exception as e:
        q.put(e)
    finally:
        acc.Quit()
        newdb = None
        workspace = None
        dbEngine = None
        accApp = None



def main(argv):
    app = QApplication(argv)
    splash = QSplashScreen(QPixmap(":/img/splash.jpg"), Qt.WindowStaysOnTopHint)
    splash.setGraphicsEffect(sombra())
    splash.show()
    s = orgselector()
    splash.finish(s)
    s.exec_()
    app.processEvents()
    splash = QSplashScreen(QPixmap(":/img/splash.jpg"), Qt.WindowStaysOnTopHint)
    splash.setGraphicsEffect(sombra())
    splash.show()
    form = Principal()
    form.show()
    splash.finish(form)
    form.panel_resultados.reubica(form.canvas)
    app.exec_()


if __name__ == '__main__':
    main(sys.argv)

