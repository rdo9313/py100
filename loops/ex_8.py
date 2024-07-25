my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

print({f'{string}': len(string) for string in my_set if len(string) % 2 == 1})