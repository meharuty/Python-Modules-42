class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    a = Plant("Rose", 25, 30)
    b = Plant("Sunflower", 80, 45)
    c = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    a.show()
    b.show()
    c.show()
