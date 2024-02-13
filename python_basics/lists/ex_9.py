destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(destination, lst):
    for location in lst:
        if location == destination:
            return True
    return False

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False