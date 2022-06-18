def ran(ma, r, c):
    if not 0 <= r < len(ma) or not 0 <= c < len(ma):
        return True
    else:
        return False


rows = 6
matrix = [input().split(" ") for i in range(rows)]
score = 0
hit_buckets = []
hit = False

for i in range(3):
    command = eval(input())
    position1, position2 = command
    if ran(matrix, position1, position2):
        continue
    if matrix[position1][position2] == "B":
        for h in range(len(hit_buckets)):
            check1, check2 = hit_buckets[h]
            if position1 == check1 and position2 == check2:
                hit = True
                continue
        if hit:
            continue
        else:
            hit_buckets.append([position1, position2])
            for i in range(6):
                if not matrix[i][position2] == "B":
                    score += int(matrix[i][position2])

if 0 <= score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
elif 100 <= score < 200:
    print(f"Good job! You scored {score} points, and you've won Football.")
elif 200 <= score < 300:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
elif score >= 300:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")