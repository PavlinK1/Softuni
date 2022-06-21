def best_list_pureness(numbers, k):
    from collections import deque
    count = 0
    highest = 0
    numbers = deque(numbers)
    for _ in range(k+1):
        for i in range(len(numbers)):
            count += i * numbers[i]
            if count > highest:
                highest = count
                r = _
        count = 0
        numbers.rotate(1)
    return f"Best pureness {highest} after {r} rotations"