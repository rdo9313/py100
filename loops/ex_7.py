def find_integers(tuple):
    result = []
    for el in tuple:
        if type(el) is int:
            result.append(el)
    return result


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
