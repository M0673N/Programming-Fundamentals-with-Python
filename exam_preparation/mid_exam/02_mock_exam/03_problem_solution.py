numbers = [int(number) for number in input().split()]
average = sum(numbers) / len(numbers)
numbers = sorted(numbers, reverse=True)
result = [num for num in numbers if num > average]
if 0 < len(result) <= 5:
    result = [str(num) for num in result]
    print(" ".join(result))
elif len(result) == 0:
    print("No")
else:
    long_result = []
    for num in range(5):
        long_result.append(str(result[num]))
    print(" ".join(long_result))
