

import random
import string

class Users:
    def __init__(self, name):
        self.name = name
        self.unique_id = self.generate_user_id()  # Generates ID
        self.user_books_borrowed = {}             # {book_title: due_date}
        self.user_book_reserved = {}              # {book_title: reservation_date}

    def generate_user_id(self):
        num_id = random.randint(10, 999)
        abc_id = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        return f"{abc_id}{num_id}"






class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__unique_id = self.generate_book_id()
        self.status = "available"  # can be 'available', 'borrowed', 'reserved'

    def generate_book_id(self):
        num_id = random.randint(10, 1500)
        abc_id = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        return f"{self.title}{abc_id}{num_id}"

    def marked_as_borrowed(self, new_status):
        if new_status in ["borrowed"]:
            return self.status = new_status

    def marked_as_available(self, new_status):
      if new_status in ["available"]:
        self.status = self_status

    def marked_as_reserved(self, new_status):
      if new_status in ["reserved"]:
         self.status = new_status

    def book_info(self, info)












