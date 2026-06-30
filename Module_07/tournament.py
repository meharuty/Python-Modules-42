from ex0 import FlameFactory, AquaFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import (
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
)


def tournament(opponents: list[tuple]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")

            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as e:
                print(
                    "Battle error, aborting tournament:",
                    e
                )
                return


print("Tournament 0 (basic)")
tournament([
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
])

print("Tournament 1 (error)")
tournament([
    (FlameFactory(), AggressiveStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
])

print("Tournament 2 (multiple)")
tournament([
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy()),
])
