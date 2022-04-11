command = input().split()

bakery = {}
client = {}

total_income = 0

while command[0] != "End":
    if command[0] == "Deliver":
        distributor_name = command[1]
        money_spent = float(command[2])
        if distributor_name not in bakery:
            bakery[distributor_name] = {"money": money_spent}
        else:
            bakery[distributor_name]["money"] += money_spent

    if command[0] == "Return":
        distributor_name = command[1]
        money_returned = float(command[2])
        if distributor_name not in bakery:
            pass
        elif money_returned < bakery[distributor_name]["money"]:
            bakery[distributor_name]["money"] -= money_returned
        else:
            bakery[distributor_name]["money"] -= money_returned
            if bakery[distributor_name]["money"] <= 0:
                bakery.pop(distributor_name)

    if command[0] == "Sell":
        client_name = command[1]
        money_earned = float(command[2])
        if client_name not in client:
            client[client_name] = {"money_earned": money_earned}
        else:
            client[client_name]['money_earned'] += money_earned

    command = input().split()

for key, value in client.items():
    print(f"{key}: {value['money_earned']:.2f}")
    total_income += value['money_earned']
print("-----------")
for key, value in bakery.items():
    print(f"{key}: {value['money']:.2f}")
print("-----------")
print(f"Total Income: {total_income:.2f}")

