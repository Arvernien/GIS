# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue Aug 08 12:16:37 2017
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
        Form.resize(544, 419)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nif = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nif.sizePolicy().hasHeightForWidth())
        self.nif.setSizePolicy(sizePolicy)
        self.nif.setObjectName(_fromUtf8("nif"))
        self.gridLayout.addWidget(self.nif, 1, 4, 1, 1)
        self.tnif = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tnif.sizePolicy().hasHeightForWidth())
        self.tnif.setSizePolicy(sizePolicy)
        self.tnif.setMaximumSize(QtCore.QSize(30, 16777215))
        self.tnif.setObjectName(_fromUtf8("tnif"))
        self.gridLayout.addWidget(self.tnif, 1, 3, 1, 1)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 5)
        self.nombre = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre.sizePolicy().hasHeightForWidth())
        self.nombre.setSizePolicy(sizePolicy)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 1, 1, 1, 2)
        self.REF = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.REF.setFont(font)
        self.REF.setAlignment(QtCore.Qt.AlignCenter)
        self.REF.setObjectName(_fromUtf8("REF"))
        self.gridLayout.addWidget(self.REF, 0, 0, 1, 5)
        self.tnombre = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tnombre.sizePolicy().hasHeightForWidth())
        self.tnombre.setSizePolicy(sizePolicy)
        self.tnombre.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tnombre.setObjectName(_fromUtf8("tnombre"))
        self.gridLayout.addWidget(self.tnombre, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.nif.setText(_translate("Form", "TextLabel", None))
        self.tnif.setText(_translate("Form", "NIF:", None))
        self.nombre.setText(_translate("Form", "TextLabel", None))
        self.REF.setText(_translate("Form", "REFERENCIA", None))
        self.tnombre.setText(_translate("Form", "NOMBRE:", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))

