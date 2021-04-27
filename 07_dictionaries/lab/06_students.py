data = {}
while True:
    info = input().split(":")
    if len(info) == 1:
        break
    name = info[0]
    id_ = info[1]
    course = info[2]
    data[id_] = [name, course]
info = info[0]
info = info.replace("_", " ")
for student in data:
    if data[student][1] == info:
        print(f"{data[student][0]} - {student}")
