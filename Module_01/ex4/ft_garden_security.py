class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if (height < 0):
            self._height = 0.0
        else:
            self._height = float(height)
        if (age < 0):
            self._age = 0
        else:
            self._age = age

    def set_height(self, sm: float) -> None:
        if (sm >= 0):
            self._height += sm
            print(f"Height updated: {int(self._height)}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days: int) -> None:
        if (days >= 0):
            self._age += days
            print(f"Age updated: {int(self._age)} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"Plant created: {self._name}: \
{self.get_height()}cm, {self.get_age()} days old")

    def show_current(self) -> None:
        print(f"Current state: {self._name}: \
{self.get_height()}cm, {self.get_age()} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    plant.show()
    print()
    plant.set_height(10)
    plant.set_age(20)
    print("")
    plant.set_height(-10)
    plant.set_age(-5)
    print("")
    plant.show_current()
