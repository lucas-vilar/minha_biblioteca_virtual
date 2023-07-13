import sys
import time
import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import csv
import EditarLivro
from Main_Window import Ui_MainWindow
import AdicionarLivroManualmente
import AdicionarLivroArquivo
import AdicionarGenero
import DB_Operations
import ProximasLeituras
import BuscaAvancada
import NovaMeta
import Livro


#Cria a classe da janela principal da aplicação
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #Cria e/ou conecta com o banco de dados
        DB_Operations.create_db()

        #Configura o tableWidget
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 750)
        self.tableWidget.setColumnWidth(2, 535)
        self.tableWidget.setColumnWidth(3, 107)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.pushButton_finalizado.setVisible(False)

        self.tableWidget.itemDoubleClicked.connect(lambda: self.item_button_clicked())

        #Conecta as funções com cada ActionButton
        self.actionAdicionar_manualmente.triggered.connect(lambda: self.adicionar_livro_manualmente_button_clicked())
        self.actionAdicionar_a_partir_de_um_arquivo.triggered.connect(lambda: self.adicionar_livro_arquivo_button_clicked())
        self.actionInserir_titulo.triggered.connect(lambda: self.proximas_leituras_button_clicked())
        self.actionBuscar.triggered.connect(lambda: self.buscar_button_clicked())

        #Ações em relação a metas
        #Conecta as funções com cada botão relacionado a meta
        self.pushButton_NovaMeta.clicked.connect(lambda: self.nova_meta_button_clicked())
        self.pushButton_MetaCumprida.clicked.connect(lambda: self.meta_cumprida_button_cliked())
        self.pushButton_DescartarMeta.clicked.connect(lambda: self.descartar_meta_button_clicked())

        #Ao clicar no botão 'finalizado' em relação a proxima leitura, chama a função proxima_leitura_completa() com o texto da label ProximaLeitura como parametro
        self.pushButton_finalizado.clicked.connect(lambda: self.proxima_leitura_completa(self.label_ProximaLeitura.text()))

        #A cada troca de foco, chama a função troca_de_foco()
        app.focusWindowChanged.connect(self.atualiza_colecao)

#A cada chamada atualiza todos os dados da tela principal
    def atualiza_colecao(self):
        #Atualização do tableWidget com todos os livros lidos
        self.tableWidget.setRowCount(0)
        colecao_atual = DB_Operations.busca_todos_livros()
        for i in range(0, len(colecao_atual)):
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(colecao_atual[i][0])))
            self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(colecao_atual[i][1]))
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(colecao_atual[i][2]))
            self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(int(colecao_atual[i][7]))))

        #Atualiza o total de livros, numero de páginas, autor, gênero e editora favoritas
        self.label_TotalLivros.setText(str(DB_Operations.total_livros_lidos()))
        self.label_TotalPaginas.setText(str(DB_Operations.total_paginas_lidas()))
        self.label_AutorFav.setText(str(DB_Operations.autor_favorito()))
        self.label_GeneroFav.setText(str(DB_Operations.genero_favorito()))
        self.label_AutorFav_2.setText(str(DB_Operations.editora_favorita()))

        #Atualiza a próxima leitura
        self.label_ProximaLeitura.setText(str(DB_Operations.busca_proxima_leitura()))

        #Caso não houver uma próxima leitura cadastrada, o texto da label será ''
        if self.label_ProximaLeitura.text() == '':
            self.pushButton_finalizado.setVisible(False)
        else:
            self.pushButton_finalizado.setVisible(True)

        #Atualizações das metas
        if DB_Operations.busca_meta():
            self.label_meta.setText(DB_Operations.busca_meta()[0])
            prazo_maximo = datetime.datetime.strptime(DB_Operations.busca_meta()[1], '%d/%m/%Y').date()
            if prazo_maximo <= datetime.date.today():
                self.label_prazo.setText('Prazo máximo estourado para a conclusão da meta!')
            else:
                #Formata a data restante para conclusão e insere no label
                data_restante = str(prazo_maximo - datetime.date.today())
                data_restante = data_restante.split(',')
                data_restante = data_restante[0].split(' ')
                self.label_prazo.setText(f'{data_restante[0]} dias restantes para conclusão da meta!')
        else:
            self.label_meta.setText('')
            self.label_prazo.setText('')

#Chama a tela de adicionar livro manualmente
    def adicionar_livro_manualmente_button_clicked(self, titulo=''):
        dialog = AdicionarLivroManualmenteWindow(self, titulo=titulo)
        dialog.exec()

