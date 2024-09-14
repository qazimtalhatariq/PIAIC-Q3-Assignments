from typing import List, Optional
import os
import json

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
class Librarian(User):
    def manage_books(self, library_manager):
        pass  # Functions to add, update, and delete books will go here

class Member(User):
    def borrow_book(self, book_id: int, library_manager):
        pass  # Function to borrow a book

    def return_book(self, book_id: int, library_manager):
        pass  # Function to return a book
class Book:
    def __init__(self, book_id: int, title: str, author: str, available: bool = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        availability = 'Available' if self.available else 'Not Available'
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {availability}"
     
class LibraryManager:
    def __init__(self):
        self.books = []
        self.users = []
        self.books_file = "books.txt"
        self.users_file = "users.txt"
        self.load_data()
    
    def load_data(self):
        # Load books data
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as f:
                book_data = json.load(f)
                for book in book_data:
                    self.books.append(Book(**book))
        else:
            print("Books file not found.")
        
        # Load users data
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                user_data = json.load(f)
                for user in user_data:
                    if user['role'] == 'Librarian':
                        self.users.append(Librarian(**user))
                    else:
                        self.users.append(Member(**user))
        else:
            print("Users file not found.")
    
    def save_data(self):
        # Save books data
        with open(self.books_file, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)
        
        # Save users data
        with open(self.users_file, 'w') as f:
            json.dump([user.__dict__ for user in self.users], f)

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_data()
    
    def update_book(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None):
        for book in self.books:
            if book.book_id == book_id:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_data()
                break
    
    def delete_book(self, book_id: int):
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_data()
    
    def borrow_book(self, book_id: int, user: Member):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                print(f"{user.name} borrowed {book.title}.")
                self.save_data()
                break
        else:
            print("Book is not available.")
    
    def return_book(self, book_id: int, user: Member):
        for book in self.books:
            if book.book_id == book_id and not book.available:
                book.available = True
                print(f"{user.name} returned {book.title}.")
                self.save_data()
                break

    def list_books(self):
        for book in self.books:
            print(book.display_info())


# Initialize the library system
library_manager = LibraryManager()

# Add a librarian and a member
librarian = Librarian(user_id=1, name="John", email="john@library.com")
member = Member(user_id=2, name="Alice", email="alice@library.com")

# Register users
library_manager.users.append(librarian)
library_manager.users.append(member)
library_manager.save_data()

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
