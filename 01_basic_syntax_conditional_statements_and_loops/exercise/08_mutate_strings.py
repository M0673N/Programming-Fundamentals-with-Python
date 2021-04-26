string1 = input()
string2 = input()
current = ""
previous = string1
for i in range(len(string2)):
    for j in range(i + 1):
        current += string2[j]
    for k in range(i + 1, len(string1)):
        current += string1[k]
    if not current == previous:
        print(current)
    previous = current
    current = ""