#Chama a tela de adicionar livros a partir de um arquivo
    def adicionar_livro_arquivo_button_clicked(self):
        dialog = AdicionarLivroArquivoWindow(self)
        dialog.exec()

#Ação ao clicar em um item no tableWidget, chama a tela de Visualizar livro, com o Id do livro selecionado
    def item_button_clicked(self):
        try:
            index_selecionado = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            dialog = VisualizarLivroWindow(self, index_selecionado)
            dialog.exec()
        except Exception as e:
            print(e)

#Chama a tela Próximas leituras
    def proximas_leituras_button_clicked(self):
        dialog = ProximasLeiturasWindow(self)
        dialog.exec()

#Ação ao clicar no botão 'finalizado'
    def proxima_leitura_completa(self, titulo):
        livro = self.label_ProximaLeitura.text()
        DB_Operations.deleta_proxima_leitura(livro)
        mensagem_dialog = QMessageBox(self)
        mensagem_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        mensagem_dialog.setIcon(QMessageBox.Question)
        mensagem_dialog.setWindowTitle("Livro finalizado")
        mensagem_dialog.setText(f"Livro '{titulo}' finalizado!\nDeseja adicioná-lo na lista de livros finalizados agora?")
        acao = mensagem_dialog.exec()
        if acao == QMessageBox.Yes:
            self.adicionar_livro_manualmente_button_clicked(livro)

#Chama a tela de metas
    def nova_meta_button_clicked(self):
        dialog = NovaMetaWindow(self)
        dialog.exec()

#Ação ao clicar no botão de meta cumprida
    def meta_cumprida_button_cliked(self):
        try:
            DB_Operations.deleta_meta()

            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Information)
            mensagem_dialog.setWindowTitle("Sucesso!")
            mensagem_dialog.setText('     Parabéns!     ')
            mensagem_dialog.exec()

        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f'Houve algum erro:\n{e}')
            mensagem_dialog.exec()

#Ação ao clicar no botão descarta meta
    def descartar_meta_button_clicked(self):
        mensagem_dialog = QMessageBox(self)
        mensagem_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        mensagem_dialog.setIcon(QMessageBox.Warning)
        mensagem_dialog.setWindowTitle("Ação irreversível!")
        mensagem_dialog.setText('Deseja realmente descartar a meta atual?')
        acao = mensagem_dialog.exec()
        if acao == QMessageBox.Yes:
            try:
                DB_Operations.deleta_meta()
                self.label_meta.setText('')
                self.label_prazo.setText('')
            except Exception as e:
                mensagem_dialog = QMessageBox(self)
                mensagem_dialog.setStandardButtons(QMessageBox.Ok)
                mensagem_dialog.setIcon(QMessageBox.Warning)
                mensagem_dialog.setWindowTitle("Erro!")
                mensagem_dialog.setText(f'Houve algum erro:\n{e}')
                mensagem_dialog.exec()

#Chama a tela Busca Avançada
    def buscar_button_clicked(self):
        dialog = BuscaAvancadaWindow(self)
        dialog.exec()


