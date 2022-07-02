class Glass:
    capacity = 250
    def __init__(self) -> None:
        self.content = 0

    def fill(self, ml):
        self.ml = ml
        if self.content + self.ml < self.capacity:
            self.content += self.ml
            self.capacity -= self.ml
            return f"Glass filled with {self.ml} ml"
        else:
            return f"Cannot add {self.ml} ml"

    def empty(self):
        self.content = 0
        self.capacity = 250
        return "Glass is now empty"

    def info(self):
        self.capacity = 250
        space_left = self.capacity - self.content
        return f"{space_left}"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())