def strenght_potion() -> str:
    from elements import create_fire, create_water
    return (
        f"Strength potion brewed with and \
        '{create_fire()}' and '{create_water()}'"
        )


def healing_potion() -> str:
    from .elements import create_air, create_earth
    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
        )
