"""
Concerned with storing and retrieving books from a csv file

Format of the csv file:
name,author,read
"""

books_file = 'books.txt'


def create_book_table():  # create_book_table() is a method to instantiate the books.txt file if the file is not existing so there won't be any error if user lists books without the file
    with open(books_file, 'w'):
        pass


def add_book(book):
    with open(books_file, 'a') as file:  # 'a' mode - append mode for a file to add at the end
        file.write(f"{book['name']}, {book['author']}, 'False'\n")


def list_books():
    with open(books_file, 'r') as file:
        file_content = [book.strip().split(',') for book in file.readlines()]
    return [
        {'name': book[0], 'author': book[1], 'read': book[2]}
        for book in file_content
    ]


def mark_book(name):
    books = list_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)  # _ at the start represents that this function should be called in this file only (kind of private function)
    # else:
    #     print(f'book with name, {name}, not found')


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = list_books()
    books_updated = []
    for book in books:
        if book['name'] != name:
            books_updated.append(book)
    _save_all_books(books_updated)
    # else:
    #     print(f'book with name, {name}, not found')
