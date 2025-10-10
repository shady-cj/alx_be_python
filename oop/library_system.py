class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
#         Book: Pride and Prejudice by Jane Austen
# EBook: Snow Crash by Neal Stephenson, File Size: 500KB
# PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234

    def list_books(self):
        for book in self.books:
            print(f"{book.__class__.__name__}: {book.title} by {book.author}{', File Size: ' + str(book.file_size) + 'KB' if isinstance(book, EBook) else ', Page Count: ' + str(book.page_count) if isinstance(book, PrintBook) else ''}")
