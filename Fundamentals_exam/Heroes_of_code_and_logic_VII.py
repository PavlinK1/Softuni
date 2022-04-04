n = int(input())
dictionary = {}
for _ in range(n):
    command = input()
    hero_info = command.split()
    hero_name = hero_info[0]
    hero_HP = int(hero_info[1])
    hero_MP = int(hero_info[2])
    dictionary[hero_name] = {"HP": hero_HP, "MP": hero_MP}

command = input()
full_command = command.split(" - ")

while full_command[0] != "End":
    if full_command[0] == "CastSpell":
        hero_name = full_command[1]
        MP_needed = int(full_command[2])
        spell_name = full_command[3]
        if dictionary[hero_name]["MP"] >= MP_needed:
            dictionary[hero_name]["MP"] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {dictionary[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    if full_command[0] == "TakeDamage":
        hero_name = full_command[1]
        damage = int(full_command[2])
        attacker = full_command[3]
        dictionary[hero_name]["HP"] -= damage
        if dictionary[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dictionary[hero_name]['HP']} HP left!")
        else:
            dictionary.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    if full_command[0] == "Recharge":
        hero_name = full_command[1]
        amount = int(full_command[2])
        how_much = 200 - dictionary[hero_name]["MP"]
        dictionary[hero_name]["MP"] += amount
        if dictionary[hero_name]["MP"] > 200:
            amount = how_much
            dictionary[hero_name]["MP"] = 200
        print(f"{hero_name} recharged for {amount} MP!")
    if full_command[0] == "Heal":
        hero_name = full_command[1]
        amount = int(full_command[2])
        how_much = 100 - dictionary[hero_name]["HP"]
        dictionary[hero_name]["HP"] += amount
        if dictionary[hero_name]["HP"] > 100:
            amount = how_much
            dictionary[hero_name]["HP"] = 100
        print(f"{hero_name} healed for {amount} HP!")
    command = input()
    full_command = command.split(" - ")
for key, value in dictionary.items():
    print(f"{key}")
    print(f" HP: {value['HP']}")
    print(f" MP: {value['MP']}")
