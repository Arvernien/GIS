# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmacion.ui'
#
# Created: Tue Aug 08 13:30:03 2017
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(570, 97)
        Dialog.setMaximumSize(QtCore.QSize(570, 16777215))
        Dialog.setStyleSheet(_fromUtf8("QPushButton {\n"
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
"}"))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.texto = QtGui.QLabel(Dialog)
        self.texto.setMaximumSize(QtCore.QSize(570, 16777215))
        self.texto.setText(_fromUtf8(""))
        self.texto.setObjectName(_fromUtf8("texto"))
        self.gridLayout.addWidget(self.texto, 0, 0, 1, 3)
        self.cancel = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.gridLayout.addWidget(self.cancel, 1, 2, 1, 1)
        self.ok = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.gridLayout.addWidget(self.ok, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.cancel.setText(_translate("Dialog", "No", None))
        self.ok.setText(_translate("Dialog", "Sí", None))

