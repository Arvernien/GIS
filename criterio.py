# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criterio.ui'
#
# Created: Fri May 19 13:01:32 2017
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
        Form.resize(263, 40)
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
        self.icono = QtGui.QLabel(Form)
        self.icono.setGeometry(QtCore.QRect(0, 0, 40, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icono.sizePolicy().hasHeightForWidth())
        self.icono.setSizePolicy(sizePolicy)
        self.icono.setMinimumSize(QtCore.QSize(40, 40))
        self.icono.setMaximumSize(QtCore.QSize(40, 40))
        self.icono.setStyleSheet(_fromUtf8("QLabel#icono { border: 2px solid rgb(143,212,0);\n"
"border-radius: 20px\n"
"}"))
        self.icono.setText(_fromUtf8(""))
        self.icono.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/25694.png")))
        self.icono.setScaledContents(True)
        self.icono.setAlignment(QtCore.Qt.AlignCenter)
        self.icono.setMargin(6)
        self.icono.setObjectName(_fromUtf8("icono"))
        self.criterio = QtGui.QLineEdit(Form)
        self.criterio.setGeometry(QtCore.QRect(46, 16, 190, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.criterio.sizePolicy().hasHeightForWidth())
        self.criterio.setSizePolicy(sizePolicy)
        self.criterio.setMinimumSize(QtCore.QSize(151, 0))
        self.criterio.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.criterio.setAcceptDrops(False)
        self.criterio.setStyleSheet(_fromUtf8("QLineEdit#criterio { border: 0px;\n"
"border-bottom: 1px solid gray; }"))
        self.criterio.setObjectName(_fromUtf8("criterio"))
        self.n_criterio = QtGui.QLabel(Form)
        self.n_criterio.setGeometry(QtCore.QRect(47, 2, 201, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_criterio.sizePolicy().hasHeightForWidth())
        self.n_criterio.setSizePolicy(sizePolicy)
        self.n_criterio.setMinimumSize(QtCore.QSize(131, 16))
        self.n_criterio.setMaximumSize(QtCore.QSize(1666666, 1666666))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.n_criterio.setFont(font)
        self.n_criterio.setStyleSheet(_fromUtf8("QLabel#n_criterio {\n"
"    color: rgb(90,90,90);\n"
"}"))
        self.n_criterio.setAlignment(QtCore.Qt.AlignCenter)
        self.n_criterio.setObjectName(_fromUtf8("n_criterio"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.n_criterio.setText(_translate("Form", "REFERENCIA CATASTRAL", None))

import ficheros_rc