#Classe da tela Adicionar Livro Manualmente
class AdicionarLivroManualmenteWindow(QtWidgets.QDialog):
    def __init__(self, parent=None, titulo=''):
        super().__init__(parent)
        self.ui = AdicionarLivroManualmente.Ui_Dialog()
        self.ui.setupUi(self)

        #Sempre retorna o último id + 1 e insere no label id
        self.ui.label_id.setText(str(DB_Operations.get_max_id()))

        #Insere o titulo no lineEdit titulo
        self.ui.lineEdit_Titulo.setText(str(titulo))

        #Conecta as funções com cada ActionButton
        self.ui.pushButton_AdicionarLivro.clicked.connect(lambda: self.adicionar_livro(self.ui.lineEdit_Titulo.text()))
        self.ui.pushButton_LimparCampos.clicked.connect(lambda: self.limpar_campos_button())
        self.ui.pushButton_adicionargenero.clicked.connect(lambda: self.adicionar_genero())

        #A cada troca de foco chama a função atualiza_genero
        app.focusWindowChanged.connect(lambda: self.atualiza_genero())

    #Chama a tela adiciona genero
    def adicionar_genero(self):
        dialog = AdicionarGeneroWindow(self)
        dialog.exec()

    #Atualiza com os generos existentes no banco e dados
    def atualiza_genero(self):
        self.ui.comboBox_Genero.clear()
        generos = DB_Operations.busca_todos_generos()
        for genero in generos:
            self.ui.comboBox_Genero.addItem(genero[0])

    #Função que adiciona um novo livro no banco de dados
    def adicionar_livro(self, titulo):
        try:
            if not self.ui.lineEdit_Paginas.text().isdigit():
                raise Exception('Por favor, digite um número de páginas válido')

            if not self.ui.lineEdit_Ano_Publi.text().isdigit():
                raise Exception('Por favor, digite um ano de publicação válido')

            livro = Livro.Livro(titulo=self.ui.lineEdit_Titulo.text(),
                          autor=self.ui.lineEdit_Autor.text(),
                          n_paginas=int(self.ui.lineEdit_Paginas.text()),
                          genero=self.ui.comboBox_Genero.currentText(),
                          ano_lancamento=self.ui.lineEdit_Ano_Publi.text(),
                          nota=int(self.ui.comboBox_Nota.currentText()),
                          id=self.ui.label_id.text(),
                          data_finalizado=datetime.datetime.strptime(self.ui.dateEdit.text(), '%d/%m/%Y').date().strftime('%Y-%m-%d'),
                          editora=self.ui.lineEdit_Editora.text(),
                          resenha=self.ui.textEdit_Resenha.toPlainText()
                          )
            if livro.titulo != '' and livro.autor != '' and livro.ano_lancamento != '' and livro.n_paginas is not None and livro.genero != '':
                DB_Operations.inserir_livro(livro)
                mensagem_dialog = QMessageBox(self)
                mensagem_dialog.setStandardButtons(QMessageBox.Ok)
                mensagem_dialog.setIcon(QMessageBox.Information)
                mensagem_dialog.setWindowTitle("Sucesso!")
                mensagem_dialog.setText(f"Livro '{titulo}' adicionado com sucesso!")
                mensagem_dialog.exec()
                self.limpar_campos_button()
            else:
                raise Exception('Erro! Você preencheu todos os campos obrigatórios?')

        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f'{e}')
            mensagem_dialog.exec()
        finally:
            self.ui.label_id.setText(str(DB_Operations.get_max_id()))

    #Função que limpa todos os campos da tela
    def limpar_campos_button(self):
        self.ui.lineEdit_Titulo.setText('')
        self.ui.lineEdit_Autor.setText('')
        self.ui.comboBox_Genero.setCurrentIndex(-1)
        self.ui.lineEdit_Paginas.setText('')
        self.ui.lineEdit_Editora.setText('')
        self.ui.lineEdit_Ano_Publi.setText('')
        self.ui.textEdit_Resenha.setText('')
        self.ui.comboBox_Nota.setCurrentIndex(0)


