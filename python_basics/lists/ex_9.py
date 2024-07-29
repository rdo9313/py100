destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, list):
    return len([destination for destination in destinations if destination == city]) > 0


contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

