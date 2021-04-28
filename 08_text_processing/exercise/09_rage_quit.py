data = input()
to_multiply = ""
result = ""
multiplier = ""
for index, char in enumerate(data):
    if 97 <= ord(char) <= 122:
        to_multiply += chr(ord(char) - 32)
    elif not char.isdigit() and not 97 <= ord(char) <= 122:
        to_multiply += char
    elif char.isdigit():
        multiplier += char
        counter = index
        while counter + 1 < len(data):
            if not data[counter + 1].isdigit():
                break
            multiplier += data[counter + 1]
            counter += 1
        to_multiply *= int(multiplier)
        result += to_multiply
        to_multiply = ""
        multiplier = ""

print(f"Unique symbols used: {len(set(result))}")
print(result)
