from . import dark_spellbook


def validate_ingredients(ingredients: str) -> str:
    lst = ingredients.split(",")

    l1 = dark_spellbook.dark_spell_allowed_ingredients()
    t = False
    for i in lst:
        if i in l1:
            t = True
            break
    if t:
        ingredients += " - VALID"
    else:
        ingredients += " - INVALIID"
    return ingredients
