import json

class Library:
    def __init__(self):
        self.books = []
        self.load_books()
        print("LOADED BOOKS:", self.books)

    def load_books(self):
        try:
            with open("books.json","r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            self.books = []
            

    def save_books(self):
        with open("books.json","w") as file:
            json.dump(self.books,file)

    def add_book(self,title,author,edition,publisher):
        #validation
        for value in (title,author,edition,publisher):
            if not value.strip():
                return "empty"

        #duplicate check
        for book in self.books:
            print("INPUT:", title,author)
            print("STORED: ", book["title"], book["author"])

            if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
                return "duplicate"

        #Create dictionary
        book = {
            "title": title,
            "author": author,
            "edition": edition,
            "publisher": publisher
        }

        #add book
        self.books.append(book)

        #Save to JSON
        self.save_books()

        #success
        return True

    def search_book(self,title):
        for book in self.books:
            if book["title"].lower() == title.lower():
               return book
        return None 

    def get_all_books(self):
        return self.books

    def remove_book(self,title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                return True

        return False

    def update_book(self,title,new_title,new_author,new_edition,new_publisher):
        book = self.search_book(title)
        if book is None:
            return False

        book["title"] = new_title
        book["author"] = new_author
        book["edition"] = new_edition
        book["publisher"] = new_publisher
        self.save_books()
        return True
