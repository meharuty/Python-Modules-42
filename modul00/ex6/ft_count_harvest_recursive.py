def recursive(i, days):
    if i > days:
        return
    print("Day", i)
    recursive(i + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive(1, days)
    print("Harvest time!")
