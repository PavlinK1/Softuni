def move(player_position, r, c, command, N):
    check = False
    if command == "up":
        r -= 1
    elif command == "down":
        r += 1
    elif command == "left":
        c -= 1
    elif command == "right":
        c += 1
    if 0 <= r < N and 0 <= c < N:
        return r, c, check
    else:
        check = True
        r, c = player_position
        return r, c, check


string = input()
N = int(input())
#matrix creation
matrix = [list(input()) for i in range(N)]

found = False
# player position parameters
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "P":
            player_position = [row, col]
            row, col = player_position
            found = True
            break
    if found:
        break

M = int(input())
for _ in range(M):
    command = input()
    if command:
        matrix[row][col] = "-"
        row, col, check = move(player_position, row, col, command, N)
        if not check:
            if not matrix[row][col] == "-" and not matrix[row][col] == "P":
                string += matrix[row][col]
            matrix[row][col] = "P"
            player_position = [row, col]
        elif check:
            row, col = player_position
            matrix[row][col] = "P"
            string = string[:-1]
            check = False

print(string)
for i in range(len(matrix)):
    print("".join(matrix[i]))



