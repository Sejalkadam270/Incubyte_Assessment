def test_borrow_book():
    library = Library()
    book = Book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    assert library.borrow_book("978-3-16-148410-0") == True
    assert book.is_available == False

def test_borrow_unavailable_book():
    library = Library()
    book = Book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.add_book(book)
    library.borrow_book("978-3-16-148410-0")
    with pytest.raises(Exception):
        library.borrow_book("978-3-16-148410-0")
