from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "Aria", "Leo", "Maya", "Noah", "Zoe",
        "Ethan", "Liam", "Nora", "Ava", "Kai"
        ]

    actions = [
        "attacks", "defends", "heals", "runs", "jumps",
        "casts spell", "collects item", "dodges", "scores", "escapes"
        ]

    i = -1
    while True:
        i += 1
        yield (random.choice(players), random.choice(actions))


print("=== Game Data Stream Processor ===")
g = gen_event()

for i in range(1000):
    tp = (next(g))
    print(f"Event {i}: Player {tp[0]} did action {tp[1]}")

ls = []
a = gen_event()
for i in range(10):
    ls.append(next(a))

print("Built list of 10 events:", ls)
for i in range(10):
    k = random.choice(ls)
    print("Got event from list:", k)
    ls.remove(k)
    print("Remains in list:", ls)
