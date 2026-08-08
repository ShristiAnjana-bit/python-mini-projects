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

    elif choice == "3":
        title = input("Enter title to search:")

        book = library.search_book(title)

        if book is None:
            print("Book not found.")
        else:
            print("\nBook found:")
            print(f"Title: {book['title']}")
            print(f"author: {book['author']}")
            print(f"Edition: {book['edition']}")
            print(f"Publisher: {book['publisher']}")
            
            
            

    elif choice == "4":
        title = input("Enter title to remove: ")

        if library.remove_book(title):
            print("Book removed successfully.")
        else:
            print("Book not found.")

        
    elif choice == "5":
        title = input("Enter title to update: ")
        new_title = input("Enter the new title:")
        new_author = input("Enter the new author:")
        new_edition = input("Enter the new edition:")
        new_publisher = input("Enter the new publisher:")
        
        if library.update_book(title,new_title,new_author,new_edition,new_publisher):
            print("Book updated successfully.")
        else:
            print("Book not found")