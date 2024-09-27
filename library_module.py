# library_module.py

class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return book
        raise Exception("Book is unavailable")

    # def return_book(self, isbn):
    #     for book in self.books:
    #         if book.isbn == isbn and book.is_borrowed:
    #             book.is_borrowed = False
    #             return
    #     raise Exception("Book was not borrowed")

    # def get_available_books(self):
    #     return [book for book in self.books if not book.is_borrowed]
