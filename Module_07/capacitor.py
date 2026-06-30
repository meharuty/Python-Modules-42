from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    base = factory.create_base()
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolved = factory.create_evolved()
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(
        factory: TransformCreatureFactory
        ) -> None:
    print("Testing Creature with transform capability")

    base = factory.create_base()
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    evolved = factory.create_evolved()
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


healing_factory = HealingCreatureFactory()
transform_factory = TransformCreatureFactory()

test_healing(healing_factory)
test_transform(transform_factory)
