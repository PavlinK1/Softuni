from collections import deque
name = input()
line = deque()
count = 0
while not name == "End":
    if name == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(name)
    name = input()

print(f"{len(line)} people remaining.")