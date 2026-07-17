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

    elif choice == "2":
        books = library.get_all_books()

        if books:
            for book in books:
                print(book)
        else:
            print("No books available.")

    elif choice == "3":
        book_name = input("Enter book name:")

        if library.search_book(book_name):
                print("Book Found")
        else:
            print("Book Not Found")

    elif choice == "4":
        book_name = input("Enter book name: ")

        if library.remove_book(book_name):
            print("Book removed successfully.")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using Library Managemant System!")
        break

    else:
        print("Invalid choice! Please try again.")