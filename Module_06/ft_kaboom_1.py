from alchemy.grimoire.dark_spellbook import dark_spell_record

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

spell = "Fantasy"
ingredients = "Earth, wind and fire"

result = dark_spell_record(spell, ingredients)

print(result)
