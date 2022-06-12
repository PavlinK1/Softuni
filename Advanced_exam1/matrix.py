from math import floor


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


matrix = []
rows = int(input())
player_position = []
coins = 0

for row_index in range(rows):
    row_data = input().split()
    if "P" in row_data:
        player_position = [row_index, row_data.index('P')]
    matrix.append(row_data)

player_path = [player_position]
row, col = player_position
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
    else:
        command = input()
        continue
    row, col = calculate_position(matrix, row, col)
    if matrix[row][col] == 'X':
        player_path.append([row, col])
        coins = coins / 2
        coins = floor(coins)
        break
    elif matrix[row][col].isdigit():
        coins += int(matrix[row][col])
        matrix[row][col] = 'P'

    player_path.append([row, col])
    command = input()
if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for coordinates in player_path:
    print(coordinates)


