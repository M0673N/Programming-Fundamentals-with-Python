n = int(input())
pieces = {}
for i in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]
command = input()
while not command == "Stop":
    command = command.split("|")
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1][0])))
for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece][0]}, Key: {pieces[piece][1]}")
