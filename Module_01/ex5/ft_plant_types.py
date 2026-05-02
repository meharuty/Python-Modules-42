class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age_ = age

    def grow(self, amount: float) -> None:
        self.height += amount

    def age(self, days: int) -> None:
        self.age_ += days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_} days old")


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
            self, name: str, height: float, age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height}cm long \
and {self.diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float, age: int,
            harvest_season: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5, 10, "April")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    vegetable.grow(42)
    vegetable.age(20)
    vegetable.show()
