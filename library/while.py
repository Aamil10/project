from library_content import book_add
from library_content import displaybook
from library_content import update_price
from library_content import exit

while True:
    print("1. Create library")
    print("2. Display library")
    print("3. Update price")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_add.create()

    if choice == 2:
        displaybook.displaybook()

    if choice == 3:
        update_price.update_price()

    if choice == 4:
        exit.exit()
