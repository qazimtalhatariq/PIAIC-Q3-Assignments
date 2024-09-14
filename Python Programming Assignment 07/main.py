from typing import List, Optional, Union
import os

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._user_id = user_id  # Using encapsulation by making attributes private
        self._name = name
        self._email = email

    def display_info(self) -> None:
        """Display the user's information."""
        print(f"User ID: {self._user_id}, Name: {self._name}, Email: {self._email}")

    @staticmethod
    def validate_email(email: str) -> bool:
        """Static method to validate an email."""
        return '@' in email and '.' in email  # Basic email validation

class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)  # Inherit from the User class

class Member(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self._borrowed_books: List[int] = []  # List to track borrowed book IDs

    def borrow_book(self, book_id: int) -> None:
        """Method for borrowing a book."""
        self._borrowed_books.append(book_id)

    def return_book(self, book_id: int) -> None:
        """Method for returning a book."""
        if book_id in self._borrowed_books:
            self._borrowed_books.remove(book_id)


class Book:
    def __init__(self, book_id: int, title: str, author: str, available: bool = True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = available

    def display_info(self) -> None:
        """Display book information."""
        availability = "Available" if self._available else "Unavailable"
        print(f"Book ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Status: {availability}")

    def borrow(self) -> bool:
        """Mark the book as borrowed."""
        if self._available:
            self._available = False
            return True
        return False

    def return_book(self) -> None:
        """Mark the book as available."""
        self._available = True


class LibraryManager:
    def __init__(self):
        self._books =[]
        self._users = []
        self._books_file = 'books.txt'
        self._users_file = 'users.txt'
        self._load_data()  # Load data from files when initializing

    def _load_data(self) -> None:
        """Load book and user data from files."""
        # Loading books
        if os.path.exists(self._books_file):
            with open(self._books_file, 'r') as f:
                for line in f:
                    book_data = line.strip().split(',')
                    self._books.append(Book(int(book_data[0]), book_data[1], book_data[2], book_data[3] == 'True'))

        # Loading users (for simplicity, only loading Member class, Librarians can be added separately)
        if os.path.exists(self._users_file):
            with open(self._users_file, 'r') as f:
                for line in f:
                    user_data = line.strip().split(',')
                    self._users.append(Member(int(user_data[0]), user_data[1], user_data[2]))

    def _save_data(self) -> None:
        """Save book and user data to files."""
        with open(self._books_file, 'w') as f:
            for book in self._books:
                f.write(f"{book._book_id},{book._title},{book._author},{book._available}\n")

        with open(self._users_file, 'w') as f:
            for user in self._users:
                if isinstance(user, Member):  # Saving only members for simplicity
                    f.write(f"{user._user_id},{user._name},{user._email}\n")

    def add_book(self, book: Book) -> None:
        """Add a new book to the system."""
        self._books.append(book)
        self._save_data()

def update_book(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None, available: Optional[bool] = None) -> None:
        """Update book information."""
        for book in self._books:
            if book._book_id == book_id:
                if title:
                    book._title = title
                if author:
                    book._author = author
                if available is not None:
                    book._available = available
                self._save_data()
                return
        print(f"Book with ID {book_id} not found.")

def delete_book(self, book_id: int) -> None:
        """Delete a book by its ID."""
        self._books = [book for book in self._books if book._book_id != book_id]
        self._save_data()

def borrow_book(self, user: Member, book_id: int) -> None:
        """Borrow a book for a member."""
        for book in self._books:
            if book._book_id == book_id and book.borrow():
                user.borrow_book(book_id)
                self._save_data()
                return
        print(f"Book with ID {book_id} is not available for borrowing.")

def return_book(self, user: Member, book_id: int) -> None:
        """Return a borrowed book."""
        for book in self._books:
            if book._book_id == book_id:
                book.return_book()
                user.return_book(book_id)
                self._save_data()
                return
        print(f"Book with ID {book_id} not found.")


# Initialize the library system
library_manager = LibraryManager()

# Add a librarian and a member
librarian = Librarian(user_id=1, name="John", email="john@library.com")
member = Member(user_id=2, name="Alice", email="alice@library.com")

# Register users
library_manager._users.append(librarian)
library_manager._users.append(member)
library_manager._save_data()

# Add books
library_manager.add_book(Book(book_id=1, title="The Great Gatsby", author="F. Scott Fitzgerald"))
library_manager.add_book(Book(book_id=2, title="1984", author="George Orwell"))

# Member borrows a book
member.borrow_book(book_id=1, library_manager=library_manager)

# List books to check availability
library_manager.list_books()

# Member returns the book
member.return_book(book_id=1, library_manager=library_manager)

# List books again
library_manager.list_books()
