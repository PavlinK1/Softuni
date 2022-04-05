command = input().split("||")
cities_info = {}
while command[0] != "Sail":
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in cities_info:
        cities_info[city] = {"population": population, "gold": gold}
    else:
        cities_info[city]["population"] += population
        cities_info[city]["gold"] += gold
    command = input().split("||")

command = input().split("=>")

while command[0] != "End":
    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        cities_info[town]["population"] -= people
        cities_info[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_info[town]["population"] == 0 or cities_info[town]["gold"] == 0:
            cities_info.pop(town)
            print(f"{town} has been wiped off the map!")

    if command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        if gold > 0:
            cities_info[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_info[town]['gold']} gold.")
        else:
            print(f"Gold added cannot be a negative number!")

    command = input().split("=>")
if cities_info:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for town, population in cities_info.items():
        print(
            f"{town} -> Population: {cities_info[town].get('population')} citizens, Gold: {cities_info[town].get('gold')} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")