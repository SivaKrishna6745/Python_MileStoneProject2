from utils import database_sqlite

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your Choice: """


# def prompt_add_book() - ask for book name and author and add it to the list of books
def prompt_add_book():
    book = input("Enter book name, author separated by commas: ")
    name = book.split(',')[0]
    author = book.split(',')[1]
    database_sqlite.add_book({
        'name': name,
        'author': author,
        'read': False
    })


# def list_all_books() - show all the books in the list
def list_all_books():
    books = database_sqlite.list_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


# def mark_book_read() - ask for book name and mark it as read in the list
def mark_book_read():
    book = input("Enter book name that you wanted to mark as read: ")
    return database_sqlite.mark_book(book)


# def delete_a_book() - ask for book name and delete the book from the list
def delete_a_book():
    book = input("Enter book name that you wanted to delete from list: ")
    return database_sqlite.delete_book(book)


operations = {
    'a': prompt_add_book,
    'l': list_all_books,
    'r': mark_book_read,
    'd': delete_a_book
}


def menu():
    database_sqlite.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        operations[user_input]()
        user_input = input(USER_CHOICE)


menu()
