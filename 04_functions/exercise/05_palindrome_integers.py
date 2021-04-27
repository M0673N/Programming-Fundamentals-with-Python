def palindrome_check(num):
    for digit in num:
        if digit == digit[::-1]:
            print("True")
        else:
            print("False")


num = input().split(", ")

palindrome_check(num)
