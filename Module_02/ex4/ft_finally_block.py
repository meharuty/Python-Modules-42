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


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
        print()
        print("Testing invalid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
