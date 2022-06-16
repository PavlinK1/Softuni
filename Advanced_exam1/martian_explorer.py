def found(ma, row, col, foundings):
    if 0 <= row < 6 and 0 <= col < 6:
        if ma[row][col] == "W":
            foundings.append("Water")
            foundings.append((row, col))
        if ma[row][col] == "M":
            foundings.append("Metal")
            foundings.append((row, col))
        if ma[row][col] == "C":
            foundings.append("Concrete")
            foundings.append((row, col))
        if ma[row][col] == "R":
            foundings.append("Rover")
            foundings.append((row, col))



matrix = []
rows = 6
water = 0
metal = 0
concrete = 0
for i in range(rows):
    matrix.append([data for data in input().split(" ")])
for data in range(len(matrix)):
    for info in range(len(matrix[data])):
        if matrix[data][info] == "E":
            rover_coordinates = data, info
            break
command = input().split(", ")
data, info = rover_coordinates
foundings = []
for co in command:
    if co == "up":
        data -= 1
        if data < 0:
            data = 5
        found(matrix, data, info, foundings)
    elif co == "down":
        data += 1
        if data > 5:
            data = 0
        found(matrix, data, info, foundings)
    elif co == "right":
        info += 1
        if info > 5:
            info = 0
        found(matrix, data, info, foundings)
    elif co == "left":
        info -= 1
        if info < 0:
            info = 5
        found(matrix, data, info, foundings)

for i in range(0, len(foundings), 2):
    if foundings[i] == "Water":
        water += 1
    if foundings[i] == "Metal":
        metal += 1
    if foundings[i] == "Concrete":
        concrete += 1
    if foundings[i] == "Rover":
        print(f"{foundings[i]} got broken at {foundings[i + 1]}")
    else:
        print(f"{foundings[i]} deposit found at {foundings[i +1]}")

if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")