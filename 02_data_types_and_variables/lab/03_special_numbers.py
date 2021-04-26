n = int(input())
for num in range(1, n + 1):
    special_check = 0
    for digit in str(num):
        special_check += int(digit)
    if special_check == 7 or special_check == 5 or special_check == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
