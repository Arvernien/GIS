# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titular.ui'
#
# Created: Tue Aug 08 10:49:34 2017
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
        Form.resize(591, 40)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fondo = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fondo.sizePolicy().hasHeightForWidth())
        self.fondo.setSizePolicy(sizePolicy)
        self.fondo.setMinimumSize(QtCore.QSize(218, 40))
        self.fondo.setMaximumSize(QtCore.QSize(16777215, 16677215))
        self.fondo.setStyleSheet(_fromUtf8("QLabel#fondo {border: 2px solid rgb(143,212,0);\n"
"border-radius: 20px;\n"
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
        self.icono.setGeometry(QtCore.QRect(0, 0, 40, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icono.sizePolicy().hasHeightForWidth())
        self.icono.setSizePolicy(sizePolicy)
        self.icono.setMinimumSize(QtCore.QSize(40, 40))
        self.icono.setMaximumSize(QtCore.QSize(40, 40))
        self.icono.setStyleSheet(_fromUtf8("QPushButton#icono { border: 2px solid rgb(143,212,0);\n"
"border-radius: 20px\n"
"}"))
        self.icono.setText(_fromUtf8(""))
        self.icono.setObjectName(_fromUtf8("icono"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(194, 5, 46, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(460, 5, 21, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.nombre = QtGui.QLabel(Form)
        self.nombre.setGeometry(QtCore.QRect(50, 18, 331, 20))
        self.nombre.setText(_fromUtf8(""))
        self.nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.nif = QtGui.QLabel(Form)
        self.nif.setGeometry(QtCore.QRect(390, 18, 161, 20))
        self.nif.setText(_fromUtf8(""))
        self.nif.setAlignment(QtCore.Qt.AlignCenter)
        self.nif.setObjectName(_fromUtf8("nif"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "NOMBRE", None))
        self.label_2.setText(_translate("Form", "NIF", None))

import ficheros_rc
