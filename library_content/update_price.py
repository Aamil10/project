from library_content.book_add import library


def update_price():
    if not library:
        print("BOOK DOESN'T EXIST")
    else:
        bookid = int(input("Enter id of the book you want to update: "))
        for book in library:
            if book['id'] == bookid:
                new_price = int(input("Enter the new price: "))
                book['price'] = new_price
                print("Price updated successfully")
                break
