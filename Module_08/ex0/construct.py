import sys
import site


def is_in_venv():
    """Whether we are in virtual env or not"""
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


if __name__ == "__main__":
    print()
    is_venv = is_in_venv()
    if not is_venv:
        print(
            "MATRIX STATUS: You're still plugged in"
            )
    else:
        print("MATRIX STATUS: Welcome to the construct")
    package_paths = site.getsitepackages()

    print()
    print("Current Python:", package_paths)
    if not is_venv:
        print("Virtual Environment: None detected")
    else:
        print("Virtual Environment: matrix_env")
        print("Environment Path:", package_paths)
