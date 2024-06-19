from main import libraries
def new_book():
    title = input("What's the name of the book?\n").capitalize()
    author = input("Who's the author of the book?\n").capitalize()
    libraries.append((title, author))