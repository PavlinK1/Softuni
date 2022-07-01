N = int(input())
total_petrol = 0
total_km = 0
n = "0"
for i in range(N):
    info = [int(x) for x in input().split()]
    amount_petrol = info[0]
    distance_pump = info[1]
    if amount_petrol + total_petrol < distance_pump + total_km:
        total_petrol = 0
        total_km = 0
        n = "0"
        continue
    elif n == "0":
        n = i
        total_petrol += amount_petrol
        total_km += distance_pump
    else:
        total_petrol += amount_petrol
        total_km += distance_pump
if total_petrol != 0:
    N -= 1

print(n)