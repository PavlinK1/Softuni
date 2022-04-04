string = input()
command = input()
full_commands = command.split(">>>")

while full_commands[0] != "Generate":
    if full_commands[0] == "Contains":
        if full_commands[1] in string:
            print(f"{string} contains {full_commands[1]}")
        else:
            print(f"Substring not found!")
    elif full_commands[0] == "Flip":
        start_index = int(full_commands[2])
        end_index = int(full_commands[3])
        if full_commands[1] == "Upper":
            string = string[:start_index] + string[start_index:end_index].upper() + string[end_index:]
            print(string)
        elif full_commands[1] == "Lower":
            string = string[:start_index] + string[start_index:end_index].lower() + string[end_index:]
            print(string)
    elif full_commands[0] == "Slice":
        start_index = int(full_commands[1])
        end_index = int(full_commands[2])
        string = string[:start_index] + string[end_index:]
        print(string)
    command = input()
    full_commands = command.split(">>>")
print(f"Your activation key is: {string}")