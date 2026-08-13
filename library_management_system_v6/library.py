import sqlite3


class Library:
    def __init__(self):
        
        self.conn = sqlite3.connect("books.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            edition TEXT,
            publisher TEXT
        )
        """)

        self.conn.commit()
       
        
    
            

    
    def add_book(self,title,author,edition,publisher):
        #validation
        for value in (title,author,edition,publisher):
            if not value.strip():
                return "empty"

        self.cursor.execute("""
            SELECT * FROM books
            WHERE title = ? AND author = ?
        """,(title,author))

        existing_book = self.cursor.fetchone()

        if existing_book:
            return "duplicate"
       

        

        self.cursor.execute("""
            INSERT INTO books (title, author, edition, publisher)
            VALUES(?, ?, ?, ?)
            """,(title,author,edition,publisher))

        self.conn.commit()
        
        #success
        return True

    def search_book(self,title):
        self.cursor.execute("""
            SELECT * FROM books
            WHERE title = ?
        """,(title,))

        book = self.cursor.fetchone()
        return book
       

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        return books

    def remove_book(self,title):
        self.cursor.execute("""
            DELETE FROM books
            WHERE title = ?
        """,(title,))
        
        self.conn.commit()

        if self.cursor.rowcount > 0:
            return True
        else:
            return False
        

    def update_book(self,title,new_title,new_author,new_edition,new_publisher):
       
        self.cursor.execute("""
            UPDATE books
            SET title = ?, author = ?, edition = ?, publisher = ?
            WHERE title = ?
        """,(new_title,new_author,new_edition,new_publisher,title))

        self.conn.commit()

        if self.cursor.rowcount > 0:
            return True
        else:
            return False
