# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProximasLeituras.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(799, 509)
        Dialog.setMinimumSize(QtCore.QSize(799, 509))
        Dialog.setMaximumSize(QtCore.QSize(799, 509))
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(537, 105, 231, 341))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 801, 531))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/proximas_leituras.png"))
        self.label.setObjectName("label")
        self.pushButton_adicionar = QtWidgets.QPushButton(Dialog)
        self.pushButton_adicionar.setGeometry(QtCore.QRect(15, 210, 111, 28))
        self.pushButton_adicionar.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_adicionar.setObjectName("pushButton_adicionar")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(23, 166, 361, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_remover = QtWidgets.QPushButton(Dialog)
        self.pushButton_remover.setGeometry(QtCore.QRect(660, 460, 111, 28))
        self.pushButton_remover.setStyleSheet("background-color: rgb(240, 65, 68);")
        self.pushButton_remover.setObjectName("pushButton_remover")
        self.label.raise_()
        self.listWidget.raise_()
        self.pushButton_adicionar.raise_()
        self.lineEdit.raise_()
        self.pushButton_remover.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Póximas leituras"))
        self.pushButton_adicionar.setText(_translate("Dialog", "Adicionar título"))
        self.pushButton_remover.setText(_translate("Dialog", "Remover título"))
