class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow = 0
            self.age = 0
            self.show = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age_ = age
        self.stat = Plant.Stats()

    @classmethod
    def anonymous(cls) -> "Plant":
        name = "Unknown plant"
        height = 0.0
        age = 0
        return cls(name, height, age)

    def grow(self, amount: float) -> None:
        self.height += amount
        self.stat.grow += 1

    def age(self, days: int) -> None:
        self.age_ += days
        self.stat.age += 1

    @staticmethod
    def age_check(days: int) -> bool:
        if (days > 365):
            print(f"Is {days} days more than a year? -> True")
            return True
        else:
            print(f"Is {days} days more than a year? -> False")
            return False

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_} days old")
        self.stat.show += 1

    def status(self) -> None:
        stats(self)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def status(self) -> None:
        super().status()


class Tree(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.diameter = float(trunk_diameter)
        self.stat4 = 0

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height}cm long \
and {self.diameter}cm wide.")
        self.stat4 += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")

    def status(self) -> None:
        super().status()
        print(f"{self.stat4} shade")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, harvest_season: str
            ) -> None:
        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def status(self) -> None:
        super().status()


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

    def status(self) -> None:
        super().status()


def stats(plant: Plant) -> None:
    print(
        f"Stats: {plant.stat.grow} grow,"
        f"{plant.stat.age} age, {plant.stat.show} show"
        )


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
    anonim = Plant.anonymous()
    anonim.show()
    anonim.status()
