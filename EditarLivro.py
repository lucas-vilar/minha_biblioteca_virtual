# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarLivro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1274, 599)
        Dialog.setMinimumSize(QtCore.QSize(1274, 599))
        Dialog.setMaximumSize(QtCore.QSize(1274, 599))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1311, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/Visualizar_livro.png"))
        self.label.setObjectName("label")
        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setEnabled(False)
        self.lineEdit_ID.setGeometry(QtCore.QRect(65, 137, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_ID.setText("")
        self.lineEdit_ID.setFrame(False)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_titulo = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_titulo.setEnabled(False)
        self.lineEdit_titulo.setGeometry(QtCore.QRect(245, 137, 671, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_titulo.setFont(font)
        self.lineEdit_titulo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_titulo.setText("")
        self.lineEdit_titulo.setFrame(False)
        self.lineEdit_titulo.setObjectName("lineEdit_titulo")
        self.lineEdit_n_paginas = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_n_paginas.setEnabled(False)
        self.lineEdit_n_paginas.setGeometry(QtCore.QRect(1095, 137, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_n_paginas.setFont(font)
        self.lineEdit_n_paginas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_n_paginas.setText("")
        self.lineEdit_n_paginas.setFrame(False)
        self.lineEdit_n_paginas.setObjectName("lineEdit_n_paginas")
        self.lineEdit_autor = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_autor.setEnabled(False)
        self.lineEdit_autor.setGeometry(QtCore.QRect(100, 240, 671, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_autor.setFont(font)
        self.lineEdit_autor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_autor.setText("")
        self.lineEdit_autor.setFrame(False)
        self.lineEdit_autor.setObjectName("lineEdit_autor")
        self.lineEdit_genero = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_genero.setEnabled(False)
        self.lineEdit_genero.setGeometry(QtCore.QRect(913, 240, 221, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_genero.setFont(font)
        self.lineEdit_genero.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_genero.setText("")
        self.lineEdit_genero.setFrame(False)
        self.lineEdit_genero.setObjectName("lineEdit_genero")
        self.lineEdit_editora = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_editora.setEnabled(False)
        self.lineEdit_editora.setGeometry(QtCore.QRect(110, 342, 221, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_editora.setFont(font)
        self.lineEdit_editora.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_editora.setText("")
        self.lineEdit_editora.setFrame(False)
        self.lineEdit_editora.setObjectName("lineEdit_editora")
        self.lineEdit_anopubli = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_anopubli.setEnabled(False)
        self.lineEdit_anopubli.setGeometry(QtCore.QRect(565, 342, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_anopubli.setFont(font)
        self.lineEdit_anopubli.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_anopubli.setText("")
        self.lineEdit_anopubli.setFrame(False)
        self.lineEdit_anopubli.setObjectName("lineEdit_anopubli")
        self.lineEdit_finalizado = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_finalizado.setEnabled(False)
        self.lineEdit_finalizado.setGeometry(QtCore.QRect(883, 342, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_finalizado.setFont(font)
        self.lineEdit_finalizado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_finalizado.setText("")
        self.lineEdit_finalizado.setFrame(False)
        self.lineEdit_finalizado.setObjectName("lineEdit_finalizado")
        self.lineEdit_nota = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nota.setEnabled(False)
        self.lineEdit_nota.setGeometry(QtCore.QRect(1095, 342, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_nota.setFont(font)
        self.lineEdit_nota.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.lineEdit_nota.setText("")
        self.lineEdit_nota.setFrame(False)
        self.lineEdit_nota.setObjectName("lineEdit_nota")
        self.textEdit_resenha = QtWidgets.QTextEdit(Dialog)
        self.textEdit_resenha.setEnabled(False)
        self.textEdit_resenha.setGeometry(QtCore.QRect(30, 473, 511, 111))
        self.textEdit_resenha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.textEdit_resenha.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_resenha.setObjectName("textEdit_resenha")
        self.pushButton_salvar = QtWidgets.QPushButton(Dialog)
        self.pushButton_salvar.setGeometry(QtCore.QRect(690, 500, 121, 41))
        self.pushButton_salvar.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.pushButton_editar = QtWidgets.QPushButton(Dialog)
        self.pushButton_editar.setGeometry(QtCore.QRect(560, 500, 121, 41))
        self.pushButton_editar.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.pushButton_deletar = QtWidgets.QPushButton(Dialog)
        self.pushButton_deletar.setGeometry(QtCore.QRect(560, 550, 121, 41))
        self.pushButton_deletar.setStyleSheet("background-color: rgb(240, 65, 68);")
        self.pushButton_deletar.setObjectName("pushButton_deletar")
        self.comboBox_nota = QtWidgets.QComboBox(Dialog)
        self.comboBox_nota.setGeometry(QtCore.QRect(1096, 344, 55, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_nota.setFont(font)
        self.comboBox_nota.setMaxVisibleItems(11)
        self.comboBox_nota.setObjectName("comboBox_nota")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.comboBox_nota.addItem("")
        self.dateEdit_finalizacao = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_finalizacao.setGeometry(QtCore.QRect(880, 345, 115, 22))
        self.dateEdit_finalizacao.setCalendarPopup(True)
        self.dateEdit_finalizacao.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_finalizacao.setObjectName("dateEdit_finalizacao")
        self.comboBox_genero = QtWidgets.QComboBox(Dialog)
        self.comboBox_genero.setGeometry(QtCore.QRect(915, 241, 231, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_genero.setFont(font)
        self.comboBox_genero.setObjectName("comboBox_genero")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Visualizar livro"))
        self.textEdit_resenha.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_salvar.setText(_translate("Dialog", "Salvar alterações"))
        self.pushButton_editar.setText(_translate("Dialog", "Editar Livro"))
        self.pushButton_deletar.setText(_translate("Dialog", "Deletar Livro"))
        self.comboBox_nota.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_nota.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_nota.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_nota.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_nota.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_nota.setItemText(5, _translate("Dialog", "5"))
        self.comboBox_nota.setItemText(6, _translate("Dialog", "6"))
        self.comboBox_nota.setItemText(7, _translate("Dialog", "7"))
        self.comboBox_nota.setItemText(8, _translate("Dialog", "8"))
        self.comboBox_nota.setItemText(9, _translate("Dialog", "9"))
        self.comboBox_nota.setItemText(10, _translate("Dialog", "10"))