#classe da tela adicionar livros a partir de um arquivo
class AdicionarLivroArquivoWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = AdicionarLivroArquivo.Ui_Dialog()
        self.ui.setupUi(self)

        #Configura o table Widget
        self.ui.tableWidget.setColumnWidth(0, 461)
        self.ui.tableWidget.setColumnWidth(1, 350)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.setColumnWidth(3, 150)
        self.ui.tableWidget.setColumnWidth(4, 150)
        self.ui.tableWidget.setColumnWidth(5, 150)
        self.ui.tableWidget.setColumnWidth(6, 100)
        self.ui.tableWidget.setColumnWidth(7, 130)
        self.ui.tableWidget.setColumnWidth(8, 100)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.ui.pushButton_importar.setVisible(False)

        #Conecta as funções com cada ActionButton
        self.ui.pushButton_escolher_arquivo.clicked.connect(lambda: self.abrir_arquivo_button_clicked())
        self.ui.pushButton_escolher_instrucao.clicked.connect(lambda: self.abrir_instrucao_button_clicked())
        self.ui.pushButton_importar.clicked.connect(lambda: self.importar_button_clicked())

    #Função chamada ao tentar abrir um novo arquivo
    def abrir_arquivo_button_clicked(self):
        nome_arquivo, _ = QFileDialog.getOpenFileName(self, "Escolher arquivo", "", "Arquivo CSV (*.csv)")
        if nome_arquivo:
            with open(nome_arquivo, 'r') as arquivo:
                reader = csv.reader(arquivo, delimiter=';')
                #pula a primeira linha, pois supõem-se que seja o cabeçalho
                next(reader)
                #Para cada livro no arquivo cria um objeto Livro
                lista_livros = map(lambda item: Livro.Livro(id=None, titulo=item[0], autor=item[1], ano_lancamento=item[2], n_paginas=item[3], genero=item[4], data_finalizado=item[5], nota=item[6], editora=item[7], resenha=item[8]), reader)
                try:
                    #Para cada livro, adiciona no tableWidget
                    for livro in lista_livros:
                        if not str(livro.n_paginas).isdigit():
                            raise Exception(f"O número de páginas do livro '{livro.titulo}' não é válido!")
                        if not str(livro.ano_lancamento).isdigit():
                            raise Exception(f"O ano de lançamento do livro {livro.titulo} não é válido!")
                        if livro.titulo != '' and livro.autor != '' and livro.ano_lancamento != '' and livro.n_paginas is not None and livro.genero != '':
                            row_position = self.ui.tableWidget.rowCount()
                            self.ui.tableWidget.insertRow(row_position)
                            self.ui.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(livro.titulo))
                            self.ui.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(livro.autor))
                            self.ui.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(livro.ano_lancamento))
                            self.ui.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(livro.n_paginas))
                            self.ui.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(livro.genero))
                            self.ui.tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(livro.data_finalizado))
                            self.ui.tableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(livro.nota))
                            self.ui.tableWidget.setItem(row_position, 7, QtWidgets.QTableWidgetItem(livro.editora))
                            self.ui.tableWidget.setItem(row_position, 8, QtWidgets.QTableWidgetItem(livro.resenha))
                        else:
                            raise Exception('Há campos obrigatórios não preenchidos no arquivo')
                except Exception as e:
                    dlg = QMessageBox(self)
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Warning)
                    dlg.setWindowTitle("Erro!")
                    dlg.setText(f"Erro na abertura do arquivo: \n{e}")
                    dlg.exec()
                else:
                    #Caso esteja tudo certo, o botão de importar torna-se visível
                    self.ui.pushButton_importar.setVisible(True)

    #Função que mostra as instruções de como deve ser o arquivo que será importado
    def abrir_instrucao_button_clicked(self):
        dlg = QMessageBox(self)
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.setWindowTitle("Instruções para importar sua coleção")
        dlg.setText('''Instruções:
1 - Clique em "Escolher arquivo"
2 - Selecione um arquivo .csv
3 - A primeira linha do .csv deve ser o cabeçalho do arquivo
4 - A ordem no arquivo deve ser: Título, autor, ano de lançamento, número de páginas, gênero, data de finalização, nota, editora e resenha
5 - Os campos obrigatórios são os mesmos que quando inserir um livro manualmente
6 - Clique em "Importar livros"''')
        dlg.exec()

    #Ações ao clicar no botão Importar
    def importar_button_clicked(self):
        try:
            for row in range(0, self.ui.tableWidget.rowCount()):
                livro = Livro.Livro(id=DB_Operations.get_max_id(),
                                titulo=self.ui.tableWidget.item(row, 0).text(),
                                autor=self.ui.tableWidget.item(row, 1).text(),
                                ano_lancamento=self.ui.tableWidget.item(row, 2).text(),
                                n_paginas=self.ui.tableWidget.item(row, 3).text(),
                                genero=self.ui.tableWidget.item(row, 4).text(),
                                data_finalizado=datetime.datetime.strptime(self.ui.tableWidget.item(row, 5).text(), '%d/%m/%Y').date().strftime('%Y-%m-%d'),
                                nota=self.ui.tableWidget.item(row, 6).text(),
                                editora=self.ui.tableWidget.item(row, 7).text(),
                                resenha=self.ui.tableWidget.item(row, 8).text())
                #Insere o livro no banco de dados
                DB_Operations.inserir_livro(livro)
                #Checa se o genero do livro existe e, se não existir, insere na tabela generos
                DB_Operations.checa_genero(livro.genero)
        except Exception as e:
            messagem_dialog = QMessageBox(self)
            messagem_dialog.setStandardButtons(QMessageBox.Ok)
            messagem_dialog.setIcon(QMessageBox.Warning)
            messagem_dialog.setWindowTitle("Erro!")
            messagem_dialog.setText(f"Erro ao inserir livros:\n{e}")
            messagem_dialog.exec()
        else:
            #Caso não ocorra nenhum erro, reseta o tableWidget e mostra uma mensagem de sucesso na tela
            messagem_dialog = QMessageBox(self)
            messagem_dialog.setStandardButtons(QMessageBox.Ok)
            messagem_dialog.setIcon(QMessageBox.Information)
            messagem_dialog.setWindowTitle("Sucesso!")
            messagem_dialog.setText("Livros inseridos com sucesso!")
            messagem_dialog.exec()
            self.ui.tableWidget.setRowCount(0)


