data = input().split()
search = input()
counter = 0
data2 = [palindrome for palindrome in data if palindrome == "".join(reversed(palindrome))]
print(data2)
print(f"Found palindrome {data.count(search)} times")
