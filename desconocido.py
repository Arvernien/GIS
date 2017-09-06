# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desconocido.ui'
#
# Created: Mon Aug 21 12:12:48 2017
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(591, 60)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fondo = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fondo.sizePolicy().hasHeightForWidth())
        self.fondo.setSizePolicy(sizePolicy)
        self.fondo.setMinimumSize(QtCore.QSize(591, 60))
        self.fondo.setMaximumSize(QtCore.QSize(16777215, 16677215))
        self.fondo.setStyleSheet(_fromUtf8("QLabel#fondo {border: 2px solid rgb(143,212,0);\n"
"border-radius: 30px;\n"
"background-color: rgb(255,255,255);\n"
" }"))
        self.fondo.setText(_fromUtf8(""))
        self.fondo.setScaledContents(False)
        self.fondo.setAlignment(QtCore.Qt.AlignCenter)
        self.fondo.setMargin(0)
        self.fondo.setIndent(0)
        self.fondo.setObjectName(_fromUtf8("fondo"))
        self.gridLayout.addWidget(self.fondo, 0, 0, 1, 1)
        self.icono = QtGui.QPushButton(Form)
        self.icono.setGeometry(QtCore.QRect(0, 0, 60, 60))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icono.sizePolicy().hasHeightForWidth())
        self.icono.setSizePolicy(sizePolicy)
        self.icono.setMinimumSize(QtCore.QSize(60, 60))
        self.icono.setMaximumSize(QtCore.QSize(60, 60))
        self.icono.setStyleSheet(_fromUtf8("QPushButton#icono { border: 2px solid rgb(143,212,0);\n"
"border-radius: 30px;\n"
"}"))
        self.icono.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/25694.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icono.setIcon(icon)
        self.icono.setIconSize(QtCore.QSize(35, 35))
        self.icono.setObjectName(_fromUtf8("icono"))
        self.borra = QtGui.QPushButton(Form)
        self.borra.setGeometry(QtCore.QRect(550, 15, 30, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borra.sizePolicy().hasHeightForWidth())
        self.borra.setSizePolicy(sizePolicy)
        self.borra.setMinimumSize(QtCore.QSize(30, 30))
        self.borra.setMaximumSize(QtCore.QSize(30, 30))
        self.borra.setStyleSheet(_fromUtf8("QPushButton#borra { border: 2px solid rgb(143,212,0);\n"
"border-radius: 15px;\n"
"}"))
        self.borra.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/borrar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.borra.setIcon(icon1)
        self.borra.setIconSize(QtCore.QSize(15, 15))
        self.borra.setObjectName(_fromUtf8("borra"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(60, 30, 490, 3))
        self.line.setMinimumSize(QtCore.QSize(0, 3))
        self.line.setStyleSheet(_fromUtf8("QFrame#line\n"
" {\n"
"color: rgb(143,212,0);\n"
"}"))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(61, 6, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 41, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.finnombre = QtGui.QLabel(Form)
        self.finnombre.setGeometry(QtCore.QRect(140, 6, 291, 16))
        self.finnombre.setObjectName(_fromUtf8("finnombre"))
        self.finnif = QtGui.QLabel(Form)
        self.finnif.setGeometry(QtCore.QRect(450, 6, 91, 16))
        self.finnif.setObjectName(_fromUtf8("finnif"))
        self.candnif = QtGui.QLabel(Form)
        self.candnif.setGeometry(QtCore.QRect(450, 41, 91, 16))
        self.candnif.setObjectName(_fromUtf8("candnif"))
        self.candnombre = QtGui.QLabel(Form)
        self.candnombre.setGeometry(QtCore.QRect(140, 41, 291, 16))
        self.candnombre.setObjectName(_fromUtf8("candnombre"))
        self.ref = QtGui.QLabel(Form)
        self.ref.setGeometry(QtCore.QRect(54, 23, 151, 16))
        self.ref.setStyleSheet(_fromUtf8("QLabel {border: 2px solid rgb(143,212,0);\n"
"border-radius: 8px;\n"
"background: white;\n"
"padding-left: 4px;\n"
" }"))
        self.ref.setObjectName(_fromUtf8("ref"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.icono.setToolTip(_translate("Form", "Ubicar desconocido", None))
        self.borra.setToolTip(_translate("Form", "Eliminar titular candidato", None))
        self.label.setText(_translate("Form", "TITULAR FIN:", None))
        self.label_2.setText(_translate("Form", "CANDIDATO:", None))
        self.finnombre.setText(_translate("Form", "NOMBRE", None))
        self.finnif.setText(_translate("Form", "DNI", None))
        self.candnif.setText(_translate("Form", "DNI", None))
        self.candnombre.setText(_translate("Form", "NOMBRE", None))
        self.ref.setText(_translate("Form", "REFCOMPLETA", None))

import ficheros_rc
