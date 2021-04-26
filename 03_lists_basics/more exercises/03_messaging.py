data = input().split()
string = input()
result = ""
for item in data:
    index = 0
    for num in item:
        index += int(num)
    if index >= len(string):
        index -= len(string)
    result += string[index]
    string = string[:index] + string[index + 1:]
print(result)
