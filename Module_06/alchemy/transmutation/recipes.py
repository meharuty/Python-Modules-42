import elements
from alchemy import potions
from ..elements import create_air


def lead_to_gold():
    str = (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{potions.strength_potion()}' "
        f"mixed with '{elements.create_fire()}'"
    )
    return (str)
