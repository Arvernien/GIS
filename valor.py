# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valor.ui'
#
# Created: Mon Aug 07 14:50:05 2017
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
        Form.resize(259, 177)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet(_fromUtf8("QFrame#fondo {\n"
"    background: white;\n"
"    border-bottom: 1px solid rgb(90,90,90);\n"
"}\n"
"QLabel {\n"
"    font-weight: bold;\n"
"    color: rgb(143,212,0);\n"
"}\n"
"QLabel#cargo {\n"
"    font-weight: bold;\n"
"    color: rgb(130,130,130);\n"
"}\n"
"QLabel#nif {\n"
"    font-weight: bold;\n"
"    color: rgb(130,130,130);\n"
"}\n"
"QLabel#titular {\n"
"    font-weight: bold;\n"
"    color: rgb(130,130,130);\n"
"}\n"
"QCheckBox#showinfo::hover:unchecked {\n"
"    background:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0.5, stop:0 rgba(143, 212, 0, 100), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"QCheckBox#showinfo::hover:checked {\n"
"    background:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.5, stop:0 rgba(143, 212, 0, 100), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QCheckBox#showinfo::indicator:checked {\n"
"    image: url(:/img/nodesplegado.png);\n"
"    padding-left: 120 px;\n"
"\n"
"}\n"
"QCheckBox#showinfo::indicator:unchecked {\n"
"    image: url(:/img/desplegado.png);\n"
"    padding-left: 120 px;\n"
"}\n"
"QWidget#info_ot {\n"
"    border: 1px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ot = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ot.sizePolicy().hasHeightForWidth())
        self.ot.setSizePolicy(sizePolicy)
        self.ot.setMinimumSize(QtCore.QSize(0, 40))
        self.ot.setObjectName(_fromUtf8("ot"))
        self.gridLayout_3 = QtGui.QGridLayout(self.ot)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.dato3 = QtGui.QLabel(self.ot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dato3.sizePolicy().hasHeightForWidth())
        self.dato3.setSizePolicy(sizePolicy)
        self.dato3.setMinimumSize(QtCore.QSize(0, 0))
        self.dato3.setObjectName(_fromUtf8("dato3"))
        self.gridLayout_3.addWidget(self.dato3, 3, 0, 1, 1)
        self.cargo = QtGui.QLabel(self.ot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cargo.sizePolicy().hasHeightForWidth())
        self.cargo.setSizePolicy(sizePolicy)
        self.cargo.setMinimumSize(QtCore.QSize(41, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.cargo.setFont(font)
        self.cargo.setText(_fromUtf8(""))
        self.cargo.setObjectName(_fromUtf8("cargo"))
        self.gridLayout_3.addWidget(self.cargo, 1, 1, 1, 2)
        self.dato1 = QtGui.QLabel(self.ot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dato1.sizePolicy().hasHeightForWidth())
        self.dato1.setSizePolicy(sizePolicy)
        self.dato1.setMinimumSize(QtCore.QSize(41, 0))
        self.dato1.setObjectName(_fromUtf8("dato1"))
        self.gridLayout_3.addWidget(self.dato1, 1, 0, 1, 1)
        self.dato2 = QtGui.QLabel(self.ot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dato2.sizePolicy().hasHeightForWidth())
        self.dato2.setSizePolicy(sizePolicy)
        self.dato2.setMinimumSize(QtCore.QSize(0, 0))
        self.dato2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dato2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dato2.setObjectName(_fromUtf8("dato2"))
        self.gridLayout_3.addWidget(self.dato2, 1, 3, 1, 1)
        self.nif = QtGui.QLabel(self.ot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nif.sizePolicy().hasHeightForWidth())
        self.nif.setSizePolicy(sizePolicy)
        self.nif.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.nif.setFont(font)
        self.nif.setText(_fromUtf8(""))
        self.nif.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nif.setObjectName(_fromUtf8("nif"))
        self.gridLayout_3.addWidget(self.nif, 1, 4, 1, 1)
        self.titular = QtGui.QLabel(self.ot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titular.sizePolicy().hasHeightForWidth())
        self.titular.setSizePolicy(sizePolicy)
        self.titular.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.titular.setFont(font)
        self.titular.setText(_fromUtf8(""))
        self.titular.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titular.setObjectName(_fromUtf8("titular"))
        self.gridLayout_3.addWidget(self.titular, 3, 1, 1, 4)
        self.mastit = QtGui.QPushButton(self.ot)
        self.mastit.setObjectName(_fromUtf8("mastit"))
        self.gridLayout_3.addWidget(self.mastit, 3, 5, 1, 1)
        self.verticalLayout.addWidget(self.ot)
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 15))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.showinfo = QtGui.QCheckBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showinfo.sizePolicy().hasHeightForWidth())
        self.showinfo.setSizePolicy(sizePolicy)
        self.showinfo.setMinimumSize(QtCore.QSize(0, 15))
        self.showinfo.setMaximumSize(QtCore.QSize(1666777, 1666777))
        self.showinfo.setAutoFillBackground(False)
        self.showinfo.setText(_fromUtf8(""))
        self.showinfo.setObjectName(_fromUtf8("showinfo"))
        self.verticalLayout_2.addWidget(self.showinfo)
        self.verticalLayout.addWidget(self.widget)
        self.info_ot = QtGui.QWidget(Form)
        self.info_ot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.info_ot.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border: 0px;\n"
"    border-radius: 0 px;\n"
"    border-bottom: 1px solid darkgrey;\n"
"    \n"
"}\n"
"QLabel {\n"
"    font-weight: bold;\n"
"    color: rgb(143,212,0);\n"
"}"))
        self.info_ot.setObjectName(_fromUtf8("info_ot"))
        self.gridLayout_2 = QtGui.QGridLayout(self.info_ot)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(5, 6, 5, 6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.l_info_3 = QtGui.QLabel(self.info_ot)
        self.l_info_3.setObjectName(_fromUtf8("l_info_3"))
        self.gridLayout_2.addWidget(self.l_info_3, 14, 3, 1, 1, QtCore.Qt.AlignTop)
        self.l_info_2 = QtGui.QLabel(self.info_ot)
        self.l_info_2.setObjectName(_fromUtf8("l_info_2"))
        self.gridLayout_2.addWidget(self.l_info_2, 13, 3, 1, 1, QtCore.Qt.AlignTop)
        self.l_info_1 = QtGui.QLabel(self.info_ot)
        self.l_info_1.setObjectName(_fromUtf8("l_info_1"))
        self.gridLayout_2.addWidget(self.l_info_1, 12, 3, 1, 1, QtCore.Qt.AlignTop)
        self.e_info_1 = QtGui.QLineEdit(self.info_ot)
        self.e_info_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_info_1.setObjectName(_fromUtf8("e_info_1"))
        self.gridLayout_2.addWidget(self.e_info_1, 12, 4, 1, 1)
        self.e_info_2 = QtGui.QLineEdit(self.info_ot)
        self.e_info_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_info_2.setObjectName(_fromUtf8("e_info_2"))
        self.gridLayout_2.addWidget(self.e_info_2, 13, 4, 1, 1)
        self.e_info_3 = QtGui.QLineEdit(self.info_ot)
        self.e_info_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.e_info_3.setObjectName(_fromUtf8("e_info_3"))
        self.gridLayout_2.addWidget(self.e_info_3, 14, 4, 1, 1)
        self.titulo = QtGui.QLabel(self.info_ot)
        self.titulo.setStyleSheet(_fromUtf8("QLabel {\n"
"    Color: rgb(90,90,90)\n"
"}"))
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.gridLayout_2.addWidget(self.titulo, 11, 3, 1, 2)
        self.verticalLayout.addWidget(self.info_ot, QtCore.Qt.AlignTop)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.dato3.setText(_translate("Form", "Titular:", None))
        self.dato1.setText(_translate("Form", "Cargo:", None))
        self.dato2.setText(_translate("Form", "NIF:", None))
        self.mastit.setText(_translate("Form", "+", None))
        self.l_info_3.setText(_translate("Form", "Período:", None))
        self.l_info_2.setText(_translate("Form", "Estado:", None))
        self.l_info_1.setText(_translate("Form", "Importe:", None))
        self.titulo.setText(_translate("Form", "Detalles del último valor", None))

import ficheros_rc
