def light_spell_allowed_ingredients() -> list[str]:
    return (["earth", "air", "fire", "water"])


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from . import light_validator
    validation_status = light_validator.validate_ingredients(ingredients)

    if "VALID" in validation_status:
        return f"Spell recorded: {spell_name} ({validation_status})"
    else:
        return f"Spell rejected: {spell_name} ({validation_status})"
