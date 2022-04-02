elements = input().split(" ")
stock = {}  # stock = dict()
check = input().split(" ")
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    stock[key] = int(value)
    quantity = int(value)
    product_el = key
for k in check:
    if k in stock:
        print(f"We have {stock[k]} of {k} left")
    else:
        print(f"Sorry, we don't have {k}")
