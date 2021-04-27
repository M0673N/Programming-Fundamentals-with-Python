data = [char for char in input()]
vowels = ['a', 'o', 'u', 'e', 'i']
data = [char for char in data if char.lower() not in vowels]
print("".join(data))
