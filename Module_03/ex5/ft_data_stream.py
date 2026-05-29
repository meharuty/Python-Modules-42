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

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(ls: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while ls:
        k = random.choice(ls)
        ls.remove(k)
        yield k


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
c = consume_event(ls)
for i in range(10):
    k = (next(c))
    print(f"Got event from list: {k}")
    print("Remains in list:", ls)
