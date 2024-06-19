from new_itinerary import add_itinerary
from itineraries_list import view_itineraries
from main import itineraries
import os
def main_menu():
   while True:
    os.system("cls")
    user_input = input("""
                       
1. Add a new itinerary
2. View list of itineraries
3. quit
    
""")
    
    if user_input == "1":
        os.system("cls")
        add_itinerary()
    elif user_input == "2":
        os.system("cls")
        view_itineraries()
    elif user_input == "3":
       break
    else:
       os.system("cls")
       input("You've not entered a valid option. Press 'enter' and try again\n ")
