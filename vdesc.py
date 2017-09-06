# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vdesc.ui'
#
# Created: Fri Aug 25 14:30:45 2017
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
        Form.resize(1100, 750)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1100, 750))
        Form.setMaximumSize(QtCore.QSize(1100, 750))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(6, -1, 6, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inmueble = QtGui.QLabel(Form)
        self.inmueble.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inmueble.setFont(font)
        self.inmueble.setAlignment(QtCore.Qt.AlignCenter)
        self.inmueble.setObjectName(_fromUtf8("inmueble"))
        self.gridLayout.addWidget(self.inmueble, 0, 0, 1, 5)
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.tfin = QtGui.QLabel(Form)
        self.tfin.setObjectName(_fromUtf8("tfin"))
        self.gridLayout.addWidget(self.tfin, 1, 1, 1, 2)
        self.labelfin = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelfin.setFont(font)
        self.labelfin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelfin.setObjectName(_fromUtf8("labelfin"))
        self.gridLayout.addWidget(self.labelfin, 1, 3, 1, 1)
        self.nfin = QtGui.QLabel(Form)
        self.nfin.setMinimumSize(QtCore.QSize(100, 0))
        self.nfin.setObjectName(_fromUtf8("nfin"))
        self.gridLayout.addWidget(self.nfin, 1, 4, 1, 1)
        self.labelnif = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelnif.setFont(font)
        self.labelnif.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelnif.setObjectName(_fromUtf8("labelnif"))
        self.gridLayout.addWidget(self.labelnif, 2, 3, 1, 1)
        self.ncand = QtGui.QLabel(Form)
        self.ncand.setText(_fromUtf8(""))
        self.ncand.setObjectName(_fromUtf8("ncand"))
        self.gridLayout.addWidget(self.ncand, 2, 4, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.tcand = QtGui.QLabel(Form)
        self.tcand.setText(_fromUtf8(""))
        self.tcand.setObjectName(_fromUtf8("tcand"))
        self.gridLayout.addWidget(self.tcand, 2, 1, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.marco = QtGui.QVBoxLayout()
        self.marco.setObjectName(_fromUtf8("marco"))
        self.horizontalLayout.addLayout(self.marco)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ldesc = QtGui.QListWidget(Form)
        self.ldesc.setMinimumSize(QtCore.QSize(310, 0))
        self.ldesc.setMaximumSize(QtCore.QSize(310, 16777215))
        self.ldesc.setObjectName(_fromUtf8("ldesc"))
        self.verticalLayout_2.addWidget(self.ldesc, QtCore.Qt.AlignRight)
        self.lcand = QtGui.QListWidget(Form)
        self.lcand.setMinimumSize(QtCore.QSize(310, 0))
        self.lcand.setMaximumSize(QtCore.QSize(310, 16777215))
        self.lcand.setObjectName(_fromUtf8("lcand"))
        self.verticalLayout_2.addWidget(self.lcand, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.salir = QtGui.QPushButton(Form)
        self.salir.setMaximumSize(QtCore.QSize(90, 16777215))
        self.salir.setObjectName(_fromUtf8("salir"))
        self.horizontalLayout_2.addWidget(self.salir)
        self.minimizar = QtGui.QPushButton(Form)
        self.minimizar.setMaximumSize(QtCore.QSize(90, 16777215))
        self.minimizar.setObjectName(_fromUtf8("minimizar"))
        self.horizontalLayout_2.addWidget(self.minimizar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.inmueble.setText(_translate("Form", "INMUEBLE", None))
        self.label.setText(_translate("Form", "TITULAR FIN:", None))
        self.tfin.setText(_translate("Form", "JUAN PEREZ", None))
        self.labelfin.setText(_translate("Form", "NIF FIN:", None))
        self.nfin.setText(_translate("Form", "JUAN PEREZ", None))
        self.labelnif.setText(_translate("Form", "NIF CANDIDATO:", None))
        self.label_4.setText(_translate("Form", "TITULAR CANDIDATO:", None))
        self.salir.setText(_translate("Form", "Salir", None))
        self.minimizar.setText(_translate("Form", "Minimizar", None))

