from main import libraries
def view_books():
    for books in libraries:
        text = f"{books[0]} by {books[1]}"
        print(text) 
    input("Press 'enter' to go back\n ")