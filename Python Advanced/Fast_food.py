from collections import deque
qty_f = int(input())
orders = deque(int(i) for i in input().split())
biggest = max(orders)
print(biggest)
while orders:
    if orders[0] <= qty_f:
        qty_f -= orders[0]
        orders.popleft()
    else:
        break

if orders:
    print(f"Orders left:",end=' ')
    while orders:
        if orders:
            print(orders.popleft(), end=' ')
        else:
            print(orders.popleft())
else:
    print("Orders complete")