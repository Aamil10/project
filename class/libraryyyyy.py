l = []


class Library:
    def __init__(self):
        self.id = ""
        self.ID = ""
        self.Title = ""
        self.Author = ""
        self.Price = ""
        self.Publisher = ""

    def create(self):
        self.ID = int(input("Enter the ID: "))
        self.Title = input("Enter the tiltle of the book: ")
        self.Author = input("Enter the name of the author: ")
        self.Price = int(input("Enter the price of the book: "))
        self.Publisher = input("Enter the name of the publisher: ")

        book_details = {
            "id":self.ID,
            "title":self.Title,
            "author":self.Author,
            "price":self.Price,
            "publisher":self.Publisher
        }
        l.append(book_details)

    def display(self):
        if not l:
            print("Book doesn't exist")
        else:
            print("BOOK EXISTS")
            for book in l:
                print(list(book.values()))


    def update(self):
        bookid = int(input("Enter the id of the book: "))
        new_price = int(input("Enter the updated price: "))
        for book in l:
            if book['id'] == bookid:
                book['price'] = new_price
                print("price updated successfully")
                break

    def exit(self):
        print("!!PROGRAM FINISHED!!")
        break


c = Library()
while True:
    print("1.CREATE LIBRARY")
    print("2.DISPLAY")
    print("3.UPDATE PRICE")
    print("4.EXIT")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        c.create()

    if choice == 2:
        c.display()

    if choice == 3:
        c.update()




