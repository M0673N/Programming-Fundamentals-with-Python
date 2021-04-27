rooms = int(input())
free_chairs = 0
flag = False
for room in range(1, rooms + 1):
    command = input().split()
    if len(command[0]) < int(command[1]):
        print(f"{int(command[1]) - len(command[0])} more chairs needed in room {room}")
        flag = True
    else:
        free_chairs += len(command[0]) - int(command[1])
if not flag:
    print(f"Game On, {free_chairs} free chairs left")
