username = input()
command = input().split(" ")

while command[0] != "Registration":
    if command[0] == "Letters":
        if command[1] == "Upper":
            username = username.upper()
        elif command[1] == "Lower":
            username = username.lower()
        print(username)

    elif command[0] == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 < start_index < len(username) and 0 < end_index < len(username):
            username_2 = username[start_index:end_index + 1]
            revers = username_2[::-1]
            print(revers)
        else:
            pass

    elif command[0] == "Substring":
        if command[1] in username:
            username = username.replace(command[1], "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {command[1]}.")

    elif command[0] == "Replace":
        if command[1] in username:
            username = username.replace(command[1], "-")
            print(username)
        else:
            pass

    elif command[0] == "IsValid":
        if command[1] in username:
            print("Valid")
        else:
            print(f"{command[1]} must be contained in your username.")

    command = input().split(" ")

