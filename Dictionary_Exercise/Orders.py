import math

products = input().split(" ")
dictionary_price = {}
dictionary_quantity = {}
count = 0
while products != ["buy"]:
    if products[0] in dictionary_price:
        dictionary_price[products[0]] = products[1]
    if products[0] in dictionary_quantity:
        dictionary_quantity[products[0]] += int(products[2])
        products = input().split(" ")
        continue
    dictionary_price[products[0]] = products[1]
    dictionary_quantity[products[0]] = int(products[2])

    products = input().split(" ")

for key, value in dictionary_price.items():
    int_value = float(value)
    total = int_value * dictionary_quantity[key]
    print(f"{key} -> {round(total,2):.2f}")