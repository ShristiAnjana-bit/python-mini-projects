from library import Library

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1.Add Book")
    print("2.View Books")
    print("3.Search Book")
    print("4.Remove Book")
    print("5.Update Book")
    print("6.Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        book_name = input("Enter book name: ")

        if library.add_book(book_name):
           print(f"'{book_name}' added successfully!")
        else:
           print("Book already exists.")
            
    elif choice == "2":
        books = library.get_all_books()
        if books:
           print("Total Books:" , library.total_books())

           for index, book in enumerate(books,start=1):
               print(f"{index}.{book}")

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
        old_book = input("Enter the old book name: ")
        new_book = input("Enter the new book name: ")

        if library.update_book(old_book,new_book):
            print("Book updated successfully.")
        else:
            print("Book update failed.")



    elif choice == "6":
        print("Thank you for using Library Managemant System!")
        break

    else:
        print("Invalid choice! Please try again.")