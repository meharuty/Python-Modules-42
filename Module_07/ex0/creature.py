from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, typee: str) -> None:
        self.name = name
        self.typee = typee

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.typee} type Creature")


class Flameling(Creature):
    def __init__(self, name, typee):
        super().__init__(name, typee)

    def attack(self) -> str:
        return ("Ember")


class Pyradon(Creature):
    def __init__(self, name, typee):
        super().__init__(name, typee)

    def attack(self) -> str:
        return ("Flamethrower")


class Aquabub(Creature):
    def __init__(self, name, typee):
        super().__init__(name, typee)

    def attack(self) -> str:
        return ("Water Gun")


class Torragon(Creature):
    def __init__(self, name, typee):
        super().__init__(name, typee)

    def attack(self) -> str:
        return ("Hydro Pump")
