"""
Concerned with storing and retrieving books from a sqlite database
"""

from database_connection import DatabaseConnection


def create_book_table():  # create_book_table() is a method to instantiate the books.txt file if the file is not existing so there won't be any error if user lists books without the file
    # connection = sqlite3.connect('data.db')  # create a connection
    # cursor = connection.cursor()  # crate a cursor to move through the data
    # cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')  # write the query - create a table
    # connection.commit()  # commit the changes
    # connection.close()  # close the connection
    with DatabaseConnection('data.db') as connection:  # create a connection
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')  # write the query - create a table


def add_book(book):
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (book["name"], book["author"]))  # insert values into table
    # connection.commit()
    # connection.close()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (book["name"], book["author"]))  # insert values into table


def list_books():
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM books')  # select data from table - no need of commit because we are just selecting the data
    # # books = cursor.fetchall()  # this will give list of tuples - like [(name, author, read), (name, author, read)]
    # books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # converting all tuples into dictionaries
    # connection.close()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')  # select data from table - no need of commit because we are just selecting the data
        # books = cursor.fetchall()  # this will give list of tuples - like [(name, author, read), (name, author, read)]
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # converting all tuples into dictionaries
    return books


def mark_book(name):
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))  # update dat in table
    # connection.commit()
    # connection.close()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))  # update dat in table


def delete_book(name):
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('DELETE FROM books WHERE name = ?', (name,))
    # connection.commit()
    # connection.close()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))
