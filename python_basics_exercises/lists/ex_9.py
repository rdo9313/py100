destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, cities):
    for element in cities:
        if element == city:
            return True
        
    return False

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False
