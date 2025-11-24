import random
import string
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.unique_id = self.generate_book_id()  # Generates a random book ID
        self.status = "available"  # Status of the book automatically set to available

    def generate_book_id(self):
        title3 = self.title[:3]  # First 3 characters of the book title
        num_id = random.randint(10, 1500) 
        abc_id = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        return f"{title3}{abc_id}{num_id}"  
        # Unique ID: first 3 characters of title + 2 random letters + random number

class User:
    def __init__(self, name):
        self.name = name
        self.unique_id = self.generate_user_id() 
        self.user_books_borrowed = {}  # {book_id: due_date}
        self.user_reserved_books = {}

    def generate_user_id(self):
        user3 = self.name[:3]  # First 3 characters of the user's name
        num_id = random.randint(10, 999)
        abc_id = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        return f"{user3}{abc_id}{num_id}"  
        # Unique ID: first 3 characters of name + 2 random letters + random number

    def borrow_book(self, book, days=14):
        """Borrow a book if available, set due date, and update records."""
        if book.status == "available":
            book.status = "borrowed"  
            due_date = datetime.now() + timedelta(days=days)
            self.user_books













