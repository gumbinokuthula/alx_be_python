# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title              # public attribute
        self.author = author            # public attribute
        self._is_checked_out = False    # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned/available."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to hold all Book objects

    def add_book(self, book):
        """Add a Book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Find a book by title and check it out if available.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Find a book by title and return it (make it available).
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out or not found.")

    def list_available_books(self):
        """
        Print all books that are currently available.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
