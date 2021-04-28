data = {}
while True:
    flag = False
    info = input().split()
    for i in range(0, len(info), 2):
        item = info[i + 1].lower()
        amount = int(info[i])
        if item not in data:
            data[item] = amount
        else:
            data[item] += amount
        if "shards" in data:
            if data["shards"] >= 250:
                data["shards"] -= 250
                print("Shadowmourne obtained!")
                flag = True
                break
        if "fragments" in data:
            if data["fragments"] >= 250:
                data["fragments"] -= 250
                print("Valanyr obtained!")
                flag = True
                break
        if "motes" in data:
            if data["motes"] >= 250:
                data["motes"] -= 250
                print("Dragonwrath obtained!")
                flag = True
                break
    if flag:
        break

junk_list = {}
for i in data:
    if not i == "shards" and not i == "motes" and not i == "fragments":
        junk_list[i] = data[i]

junk_list = dict(sorted(junk_list.items(), key=lambda x: x[0]))

new_data = {}
for i in data:
    if i == "shards":
        new_data[i] = data[i]
    elif i == "motes":
        new_data[i] = data[i]
    elif i == "fragments":
        new_data[i] = data[i]

if "fragments" not in new_data:
    new_data["fragments"] = 0
if "motes" not in new_data:
    new_data["motes"] = 0
if "shards" not in new_data:
    new_data["shards"] = 0

new_data = dict(sorted(new_data.items(), key=lambda x: (-x[1], x[0])))

for i, j in new_data.items():
    print(f"{i}: {j}")
for i, j in junk_list.items():
    print(f"{i}: {j}")
