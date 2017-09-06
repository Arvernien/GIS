# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inmueble.ui'
#
# Created: Fri Aug 25 14:02:49 2017
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
        Form.resize(300, 30)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 30))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
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
        self.ref = QtGui.QLabel(Form)
        self.ref.setGeometry(QtCore.QRect(65, 7, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ref.setFont(font)
        self.ref.setAlignment(QtCore.Qt.AlignCenter)
        self.ref.setObjectName(_fromUtf8("ref"))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ref.setText(_translate("Form", "TextLabel", None))

import ficheros_rc
