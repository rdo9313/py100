def is_empty_or_blank(string):
    return len(string) == 0 or string.isspace()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True