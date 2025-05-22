my_list = [6, 3, 0, 11, 20, 4, 17]

idx = 0
while idx < len(my_list):
    num = my_list[idx]
    if num % 2 == 0:
        print(num)
    idx += 1

for num in my_list:
    if num % 2 == 1:
        print(num)