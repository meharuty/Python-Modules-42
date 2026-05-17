import random


def gen_event():
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
        yield (
            f"Event {i}: Player {random.choice(players)} "
            f"did {random.choice(actions)}"
            )


print(gen_event())
