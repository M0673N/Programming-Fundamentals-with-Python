def calculate_factorial(a, b):
    sum_1 = a
    for num in range(a - 1, 0, -1):
        sum_1 *= num
    sum_2 = b
    for num in range(b - 1, 0, -1):
        sum_2 *= num
    result = sum_1 / sum_2
    print(f"{result:.2f}")


num1 = int(input())
num2 = int(input())

calculate_factorial(num1, num2)
