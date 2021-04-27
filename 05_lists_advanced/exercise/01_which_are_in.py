line1 = input().split(", ")
line2 = input().split(", ")
result = [substring for substring in line1 if substring in str(line2)]
print(result)
