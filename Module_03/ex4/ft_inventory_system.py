import sys


def maximum(dc: list[int]) -> int:
    max = dc[0]
    for item in dc:
        if (item > max):
            max = item
    return max


def minimum(dc: list[int]) -> int:
    min = dc[0]
    for item in dc:
        if (item < min):
            min = item
    return min


def gain_input(argv: list[str]) -> dict[str, int]:
    dc = {}
    for x in argv[1:]:
        if ":" not in x:
            print(f"Error - invalid parameter '{x}'")
            continue

        item, qty = x.split(":")
        try:
            qty = int(qty)  # type: ignore
        except ValueError as e:
            print(f"Quantity error for 'key': {e}")
            continue

        if item in dc:
            print(f"Redundant item {item} - discarding")
            continue

        dc[item] = int(qty)
    return dc


print("=== Inventory System Analysis ===")

dc = gain_input(sys.argv)

print("Got inventory:", dc)

if (len(dc) > 0):
    sum = 0.0
    quantity = 0

    for item in dc:
        sum += dc[item]

    for item in dc:
        quantity += 1

    print(f"Total quantity of the {quantity} items: {sum}")

    for item in dc:
        print(f"Item {item} represents {round(dc[item]*100/sum, 1)}%")

    max_value = maximum(list(dc.values()))
    min_value = minimum(list(dc.values()))

    for item in dc:
        if (dc[item] == min_value):
            min_item = item

    for item in dc:
        if (dc[item] == max_value):
            max_item = item

    print(f"Item most abundant: {max_item} with quantity {max_value}")
    print(f"Item least abundant: {min_item} with quantity {min_value}")

    dc.update({"magic items": int(1)})

    print(f"Updated inventory: {dc}")
