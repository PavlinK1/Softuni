def find(w_p_r, b_p_r, w_p_c, b_p_c, turn):
    if w_p_r - 1 == b_p_r and w_p_c + 1 == b_p_c or w_p_r - 1 == b_p_r and w_p_c - 1 == b_p_c:
        if turn % 2 == 0:
            return "white"
        elif turn % 2 == 1:
            return "black"
        else:
            None
    if w_p_r + 1 == b_p_r and w_p_c + 1 == b_p_c or w_p_r + 1 == b_p_r and w_p_c - 1 == b_p_c:
        if turn % 2 == 0:
            return "white"
        elif turn % 2 == 1:
            return "black"
        else:
            None

def letter(p_c):
    if p_c == 0:
        p_c = "a"
        return p_c
    elif p_c == 1:
        p_c = "b"
        return p_c
    elif p_c == 2:
        p_c = "c"
        return p_c
    elif p_c == 3:
        p_c = "d"
        return p_c
    elif p_c == 4:
        p_c = "e"
        return p_c
    elif p_c == 5:
        p_c = "f"
        return p_c
    elif p_c == 6:
        p_c = "g"
        return p_c
    elif p_c == 7:
        p_c = "h"
        return p_c
    else:
        return None


rows = 8
cols = 8
matrix = [input().split(" ") for _ in range(rows)]

white = False
black = False
for row in range(rows):
    if white or black:
        break
    for col in range(cols):
        if matrix[row][col] == "w":
            w_p = [row, col]
            print(w_p)
        elif matrix[row][col] == "b":
            b_p = [row, col]
w_p_r, w_p_c = w_p
b_p_r, b_p_c = b_p
turn = 0
while w_p[0] != 7 or b_p[0] != 0:
    if find(w_p_r, b_p_r, w_p_c, b_p_c, turn) == "white":
        let = letter(b_p_c)
        num = abs(b_p_r - 8)
        print(let)
        print(f"Game over! White pawn is promoted to a queen at {let}{num}.")
        break
    w_p_r = w_p[0] + 1
    w_p = (w_p_r, col)

    if w_p[0] >= 7:
        white = True
        break
    if find(w_p_r, b_p_r, w_p_c, b_p_c, turn) == "black":
        let = letter(w_p_c)
        num = abs(w_p_r - 8)
        print(f"Game over! black pawn is promoted to a queen at {let}{num}.")
        break
    b_p_r = b_p[0] - 1
    b_p = (b_p_r, col)
    if b_p[0] <= 0:
        black = True
        break
    turn += 1
if white:
    let = letter(w_p_c)
    num = abs(w_p_r - 8)
    print(f"Game over! White pawn is promoted to a queen at {let}{num}.")
elif black:
    let = letter(b_p_c)
    num = abs(b_p_r - 8)
    print(f"Game over! Black pawn is promoted to a queen at {let}{num}.")



'''
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
'''
