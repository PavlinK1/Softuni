ROWS = 6
COLS = 6
name_1, name_2 = input().split(", ")
matrix = [input().split(" ") for _ in range(ROWS)]

command = eval(input())
turn = 1
fail_1 = ""
fail_2 = ""
check = ""
while command:
    row, col = command
    if not fail_1 == "" and fail_1[1] % 2 == turn % 2:
        command = eval(input())
        fail_1 = ""
        check = ""
        turn += 1
        continue
    if not fail_2 == "" and fail_2[1] % 2 == turn % 2:
        command = eval(input())
        fail_2 = ""
        check = ""
        turn += 1
        continue
    if matrix[row][col] == "E":
        if turn % 2 == 1:
            print(f"{name_1} found the Exit and wins the game!")
        else:
            print(f"{name_2} found the Exit and wins the game!")
        break
    elif matrix[row][col] == "T":
        if turn % 2 == 1:
            print(f"{name_1} is out of the game! The winner is {name_2}.")
        else:
            print(f"{name_2} is out of the game! The winner is {name_1}.")
        break
    elif matrix[row][col] == "W":
        if turn % 2 == 1:
            print(f"{name_1} hits a wall and needs to rest.")
            fail_1 = [name_1, turn]
            check = turn % 2
        else:
            print(f"{name_2} hits a wall and needs to rest.")
            fail_2 = [name_2, turn]
            check = turn % 2
    turn += 1
    command = eval(input())
