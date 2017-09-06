# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectordialog.ui'
#
# Created: Tue Aug 08 15:00:44 2017
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
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(375, 351)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("QWidget#organismos {\n"
"    border: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
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
"}"))
        self.organismos = QtGui.QListWidget(Dialog)
        self.organismos.setGeometry(QtCore.QRect(21, 110, 331, 192))
        self.organismos.setStyleSheet(_fromUtf8(""))
        self.organismos.setObjectName(_fromUtf8("organismos"))
        self.aceptar = QtGui.QPushButton(Dialog)
        self.aceptar.setGeometry(QtCore.QRect(138, 319, 111, 23))
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(134, 9, 101, 71))
        self.frame.setStyleSheet(_fromUtf8("QFrame {\n"
"background-image: url(:/img/fondo.jpg);\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(25, 89, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.aceptar.setText(_translate("Dialog", "Aceptar", None))
        self.label.setText(_translate("Dialog", "Seleccione organismo:", None))

import ficheros_rc
