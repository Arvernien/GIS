# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadshp.ui'
#
# Created: Wed Aug 23 12:10:59 2017
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
        Form.resize(542, 266)
        self.ruta = QtGui.QLineEdit(Form)
        self.ruta.setGeometry(QtCore.QRect(40, 38, 441, 20))
        self.ruta.setObjectName(_fromUtf8("ruta"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.abrir = QtGui.QPushButton(Form)
        self.abrir.setGeometry(QtCore.QRect(490, 36, 41, 25))
        self.abrir.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/carpeta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abrir.setIcon(icon)
        self.abrir.setObjectName(_fromUtf8("abrir"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(9, 71, 521, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 47, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 75, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 101, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.inmueble = QtGui.QComboBox(self.groupBox)
        self.inmueble.setGeometry(QtCore.QRect(90, 44, 411, 22))
        self.inmueble.setObjectName(_fromUtf8("inmueble"))
        self.titular = QtGui.QComboBox(self.groupBox)
        self.titular.setGeometry(QtCore.QRect(90, 70, 411, 22))
        self.titular.setObjectName(_fromUtf8("titular"))
        self.dni = QtGui.QComboBox(self.groupBox)
        self.dni.setGeometry(QtCore.QRect(90, 97, 411, 22))
        self.dni.setObjectName(_fromUtf8("dni"))
        self.cargar = QtGui.QPushButton(Form)
        self.cargar.setEnabled(False)
        self.cargar.setGeometry(QtCore.QRect(191, 226, 75, 23))
        self.cargar.setObjectName(_fromUtf8("cargar"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 521, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.salir = QtGui.QPushButton(Form)
        self.salir.setEnabled(True)
        self.salir.setGeometry(QtCore.QRect(290, 226, 75, 23))
        self.salir.setObjectName(_fromUtf8("salir"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Ruta:", None))
        self.groupBox.setTitle(_translate("Form", "Datos", None))
        self.label_2.setText(_translate("Form", "Inmueble:", None))
        self.label_3.setText(_translate("Form", "Titular:", None))
        self.label_4.setText(_translate("Form", "Dni:", None))
        self.cargar.setText(_translate("Form", "Cargar", None))
        self.label_5.setText(_translate("Form", "CARGAR FICHERO SHP", None))
        self.salir.setText(_translate("Form", "Salir", None))

import ficheros_rc
