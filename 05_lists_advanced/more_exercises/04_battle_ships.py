rows = int(input())
data = []
total = 0
new_data = []
for i in range(rows):
    data.append(input().split())
    data[i] = [int(item) for item in data[i]]
attacks = input().split()
for attack in attacks:
    row = int(attack.split("-")[0])
    col = int(attack.split("-")[1])
    if not data[row][col] == 0:
        data[row][col] -= 1
        if data[row][col] == 0:
            total += 1
print(total)
