class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.my_books = []


class Library:
    def __init__(self):
        self.all_books = []
        self.all_patrons = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.all_books.append(new_book)
        print(f"Added book: {title}")

    def register_patron(self, name):
        new_patron = Patron(name)
        self.all_patrons.append(new_patron)
        print(f"Registered user: {name}")

    def borrow_book(self, patron_name, book_title):
        found_book = None
        for b in self.all_books:
            if b.title == book_title:
                found_book = b

        found_patron = None
        for p in self.all_patrons:
            if p.name == patron_name:
                found_patron = p

        if found_book == None:
            print("Book not found!")
        elif found_patron == None:
            print("User not found!")
        elif found_book.is_available == False:
            print("Book is already borrowed!")
        else:
            found_book.is_available = False
            found_patron.my_books.append(found_book)
            print(f"{patron_name} successfully borrowed {book_title}")

    def return_book(self, patron_name, book_title):
        found_patron = None
        for p in self.all_patrons:
            if p.name == patron_name:
                found_patron = p

        if found_patron == None:
            print("User not found!")
            return

        found_book = None
        for b in found_patron.my_books:
            if b.title == book_title:
                found_book = b

        if found_book == None:
            print(f"{patron_name} does not have this book!")
        else:
            found_book.is_available = True
            found_patron.my_books.remove(found_book)
            print(f"{patron_name} successfully returned {book_title}")


lib = Library()

lib.add_book("Harry Potter", "J.K. Rowling")
lib.register_patron("Sam")

lib.borrow_book("Sam", "Harry Potter")

lib.return_book("Sam", "Harry Potter")