def input_temperature(temp_str:str) -> int:
    temp_str = int(temp_str)
    if(temp_str > 40):
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    elif (temp_str < 0):
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    return (temp_str)


def test_temperature() -> None:
    print("Input data is '25'")
    print(f"Temperature is now {input_temperature('25')}°C")
    print()
    try:
        print("Input data is 'abc'")
        input_temperature('abc')
    except ValueError:
        print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'")
    print()
    try:
        print("Input data is '100'")
        input_temperature('100')
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print("Input data is '-50'")
        input_temperature('-50')
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")