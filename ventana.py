# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gttgis3.ui'
#
# Created: Wed Aug 09 11:55:28 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1243, 889)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QFrame#frame {background: white;\n"
"border: 2px solid rgb(143,212,0);\n"
"\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: dark grey;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: darkgrey;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"    \n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    background: darkgrey;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    font-weight: light;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: rgb(143,212,0);\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/img/desplegado.png);\n"
"}\n"
"\n"
"QLineEdit {\n"
"border: 2px solid rgb(143,212,0);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(143,212,0);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(143,212,0);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(143,212,0);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(143,212,0);\n"
"\n"
"}\n"
"QScrollBar:vertical {               \n"
"    border: 0px solid #999999;\n"
"    background:white;\n"
"    width:5px; \n"
"    margin: 0px 0px 0px 2px;\n"
"    }\n"
"QScrollBar::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0  rgb(130, 130, 130), stop: 0.5 rgb(130, 130, 130),  stop:1 rgb(130, 130, 130));\n"
"    min-height: 0px;\n"
"    }\n"
"   QScrollBar::add-line:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(143, 212, 0), stop: 0.5 rgb(143, 212, 0),  stop:1 rgb(143, 212, 0));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(143, 212, 0), stop: 0.5 rgb(143, 212, 0),  stop:1 rgb(143, 212, 0));\n"
"       height: 0px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    \n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 3ex; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font: Arial;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 2 5px 2 5px;\n"
"    top: 2px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;    \n"
"}\n"
"\n"
"QWidget#muelle {\n"
"    border: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"    background: white;\n"
"}\n"
"QWidget#marco {\n"
"    border: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox#c_capas {\n"
"    color: rgb(90, 90, 90);\n"
"    font-weight: bold;\n"
"    spacing: 100px;\n"
"}\n"
"QCheckBox#c_Busquedas {\n"
"    color: rgb(90, 90, 90);\n"
"    font-weight: bold;\n"
"    spacing: 90px;\n"
"}\n"
"QCheckBox#c_resultados {\n"
"    color: rgb(90, 90, 90);\n"
"    font-weight: bold;\n"
"    spacing: 90px;\n"
"}\n"
"QCheckBox#c_resultados:unchecked {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox#c_resultados::indicator:unchecked {\n"
"    image: url(:/img/recogido.png);\n"
"\n"
"}\n"
"\n"
"QCheckBox#c_resultados::indicator:checked {\n"
"    image: url(:/img/desplegado.png);\n"
"}\n"
"QCheckBox#c_estadisticas {\n"
"    color: rgb(90, 90, 90);\n"
"    font-weight: bold;\n"
"    spacing: 95px;\n"
"}\n"
"QCheckBox#c_estadisticas:unchecked {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox#c_estadisticas::indicator:unchecked {\n"
"    image: url(:/img/recogido.png);\n"
"\n"
"}\n"
"\n"
"QCheckBox#c_estadisticas::indicator:checked {\n"
"    image: url(:/img/desplegado.png);\n"
"}\n"
"QCheckBox#c_criterios {\n"
"    padding-left:60px;\n"
"    color: rgb(90, 90, 90);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QCheckBox#c_criterios::indicator:unchecked {\n"
"    image: url(:/img/norecogido.png);\n"
"}\n"
"\n"
"QCheckBox#c_criterios::indicator:checked {\n"
"    image: url(:/img/recogido.png)\n"
"}\n"
"QCheckBox#c_seleccion {\n"
"    color: rgb(90, 90, 90);\n"
"    font-weight: bold;\n"
"    spacing: 95px;\n"
"}\n"
"QCheckBox#c_seleccion:unchecked {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox#c_seleccion::indicator:unchecked {\n"
"    image: url(:/img/recogido.png);\n"
"}\n"
"\n"
"QCheckBox#c_seleccion::indicator:checked {\n"
"    image: url(:/img/desplegado.png);\n"
"}\n"
"QCheckBox#c_Busquedas:unchecked {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox#c_Busquedas::indicator:unchecked {\n"
"    image: url(:/img/recogido.png);\n"
"\n"
"}\n"
"\n"
"QCheckBox#c_Busquedas::indicator:checked {\n"
"    image: url(:/img/desplegado.png);\n"
"}\n"
"\n"
"QCheckBox#c_capas:unchecked {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox#c_capas::indicator:unchecked {\n"
"    image: url(:/img/recogido.png);\n"
"\n"
"}\n"
"\n"
"QCheckBox#c_capas::indicator:checked {\n"
"    image: url(:/img/desplegado.png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QWidget#g_busquedas {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"QWidget#g_resultados {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QWidget#g_seleccion {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"QWidget#g_capas {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}\n"
"QWidget#g_estadisticas {\n"
"    border-bottom: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.layout = QtGui.QHBoxLayout()
        self.layout.setObjectName(_fromUtf8("layout"))
        self.horizontalLayout_4.addLayout(self.layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1243, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(275, 331))
        self.dockWidget.setMaximumSize(QtCore.QSize(275, 524287))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dockWidget.setFont(font)
        self.dockWidget.setStyleSheet(_fromUtf8("QDockWidget {\n"
"    border: 2px solid rgb(143,212,0);\n"
"    background: white;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    text-align: center; /* align the text to the left */\n"
"    border: 2px solid rgb(143,212,0);\n"
"    background: white;\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
""))
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.muelle = QtGui.QWidget(self.dockWidgetContents)
        self.muelle.setStyleSheet(_fromUtf8(""))
        self.muelle.setObjectName(_fromUtf8("muelle"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.muelle)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setMargin(4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.muelle)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -29, 262, 978))
        self.scrollAreaWidgetContents.setStyleSheet(_fromUtf8("QWidget#scrollAreaWidgetContents { background: white;}"))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gc_seleccion = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gc_seleccion.sizePolicy().hasHeightForWidth())
        self.gc_seleccion.setSizePolicy(sizePolicy)
        self.gc_seleccion.setStyleSheet(_fromUtf8(""))
        self.gc_seleccion.setObjectName(_fromUtf8("gc_seleccion"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.gc_seleccion)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.c_seleccion = QtGui.QCheckBox(self.gc_seleccion)
        self.c_seleccion.setMinimumSize(QtCore.QSize(0, 20))
        self.c_seleccion.setStyleSheet(_fromUtf8(""))
        self.c_seleccion.setObjectName(_fromUtf8("c_seleccion"))
        self.horizontalLayout.addWidget(self.c_seleccion)
        self.verticalLayout_3.addWidget(self.gc_seleccion)
        self.g_seleccion = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.g_seleccion.setMaximumSize(QtCore.QSize(16777215, 102))
        self.g_seleccion.setStyleSheet(_fromUtf8(""))
        self.g_seleccion.setObjectName(_fromUtf8("g_seleccion"))
        self.gridLayout_2 = QtGui.QGridLayout(self.g_seleccion)
        self.gridLayout_2.setContentsMargins(0, 6, 0, 6)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sel_custom = QtGui.QPushButton(self.g_seleccion)
        self.sel_custom.setMinimumSize(QtCore.QSize(50, 30))
        self.sel_custom.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sel_custom.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/custom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sel_custom.setIcon(icon1)
        self.sel_custom.setIconSize(QtCore.QSize(20, 20))
        self.sel_custom.setObjectName(_fromUtf8("sel_custom"))
        self.gridLayout_2.addWidget(self.sel_custom, 1, 2, 1, 1)
        self.sel_rect = QtGui.QPushButton(self.g_seleccion)
        self.sel_rect.setMinimumSize(QtCore.QSize(0, 30))
        self.sel_rect.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sel_rect.setWhatsThis(_fromUtf8(""))
        self.sel_rect.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/rectangulo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sel_rect.setIcon(icon2)
        self.sel_rect.setIconSize(QtCore.QSize(20, 20))
        self.sel_rect.setObjectName(_fromUtf8("sel_rect"))
        self.gridLayout_2.addWidget(self.sel_rect, 1, 0, 1, 1)
        self.sel_circ = QtGui.QPushButton(self.g_seleccion)
        self.sel_circ.setMinimumSize(QtCore.QSize(0, 30))
        self.sel_circ.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/circulo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sel_circ.setIcon(icon3)
        self.sel_circ.setIconSize(QtCore.QSize(20, 20))
        self.sel_circ.setObjectName(_fromUtf8("sel_circ"))
        self.gridLayout_2.addWidget(self.sel_circ, 2, 0, 1, 1)
        self.sel_idtool = QtGui.QPushButton(self.g_seleccion)
        self.sel_idtool.setMinimumSize(QtCore.QSize(50, 30))
        self.sel_idtool.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sel_idtool.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sel_idtool.setIcon(icon4)
        self.sel_idtool.setIconSize(QtCore.QSize(20, 20))
        self.sel_idtool.setObjectName(_fromUtf8("sel_idtool"))
        self.gridLayout_2.addWidget(self.sel_idtool, 1, 1, 1, 1)
        self.sel_buf_point = QtGui.QPushButton(self.g_seleccion)
        self.sel_buf_point.setMinimumSize(QtCore.QSize(50, 30))
        self.sel_buf_point.setMaximumSize(QtCore.QSize(50, 16777215))
        self.sel_buf_point.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bufferpunto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sel_buf_point.setIcon(icon5)
        self.sel_buf_point.setIconSize(QtCore.QSize(20, 20))
        self.sel_buf_point.setObjectName(_fromUtf8("sel_buf_point"))
        self.gridLayout_2.addWidget(self.sel_buf_point, 2, 1, 1, 1)
        self.self_buf_line = QtGui.QPushButton(self.g_seleccion)
        self.self_buf_line.setMinimumSize(QtCore.QSize(50, 30))
        self.self_buf_line.setMaximumSize(QtCore.QSize(50, 16777215))
        self.self_buf_line.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bufferlineal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.self_buf_line.setIcon(icon6)
        self.self_buf_line.setIconSize(QtCore.QSize(20, 20))
        self.self_buf_line.setObjectName(_fromUtf8("self_buf_line"))
        self.gridLayout_2.addWidget(self.self_buf_line, 2, 2, 1, 1)
        self.sel_Del = QtGui.QPushButton(self.g_seleccion)
        self.sel_Del.setMinimumSize(QtCore.QSize(0, 30))
        self.sel_Del.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/borrar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sel_Del.setIcon(icon7)
        self.sel_Del.setIconSize(QtCore.QSize(20, 20))
        self.sel_Del.setObjectName(_fromUtf8("sel_Del"))
        self.gridLayout_2.addWidget(self.sel_Del, 3, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.g_seleccion)
        self.gc_capas = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gc_capas.sizePolicy().hasHeightForWidth())
        self.gc_capas.setSizePolicy(sizePolicy)
        self.gc_capas.setStyleSheet(_fromUtf8(""))
        self.gc_capas.setObjectName(_fromUtf8("gc_capas"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.gc_capas)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.c_capas = QtGui.QCheckBox(self.gc_capas)
        self.c_capas.setMinimumSize(QtCore.QSize(0, 20))
        self.c_capas.setStyleSheet(_fromUtf8(""))
        self.c_capas.setObjectName(_fromUtf8("c_capas"))
        self.horizontalLayout_3.addWidget(self.c_capas)
        self.verticalLayout_3.addWidget(self.gc_capas)
        self.g_capas = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_capas.sizePolicy().hasHeightForWidth())
        self.g_capas.setSizePolicy(sizePolicy)
        self.g_capas.setMaximumSize(QtCore.QSize(16777215, 180))
        self.g_capas.setStyleSheet(_fromUtf8(""))
        self.g_capas.setObjectName(_fromUtf8("g_capas"))
        self.formLayout_3 = QtGui.QFormLayout(self.g_capas)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(0, 6, 0, 6)
        self.formLayout_3.setSpacing(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.listCapas = QtGui.QListWidget(self.g_capas)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listCapas.sizePolicy().hasHeightForWidth())
        self.listCapas.setSizePolicy(sizePolicy)
        self.listCapas.setFrameShape(QtGui.QFrame.NoFrame)
        self.listCapas.setObjectName(_fromUtf8("listCapas"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.listCapas)
        self.verticalLayout_3.addWidget(self.g_capas)
        self.gc_busquedas = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gc_busquedas.sizePolicy().hasHeightForWidth())
        self.gc_busquedas.setSizePolicy(sizePolicy)
        self.gc_busquedas.setStyleSheet(_fromUtf8(""))
        self.gc_busquedas.setObjectName(_fromUtf8("gc_busquedas"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.gc_busquedas)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.c_Busquedas = QtGui.QCheckBox(self.gc_busquedas)
        self.c_Busquedas.setMinimumSize(QtCore.QSize(0, 20))
        self.c_Busquedas.setStyleSheet(_fromUtf8(""))
        self.c_Busquedas.setObjectName(_fromUtf8("c_Busquedas"))
        self.horizontalLayout_2.addWidget(self.c_Busquedas)
        self.verticalLayout_3.addWidget(self.gc_busquedas)
        self.g_busquedas = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.g_busquedas.setMaximumSize(QtCore.QSize(16777215, 205))
        self.g_busquedas.setStyleSheet(_fromUtf8(""))
        self.g_busquedas.setObjectName(_fromUtf8("g_busquedas"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.g_busquedas)
        self.verticalLayout_12.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.c_criterios = QtGui.QCheckBox(self.g_busquedas)
        self.c_criterios.setObjectName(_fromUtf8("c_criterios"))
        self.verticalLayout_12.addWidget(self.c_criterios)
        self.verticalLayout_3.addWidget(self.g_busquedas)
        self.gc_resultados = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gc_resultados.sizePolicy().hasHeightForWidth())
        self.gc_resultados.setSizePolicy(sizePolicy)
        self.gc_resultados.setStyleSheet(_fromUtf8(""))
        self.gc_resultados.setObjectName(_fromUtf8("gc_resultados"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.gc_resultados)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.c_resultados = QtGui.QCheckBox(self.gc_resultados)
        self.c_resultados.setMinimumSize(QtCore.QSize(0, 20))
        self.c_resultados.setStyleSheet(_fromUtf8(""))
        self.c_resultados.setObjectName(_fromUtf8("c_resultados"))
        self.horizontalLayout_5.addWidget(self.c_resultados)
        self.verticalLayout_3.addWidget(self.gc_resultados)
        self.g_resultados = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_resultados.sizePolicy().hasHeightForWidth())
        self.g_resultados.setSizePolicy(sizePolicy)
        self.g_resultados.setMaximumSize(QtCore.QSize(16777215, 16777))
        self.g_resultados.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border: 0px;\n"
"    border-radius: 0 px;\n"
"    border-bottom: 1px solid darkgrey;\n"
"    \n"
"}"))
        self.g_resultados.setObjectName(_fromUtf8("g_resultados"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.g_resultados)
        self.verticalLayout_4.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.g_resultados)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("QLabel {\n"
"    color: rgb(91,91,91);\n"
"    font-weight:bold;\n"
"    padding-left: 3px;\n"
"}"))
        self.label.setMargin(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.fincas = QtGui.QComboBox(self.g_resultados)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fincas.sizePolicy().hasHeightForWidth())
        self.fincas.setSizePolicy(sizePolicy)
        self.fincas.setObjectName(_fromUtf8("fincas"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fincas)
        self.direccion = QtGui.QLineEdit(self.g_resultados)
        self.direccion.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.direccion.setFont(font)
        self.direccion.setStyleSheet(_fromUtf8(""))
        self.direccion.setReadOnly(True)
        self.direccion.setObjectName(_fromUtf8("direccion"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.direccion)
        self.label_2 = QtGui.QLabel(self.g_resultados)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(_fromUtf8("QLabel {\n"
"    color: rgb(91,91,91);\n"
"    font-weight:bold;\n"
"    padding-left: 3px;\n"
"}"))
        self.label_2.setMargin(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.tributos = QtGui.QTabWidget(self.g_resultados)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tributos.sizePolicy().hasHeightForWidth())
        self.tributos.setSizePolicy(sizePolicy)
        self.tributos.setMinimumSize(QtCore.QSize(0, 205))
        self.tributos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tributos.setToolTip(_fromUtf8(""))
        self.tributos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tributos.setStyleSheet(_fromUtf8("QTabWidget::pane {\n"
"    border-top: 1px solid rgb(143,212,0);\n"
"}\n"
"QTabBar::tab {\n"
"    border: 1px solid rgb(143,212,0);\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    background: rgb(200,200,200);\n"
"    padding-left: 7.5px;\n"
"    width:30;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background: white;\n"
"    height: 27px;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background: white;\n"
"    height: 27px;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    margin-top: 2px;\n"
"    height: 25px;\n"
"}\n"
"QTabBar::scroller{\n"
"    height: 25px;\n"
"    width:15px;\n"
"}\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background-color: white;\n"
"    height: 25px;    \n"
"}\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(:/img/recogido.png);\n"
"}\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(:/img/norecogido.png);\n"
"}"))
        self.tributos.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tributos.setTabShape(QtGui.QTabWidget.Rounded)
        self.tributos.setIconSize(QtCore.QSize(20, 20))
        self.tributos.setDocumentMode(False)
        self.tributos.setObjectName(_fromUtf8("tributos"))
        self.ibi = QtGui.QWidget()
        self.ibi.setObjectName(_fromUtf8("ibi"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.ibi)
        self.verticalLayout_5.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.resultados_ibi = QtGui.QListWidget(self.ibi)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultados_ibi.sizePolicy().hasHeightForWidth())
        self.resultados_ibi.setSizePolicy(sizePolicy)
        self.resultados_ibi.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"    border-bottom: 1px solid darkgrey;\n"
"    padding-bottom: 5px;\n"
"}"))
        self.resultados_ibi.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultados_ibi.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultados_ibi.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.resultados_ibi.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultados_ibi.setMovement(QtGui.QListView.Free)
        self.resultados_ibi.setResizeMode(QtGui.QListView.Adjust)
        self.resultados_ibi.setSpacing(2)
        self.resultados_ibi.setSelectionRectVisible(False)
        self.resultados_ibi.setObjectName(_fromUtf8("resultados_ibi"))
        self.verticalLayout_5.addWidget(self.resultados_ibi)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/25694.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tributos.addTab(self.ibi, icon8, _fromUtf8(""))
        self.vados = QtGui.QWidget()
        self.vados.setObjectName(_fromUtf8("vados"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.vados)
        self.verticalLayout_6.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.resultados_vados = QtGui.QListWidget(self.vados)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultados_vados.sizePolicy().hasHeightForWidth())
        self.resultados_vados.setSizePolicy(sizePolicy)
        self.resultados_vados.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"    border-bottom: 1px solid darkgrey;\n"
