class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow = 0
            self.age = 0
            self.show = 0
            self.shade = 0

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
            return True
        else:
            return False

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_} days old")
        self.stat.show += 1


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


class Tree(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height}cm long \
and {self.diameter}cm wide.")
        self.stat.shade += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")


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


def stats(plant: Plant) -> None:
    print(
        f"Stats: {plant.stat.grow} grow, "
        f"{plant.stat.age} age, {plant.stat.show} show"
        )
    if plant.__class__ == Tree:
        print(f"{plant.stat.shade} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    flower1 = Flower("Rose", 15, 10, "red")
    print(f"Is 30 days more than a year? -> {flower1.age_check(30)}")
    print(f"Is 400 days more than a year? -> {flower1.age_check(400)}")
    print()
    print("=== Flower")
    flower1.show()
    print("[statistics for Rose]")
    stats(flower1)
    print("[asking the rose to grow and bloom]")
    flower1.grow(8)
    flower1.bloom()
    flower1.show()
    print("[statistics for Rose]")
    stats(flower1)
    print()

    print("=== Tree")
    tree1 = Tree("Oak", 200, 365, 5)
    tree1.show()
    print("[statistics for Oak]")
    stats(tree1)
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("[statistics for Oak]")
    stats(tree1)
    print()

    print("=== Seed")
    flower2 = Seed("Sunflower", 80, 45, "yellow")
    flower2.show()
    stats(flower2)
    print("[make sunflower grow, age and bloom]")
    flower2.grow(30)
    flower2.age(20)
    flower2.bloom()
    flower2.show()
    print("[statistics for Sunflower]")
    stats(flower2)
    print()

    print("=== Anonymous")
    anonim = Plant.anonymous()
    anonim.show()
    print("[statistics for Unknown plant]")
    stats(anonim)
