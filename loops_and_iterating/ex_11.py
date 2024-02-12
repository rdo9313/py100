my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0
while index < len(my_list):
    idx = 0
    sublist = my_list[index]
    while idx < len(sublist):
        if sublist[idx] % 2 == 0:
            print(sublist[idx])
        idx += 1
    index += 1