class Plant:
    def __init__(self, name, height: float, age):
        self._name = name
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0
        else:
            self._height = float(height)
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def set_height(self, sm):
        if (sm >= 0):
            self._height += sm
            print(f"Height updated: {int(self._height)}cm")
        else:
            print("Height update rejected")

    def set_age(self, days):
        if (days >= 0):
            self._age += days
            print(f"Age updated: {int(self._age)} days")
        else:
            print("Age update rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        print(f"Created: {self._name}: \
{self._height}cm, {self._age} days old\n")

    def show_current(self):
        print(f"Current state: {self._name}: \
{self._height}cm, {self._age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    plant.show()
    plant.set_height(10)
    plant.set_age(20)
    print("")
    plant.set_height(-10)
    plant.set_age(-5)
    print("")
    plant.show_current()
