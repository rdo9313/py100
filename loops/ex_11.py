my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

idx = 0
while idx < len(my_list):
    current_list = my_list[idx]
    size = 0
    while size < len(current_list):
        if current_list[size] % 2 == 0:
            print(current_list[size])
        size += 1
    idx += 1