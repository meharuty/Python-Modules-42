import random


def gen_player_achievements() -> set:
    achievements = [
                    'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer'
                    ]
    a = random.randint(1, 10)
    return (set(random.sample(achievements, a)))


print("=== Achievement Tracker System ===")
print()

achievements = {
                    'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer'
                }

Alice = gen_player_achievements()
Bob = gen_player_achievements()
Charlie = gen_player_achievements()
Dylan = gen_player_achievements()
Vazgen = gen_player_achievements()

print("Player Alice:", Alice)
print("Player Bob:", Bob)
print("Player Charlie:", Charlie)
print("Player Dylan:", Dylan)
print("Player Vazgen:", Vazgen)

print()
print(
    "All distinct achievements:", set.union(
        Alice, Bob,
        Charlie, Dylan, Vazgen
        )
        )
print()
print(
    "Common achievements:", set.intersection(
        Alice, Bob,
        Charlie, Dylan, Vazgen
        )
        )
print()
print("Only Alice has:", Alice.difference(Bob, Charlie, Dylan, Vazgen))
print("Only Bob has:", Bob.difference(Alice, Charlie, Dylan, Vazgen))
print("Only Charlie has:", Charlie.difference(Bob, Alice, Dylan, Vazgen))
print("Only Dylan has:", Dylan.difference(Bob, Charlie, Alice, Vazgen))
print("Only Vazgen has:", Vazgen.difference(Bob, Charlie, Dylan, Alice))

print()
print("Alice is missing:", achievements.difference(Alice))
print("Bob is missing:", achievements.difference(Bob))
print("Charlie is missing:", achievements.difference(Charlie))
print("Dylan is missing:", achievements.difference(Dylan))
print("Vazgen is missing:", achievements.difference(Vazgen))
