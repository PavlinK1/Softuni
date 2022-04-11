command = input()
cities, population, gold = command.split("||")
dictionary = {}
while True:
    if cities not in dictionary:
        dictionary[cities] = {"population": int(population), "gold": int(gold)}
    else:
        dictionary[cities]['gold'] += int(gold)
        dictionary[cities]['population'] += int(population)
    command = input()
    if command == "Sail":
        break
    cities, population, gold = command.split("||")


command = input().split("=>")

while command[0] != "End":

    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        dictionary[town]["gold"] -= gold
        dictionary[town]["population"] -= people
        if dictionary[town]["gold"] <= 0 or dictionary[town]["population"] <= 0:
            dictionary.pop(town)
            print(f"{town} has been wiped off the map!")

    if command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        if gold <= 0:
            print(f"Gold added cannot be a negative number!")
        else:
            dictionary[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town]['gold']} gold.")

    command = input().split("=>")

if len(dictionary) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
    for key, value in dictionary.items():

        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
