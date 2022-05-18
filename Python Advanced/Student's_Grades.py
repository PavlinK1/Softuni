from statistics import mean

N = int(input())
students = {}
for _ in range(N):
    student, grade = input().split()
    if student in students:
        students[student].append(float(grade))
    else:
        students[student] = [float(grade)]

for data in students.items():
    print(f"{data[0]} -> {' '.join(f'{el:.2f}' for el in data[1])} (avg: {mean(data[1]):.2f})")