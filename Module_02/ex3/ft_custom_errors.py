class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)