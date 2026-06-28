from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> None:
        pass

    @abstractmethod
    def create_evolved() -> None:
        pass
