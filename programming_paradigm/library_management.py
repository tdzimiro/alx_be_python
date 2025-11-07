class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []  # private list to store books

    def add_book(self, book):
        """Add a book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Find a book by title and return it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

