# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\BuscaAvancada.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1174, 781)
        Dialog.setMinimumSize(QtCore.QSize(1174, 781))
        Dialog.setMaximumSize(QtCore.QSize(1174, 781))
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(23, 110, 311, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_Titulo = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Titulo.setGeometry(QtCore.QRect(10, 30, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_Titulo.setFont(font)
        self.radioButton_Titulo.setObjectName("radioButton_Titulo")
        self.radioButton_Autor = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Autor.setGeometry(QtCore.QRect(10, 60, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_Autor.setFont(font)
        self.radioButton_Autor.setObjectName("radioButton_Autor")
        self.radioButton_Genero = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Genero.setGeometry(QtCore.QRect(10, 90, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_Genero.setFont(font)
        self.radioButton_Genero.setObjectName("radioButton_Genero")
        self.radioButton_Publicacao = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Publicacao.setGeometry(QtCore.QRect(10, 120, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_Publicacao.setFont(font)
        self.radioButton_Publicacao.setObjectName("radioButton_Publicacao")
        self.radioButton_Nota = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Nota.setGeometry(QtCore.QRect(10, 150, 95, 20))
        self.radioButton_Nota.setObjectName("radioButton_Nota")
        self.radioButton_finalizado = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_finalizado.setGeometry(QtCore.QRect(10, 180, 181, 20))
        self.radioButton_finalizado.setObjectName("radioButton_finalizado")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 441, 1101, 311))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1301, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UI\\../design/busca_avancada.png"))
        self.label.setObjectName("label")
        self.pushButton_buscar = QtWidgets.QPushButton(Dialog)
        self.pushButton_buscar.setGeometry(QtCore.QRect(1032, 387, 111, 41))
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_titulo = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_titulo.setGeometry(QtCore.QRect(90, 341, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_titulo.setFont(font)
        self.lineEdit_titulo.setObjectName("lineEdit_titulo")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(240, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_autor = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_autor.setGeometry(QtCore.QRect(300, 341, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_autor.setFont(font)
        self.lineEdit_autor.setObjectName("lineEdit_autor")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(450, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(680, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_publicacao = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_publicacao.setGeometry(QtCore.QRect(850, 340, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_publicacao.setFont(font)
        self.lineEdit_publicacao.setObjectName("lineEdit_publicacao")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 389, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(240, 389, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.dateEdit_inicio = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_inicio.setGeometry(QtCore.QRect(410, 390, 121, 31))
        self.dateEdit_inicio.setCalendarPopup(True)
        self.dateEdit_inicio.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_inicio.setObjectName("dateEdit_inicio")
        self.dateEdit_termino = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_termino.setGeometry(QtCore.QRect(570, 390, 121, 31))
        self.dateEdit_termino.setCalendarPopup(True)
        self.dateEdit_termino.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_termino.setObjectName("dateEdit_termino")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(547, 395, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox_genero = QtWidgets.QComboBox(Dialog)
        self.comboBox_genero.setGeometry(QtCore.QRect(527, 340, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_genero.setFont(font)
        self.comboBox_genero.setObjectName("comboBox_genero")
        self.comboBox_nota = QtWidgets.QComboBox(Dialog)
        self.comboBox_nota.setGeometry(QtCore.QRect(90, 390, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_nota.setFont(font)
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
        self.label.raise_()
        self.groupBox.raise_()
        self.tableWidget.raise_()
        self.pushButton_buscar.raise_()
        self.label_2.raise_()
        self.lineEdit_titulo.raise_()
        self.label_3.raise_()
        self.lineEdit_autor.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_publicacao.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.dateEdit_inicio.raise_()
        self.dateEdit_termino.raise_()
        self.label_8.raise_()
        self.comboBox_genero.raise_()
        self.comboBox_nota.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Busca Avançada"))
        self.groupBox.setTitle(_translate("Dialog", "Buscar por:"))
        self.radioButton_Titulo.setText(_translate("Dialog", "Título"))
        self.radioButton_Autor.setText(_translate("Dialog", "Autor"))
        self.radioButton_Genero.setText(_translate("Dialog", "Gênero"))
        self.radioButton_Publicacao.setText(_translate("Dialog", "Ano de publicação"))
        self.radioButton_Nota.setText(_translate("Dialog", "Nota"))
        self.radioButton_finalizado.setText(_translate("Dialog", "Data de finalização"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "índex"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Título"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Autor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Nota"))
        self.pushButton_buscar.setText(_translate("Dialog", "Buscar"))
        self.label_2.setText(_translate("Dialog", "Título:"))
        self.label_3.setText(_translate("Dialog", "Autor:"))
        self.label_4.setText(_translate("Dialog", "Gênero:"))
        self.label_5.setText(_translate("Dialog", "Ano de publicação:"))
        self.label_6.setText(_translate("Dialog", "Nota:"))
        self.label_7.setText(_translate("Dialog", "Busca entre datas:"))
        self.label_8.setText(_translate("Dialog", "-"))
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