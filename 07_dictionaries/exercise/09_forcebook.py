data_user = {}
data_side = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        side, user = command.split(" | ")
        if user not in data_user:
            data_user[user] = side
            if side not in data_side:
                data_side[side] = [user]
            else:
                data_side[side].append(user)
    elif "->" in command:
        user, side = command.split(" -> ")
        if user not in data_user:
            data_user[user] = side
            if side not in data_side:
                data_side[side] = [user]
            else:
                data_side[side].append(user)
        else:
            if data_user[user] == side:
                continue
            data_side[data_user[user]].remove(user)
            data_user[user] = side
            if side not in data_side:
                data_side[side] = [user]
            else:
                data_side[side].append(user)
        print(f"{user} joins the {side} side!")

data_side = dict(sorted(data_side.items(), key=lambda x: (-len(x[1]), x[0])))
for side in data_side:
    if len(data_side[side]) == 0:
        continue
    print(f"Side: {side}, Members: {len(data_side[side])}")
    data_side[side] = sorted(data_side[side])
    for user in data_side[side]:
        print(f"! {user}")
