class LibraryItem:
    """Base class demonstrating Abstraction and Encapsulation."""

    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self._is_borrowed = False  

    def borrow(self):
        if self._is_borrowed:
            return False
        self._is_borrowed = True
        return True

    def return_item(self):
        if not self._is_borrowed:
            return False
        self._is_borrowed = False
        return True

    def get_details(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"[{self.__class__.__name__}] ID: {self.item_id} | Title: '{self.title}' | Author: {self.author} | Status: {status}"


class Book(LibraryItem):
    """Subclass inheriting from LibraryItem."""

    def __init__(self, item_id, title, author, genre):
        super().__init__(item_id, title, author)
        self.genre = genre

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Genre: {self.genre}"


class Patron:
    """Class representing library users."""

    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        if item.borrow():
            self.borrowed_items.append(item)
            return True
        return False

    def return_item(self, item):
        if item in self.borrowed_items and item.return_item():
            self.borrowed_items.remove(item)
            return True
        return False

    def get_details(self):
        titles = [item.title for item in self.borrowed_items]
        borrowed_str = ", ".join(titles) if titles else "None"
        return f"Patron ID: {self.patron_id} | Name: {self.name} | Borrowed Items: {borrowed_str}"


class Library:
    """Manager class coordinating items and patrons."""

    def __init__(self, name):
        self.name = name
        self.items = {}
        self.patrons = {}

    def add_item(self, item):
        self.items[item.item_id] = item
        print(f"Added: '{item.title}'")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Registered Patron: {patron.name}")

    def borrow_book(self, patron_id, item_id):
        if patron_id not in self.patrons:
            print("Error: Patron not found.")
            return
        if item_id not in self.items:
            print("Error: Item not found.")
            return

        patron = self.patrons[patron_id]
        item = self.items[item_id]

        if patron.borrow_item(item):
            print(f"Success: {patron.name} borrowed '{item.title}'")
        else:
            print(f"Error: '{item.title}' is already borrowed.")

    def return_book(self, patron_id, item_id):
        if patron_id not in self.patrons or item_id not in self.items:
            print("Error: Invalid Patron ID or Item ID.")
            return

        patron = self.patrons[patron_id]
        item = self.items[item_id]

        if patron.return_item(item):
            print(f"Success: {patron.name} returned '{item.title}'")
        else:
            print(f"Error: {patron.name} does not have '{item.title}' borrowed.")

    def display_all_items(self):
        print(f"\n--- {self.name} Inventory ---")
        if not self.items:
            print("No items in library.")
        for item in self.items.values():
            print(item.get_details())

    def display_all_patrons(self):
        print(f"\n--- {self.name} Registered Patrons ---")
        if not self.patrons:
            print("No registered patrons.")
        for patron in self.patrons.values():
            print(patron.get_details())
if __name__ == "__main__":
    city_library = Library("Central Library")

    print("--- Adding Books ---")
    book1 = Book("B101", "Clean Code", "Robert C. Martin", "Software Engineering")
    book2 = Book("B102", "Design Patterns", "Erich Gamma", "Software Engineering")
    city_library.add_item(book1)
    city_library.add_item(book2)

    print("\n--- Registering Patrons ---")
    patron1 = Patron("P001", "Alice")
    patron2 = Patron("P002", "Bob")
    city_library.register_patron(patron1)
    city_library.register_patron(patron2)

    print("\n--- Borrowing Books ---")
    city_library.borrow_book("P001", "B101")
    city_library.borrow_book("P002", "B101")  

    city_library.display_all_items()
    city_library.display_all_patrons()

    print("\n--- Returning Books ---")
    city_library.return_book("P001", "B101")

    city_library.display_all_items()