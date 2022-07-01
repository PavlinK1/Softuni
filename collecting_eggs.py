from collections import deque

eggs = deque(map(int, input().split(", ")))
paper_size = deque(map(int, input().split(", ")))
total_boxes = 0
box = 50

while paper_size and eggs:
    first_egg = eggs[0]
    last_paper = paper_size[-1]
    if first_egg == 13:
        eggs.popleft()
        left = paper_size.popleft()
        paper_size.appendleft(paper_size.pop())
        paper_size.append(left)
        continue
    if first_egg <= 0:
        eggs.popleft()
        continue
    if first_egg + last_paper <= box:
        wrap = first_egg + last_paper
        total_boxes += 1
        eggs.popleft()
        paper_size.pop()
    else:
        eggs.popleft()
        paper_size.pop()


if total_boxes >= 1:
    print(f"Great! You filled {total_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print("Eggs left:", end=" ")
    print(*eggs, sep=", ")

if paper_size:
    print("Pieces of paper left:", end=" ")
    print(*paper_size, sep=", ")