"    padding-bottom: 5px;\n"
"}"))
        self.resultados_vados.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultados_vados.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultados_vados.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.resultados_vados.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultados_vados.setMovement(QtGui.QListView.Free)
        self.resultados_vados.setResizeMode(QtGui.QListView.Adjust)
        self.resultados_vados.setSpacing(2)
        self.resultados_vados.setSelectionRectVisible(False)
        self.resultados_vados.setObjectName(_fromUtf8("resultados_vados"))
        self.verticalLayout_6.addWidget(self.resultados_vados)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/vados.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tributos.addTab(self.vados, icon9, _fromUtf8(""))
        self.basuras = QtGui.QWidget()
        self.basuras.setObjectName(_fromUtf8("basuras"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.basuras)
        self.verticalLayout_7.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.resultados_basuras = QtGui.QListWidget(self.basuras)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultados_basuras.sizePolicy().hasHeightForWidth())
        self.resultados_basuras.setSizePolicy(sizePolicy)
        self.resultados_basuras.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"    border-bottom: 1px solid darkgrey;\n"
"    padding-bottom: 5px;\n"
"}"))
        self.resultados_basuras.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultados_basuras.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultados_basuras.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.resultados_basuras.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultados_basuras.setMovement(QtGui.QListView.Free)
        self.resultados_basuras.setResizeMode(QtGui.QListView.Adjust)
        self.resultados_basuras.setSpacing(2)
        self.resultados_basuras.setSelectionRectVisible(False)
        self.resultados_basuras.setObjectName(_fromUtf8("resultados_basuras"))
        self.verticalLayout_7.addWidget(self.resultados_basuras)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/basura.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tributos.addTab(self.basuras, icon10, _fromUtf8(""))
        self.agua = QtGui.QWidget()
        self.agua.setObjectName(_fromUtf8("agua"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.agua)
        self.verticalLayout_8.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.resultados_agua = QtGui.QListWidget(self.agua)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultados_agua.sizePolicy().hasHeightForWidth())
        self.resultados_agua.setSizePolicy(sizePolicy)
        self.resultados_agua.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"    border-bottom: 1px solid darkgrey;\n"
