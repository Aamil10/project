library = []

while True:
    print("1. Create library")
    print("2. Display library")
    print("3. Update price")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter the book ID: "))
        name = input("Enter the name of the book: ")
        author = input("Enter the name of the author: ")
        price = int(input("Enter the price of the book: "))
        publisher = input("Enter the name of the publisher: ")

        book_details = {
            "id": book_id,
            "name": name,
            "author": author,
            "price": price,
            "publisher": publisher
        }

        library.append(book_details)
        print("Book added successfully!")

    elif choice == 2:
        if not library:
            print("Library is empty.")
        else:
            print("Books in the library:")
            for book in library:
                print(list(book.values()))


    elif choice == 3:
        if not library:
            print("Library is empty.")
        else:
            book_id = int(input("Enter the ID of the book you want to update: "))
            for book in library:
                if book['id'] == book_id:
                    new_price = int(input("Enter the new price: "))
                    book['price'] = new_price
                    print("Price updated successfully!")
                    break
            else:
                print("Book not found in the library.")

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
