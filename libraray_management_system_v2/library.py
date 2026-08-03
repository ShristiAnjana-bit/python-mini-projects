import json

class Library:
    def __init__(self):
        self.books=[]
        self.load_books()

    def load_books(self):
        try:
            with open("books.json","r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            pass

    def save_books(self):
        with open("books.json","w") as file:
            json.dump(self.books,file)
