my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

idx = 0
while idx < len(my_list):
    nested_list = my_list[idx]
    nested_idx = 0
    while nested_idx < len(nested_list):
        num = nested_list[nested_idx]
        if num % 2 == 0:
            print(num)
        nested_idx += 1
    idx += 1