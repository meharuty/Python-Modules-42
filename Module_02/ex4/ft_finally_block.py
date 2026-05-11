class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error",
                 name: str = "garden") -> None:
        self.message = message
        self.name = name
        super().__init__(message)

    def __str__(self) -> str:
        return f"{self.message} '{self.name}'"


class PlantError(GardenError):
    def __init__(self, status: str = "Unknown plant error",
                 name: str = "plant") -> None:
        super().__init__(status, name)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError("Invalid plant name to water:", plant_name)


def test_watering_system(ls: list[str]) -> None:
    print("Opening watering system")
    try:
        for item in ls:
            water_plant(item)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    ls1 = ["Tomato", "Lettuce", "Carrots"]
    ls2 = ["Tomato", "lettuce", "Carrots"]
    print("Testing valid plants...")
    test_watering_system(ls1)
    print()
    print("Testing invalid plants...")
    test_watering_system(ls2)
    print()
    print("Cleanup always happens, even with errors!")
