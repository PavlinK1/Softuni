def shopping_cart(*args):
    menu = {
        "Dessert": {'prod_numbers': 0, "products": []},
        "Soup": {'prod_numbers': 0, "products": []},
        "Pizza": {'prod_numbers': 0, "products": []}
    }
    keys = []
    values = []
    result = ''
    check = False
    for i in range(len(args)):
        if args[0] == "Stop" and result == '':
            return f"No products in the cart!"
        if args[i][0] in menu:
            recipe = args[i][0]
            product = args[i][1]
            if recipe == "Soup" and menu[recipe]["prod_numbers"] == 3:
                break
            if recipe == "Pizza" and menu[recipe]["prod_numbers"] == 4:
                break
            if recipe == "Dessert" and menu[recipe]["prod_numbers"] == 2:
                break
            menu[recipe]["prod_numbers"] += 1
            if product not in menu[recipe]['products']:
                menu[recipe]['products'].append(product)

    for key, value in menu.items():
        values.append((key, value['prod_numbers'], value['product']))
    values.sort(key=lambda y: (y[1]), reverse=True)
    for i in range(0, len(values)):
        for k in range(len(values[i])):
            if type(values[i][k]) is list:
                values[i][k].sort()
                break

    for pr in range(len(values)):
        result += f"{values[pr][0]}:\n"
        for kr in range(len(values[pr])):
            if type(values[pr][kr]) is list:
                for j in range(len(values[pr][kr])):
                    result += f"- {values[pr][kr][j]}\n"
    return result


print(shopping_cart(
    ('Pizza', 'hawm'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

