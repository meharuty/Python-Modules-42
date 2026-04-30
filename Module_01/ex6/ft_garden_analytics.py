def stats(a1, a2, a3):
    print(f"Stats: {a1} grow, {a2} age, {a3} show")


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age_ = age
        self.stat1 = 0
        self.stat2 = 0
        self.stat3 = 0

    @classmethod
    def anonimous(cls):
        name = "Unknown plant"
        height = 0
        age = 0
        return cls(name, height, age)

    def grow(self, amount):
        self.height += amount
        self.stat1 += 1

    def age(self, days):
        self.age_ += days
        self.stat2 += 1

    @staticmethod
    def age_check(days):
        if (days > 365):
            print(f"Is {days} days more than a year? -> True")
            return True
        else:
            print(f"Is {days} days more than a year? -> False")
            return False

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age_} days old")
        self.stat3 += 1

    def status(self):
        stats(self.stat1, self.stat2, self.stat3)


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

    def status(self):
        super().status()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.diameter = float(trunk_diameter)
        self.stat4 = 0

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}cm long \
and {self.diameter}cm wide.")
        self.stat4 += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")

    def status(self):
        super().status()
        print(f"{self.stat4} shade")


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

    def status(self):
        super().status()


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds += 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

    def status(self):
        super().status()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    flower1 = Flower("Rose", 15, 10, "red")
    flower1.age_check(30)
    flower1.age_check(400)
    print()
    print("=== Flower")
    flower1.show()
    flower1.status()
    flower1.grow(8)
    flower1.bloom()
    flower1.show()
    flower1.status()
    print()

    print("=== Tree")
    tree1 = Tree("Oak", 200, 365, 5)
    tree1.show()
    tree1.status()
    tree1.produce_shade()
    tree1.status()
    print()

    print("=== Seed")
    flower2 = Seed("sunflower", 80, 45, "yellow")
    flower2.show()
    flower2.status()
    flower2.grow(30)
    flower2.age(20)
    flower2.bloom()
    flower2.show()
    flower2.status()
    print()

    print("=== Anonymous")
    anonim = Plant.anonimous()
    anonim.show()
    anonim.status()
