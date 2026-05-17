import random


print("=== Game Data Alchemist ===\n")
players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
        ]

print("Initial list of players:", players)

pl_capitalized = [x.capitalize() for x in players]
print("New list with all names capitalized:", pl_capitalized)

only_cap = [x for x in players if x == x.capitalize()]
print("New list of capitalized names only:", only_cap)
print()
scores = {x: random.randint(0, 1000) for x in pl_capitalized}
print("Score dict:", scores)

average = sum(scores.values())/len(scores)
print(f"Score average is {round(average, 2)}")
highest = {x: scores[x] for x in scores if scores[x] > average}
print("High scores:", highest)
