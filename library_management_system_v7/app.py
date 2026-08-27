from dotenv import load_dotenv
import os
from flask import Flask, render_template,request,redirect,flash,session
from library import Library
from werkzeug.security import generate_password_hash,check_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/register" , methods=["GET","POST"]) 
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        password_hash = generate_password_hash(password)

        library = Library()
        result = library.register_user(username,password_hash)
        if result == "duplicate":
            flash("Username already exists")
            return redirect("/register")

        flash("Registration successful")
        return redirect("/register")
    return render_template("register.html")
 

@app.route("/")
def home():
    print("SESSION:", session)
    if "user_id" not in session:
        return redirect("/login")

    library = Library()
    books = library.get_all_books()
    return render_template("books.html", books=books, heading="All Books")

@app.route("/search_book")
def search_book():
    library = Library()
    
    query = request.args.get("title")
    result = library.search_book(query)
    return render_template("books.html",books=result, heading="Search Results")

@app.route("/add_book",methods=["POST"])
def add_book():
    if "user_id" not in session:
        return redirect("/login")
    library = Library()

    title = request.form.get("title")
    author = request.form.get("author")
    edition = request.form.get("edition")
    publisher = request.form.get("publisher")
    result = library.add_book(title,author,edition,publisher)
    if result == "duplicate":
        flash("Book already exists")
        return redirect("/")
    elif result == "empty":
        flash("All fields are required")
        return redirect("/")
    else:
        return redirect("/")

@app.route("/edit_book/<id>", methods=["GET" , "POST"])
def edit_book(id):
    if "user_id" not in session:
        return redirect("/login")

    library = Library()
    book = library.get_book_by_id(id)
    if request.method == "POST":
        
        title = request.form.get("title")
        author = request.form.get("author")
        edition = request.form.get("edition")
        publisher = request.form.get("publisher")
        
        result = library.update_book(
            book["title"],
            title,
            author,
            edition,
            publisher
        )
        if result:
            flash("Book updated successfully")
            return redirect("/")
        else:
            flash("Book could not be updated")
            return redirect("/")

    return render_template("edit_book.html",book=book)
    
@app.route("/delete_book/<id>", methods=["POST"])
def delete_book(id):
    if "user_id" not in session:
        return redirect("/login")
        
    library = Library()
    result = library.delete_book(id)

    if result:
        flash("Book deleted successfully")
        return redirect("/")

    else:
        flash("Book could not be deleted")
        return redirect("/")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        
        password = request.form.get("password")

        library = Library()
        user = library.get_user_by_username(username)
        
        
        if user is None:
            flash("Invalid username or password")
            return redirect("/login")
        
        if check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            
            return redirect("/")
        else:
            flash("Invalid username or password")
            return redirect("/login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect("/login")




if __name__ == "__main__":
    app.run(debug=True)