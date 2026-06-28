from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def fight(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    print("Testing battle")
    base_1 = factory_1.create_base()
    base_2 = factory_2.create_base()
    print(base_1.describe())
    print(" vs.")
    print(base_2.describe())
    print(" fight!")
    print(base_1.attack())
    print(base_2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    fight(flame_factory, aqua_factory)