"    padding-bottom: 5px;\n"
"}"))
        self.resultados_agua.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultados_agua.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultados_agua.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.resultados_agua.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultados_agua.setMovement(QtGui.QListView.Free)
        self.resultados_agua.setResizeMode(QtGui.QListView.Adjust)
        self.resultados_agua.setSpacing(2)
        self.resultados_agua.setSelectionRectVisible(False)
        self.resultados_agua.setObjectName(_fromUtf8("resultados_agua"))
        self.verticalLayout_8.addWidget(self.resultados_agua)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/grifo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tributos.addTab(self.agua, icon11, _fromUtf8(""))
        self.plusvalias = QtGui.QWidget()
        self.plusvalias.setObjectName(_fromUtf8("plusvalias"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.plusvalias)
        self.verticalLayout_10.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.resultados_plusvalias = QtGui.QListWidget(self.plusvalias)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultados_plusvalias.sizePolicy().hasHeightForWidth())
        self.resultados_plusvalias.setSizePolicy(sizePolicy)
        self.resultados_plusvalias.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"    border-bottom: 1px solid darkgrey;\n"
"    padding-bottom: 5px;\n"
"}"))
        self.resultados_plusvalias.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultados_plusvalias.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultados_plusvalias.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.resultados_plusvalias.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultados_plusvalias.setMovement(QtGui.QListView.Free)
        self.resultados_plusvalias.setResizeMode(QtGui.QListView.Adjust)
        self.resultados_plusvalias.setSpacing(2)
        self.resultados_plusvalias.setSelectionRectVisible(False)
        self.resultados_plusvalias.setObjectName(_fromUtf8("resultados_plusvalias"))
        self.verticalLayout_10.addWidget(self.resultados_plusvalias)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/plusvalias.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tributos.addTab(self.plusvalias, icon12, _fromUtf8(""))
        self.icio = QtGui.QWidget()
        self.icio.setObjectName(_fromUtf8("icio"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.icio)
        self.verticalLayout_11.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.resultados_icio = QtGui.QListWidget(self.icio)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultados_icio.sizePolicy().hasHeightForWidth())
        self.resultados_icio.setSizePolicy(sizePolicy)
        self.resultados_icio.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"    border-bottom: 1px solid darkgrey;\n"
