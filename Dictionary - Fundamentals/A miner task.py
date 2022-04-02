def resource_check(diction, locke):
    if locke not in diction:
        diction[resource] = 0


dictionary = {}

while True:
    resource = input()
    if resource == "stop":
        break
    resource_check(dictionary, resource)
    quantity = int(input())
    dictionary[resource] += quantity

for key, value in dictionary.items():
    print(f"{key} -> {value}")


