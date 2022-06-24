from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employees = deque(map(int, input().split(", ")))
total_pizza = 0

while pizza_orders and employees:
    first_pizzas = pizza_orders[0]
    last_employee = employees[-1]
    if first_pizzas > 10 or first_pizzas <= 0:
        pizza_orders.popleft()
        continue
    if first_pizzas <= last_employee:
        pizza_orders.popleft()
        employees.pop()
        total_pizza += first_pizzas
    else:
        pizza_orders[0] -= last_employee
        total_pizza += last_employee
        employees.pop()
        if not employees:
            break

if not pizza_orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print("Employees:", end=" ")
    print(*employees, sep=", ")
else:
    print("Not all orders are completed.")
    print(f"Orders left:", end=" ")
    print(*pizza_orders, sep=", ")