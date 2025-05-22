b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# [10, 2, 3]. Line 4 references the global variable b and mutates the list.