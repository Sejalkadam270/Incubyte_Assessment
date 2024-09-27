import pytest
from library_module import Library, Book

def test_borrow_book():
    library = Library()
    book = Book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("978-3-16-148410-0")
    assert book.is_borrowed is True

def test_borrow_unavailable_book():
    library = Library()
    book = Book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("978-3-16-148410-0")
    with pytest.raises(Exception):
        library.borrow_book("978-3-16-148410-0")
