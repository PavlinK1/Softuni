player1, player2 = input().split(", ")
players = {
            player1: {"score": 501, "move": 0},
            player2: {"score": 501, "move": 0}
           }
matrix = [input().split(" ") for i in range(7)]

command = eval(input())
move = 0
while command:
    dx, dy = command
    dx = dx
    dy = dy
    move += 1
    if dx < 0 or dx > 7 or dy < 0 or dy > 7:
        command = eval(input())
        if move % 2 == 0:
            players[player2]["move"] += 1
        elif move % 2 == 1:
            players[player1]["move"] += 1
        continue
    if matrix[dx][dy].isdigit():
        result = int(matrix[dx][dy])
    if matrix[dx][dy] == "B":
        if move % 2 == 1:
            players[player1]['move'] += 1
            print(f"{player1} won the game with {players[player1]['move']} throws!")
        else:
            players[player2]['move'] += 1
            print(f"{player2} won the game with {players[player2]['move']} throws!")
        break
    elif matrix[dx][dy] == "D":
        result = (int(matrix[dx][0]) + int(matrix[dx][-1]) + int(matrix[0][dy]) + int(matrix[-1][dy])) * 2
    elif matrix[dx][dy] == "T":
        result = (int(matrix[dx][0]) + int(matrix[dx][-1]) + int(matrix[0][dy]) + int(matrix[-1][dy])) * 3
    else:
        result = int(matrix[dx][dy])

    if move % 2 == 0 and not matrix[dx][dy] == "B":
        players[player2]["score"] -= result
        players[player2]["move"] += 1
    elif not matrix[dx][dy] == "B" and move % 2 == 1:
        players[player1]["score"] -= result
        players[player1]["move"] += 1

    if players[player2]["score"] <= 0 or players[player1]["score"] <= 0:
        break

    command = eval(input())

if players[player2]["score"] <= 0 or players[player1]["score"] <= 0:
    if players[player1]["score"] <= 0:
        print(f"{player1} won the game with {players[player1]['move']} throws!")
    elif players[player2]["score"] <= 0:
        print(f"{player2} won the game with {players[player2]['move']} throws!")