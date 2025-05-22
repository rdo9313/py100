my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

dict = {string: len(string) for string in my_set if len(string) % 2 == 1}
print(dict)