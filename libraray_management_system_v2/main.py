from library import Library

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2.View Books")
    print("3.Search Book")
    print("4.Remove Book")
    print("5.Update Book")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title:")
        author = input("Enter author:")
        edition = input("Enter edition:")
        publisher = input("Enter publisher:")

        if library.add_book(title,author,edition,publisher):
            print("Book added successfully.")
        else:
             print("Please fill in all the fields.")

    elif choice == "2":
        books = library.get_all_books()

        if not books:
            print("No books available.")
        else:
            print("\n==== All Books =====.")

            for book in books:
                print(f"Title: {book['title']}")
                print(f"Author:{book['author']}")
                print(f"Edition: {book['edition']}")
                print(f"Publisher:{book['publisher']}")
                print("-"*30)

    elif choice == "4":
        title = input("Enter title to remove: ")

        if library.remove_book(title):
            print("Book removed successfully.")
        else:
            print("Book not found.")
