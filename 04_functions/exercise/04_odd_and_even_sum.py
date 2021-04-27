def odd_even_sum(num):
    odd = 0
    even = 0
    for digit in num:
        if int(digit) % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    print(f"Odd sum = {odd}, Even sum = {even}")


num = input()

odd_even_sum(num)
