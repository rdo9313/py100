def multiply(num1, num2):
    return float(num1) * float(num2)

first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
product = multiply(first_num, second_num)

print(f"{first_num} * {second_num} = {product}")