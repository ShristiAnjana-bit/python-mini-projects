from library import Library

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1.Add Book")
    print("2.View Books")
    print("3.Search Book")
    print("4.Remove Book")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_name = input("Enter book name: ")
        library.add_book(book_name)
        print(f"'{book_name}' added successfully!")

    if choice == "2":
        books = library.get_all_books()

        if books:
            for book in books:
                print(book)
        else:
            print("No books available.")

    