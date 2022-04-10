raw_activation_key = input()
instructions = input().split(">>>")

while instructions[0] != "Generate":
    if instructions[0] == "Contains":

        if instructions[1] in raw_activation_key:
            print(f"{raw_activation_key} contains {instructions[1]}")
        else:
            print(f"Substring not found!")

    elif instructions[0] == "Flip":
        start_index = int(instructions[2])
        end_index = int(instructions[3])

        if instructions[1] == "Upper":

            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
            print(raw_activation_key)

        elif instructions[1] == "Lower":

            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
            print(raw_activation_key)

    elif instructions[0] == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])

        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

    instructions = input().split(">>>")
print(f"Your activation key is: {raw_activation_key}")