#Classe da tela visualizar livro
class VisualizarLivroWindow(QtWidgets.QDialog):
    def __init__(self, parent=None, index_livro=''):
        super().__init__(parent)
        self.ui = EditarLivro.Ui_Dialog()
        self.ui.setupUi(self)

        #Torna o botão salvar e comboboxes e dateEdit invisiveis
        self.ui.pushButton_salvar.setVisible(False)
        self.ui.comboBox_nota.setVisible(False)
        self.ui.comboBox_genero.setVisible(False)
        self.ui.dateEdit_finalizacao.setVisible(False)

        #Recupera o livro com base no Id do item clicado no tableWidget da janela principal
        livro = DB_Operations.busca_livro_id(index_livro)

        #Preenche os campos com o livro selecionado
        self.ui.lineEdit_ID.setText(str(livro[0]))
        self.ui.lineEdit_titulo.setText(livro[1])
        self.ui.lineEdit_autor.setText(livro[2])
        self.ui.lineEdit_anopubli.setText(livro[3])
        self.ui.lineEdit_n_paginas.setText(str(livro[4]))
        self.ui.lineEdit_genero.setText(livro[5])
        generos = DB_Operations.busca_todos_generos()
        for genero in generos:
            self.ui.comboBox_genero.addItem(genero[0])
        self.ui.comboBox_genero.setCurrentText(livro[5])
        self.ui.lineEdit_finalizado.setText(str(livro[6]))
        self.ui.dateEdit_finalizacao.setDate(QtCore.QDate.fromString(livro[6], 'yyyy-MM-dd'))
        self.ui.lineEdit_nota.setText(str(int(livro[7])))
        self.ui.comboBox_nota.setCurrentIndex(int(livro[7]))
        self.ui.lineEdit_editora.setText(livro[8])
        self.ui.textEdit_resenha.setText(livro[9])

        #Conecta as funções com cada botão relacionado a meta
        self.ui.pushButton_editar.clicked.connect(lambda: self.editar_livro_button_clicked())
        self.ui.pushButton_salvar.clicked.connect(lambda: self.salva_edicao_button_clicked())
        self.ui.pushButton_deletar.clicked.connect(lambda: self.deletar_livro_button_clicked(self.ui.lineEdit_titulo.text()))

    #Ações ao clicar no botão editar livro
    def editar_livro_button_clicked(self):
        try:
            #Torna todos os campos editáveis
            self.ui.lineEdit_titulo.setEnabled(True)
            self.ui.lineEdit_autor.setEnabled(True)
            self.ui.lineEdit_editora.setEnabled(True)
            self.ui.lineEdit_genero.setEnabled(True)
            self.ui.lineEdit_n_paginas.setEnabled(True)
            self.ui.lineEdit_anopubli.setEnabled(True)
            self.ui.textEdit_resenha.setEnabled(True)
            self.ui.pushButton_salvar.setVisible(True)
            self.ui.comboBox_nota.setVisible(True)
            self.ui.comboBox_genero.setVisible(True)
            self.ui.dateEdit_finalizacao.setVisible(True)

        except Exception as e:
            print(e)

    #Ação ao clicar no botão Salvar edições
    def salva_edicao_button_clicked(self):
        try:
            if not self.ui.lineEdit_n_paginas.text().isdigit():
                raise Exception('Por favor, digite um número de páginas válido')
            if not self.ui.lineEdit_anopubli.text().isdigit():
                raise Exception('Por favor, digite um ano de publicação válido')

            livro = Livro.Livro(titulo=self.ui.lineEdit_titulo.text(),
                                autor=self.ui.lineEdit_autor.text(),
                                n_paginas=int(self.ui.lineEdit_n_paginas.text()),
                                genero=self.ui.comboBox_genero.currentText(),
                                ano_lancamento=self.ui.lineEdit_anopubli.text(),
                                nota=int(self.ui.comboBox_nota.currentText()),
                                id=self.ui.lineEdit_ID.text(),
                                data_finalizado=datetime.datetime.strptime(self.ui.dateEdit_finalizacao.text(), '%d/%m/%Y').date().strftime('%Y-%m-%d'),
                                editora=self.ui.lineEdit_editora.text(),
                                resenha=self.ui.textEdit_resenha.toPlainText()
                                )
            if livro.titulo != '' and livro.autor != '' and livro.ano_lancamento != '' and livro.n_paginas is not None and livro.genero != '':
                DB_Operations.altera_livro(livro)
            else:
                raise Exception('Erro! Você preencheu todos os campos obrigatórios?')
        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f"{e}")
            mensagem_dialog.exec()
        else:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Information)
            mensagem_dialog.setWindowTitle("Sucesso!")
            mensagem_dialog.setText("Livro atualizado com sucesso!")
            mensagem_dialog.exec()
            time.sleep(0.3)
            self.close()

    #Ações co clicar no botão deletar o livro
    def deletar_livro_button_clicked(self, titulo):
        mensagem_dialog = QMessageBox(self)
        mensagem_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        mensagem_dialog.setIcon(QMessageBox.Warning)
        mensagem_dialog.setWindowTitle("Ação permanente!")
        mensagem_dialog.setText(f"Você tem certeza que deseja deletar o livro '{titulo}'?\nEssa ação não poderá ser revertida")
        acao = mensagem_dialog.exec()
        #Caso o usuário confirme a ação de deletar, o livro será excluído do banco de dados
        if acao == QMessageBox.Yes:
            try:
                DB_Operations.deleta_livro(int(self.ui.lineEdit_ID.text()))
            except Exception as e:
                print(e)
            else:
                time.sleep(0.3)
                self.close()


