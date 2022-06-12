def calculate_position(matr_len, row_, column):
    if row_ < 0:
        row_ = len(matr_len) - 1
    if column < 0:
        column = len(matr_len) - 1

    if column > len(matr_len) - 1:
        column = 0
    if row_ > len(matr_len) - 1:
        row_ = 0

    return row_, column


rows = int(input())
matrix = []
burrows = []
snake_position = []
food = 0

for row_index in range(rows):
    row_data = input()
    matrix.append(list(row_data))
    if "S" in row_data:
        snake_position = [row_index, row_data.index("S")]
    if "B" in row_data:
        burrows.append([row_index, row_data.index("B")])

row, col = snake_position
command = input()
while command:
    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'right':
        col += 1
    elif command == 'left':
        col -= 1

    row, col = calculate_position(matrix, row, col)
    if matrix[row][col] == "B":
        matrix[row][col] = '.'
        for burrow in burrows:
            if not burrow == [row, col]:
                row, col = burrow
    if matrix[row][col] == "*":
        food += 1
        matrix[row][col] = "."

    command = input()
# print(["".join(n) for n in (", ".join(m) for m in matrix)])
matrix = ", ".join()
print([", ".join(m) for m in matrix])
