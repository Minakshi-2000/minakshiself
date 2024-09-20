# Class to represent a Book
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_issued = False

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Issued: {self.is_issued}"

# Class to represent a User
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.issued_books = []

    def issue_book(self, book):
        if not book.is_issued:
            self.issued_books.append(book)
            book.is_issued = True
            print(f"{self.name} has issued the book: {book.title}")
        else:
            print(f"The book '{book.title}' is already issued.")

    def return_book(self, book):
        if book in self.issued_books:
            self.issued_books.remove(book)
            book.is_issued = False
            print(f"{self.name} has returned the book: {book.title}")
        else:
            print(f"{self.name} does not have the book '{book.title}' issued.")

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Issued Books: {[book.title for book in self.issued_books]}"

# Class to represent the Library
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    # Add book to library
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    # Register user
    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' has been registered.")

    # Display available books
    def display_books(self):
        print(f"\nBooks available in {self.name}:")
        for book in self.books:
            print(book)

    # Find book by title or id
    def find_book(self, book_id=None, title=None):
        for book in self.books:
            if book_id and book.book_id == book_id:
                return book
            elif title and book.title.lower() == title.lower():
                return book
        return None

# Main program to test the system
def main():
    # Create a library
    my_library = Library("City Library")

    # Add books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1)
    book2 = Book("1984", "George Orwell", 2)
    book3 = Book("To Kill a Mockingbird", "Harper Lee", 3)

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Register users
    user1 = User(101, "Minakshi Kumari")
    user2 = User(102, "Amit Sharma")

    my_library.register_user(user1)
    my_library.register_user(user2)

    # Issue books
    user1.issue_book(book1)  # Minakshi issues 'The Great Gatsby'
    user2.issue_book(book1)  # Attempt to issue 'The Great Gatsby' again by Amit
    user2.issue_book(book2)  # Amit issues '1984'

    # Display all books in library
    my_library.display_books()

    # Return books
    user1.return_book(book1)  # Minakshi returns 'The Great Gatsby'
    user2.issue_book(book1)   # Amit issues 'The Great Gatsby'

    # Display all books in library again
    my_library.display_books()

if __name__ == "__main__":
    main()