#Classe da tela adicionar genero
class AdicionarGeneroWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = AdicionarGenero.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_adicionargenero.clicked.connect(lambda: self.inserir_genero())

    #Ação de inserir um novo genero
    def inserir_genero(self):
        try:
            if self.ui.lineEdit_genero.text() == '':
                raise Exception('Por favor insira um gênero!')
            DB_Operations.inserir_genero(self.ui.lineEdit_genero.text())
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Information)
            mensagem_dialog.setWindowTitle("Sucesso!")
            mensagem_dialog.setText("Gênero inserido com sucesso!")
            mensagem_dialog.exec()
            time.sleep(0.3)
            self.close()
        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f"{e}")
            mensagem_dialog.exec()
            time.sleep(0.3)
            self.close()


#Classe da tela próximas leituras
class ProximasLeiturasWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ProximasLeituras.Ui_Dialog()
        self.ui.setupUi(self)

        #Conecta as funções com cata botão
        self.ui.pushButton_adicionar.clicked.connect(lambda: self.inserir_proximo_livro())
        self.ui.pushButton_remover.clicked.connect(lambda: self.deletar_item_selecionado(self.ui.listWidget.currentItem().text()) if self.ui.listWidget.currentItem() else self.deletar_item_selecionado(''))

        #A cada troca de foco, a função muda_foco() é chamada
        app.focusWindowChanged.connect(lambda: self.muda_foco())

    def muda_foco(self):
        #Atualiza a lista com as próximas leituras
        self.ui.listWidget.clear()
        try:
            proximas_leituras = DB_Operations.busca_proximas_leituras()
            if proximas_leituras:
                for titulo in proximas_leituras:
                    self.ui.listWidget.addItem(titulo[0])
        except Exception as e:
            dlg = QMessageBox(self)
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)
            dlg.setWindowTitle("Erro!")
            dlg.setText(f"{e}")
            dlg.exec()
        #Caso haja elementos na lista, o botão de remover um título torna-se visível
        if self.ui.listWidget.count():
            self.ui.pushButton_remover.setVisible(True)
        else:
            self.ui.pushButton_remover.setVisible(False)

    #Ação de inserir um novo título para proxima leitura
    def inserir_proximo_livro(self):
        try:
            if self.ui.lineEdit.text() == '':
                raise Exception('Por favor insira um título!')
            DB_Operations.insere_proxima_leitura(self.ui.lineEdit.text())
            self.ui.listWidget.addItem(self.ui.lineEdit.text())
        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f"{e}")
            mensagem_dialog.exec()
        else:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Information)
            mensagem_dialog.setWindowTitle("Sucesso!")
            mensagem_dialog.setText('Título adicionado com sucesso!')
            mensagem_dialog.exec()

    #Ação de deletar um título das proximas leituras
    def deletar_item_selecionado(self, titulo):
        try:
            if titulo == '':
                raise Exception('Nenhum título selecionado')
            DB_Operations.deleta_proxima_leitura(titulo)
        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f'Houve um erro na deleção do título:\n{e}')
            mensagem_dialog.exec()
        else:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Sucesso!")
            mensagem_dialog.setText(f'''Título '{titulo}' removido das próximas leituras!''')
            mensagem_dialog.exec()


