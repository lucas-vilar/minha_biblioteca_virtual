# Minha biblioteca virtual (My virtual bookshelf)

Desktop (and portuguese) version of "My virtual bookshelf".

Just like My virtual bookshelf, "Minha biblioteca virtual" is a Book collection management system software, where users can manage their collection, create reading goals, and organize their future readings.

This was my first Python project after doing Codecademy Python courses. I had the chance to put my knowledge into practice, and also learn how to use PyQt5 to create GUI applications and work with SQLite3 in Python.  

To start the application, run the app.py

## Inserting a new book 📖
 There are two ways to insert new books in Minha biblioteca virtual:
 - Manually insert
 - Import books from .cvs files

### Manually inserting books:
To insert books manually, in the main window select "Adicionar Livro" > "Adicionar Livro Manualmente"

In this screen, manually insert book's information (e.g., Title, and Author). To create new genres, click in "Adicionar genero" button. In the next screen, write the genre's name and click "Adicionar genero". To save the new book click in "Adicionar livro". Choose "Limpar campos" button to clear all fields.

### Importing books from a .csv file:
To import books from a .csv file, select "Adicionar Livro" > "Adicionar a partir de um arquivo"

To load books from a file click "Escolher arquivo". To save the books click "Importar livros"

See the example_file.cvs to better understand how to organize book's information in the .csv file.

## Updating a book 🔄
To update a book in your collection, double click the book in main window. In this new window, click "Editar Livro" to allow you to make changes in the Line edits. To update the book, click "Salvar alterações".


## Deleting a book ❌
Just like to update a book, to perform a delete action, double the book in the main window. In the next window click "Deletar livro" and "Yes". This action can't be undone.

## Filtering through the collection 🔎
There are several ways to filter your collection in "Minha biblioteca virtual". You can filter By:
- Title
- Author
- Genre
- Publication year
- Grade
- Finish date

#### Filtering by title:
In the main window click "Busca avançada" > "Buscar Livros".

Select "Título" radio button, write the book's title in the enabled Line edit, and click "Buscar".

#### Filtering by Author
In the main window click "Busca avançada" > "Buscar Livros".

Select "Autor" radio button, write the author's name in the enabled Line edit, and click "Buscar".

#### Filtering by Genre
In the main window click "Busca avançada" > "Buscar Livros".

Select "Gênero" radio button, select the genre, and click "Buscar".

#### Filtering by Publication year
In the main window click "Busca avançada" > "Buscar Livros".

Select "Ano de publicação" radio button, write the book's publication year in the enabled Line edit, and click "Buscar".

#### Filtering by grade
In the main window click "Busca avançada" > "Buscar Livros".

Select "Nota" radio button, select the grade, and click "Buscar".

#### Filtering by finish date
In the main window click "Busca avançada" > "Buscar Livros".

Select "Data de finalização" radio button.

Return all read books between the given time period.


## Creating new goals ✅
To create new goals, in the main window click "Nova Meta".
Write your goal and choose a deadline. To confirm click "Adicionar meta".

**OBS:** You can only have one active goal. If you create a second goal, the first one will be deleted.

If your goal is accomplished you can click "Meta cumprida" to receive congratulations!

To discard a goal click "Descartar meta meta"


## Creating future readings 🔜
To create future readings click "Próximas leituras" >  "Inserir título". To add a new title to the queue click "Adicionar título". To remove a title click "Remover título"

The next title will be shown in the main window.

If you finish the book, click "Finalizado" to remove it from the queue and manually insert into the collection.


