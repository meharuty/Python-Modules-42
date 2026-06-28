import alchemy

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potio)ns")
print("Testing strength_potion:", alchemy.potions.strength_potion())
print("Testing heal alias:", alchemy.heal())   # type: ignore
