from library_content.book_add import library


def displaybook():
    if not library:
        print("BOOk DOESN'T EXIST")
    else:
        print("BOOK EXISTS")
        for book in library:
            print(list(book.values()))