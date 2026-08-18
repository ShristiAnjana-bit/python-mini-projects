from flask import Flask, render_template
from library import Library
from flask import request


app = Flask(__name__)


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

if __name__ == "__main__":
    app.run(debug=True)