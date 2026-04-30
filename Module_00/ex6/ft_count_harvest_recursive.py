def recursive(i: int, days: int) -> None:
    if i > days:
        return
    print("Day", i)
    recursive(i + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive(1, days)
    print("Harvest time!")
