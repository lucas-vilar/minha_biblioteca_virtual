#Criação da classe livro
class Livro:
    def __init__(self, titulo, autor, n_paginas, genero, ano_lancamento, nota, id=None, data_finalizado=None, editora=None, resenha=None):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._n_paginas = n_paginas
        self._genero = genero
        self._ano_lancamento = ano_lancamento
        self._data_finalizado = data_finalizado
        self._nota = nota
        self._editora = editora
        self._resenha = resenha


#Criando os getters e setters de cada variável da classe livro utilizando decorators
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor

    @property
    def n_paginas(self):
        return self._n_paginas

    @n_paginas.setter
    def n_paginas(self, novo_n_paginas):
        self._n_paginas = novo_n_paginas

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, novo_genero):
        self._genero = novo_genero

    @property
    def ano_lancamento(self):
        return self._ano_lancamento

    @ano_lancamento.setter
    def ano_lancamento(self, novo_lancamento):
        self._ano_lancamento = novo_lancamento

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nova_nota):
        self._nota = nova_nota

    @property
    def data_finalizado(self):
        return self._data_finalizado

    @data_finalizado.setter
    def data_finalizado(self, nova_finalizado):
        self._data_finalizado = nova_finalizado

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, nova_editora):
        self._editora = nova_editora

    @property
    def resenha(self):
        return self._resenha

    @resenha.setter
    def resenha(self, nova_resenha):
        self._resenha = nova_resenha
