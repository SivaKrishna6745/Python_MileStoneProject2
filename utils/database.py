"""
Concerned with storing and retrieving books from a list
"""

books = []


def add_book(book):
    books.append(book)


def list_books():
    for book in books:
        print(book)


def mark_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            print(book)
            return
    else:
        print(f'book with name, {name}, not found')


def delete_book(name):
    for book in books:
        if book['name'] == name:
            print(book)
            books.remove(book)
            return
    else:
        print(f'book with name, {name}, not found')

