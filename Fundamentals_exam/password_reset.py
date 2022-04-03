string = input()
command = input()
command_list = command.split()
password = string
while command_list[0] != "Done":
    if command_list[0] == "TakeOdd":
        curr_password = password
        password = ""
        for i in range(1, len(curr_password), 2):
            password += curr_password[i]
        print(password)
    elif command_list[0] == "Cut":
        index = int(command_list[1])
        length = int(command_list[2])
        until = index + length
        substring = password[index:until]
        password = password.replace(substring, "", 1)
        print(password)
    elif command_list[0] == "Substitute":
        substring = command_list[1]
        substitute = command_list[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f"Nothing to replace!")
    command = input()
    command_list = command.split()
print(f"Your password is: {password}")
