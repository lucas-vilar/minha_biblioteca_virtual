from functools import reduce
import sqlite3


#Função de cria o banco de dados 'livros' e as tabelas 'livros', 'generos', 'proximas_leituras' e 'metas'
def create_db():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_lanc TEXT NOT NULL,
    n_paginas INTEGER NOT NULL,
    genero TEXT NOT NULL,
    data_finalizado TEXT,
    nota REAL,
    editora TEXT,
    resenha TEXT);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS generos(
            genero TEXT NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS proximas_leituras(
        titulo TEXT NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS metas(
            meta TEXT NOT NULL,
            prazo TEXT NOT NULL);''')

    cursor.close()


#Operações com a tabela livros
#Inserir um livro individualmente
def inserir_livro(livro):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO livros VALUES (
    {livro.id}, "{livro.titulo}", "{livro.autor}", "{livro.ano_lancamento}", {livro.n_paginas}, "{livro.genero}", "{livro.data_finalizado}", {livro.nota}, "{livro.editora}", "{livro.resenha}");''')
    connection.commit()
    cursor.close()


#Garantir que sempre um Id único e uma unidade maior que o anterior apareça na tela de inserir livro manualmente
def get_max_id():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    ultimo_id = cursor.execute('''SELECT * FROM livros ORDER BY id DESC''').fetchone()
    cursor.close()
    if ultimo_id is None:
        return 1
    return ultimo_id[0] + 1


#Retorna todos os livros cadastrados pelo usuário
def busca_todos_livros():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    minha_colecao = cursor.execute(f'''SELECT * FROM livros ORDER BY id DESC;''').fetchall()
    cursor.close()
    return minha_colecao


#Retorna o livro com base no ID
def busca_livro_id(id_selecionado):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    livro_id = cursor.execute(f'''SELECT * FROM livros WHERE id = {id_selecionado};''').fetchone()
    cursor.close()
    return livro_id


#Edita um livro na tabela livros com base no ID
def altera_livro(livro):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute(f''' UPDATE livros SET titulo = '{livro.titulo}', 
    autor = "{livro.autor}",
    ano_lanc = "{livro.ano_lancamento}",
    n_paginas = {livro.n_paginas},
    genero = "{livro.genero}",
    data_finalizado = "{livro.data_finalizado}",
    nota = {livro.nota},
    editora = "{livro.editora}",
    resenha = "{livro.resenha}" 
    WHERE id = {livro.id};''')
    connection.commit()
    cursor.close()


#Deleta um livro com base no ID
def deleta_livro(id_selecionado):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute(f''' DELETE FROM livros WHERE id = {id_selecionado};''')
    connection.commit()
    cursor.close()


#Retorna o número de livros lidos pelo usuário
def total_livros_lidos():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    total_livros = cursor.execute(f'''SELECT COUNT(*) FROM livros;''').fetchone()
    cursor.close()
    if total_livros is None:
        return '0'
    return total_livros[0]


#Retorna o total de páginas lidas pelo usuário
def total_paginas_lidas():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    total_paginas = cursor.execute(f'''SELECT SUM(n_paginas) FROM livros;''').fetchone()
    cursor.close()
    if total_paginas[0] is None:
        return '0'
    return total_paginas[0]


#Retorna o autor com maior número de livros lidos
def autor_favorito():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    if busca_todos_livros():
        autor_mais_frequente = reduce(lambda x, y: x if x[1] > y[1] else y, cursor.execute('''SELECT autor, COUNT(*) FROM livros GROUP BY autor;''').fetchall())
        cursor.close()
        return autor_mais_frequente[0]
    cursor.close()
    return ''


#Retorna o Gênero mais lido pelo usuário
def genero_favorito():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    if busca_todos_livros():
        genero_mais_frequente = reduce(lambda x, y: x if x[1] > y[1] else y, cursor.execute('''SELECT genero, COUNT(*) FROM livros GROUP BY genero;''').fetchall())
        cursor.close()
        return genero_mais_frequente[0]
    cursor.close()
    return ''


#Retorna a editora mais lida pelo usuário
def editora_favorita():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    if cursor.execute('''SELECT editora, COUNT(*) FROM livros WHERE editora != '' GROUP BY editora;''').fetchall():
        editora_mais_frequente = reduce(lambda x,y: x if x[1] > y[1] else y, cursor.execute('''SELECT editora, COUNT(*) FROM livros WHERE editora != '' GROUP BY editora;''').fetchall())
        cursor.close()
        return editora_mais_frequente[0]
    cursor.close()
    return ''


#Retorna livros que o título contenha a entrada do usuario
def retorna_titulos_parciais(entrada):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    resultados = cursor.execute(f'''SELECT * FROM livros WHERE titulo LIKE "%{entrada}%" ORDER BY id DESC;''').fetchall()
    cursor.close()
    return resultados


#Retorna livros que o autor contenha a entrada do usuário
def retorna_autor_selecionado(entrada):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    resultados = cursor.execute(f'''SELECT * FROM livros WHERE autor LIKE "%{entrada}%" ORDER BY id DESC;''').fetchall()
    cursor.close()
    return resultados


#Retorna livros que sejam do gênero de entrada do usuário
def retorna_genero_selecionado(entrada):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    resultados = cursor.execute(f'''SELECT * FROM livros WHERE genero = "{entrada}" ORDER BY id DESC;''').fetchall()
    cursor.close()
    return resultados


#Retorna livros que contenham a nota de entrada do usuário
def retorna_nota_selecionado(entrada):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    resultados = cursor.execute(f'''SELECT * FROM livros WHERE nota = {entrada} ORDER BY id DESC;''').fetchall()
    cursor.close()
    return resultados


#Retorna livros que tenham sido publicados no ano da entrada do usuário
def retorna_publicacao_selecionado(entrada):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    resultados = cursor.execute(f'''SELECT * FROM livros WHERE ano_lanc = {entrada} ORDER BY id DESC;''').fetchall()
    cursor.close()
    return resultados


#Retorna os livros que tenham sido finalizados entre as datas informadas pelo usuário
def retorna_finalizado_selecionado(entrada1, entrada2):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    resultados = cursor.execute(f'''SELECT * FROM livros WHERE data_finalizado BETWEEN "{entrada1}" AND "{entrada2}" ORDER BY id DESC;''').fetchall()
    cursor.close()
    return resultados


#Operações na tabela generos
#Inserir um gênero
def inserir_genero(genero):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO generos VALUES ("{genero}");''')
    connection.commit()
    cursor.close()


#Retornar todos os generos
def busca_todos_generos():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    todos_generos = cursor.execute(f'''SELECT * FROM generos ORDER BY genero;''').fetchall()
    cursor.close()
    return todos_generos


#Checa se o genero importado no arquivo é novo. Se for, será inserido na tabela generos
def checa_genero(genero):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    checa_generos = cursor.execute(f'''SELECT genero FROM generos WHERE genero = "{genero}"; ''').fetchall()
    if not checa_generos:
        inserir_genero(genero)


#Ações na tabela proximas_leituras
#Adicionar um título
def insere_proxima_leitura(titulo):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO proximas_leituras VALUES ("{titulo}");''')
    connection.commit()
    cursor.close()


#Retorna todas as próximas leituras
def busca_proximas_leituras():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    proximas = cursor.execute(f'''SELECT * FROM proximas_leituras;''').fetchall()
    cursor.close()
    return proximas


def busca_proxima_leitura():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    if busca_proximas_leituras():
        proxima = cursor.execute(f'''SELECT * FROM proximas_leituras;''').fetchone()
        cursor.close()
        return proxima[0]
    return ''


def deleta_proxima_leitura(titulo):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute(f'''DELETE FROM proximas_leituras WHERE titulo = "{titulo}";''')
    connection.commit()
    cursor.close()


#Ações na tabela metas
#Inserir uma nova meta
def insere_meta(titulo, prazo):
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO metas VALUES("{titulo}","{prazo}");''')
    connection.commit()
    cursor.close()


#Retorna a meta estabelecida
def busca_meta():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    meta = cursor.execute('''SELECT * FROM metas;''').fetchone()
    cursor.close()
    return meta


#Deleta a meta
def deleta_meta():
    connection = sqlite3.connect('livros.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM metas;''')
    connection.commit()
    cursor.close()
