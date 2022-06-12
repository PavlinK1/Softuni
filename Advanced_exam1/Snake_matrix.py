command = input()
while command:
    matrix[row][col] = "."
    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'right':
        col += 1
    elif command == 'left':
        col -= 1

    if calculate_position(matrix, row, col) == True:
        print("Game over!")
        print(f"Food eaten: {food}")
        done = False
        break
    if matrix[row][col] == "B":
        matrix[row][col] = '.'
        for burrow in burrows:
            if not burrow == [row, col]:
                row, col = burrow
                matrix[row][col] = '.'
    if matrix[row][col] == "*":
        food += 1
        if food == 10:
            matrix[row][col] = "S"
            break
        matrix[row][col] = "."
    if matrix[row][col] == "-":
        matrix[row][col] = "."
    command = False
    if command == False:
        matrix[row][col] = "S"
    command = input()

matrix = "\n".join(["".join(m) for m in matrix])
if done and food >= 10:
    print("You won! You fed the snake.")
    print(f"Food eaten: {food}")
print(matrix)