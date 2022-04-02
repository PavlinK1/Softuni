elements = input().split(" ")
stock = {}  # stock = dict()

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    stock[key]= int(value)
    print(stock)