# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contador.ui'
#
# Created: Mon Sep 04 13:00:39 2017
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
        Form.resize(300, 60)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 30))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fondo = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fondo.sizePolicy().hasHeightForWidth())
        self.fondo.setSizePolicy(sizePolicy)
        self.fondo.setMinimumSize(QtCore.QSize(300, 30))
        self.fondo.setMaximumSize(QtCore.QSize(30, 16677215))
        self.fondo.setStyleSheet(_fromUtf8("QLabel#fondo {border: 2px solid rgb(143,212,0);\n"
"border-radius: 15px;\n"
"background-color: rgb(255,255,255);\n"
" }"))
        self.fondo.setText(_fromUtf8(""))
        self.fondo.setScaledContents(False)
        self.fondo.setAlignment(QtCore.Qt.AlignCenter)
        self.fondo.setMargin(0)
        self.fondo.setIndent(0)
        self.fondo.setObjectName(_fromUtf8("fondo"))
        self.gridLayout.addWidget(self.fondo, 0, 0, 1, 1)
        self.titular = QtGui.QLabel(Form)
        self.titular.setGeometry(QtCore.QRect(35, 7, 251, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titular.setFont(font)
        self.titular.setAlignment(QtCore.Qt.AlignCenter)
        self.titular.setObjectName(_fromUtf8("titular"))
        self.icono = QtGui.QLabel(Form)
        self.icono.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.icono.setStyleSheet(_fromUtf8("QLabel#icono { border: 2px solid rgb(143,212,0);\n"
"border-radius: 15px\n"
"}"))
        self.icono.setText(_fromUtf8(""))
        self.icono.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/25694.png")))
        self.icono.setScaledContents(True)
        self.icono.setMargin(3)
        self.icono.setObjectName(_fromUtf8("icono"))
        self.porc = QtGui.QLabel(Form)
        self.porc.setGeometry(QtCore.QRect(270, 30, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.porc.setFont(font)
        self.porc.setStyleSheet(_fromUtf8(""))
        self.porc.setScaledContents(True)
        self.porc.setAlignment(QtCore.Qt.AlignCenter)
        self.porc.setMargin(3)
        self.porc.setObjectName(_fromUtf8("porc"))
        self.dni = QtGui.QLabel(Form)
        self.dni.setGeometry(QtCore.QRect(21, 34, 241, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dni.setFont(font)
        self.dni.setAlignment(QtCore.Qt.AlignCenter)
        self.dni.setObjectName(_fromUtf8("dni"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.titular.setText(_translate("Form", "TextLabel", None))
        self.porc.setText(_translate("Form", "68%", None))
        self.dni.setText(_translate("Form", "TextLabel", None))

import ficheros_rc
