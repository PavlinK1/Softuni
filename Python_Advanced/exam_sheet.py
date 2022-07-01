'''
#1 task tips:

from collections import deque

pizza_orders = deque(map(int, input().split(", "))) - queue with int formatter
employees = deque(map(int, input().split(", "))) - queue with int formatter
total_pizza = 0 - total counter if needed

while pizza_orders and employees:
    first_pizzas = pizza_orders[0]
    last_employee = employees[-1]


# Printing tips
if not pizza_orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print("Employees:", end=" ")
    print(*employees, sep=", ")
else:
    print("Not all orders are completed.")
    print(f"Orders left:", end=" ")
    print(*pizza_orders, sep=", ")

# 2 task tips:

matrix = [input().split(" ") for _ in range(ROWS)]
wh, b = find_player(matrix)
w_p_r, w_p_c = wh
b_p_r, b_p_c = b

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

# 3 task tips:
judge
def start_spring(**kwargs):
    def check(adict: dict):
        max_key = 0
        result = ''
        sorted_tuples = sorted(adict.items(), key=lambda x: (-len(x[1]), x[0]))
        for tuple_ in sorted_tuples:

            type_object = tuple_[0]
            list_of_objects = tuple_[1]
            sorted_list_of_objects = sorted(list_of_objects)
            result += f"{type_object}:\n"
            for obj in sorted_list_of_objects:
                result += f"-{obj}\n"
        return result.strip()
    a_dict = {}
    for key, value in kwargs.items():
        if value in a_dict:
            a_dict[value].append(key)
        else:
            a_dict[value] = [key]
    max_k = check(a_dict)
    return max_k
'''








