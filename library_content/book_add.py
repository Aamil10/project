library=[]
def create():
    book_id=int(input("Enter book id: "))
    name=input("enter the name of the book: ")
    author=input("Enter the name of the author: ")
    price=int(input("Enter the price of the book: "))
    publisher=input("Enter the name of the publisher: ")

    book_details = {
    "id": book_id,
    "name":name,
    "author":author,
    "price": price,
    "publisher": publisher
        }
    library.append(book_details)
    print("Book added successfully!")

