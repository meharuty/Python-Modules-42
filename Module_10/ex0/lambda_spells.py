def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mages: mages['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda st: '* ' + st + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2,
        )
    }


def main() -> None:
    a = [
        {
            "name": "Dragon Orb",
            "power": 95,
            "type": "orb",
        },
        {
            "name": "Phoenix Feather",
            "power": 78,
            "type": "ingredient",
        },
        {
            "name": "Crystal Wand",
            "power": 88,
            "type": "weapon",
        },
        {
            "name": "Ancient Tome",
            "power": 65,
            "type": "book",
        },
        {
            "name": "Shadow Dagger",
            "power": 91,
            "type": "weapon",
        },
    ]

    m = [
        {
            "name": "Merlin",
            "power": 98,
            "element": "air",
        },
        {
            "name": "Morgana",
            "power": 85,
            "element": "dark",
        },
        {
            "name": "Gandalf",
            "power": 100,
            "element": "light",
        },
        {
            "name": "Saruman",
            "power": 92,
            "element": "earth",
        },
        {
            "name": "Elminster",
            "power": 76,
            "element": "fire",
        },
    ]

    s = [
        "Fireball",
        "Ice Storm",
        "Lightning Bolt",
        "Heal",
        "Teleport",
    ]

    print(artifact_sorter(artifacts=a))
    print()

    print(power_filter(mages=m, min_power=80))
    print()

    print(spell_transformer(s))
    print()

    print(mage_stats(m))


if __name__ == "__main__":
    main()
