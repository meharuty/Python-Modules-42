class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age_ = age

    def grow(self, amount):
        self.height += amount

    def age(self, days):
        self.age_ += days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age_} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.diameter = float(trunk_diameter)

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}cm long \
and {self.diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount):
        super().grow(amount)
        self.nutritional_value += 1

    def age(self, days):
        super().age(days)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.nutritional_value}")
