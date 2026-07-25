from functools import reduce, singledispatch
import operator
from typing import Callable, Any
from functools import partial, lru_cache


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError("Unknown operation")
    func = operations[operation]
    return reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    el_earth = partial(base_enchantment, 50, 'earth')
    el_water = partial(base_enchantment, 50, 'water')
    el_fire = partial(base_enchantment, 50, 'fire')
    return {
        "earth_enchant": el_earth,
        "water_enchant": el_water,
        "fire_enchant": el_fire
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if (n < 2):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def A(value: int) -> str:
        return f"Damage spell: {value} damage"

    @spell.register(str)
    def B(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register(list)
    def C(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return spell


def main() -> None:
    lst1 = [1, 2, 3, 4, 5, 6]
    r1 = spell_reducer(lst1, "min")
    print(r1)

    def func2(power: int, element: str, target: str) -> str:
        return (f"The power of {element} for hitting {target} is {power}")

    d2 = partial_enchanter(func2)
    print(d2["earth_enchant"]("sword"))
    print(d2["water_enchant"]("sword"))
    print(d2["fire_enchant"]("sword"))

    print(memoized_fibonacci(7))

    r4 = spell_dispatcher()
    print(r4(42))
    print(r4("fireball"))
    print(r4(lst1))
    print(r4(258.45))


if __name__ == "__main__":
    main()
