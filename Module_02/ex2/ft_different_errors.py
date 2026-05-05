def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int('abc')
    elif (operation_number == 1):
        6 / 0
    elif (operation_number == 2):
        f = open("no.txt", "r")
        f.read()
    elif (operation_number == 3):
        "mel" + 5   # type: ignore


def test_error_types() -> None:
    try:
        garden_operations(0)
    except (ValueError, TypeError) as e:
        print(f"Caught ValueError: {e}")
    for i in (1, 2, 3, 4):
        try:
            print(f"\nTesting operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(
                f"Caught ValueError: {e}"
                )
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(
                f"Caught FileNotFoundError: {e}"
                )
        except TypeError as e:
            print(
                f"Caught TypeError: {e}"
                )


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
