from typing import Callable
from typing import Any


def mage_counter() -> Callable:
    m_count = 0

    def self_count() -> int:
        nonlocal m_count
        m_count += 1
        return (m_count)
    return self_count


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def total_power(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return total_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    mem = {}

    def store(key: str, value: Any) -> None:
        mem[key] = value

    def recall(key: str) -> Any:
        if key in mem:
            return mem[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    r1 = mage_counter()
    r2 = mage_counter()
    for i in range(2):
        res1 = r1()
    print(res1)

    for i in range(4):
        res2 = r2()
    print(res2)

    r3 = spell_accumulator(10)
    for i in range(10):
        res3 = r3(i)
    print(res3)

    r4 = enchantment_factory("Flameling")
    res4 = r4("Sword")
    print(res4)

    r5 = memory_vault()
    r5["store"]("weapon", "Sword")
    r5["store"]("spell", "Fireball")
    r5["store"]("level", 42)

    print(r5["recall"]("weapon"))
    print(r5["recall"]("spell"))
    print(r5["recall"]("level"))
    print(r5["recall"]("armor"))


if __name__ == "__main__":
    main()
