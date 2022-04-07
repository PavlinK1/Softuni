n = int(input())
# "{plant}<->{rarity}".
# Store that information because you will need it later.
# If you receive a plant more than once, update its rarity.
dictionary = {}
command = input()
check = True
for i in range(n):
    plant, rate = command.split("<->")
    dictionary[plant] = {"Rarity": rate, "Rating": []}
    command = input()

while command != "Exhibition":
    if "Rate" in command:
        take = command[6:]
        split_command = take.split(" - ")
        if split_command[0] in dictionary:
            dictionary[split_command[0]]["Rating"].append(split_command[1])
        else:
            print("error")

    elif "Update" in command:
        take = command[8:]
        split_command = take.split(" - ")
        if split_command[0] in dictionary:
            dictionary[split_command[0]]["Rarity"] = split_command[1]
        else:
            print("error")
    elif "Reset" in command:
        take = command[7:]
        split_command = take.split(" - ")
        if split_command[0] in dictionary:
            dictionary[split_command[0]]["Rating"] = []
        else:
            print("error")
    else:
        print("error")
        check = False
        break
    command = input()
print(f"Plants for the exhibition:")
if check:
    for i in dictionary:
        plant_name = i
        rarity = dictionary[i]["Rarity"]
        rating = dictionary[i]["Rating"]
        join_rating = 0
        for i in rating:
            integer = int(i)
            join_rating += integer
        if not join_rating == 0:
            avarage_rating = join_rating / len(rating)
        else:
            avarage_rating = 0
        print(f"- {plant_name}; Rarity: {rarity}; Rating: {avarage_rating:.2f}")