#Classe da tela metas
class NovaMetaWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = NovaMeta.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(lambda: self.adicionar_meta())

    #Ação de adicionar uma nova meta
    def adicionar_meta(self):
        try:
            #Alerta o usuário que, ao adicionar uma nova meta, a meta atual será excluída
            if DB_Operations.busca_meta():
                mensagem_dialog = QMessageBox(self)
                mensagem_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                mensagem_dialog.setIcon(QMessageBox.Warning)
                mensagem_dialog.setWindowTitle("Ação permanente!")
                mensagem_dialog.setText(f'''Ao adicionar uma nova meta, a meta atual será descartada. Deseja confirmar a ação?''')
                acao = mensagem_dialog.exec()
                if acao == QMessageBox.Yes:
                    prazo = datetime.datetime.strptime(self.ui.dateEdit.text(), '%d/%m/%Y').date()
                    # Não permite o usuario criar uma meta com um prazo que já passou
                    if prazo < datetime.date.today():
                        raise Exception('Você não pode cumprir uma meta que o prazo máximo já passou!')
                    DB_Operations.deleta_meta()
                    DB_Operations.insere_meta(self.ui.textEdit.toPlainText(), prazo.strftime('%d/%m/%Y'))
            else:
                prazo = datetime.datetime.strptime(self.ui.dateEdit.text(), '%d/%m/%Y').date()
                #Não permite o usuario criar uma meta com um prazo que já passou
                if prazo < datetime.date.today():
                    raise Exception('Você não pode cumprir uma meta que o prazo máximo já passou!')
                DB_Operations.insere_meta(self.ui.textEdit.toPlainText(), prazo.strftime('%d/%m/%Y'))
        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f'''{e}''')
            mensagem_dialog.exec()
        else:
            time.sleep(0.3)
            self.close()


