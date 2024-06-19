from new_book import new_book
from view_books import view_books
from main import libraries
import os
def library_menu():
   while True:
    os.system("cls")
    user_input = input("""
                       
1. Log a new book in
2. View list of books
3. quit
    
""")
    
    if user_input == "1":
        os.system("cls")
        new_book()
    elif user_input == "2":
        os.system("cls")
        view_books()
    elif user_input == "3":
       break
    else:
       os.system("cls")
       input("You've not entered a valid option. Press 'enter' and try again\n ")