"    padding-bottom: 5px;\n"
"}"))
        self.resultados_icio.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultados_icio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultados_icio.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.resultados_icio.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultados_icio.setMovement(QtGui.QListView.Free)
        self.resultados_icio.setResizeMode(QtGui.QListView.Adjust)
        self.resultados_icio.setSpacing(2)
        self.resultados_icio.setSelectionRectVisible(False)
        self.resultados_icio.setObjectName(_fromUtf8("resultados_icio"))
        self.verticalLayout_11.addWidget(self.resultados_icio)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gancho.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tributos.addTab(self.icio, icon13, _fromUtf8(""))
        self.expedientes = QtGui.QWidget()
        self.expedientes.setObjectName(_fromUtf8("expedientes"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.expedientes)
        self.verticalLayout_9.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.resultados_expedientes = QtGui.QListWidget(self.expedientes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultados_expedientes.sizePolicy().hasHeightForWidth())
        self.resultados_expedientes.setSizePolicy(sizePolicy)
        self.resultados_expedientes.setStyleSheet(_fromUtf8("QListWidget:item {\n"
"    border-bottom: 1px solid darkgrey;\n"
"    padding-bottom: 5px;\n"
"}"))
        self.resultados_expedientes.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultados_expedientes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultados_expedientes.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.resultados_expedientes.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultados_expedientes.setMovement(QtGui.QListView.Free)
        self.resultados_expedientes.setResizeMode(QtGui.QListView.Adjust)
        self.resultados_expedientes.setSpacing(2)
        self.resultados_expedientes.setSelectionRectVisible(False)
        self.resultados_expedientes.setObjectName(_fromUtf8("resultados_expedientes"))
        self.verticalLayout_9.addWidget(self.resultados_expedientes)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/expediente.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tributos.addTab(self.expedientes, icon14, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tributos)
        self.verticalLayout_3.addWidget(self.g_resultados)
        self.gc_estadisticas = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.gc_estadisticas.setObjectName(_fromUtf8("gc_estadisticas"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.gc_estadisticas)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.c_estadisticas = QtGui.QCheckBox(self.gc_estadisticas)
        self.c_estadisticas.setMinimumSize(QtCore.QSize(0, 20))
        self.c_estadisticas.setObjectName(_fromUtf8("c_estadisticas"))
        self.horizontalLayout_6.addWidget(self.c_estadisticas)
        self.verticalLayout_3.addWidget(self.gc_estadisticas)
        self.g_estadisticas = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.g_estadisticas.setObjectName(_fromUtf8("g_estadisticas"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.g_estadisticas)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setMargin(0)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.westadisticas = QtGui.QTabWidget(self.g_estadisticas)
        self.westadisticas.setStyleSheet(_fromUtf8("QTabWidget::pane {\n"
"    border-top: 1px solid rgb(143,212,0);\n"
"}\n"
"QTabBar::tab {\n"
"    border: 1px solid rgb(143,212,0);\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    background: rgb(200,200,200);\n"
"    padding-left: 7.5px;\n"
"    width:30;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background: white;\n"
"    height: 27px;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background: white;\n"
"    height: 27px;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    margin-top: 2px;\n"
"    height: 25px;\n"
"}\n"
"QTabBar::scroller{\n"
"    height: 25px;\n"
"    width:15px;\n"
"}\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background-color: white;\n"
"    height: 25px;    \n"
"}\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(:/img/recogido.png);\n"
"}\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(:/img/norecogido.png);\n"
"}"))
        self.westadisticas.setObjectName(_fromUtf8("westadisticas"))
        self.desc = QtGui.QWidget()
        self.desc.setObjectName(_fromUtf8("desc"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.desc)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setMargin(0)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.widget = QtGui.QWidget(self.desc)
        self.widget.setMinimumSize(QtCore.QSize(0, 150))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_14.addWidget(self.widget)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/desconocido.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.westadisticas.addTab(self.desc, icon15, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.westadisticas)
        self.verticalLayout_3.addWidget(self.g_estadisticas)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.muelle)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tributos.setCurrentIndex(0)
        self.westadisticas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "gttSIG", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Herramientas", None))
        self.c_seleccion.setText(_translate("MainWindow", "Selección", None))
        self.sel_custom.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Selección libre</p></body></html>", None))
        self.sel_rect.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Selección rectangular</span></p></body></html>", None))
        self.sel_circ.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Selección circular</p></body></html>", None))
        self.sel_idtool.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Selección individual</p></body></html>", None))
        self.sel_buf_point.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Buffer radial</p></body></html>", None))
        self.self_buf_line.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Buffer lineal</p></body></html>", None))
        self.sel_Del.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Eliminar selección</p></body></html>", None))
        self.c_capas.setText(_translate("MainWindow", "Capas", None))
        self.c_Busquedas.setText(_translate("MainWindow", "Búsquedas", None))
        self.c_criterios.setText(_translate("MainWindow", "Mostrar criterios", None))
        self.c_resultados.setText(_translate("MainWindow", "Resultados", None))
        self.label.setText(_translate("MainWindow", "Finca:", None))
        self.label_2.setText(_translate("MainWindow", "Dirección:", None))
        self.ibi.setToolTip(_translate("MainWindow", "<html><head/><body><p>IBI</p></body></html>", None))
        self.vados.setToolTip(_translate("MainWindow", "<html><head/><body><p>Entradas de vehículo</p></body></html>", None))
        self.basuras.setToolTip(_translate("MainWindow", "<html><head/><body><p>Residuos</p></body></html>", None))
        self.agua.setToolTip(_translate("MainWindow", "<html><head/><body><p>Agua</p></body></html>", None))
        self.expedientes.setToolTip(_translate("MainWindow", "<html><head/><body><p>Expedientes</p></body></html>", None))
        self.c_estadisticas.setText(_translate("MainWindow", "Estadísticas", None))

import ficheros_rc
