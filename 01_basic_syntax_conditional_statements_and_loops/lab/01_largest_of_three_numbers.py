from sys import maxsize
num1 = int(input())
num2 = int(input())
num3 = int(input())
biggest = -maxsize
if num1 > biggest:
    biggest = num1
if num2 > biggest:
    biggest = num2
if num3 > biggest:
    biggest = num3
print(biggest)
