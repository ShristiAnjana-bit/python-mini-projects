class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)

    # def display_books(self):
    #     for book_name in self.books:
    #        print(book_name)

    def get_all_books(self):
        return self.books

    def search_book(self, book_name):
        return book_name in self.books
    
    def remove_book(self,book_name):
        if self.search_book(book_name):
           self.books.remove(book_name)
           return True

        return False