#Classe da tela busca avançada
class BuscaAvancadaWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = BuscaAvancada.Ui_Dialog()
        self.ui.setupUi(self)

        #configura o tableWidget
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 600)
        self.ui.tableWidget.setColumnWidth(2, 335)
        self.ui.tableWidget.setColumnWidth(3, 66)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        #Torna todos os campos não alteráveis
        self.ui.lineEdit_autor.setEnabled(False)
        self.ui.comboBox_genero.setEnabled(False)
        self.ui.lineEdit_titulo.setEnabled(False)
        self.ui.comboBox_nota.setEnabled(False)
        self.ui.lineEdit_publicacao.setEnabled(False)
        self.ui.dateEdit_inicio.setEnabled(False)
        self.ui.dateEdit_termino.setEnabled(False)
        #Adiciona todos os generos no combobox
        generos = DB_Operations.busca_todos_generos()
        for genero in generos:
            self.ui.comboBox_genero.addItem(genero[0])

        #Conecta as ações com cada radiobutton
        self.ui.radioButton_Titulo.clicked.connect(lambda: self.radio_titulo_clicked())
        self.ui.radioButton_Autor.clicked.connect(lambda: self.radio_autor_clicked())
        self.ui.radioButton_Genero.clicked.connect(lambda: self.radio_genero_clicked())
        self.ui.radioButton_Nota.clicked.connect(lambda: self.radio_nota_clicked())
        self.ui.radioButton_Publicacao.clicked.connect(lambda: self.radio_publicacao_clicked())
        self.ui.radioButton_finalizado.clicked.connect(lambda: self.radio_finalizado_clicked())
        self.ui.pushButton_buscar.clicked.connect(lambda: self.buscar_button_clicked())

    #Para cada radiobutton clicado, torna apenas o respectivo campo editável
    def radio_titulo_clicked(self):
        self.ui.lineEdit_autor.setEnabled(False)
        self.ui.comboBox_genero.setEnabled(False)
        self.ui.lineEdit_titulo.setEnabled(True)
        self.ui.comboBox_nota.setEnabled(False)
        self.ui.lineEdit_publicacao.setEnabled(False)
        self.ui.dateEdit_inicio.setEnabled(False)
        self.ui.dateEdit_termino.setEnabled(False)

    def radio_autor_clicked(self):
        self.ui.lineEdit_autor.setEnabled(True)
        self.ui.comboBox_genero.setEnabled(False)
        self.ui.lineEdit_titulo.setEnabled(False)
        self.ui.comboBox_nota.setEnabled(False)
        self.ui.lineEdit_publicacao.setEnabled(False)
        self.ui.dateEdit_inicio.setEnabled(False)
        self.ui.dateEdit_termino.setEnabled(False)

    def radio_genero_clicked(self):
        self.ui.lineEdit_autor.setEnabled(False)
        self.ui.comboBox_genero.setEnabled(True)
        self.ui.lineEdit_titulo.setEnabled(False)
        self.ui.comboBox_nota.setEnabled(False)
        self.ui.lineEdit_publicacao.setEnabled(False)
        self.ui.dateEdit_inicio.setEnabled(False)
        self.ui.dateEdit_termino.setEnabled(False)

    def radio_nota_clicked(self):
        self.ui.lineEdit_autor.setEnabled(False)
        self.ui.comboBox_genero.setEnabled(False)
        self.ui.lineEdit_titulo.setEnabled(False)
        self.ui.comboBox_nota.setEnabled(True)
        self.ui.lineEdit_publicacao.setEnabled(False)
        self.ui.dateEdit_inicio.setEnabled(False)
        self.ui.dateEdit_termino.setEnabled(False)

    def radio_publicacao_clicked(self):
        self.ui.lineEdit_autor.setEnabled(False)
        self.ui.comboBox_genero.setEnabled(False)
        self.ui.lineEdit_titulo.setEnabled(False)
        self.ui.comboBox_nota.setEnabled(False)
        self.ui.lineEdit_publicacao.setEnabled(True)
        self.ui.dateEdit_inicio.setEnabled(False)
        self.ui.dateEdit_termino.setEnabled(False)

    def radio_finalizado_clicked(self):
        self.ui.lineEdit_autor.setEnabled(False)
        self.ui.comboBox_genero.setEnabled(False)
        self.ui.lineEdit_titulo.setEnabled(False)
        self.ui.comboBox_nota.setEnabled(False)
        self.ui.lineEdit_publicacao.setEnabled(False)
        self.ui.dateEdit_inicio.setEnabled(True)
        self.ui.dateEdit_termino.setEnabled(True)

    #Ação do botão buscar
    def buscar_button_clicked(self):
        try:
            resultado_busca = ''
            #Dependendo de qual radiobutton estiver ativo, diferentes queries podem ser chamadas
            if self.ui.radioButton_Titulo.isChecked():
                resultado_busca = DB_Operations.retorna_titulos_parciais(self.ui.lineEdit_titulo.text())
            elif self.ui.radioButton_Autor.isChecked():
                resultado_busca = DB_Operations.retorna_autor_selecionado(self.ui.lineEdit_autor.text())
            elif self.ui.radioButton_Genero.isChecked():
                resultado_busca = DB_Operations.retorna_genero_selecionado(self.ui.comboBox_genero.currentText())
            elif self.ui.radioButton_Nota.isChecked():
                resultado_busca = DB_Operations.retorna_nota_selecionado(int(self.ui.comboBox_nota.currentText()))
            elif self.ui.radioButton_Publicacao.isChecked():
                resultado_busca = DB_Operations.retorna_publicacao_selecionado(int(self.ui.lineEdit_publicacao.text()))
            elif self.ui.radioButton_finalizado.isChecked():
                resultado_busca = DB_Operations.retorna_finalizado_selecionado(datetime.datetime.strptime(self.ui.dateEdit_inicio.text(), '%d/%m/%Y').date().strftime('%Y-%m-%d'), datetime.datetime.strptime(self.ui.dateEdit_termino.text(), '%d/%m/%Y').date().strftime('%Y-%m-%d'))
            self.ui.tableWidget.setRowCount(0)
            #Insere os resultados das buscas no tableWidget
            for i in range(0, len(resultado_busca)):
                row_position = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_position)
                self.ui.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(resultado_busca[i][0])))
                self.ui.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(resultado_busca[i][1]))
                self.ui.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(resultado_busca[i][2]))
                self.ui.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(int(resultado_busca[i][7]))))
        except Exception as e:
            mensagem_dialog = QMessageBox(self)
            mensagem_dialog.setStandardButtons(QMessageBox.Ok)
            mensagem_dialog.setIcon(QMessageBox.Warning)
            mensagem_dialog.setWindowTitle("Erro!")
            mensagem_dialog.setText(f'''{e}''')
            mensagem_dialog.exec()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
