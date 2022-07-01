times = {}
numbers = [float(i) for i in input().split(" ")]

for num in numbers:
    if num in times:
        times[num] += 1
    else:
        times[num] = 1

for key, value in times.items():
    print(f"{key} - {value} times")