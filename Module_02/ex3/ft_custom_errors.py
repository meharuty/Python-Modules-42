class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error",
                 name: str = "garden") -> None:
        self.message = message
        self.name = name
        super().__init__(message)

    def __str__(self) -> str:
        if self.message == "is wilting":
            return f"The {self.name} plant {self.message}!"
        else:
            return f"{self.message} in the {self.name}!"


class PlantError(GardenError):
    def __init__(self, status: str = "Unknown plant error",
                 name: str = "plant") -> None:
        super().__init__(status, name)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error",
                 name: str = "water") -> None:
        super().__init__(message, name)


def check_plant(status: str, name: str) -> None:
    if status == "wilting":
        raise PlantError("is wilting", name)


def check_water(days: int, name: str) -> None:
    if (days > 5):
        raise WaterError("Not enough water", name)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    try:
        print("Testing PlantError...")
        check_plant("wilting", "tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        check_water(7, "tank")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("wilting", "tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(7, "tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print()
    print("All custom error types work correctly!")
