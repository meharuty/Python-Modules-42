from typing import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, word: str) -> tuple[Callable, Callable]:
        return ((spell1(target, word), spell2(target, word)))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> int:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if (condition(target, power)):
            return (spell(target, power))
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def union_seq(target: str, power: int) -> list[Any]:
        res = []
        for spell in spells:
            res.append(spell(target, power))
        return res
    return union_seq


def main() -> None:
    def sp1(target: str, word: str) -> str:
        return (f"Fireball {word} {target}")

    def sp2(target: str, word: str) -> str:
        return (f"{word} {target}")

    print("Testing spell combiner...")
    r1 = spell_combiner(spell1=sp1, spell2=sp2)
    print("Combined spell result:", r1("Heals", "Dragon"))
    print()

    def fireball(target: str, power: int) -> str:
        return f"{target} has {power} power"

    print("Testing power amplifier...")
    r2 = power_amplifier(fireball, 3)
    print("Original:", fireball("Fireball", 10))
    print("Amplified", r2("Fireball", 10))
    print()

    def cond(target: str, power: int) -> bool:
        if power >= 30 and target == 'Fireball':
            return True
        return False

    def sp3(target: str, power: int) -> str:
        return (f"{target} has power {power}")

    print("Testing conditional caster...")
    r3 = conditional_caster(condition=cond, spell=sp3)

    print(r3("Fireball", 10))
    print(r3("Fireball", 40))
    print()

    ls = [sp1, sp2]

    print("Testing spell sequence...")
    r4 = spell_sequence(ls)
    print(r4('Dragon', 15))


if __name__ == "__main__":
    main()
