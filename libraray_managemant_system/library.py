class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book_name):
        self.books.append(book_name)

    def display_books(self):
        for book_name in self.books:
           print(book_name)