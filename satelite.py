# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'satelite.ui'
#
# Created: Mon Aug 07 09:32:28 2017
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
        Form.resize(79, 79)
        self.satelite = QtGui.QCheckBox(Form)
        self.satelite.setGeometry(QtCore.QRect(2, 2, 75, 75))
        self.satelite.setStyleSheet(_fromUtf8("QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/catastro.jpg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/img/satelite.jpg)\n"
"}"))
        self.satelite.setText(_fromUtf8(""))
        self.satelite.setObjectName(_fromUtf8("satelite"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

import ficheros_rc
