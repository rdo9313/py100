def multiply(left, right):
    return left * right

first_num = float(input('Enter the first number: '))
second_num = float(input('Enter the second number: '))
product = multiply(first_num, second_num)
print(f'{first_num} * {second_num} = {product}')