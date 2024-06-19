from main import itineraries
def view_itineraries():
    for itinerary in itineraries:
        itinerary_num, traveler_name, origin, destination = itinerary
        print(f"{itinerary_num}: {traveler_name} - From {origin} to {destination}")
    input("To go back press 'enter'\n ")