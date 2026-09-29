# This file contains basic library catalog functions.

def search_book(title, books):
    for book in books:
        if title.lower() in book.lower():
            print(book)

books = ["Python Basics", "Data Science", "Clean Code"]

search_book("python", books)