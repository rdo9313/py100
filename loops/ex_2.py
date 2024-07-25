age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')