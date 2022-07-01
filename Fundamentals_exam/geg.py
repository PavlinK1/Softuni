password = input()
command = input()

new_password = password  # changed

while True:
    tokens = command.split()
    if tokens[0] == "TakeOdd":
        curr_password = new_password  # changed
        new_password = ""  # changed
        for char in range(len(curr_password)):  # changed
            if char % 2 != 0:
                letter = curr_password[char]  # changed
                new_password += letter
        print(new_password)
    elif tokens[0] == "Cut":
        index = int(tokens[1])
        length = new_password[index:(index + int(tokens[2]))]
        new_password = new_password.replace(length, "", 1)
        print(new_password)
    elif tokens[0] == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")

    command = input()

    if command == "Done":
        print(f"Your password is: {new_password}")