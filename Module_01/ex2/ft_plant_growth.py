class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_ = age

    def show(self):
        print(f"{self.name}: {round(self.height, 2)}cm, {self.age_} days old")

    def grow(self):
        self.height += 0.8

    def age(self):
        self.age_ += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    height_1 = plant.height
    plant.show()
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"===Day {i}===")
        plant.grow()
        plant.age()
        plant.show()
    height_2 = plant.height
    h = height_2 - height_1
    print(f"Growth this week: {round(h, 1)}cm")
