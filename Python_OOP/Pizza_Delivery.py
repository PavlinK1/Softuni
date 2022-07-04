class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        self.ingredient = ingredient
        self.quantity = quantity
        self.price_per_quantity = price_per_quantity
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if self.ingredient in self.ingredients:
            self.ingredients[self.ingredient] += 1
            self.price += self.quantity * self.price_per_quantity
        else:
            self.ingredients[self.ingredient] = 1
            self.price += self.quantity * self.price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        self.ingredient = ingredient
        self.quantity = quantity
        self.price_per_quantity = price_per_quantity
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if self.ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {self.ingredient} in {self.name}!"
        elif self.quantity > self.ingredients[self.ingredient]:
            return f"Please check again the desired quantity of {self.ingredient}!"
        else:
            self.ingredients[self.ingredient] -= self.quantity
            self.price -= self.quantity * self.price_per_quantity

    def make_order(self):
        self.ordered = True
        result = ', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {result} and the price will be {self.price}lv."