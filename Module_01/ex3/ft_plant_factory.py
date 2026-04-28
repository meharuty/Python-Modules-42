class Plant:
    def __init__(self, name, height: float, age):
        self.name = name
        self.height = float(height)
        self.age_ = age

    def show(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age_} days old")


if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Oak", 200, 365)
    plant_3 = Plant("Cactus", 5, 90)
    plant_4 = Plant("Sunflower", 80, 45)
    plant_5 = Plant("Fern", 15, 120)
    print("=== Garden Factory Output ===")
    plant_1.show()
    plant_2.show()
    plant_3.show()
    plant_4.show()
    plant_5.show()
