from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper() -> str:
        print(f"Casting {func.__name__} ...")
        start = time.perf_counter()
        res = func()
        print(f"Spell completed in {time.perf_counter() - start:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]  # last positional argument
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    curr_attempt = 0

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper() -> str:
            nonlocal curr_attempt
            while (curr_attempt < max_attempts):
                try:
                    result = func()
                    curr_attempt = 0
                    return result
                except Exception:
                    curr_attempt += 1
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {curr_attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (len(name) > 2 and
                all(char.isalpha() or char.isspace() for char in name)):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        return "Fireball cast!"
    print(fireball())

    @power_validator(10)
    def func2(power: int) -> int:
        return power * power
    print(func2(15))

    attempts = 0

    @retry_spell(3)
    def unstable_spell() -> str:
        nonlocal attempts

        attempts += 1

        if attempts < 3:
            raise Exception("Spell failed")

        return "Spell casting failed after 3 attempts"

    print(unstable_spell())
    print()

    obj = MageGuild()
    print(obj.validate_mage_name("ab"))
    print(obj.validate_mage_name("abc"))
    print(obj.cast_spell('fireball', 15))
    print(obj.cast_spell('fireball', 8))


if __name__ == "__main__":
    main()
