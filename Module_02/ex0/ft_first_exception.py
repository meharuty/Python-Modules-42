def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("Input data is '25'")
    print(f"Temperature is now {input_temperature('25')}°C")
    print()
    try:
        print("Input data is 'abc'")
        input_temperature('abc')
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
