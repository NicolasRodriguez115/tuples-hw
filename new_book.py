from main import libraries
def new_book():
    title = input("What's the name of the book?\n").title()
    author = input("Who's the author of the book?\n").title()
    if (title, author) in libraries:
        input("This book is already in your library! Press 'enter' to return to the main menu.\n ")
    else: 
        libraries.append((title, author))