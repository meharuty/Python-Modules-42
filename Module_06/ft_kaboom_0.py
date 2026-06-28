from alchemy import grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")

spell = "Fantasy"
ingredients = "Earth, wind and fire"

result = grimoire.light_spellbook.light_spell_record(spell, ingredients)

print(result)
