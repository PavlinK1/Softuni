n = int(input())
dictionary = {}

for i in range(n):
    piece, composer, key = input().split("|")
    dictionary[piece] = {"Composer": composer, "Key": key}
command = input()
listed = command.split("|")

while listed[0] != "Stop":
    if listed[0] == "Add":
        piece, composer, key = listed[1:]
        if piece in dictionary:
            print(f"{piece} is already in the collection!")
        else:
            dictionary[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif listed[0] == "Remove":
        piece = listed[1]
        if piece in dictionary:
            del dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif listed[0] == "ChangeKey":
        piece, new_key = listed[1:]
        if piece in dictionary:
            dictionary[piece]['Key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
    listed = command.split("|")

for key, value in dictionary.items():
    print(f"{key} -> Composer: {dictionary[key].get('Composer')}, Key: {dictionary[key].get('Key')}")