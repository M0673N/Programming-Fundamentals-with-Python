def add_and_subtract(a, b, c):
    def sum_numbers(a, b):
        result = a + b
        return result

    result = sum_numbers(a, b)

    def subtract(c):
        result2 = result - c
        return result2

    result2 = subtract(c)
    return result2


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
