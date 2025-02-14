class Book:
    def __init__(self, title, author, year_public, isbn):
        self.title = title
        self.author = author
        self.year_public = year_public
        self.isbn = isbn
        self.num_copy = 0
        print(f"\nBook {title} created\n")
        
    def get_title(self):
        return f"{self.title}"
    
    def get_author(self):
        return f"{self.author}"
    
    def get_year(self):
        return f"{self.year_public}"

    def get_isbn(self):
        return f"{self.isbn}"
    
    def display_info(self):
        return f"{self.title} by {self.author}. First publication {self.year_public}. ISBN is {self.isbn}"
    
    def add_user(self, user):
        if self.isbn not in user.borrow_book:
            self.num_copy += 1 
            print(f"\n{user.name} ({user.user_id}) took {self.title} ({self.isbn})\n")
            return True
        print(f"\n{user.name} ({user.user_id}) has taken {self.title} ({self.isbn}) already\n")
        return False
    
    def remove_user(self, user):
        if self.isbn in user.borrow_book:
            self.num_copy -= 1 
            print(f"\n{user.name} ({user.user_id}) returned {self.title} ({self.isbn})\n")
            return True
        print(f"\n{user.name} ({user.user_id}) hasn't taken {self.title} ({self.isbn})\n")
        return False 
    

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrow_book = set()
        print(f"\nUser {self.name} registered\n")
        
    def take_book(self, book):
        if book.add_user(self):
            self.borrow_book.add(book.isbn)
            return True
        return False

    def back_book(self, book):
        if book.remove_user(self):
            self.borrow_book.remove(book.isbn)
            return True
        return False
    
    def books_info(self, library):
        return [book.display_info() for book in library.list_books if book.isbn in self.borrow_book]
    
class Library:
    def __init__(self):
        self.list_books = set()
        self.list_users = set()
        self.transaction_history = []
        print("\nlibrary was created\n")
        
    def register_book(self, book):
        if book in self.list_books:
            print(f"\nERROR! Book {book.title} has added in library already\n")
            return False
        if book.num_copy != 0:
            self.list_books.add(book)
            self.transaction_history.append(f"\nBook {book.title} ({book.isbn}) added in library\n")
            print(f"\nBook {book.title} added in library\n")
            return True 
        print(f"\nERROR! Book {book.title} didn't add in library\n")
        return False
    
    def drop_book(self, book):
        if book not in self.list_books:
            print(f"\nERROR! Book {book.title} hasn't been registered\n")
            return False
        if book.num_copy == 0:
            self.list_books.remove(book)
            self.transaction_history.append(f"Book {book.title} ({book.isbn}) droped from library")
            print(f"\nBook {book.title} droped from library\n")
            return True
        print(f"\nERROR! Book {book.title} didn't drop from library\n")
        return False
    
    def register_user(self, user):
        if user.user_id in self.list_users:
            print(f"\nERROR! User {user.name} has added in library\n")
            return False
        self.list_users.add(user.user_id)
        self.transaction_history.append(f"User {user.name} ({user.user_id}) added in library")
        print(f"\nUser {user.name} added in library\n")
        return True
    
    def drop_user(self, user):
        if len(user.borrow_book) != 0:
            print(f"\nERROR! User {user.name} must returns books\n")
            return False
        self.list_users.remove(user.user_id)
        self.transaction_history.append(f"User {user.name} ({user.user_id}) droped from library")
        print(f"\nUser {user.name} deleted from library\n")
        return True
    
    def display_history(self):
        for record in self.transaction_history:
            print(record)
            

library = Library()

book1 = Book("mathematical analysis", "Demidovich", 1955, "19-5-5")
library.register_book(book1) # Предполагается, что не будет добавлена, так как не была никому выдана

print(book1.get_title())
print(book1.get_author())
print(book1.get_year())
print(book1.get_isbn())
print(book1.display_info())

user1 = User("Dmitry", 1)
library.register_user(user1)

user1.take_book(book1)
library.drop_user(user1) # Предполагается, что не будет удален
library.register_book(book1) # Предполагается, что будет добавлена, так как была выдана
library.drop_book(book1) # Предполагается, что не будет удалена
print(user1.books_info(library))
user1.back_book(book1)
library.drop_book(book1) # Предполагается, что будет удалена
library.drop_user(user1) # Предполагается, что будет удален
library.display_history()


