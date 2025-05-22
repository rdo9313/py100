a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# 2. 'a' on Line 5 reassigns the global variable 'a' to 2.