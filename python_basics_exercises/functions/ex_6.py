def compare_by_length(str1, str2):
    first = len(str1)
    second = len(str2)

    if first < second:
        return -1
    elif first > second:
        return 1
    else:
        return 0

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0