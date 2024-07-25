my_list = [6, 3, 0, 11, 20, 4, 17]

count = 0
while count < len(my_list):
    if my_list[count] % 2 == 0:
        print(my_list[count])
    count += 1

for number in my_list:
    if number % 2 == 1:
        print(number)