num = float(input())
if num == 0:
    print("zero")
elif num > 0:
    if abs(num) < 1:
        print("small", end=" ")
    elif abs(num) > 1000000:
        print("large", end=" ")
    print("positive")
else:
    if abs(num) < 1:
        print("small", end=" ")
    elif abs(num) > 1000000:
        print("large", end=" ")
    print("negative")
