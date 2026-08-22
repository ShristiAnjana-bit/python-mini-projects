from flask import Flask, render_template,request,redirect,flash
from library import Library



app = Flask(__name__)
app.secret_key ="your-secret-key"


@app.route("/")
def home():
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
    
@app.route("/delete_book/<id>")
def delete_book(id):
    library = Library()
    result = library.delete_book(id)

    if result:
        flash("Book deleted successfully")
        return redirect("/")

    else:
        flash("Book could not be deleted")
        return redirect("/")

    
    
if __name__ == "__main__":
    app.run(debug=True)