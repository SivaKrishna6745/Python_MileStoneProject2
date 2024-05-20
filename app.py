from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your Choice: """


# def add_book() - ask for book name and author and add it to the list of books
def add_book():
    book = input("Enter book name, author separated by commas: ")
    name = book.split(',')[0]
    author = book.split(',')[1]
    database.add_book({
        'name': name,
        'author': author,
        'read': False
    })


# def list_books() - show all the books in the list
def list_books():
    return database.list_books()


# def mark_book() - ask for book name and mark it as read in the list
def mark_book():
    book = input("Enter book name that you wanted to mark as read: ")
    return database.mark_book(book)


# def delete_book() - ask for book name and delete the book from the list
def delete_book():
    book = input("Enter book name that you wanted to delete from list: ")
    return database.delete_book(book)


operations = {
    'a': add_book,
    'l': list_books,
    'r': mark_book,
    'd': delete_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        operations[user_input]()
        user_input = input(USER_CHOICE)


menu()
