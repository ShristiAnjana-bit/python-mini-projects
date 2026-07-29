class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, book_name):
        if not book_name.strip():
            return False

            #next validation
        if self.search_book(book_name):
            return False
            
        self.books.append(book_name)
        self.save_books()
        return True

    # def display_books(self):
    #     for book_name in self.books:
    #        print(book_name)

    def get_all_books(self):
        self.books.sort()
        return self.books

    def total_books(self):
        return len(self.books)
    

    def search_book(self, book_name):
        for book in self.books:
            if book.lower() == book_name.lower():
                return True

        return False
        
    
    def remove_book(self,book_name):
        for book in self.books:
            if book.lower() == book_name.lower():
               self.books.remove(book)
               self.save_books()
               return True

        return False

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                lines = file.readlines()

                for line in lines:
                    clean_line = line.strip()
                    self.books.append(clean_line)
                    #what if book.txt doesn't exist then we will
                    #use exception handling(try/except)
        
        except FileNotFoundError:
            pass

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(book + "\n")

                
                
    


