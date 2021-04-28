data = input()
result = ""
take_next_index = False
size = 0
for char in data:
    if not take_next_index:
        if not char == ">" and size == 0:
            result += char
        elif char == ">":
            take_next_index = True
            result += char
        else:
            size -= 1
    else:
        size += int(char) - 1
        if size == -1:
            result += char

        take_next_index = False

print(result)
