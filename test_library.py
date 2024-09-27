import pytest
from library import Library, Book

def test_add_book():
    library = Library()
    book = Book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    assert len(library.get_available_books()) == 1
    assert library.get_available_books()[0].title == "The Great Gatsby"
