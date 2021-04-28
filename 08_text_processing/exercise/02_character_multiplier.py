data = input().split()
string_1 = [ord(el) for el in data[0]]
string_2 = [ord(el) for el in data[1]]

total_sum = 0

if len(string_1) == len(string_2):
    for i in range(len(string_1)):
        total_sum += string_1[i] * string_2[i]

elif len(string_1) > len(string_2):
    for i in range(len(string_2)):
        total_sum += string_1[i] * string_2[i]
    for i in range(len(string_2), len(string_1)):
        total_sum += string_1[i]

else:
    for i in range(len(string_1)):
        total_sum += string_1[i] * string_2[i]
    for i in range(len(string_1), len(string_2)):
        total_sum += string_2[i]

print(total_sum)
