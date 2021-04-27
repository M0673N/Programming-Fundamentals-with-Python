numbers = input().split(", ")
positive = [num for num in numbers if int(num) >= 0]
negative = [num for num in numbers if int(num) < 0]
even = [num for num in numbers if int(num) % 2 == 0]
odd = [num for num in numbers if int(num) % 2 == 1]
print(f"Positive: {', '.join(positive)}\n"
      f"Negative: {', '.join(negative)}\n"
      f"Even: {', '.join(even)}\n"
      f"Odd: {', '.join(odd)}")
