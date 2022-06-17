def is_in_matrix(size, row, col):
    return 0 <= row < size and 0 <= col < size


def neighbour_count(matrix, row, col):
    count = 0
    if is_in_matrix(len(matrix), row - 1, col) and matrix[row - 1][col] == "*":
        count += 1
    if is_in_matrix(len(matrix), row + 1, col) and matrix[row + 1][col] == "*":
        count += 1
    if is_in_matrix(len(matrix), row, col - 1) and matrix[row][col - 1] == "*":
        count += 1
    if is_in_matrix(len(matrix), row, col + 1) and matrix[row][col + 1] == "*":
        count += 1
    if is_in_matrix(len(matrix), row - 1, col - 1) and matrix[row - 1][col - 1] == "*":
        count += 1
    if is_in_matrix(len(matrix), row + 1, col - 1) and matrix[row + 1][col - 1] == "*":
        count += 1
    if is_in_matrix(len(matrix), row - 1, col + 1) and matrix[row - 1][col + 1] == "*":
        count += 1
    if is_in_matrix(len(matrix), row + 1, col + 1) and matrix[row + 1][col + 1] == "*":
        count += 1
    return count

rows = int(input())
bombs = int(input())
all_bombs = []
matrix = []

for row_index in range(rows):
    matrix.append([0 for i in range(rows)])

for bomb in range(bombs):
    coordinates = input()
    coordinates = tuple([int(i) for i in coordinates if i.isdigit()])
    dx, dy = coordinates
    matrix[dx][dy] = "*"
    all_bombs.append(coordinates)

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == '*':
            continue
        cell_value = neighbour_count(matrix, row, col)
        matrix[row][col] = cell_value

for row in matrix:
    print(*row)