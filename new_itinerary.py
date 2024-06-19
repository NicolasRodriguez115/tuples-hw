from main import itineraries
def add_itinerary():
    index = len(itineraries)
    itinerary_num = f"Itinerary {index + 1}"
    traveler_name = input("What's the name of the person traveling?\n").capitalize()
    origin = input("Where are they leaving from?\n").capitalize()
    destination = input("What's their final destination?\n").capitalize()
    itineraries.append((itinerary_num, traveler_name, origin, destination))