import sys
import site
import os


def is_in_venv() -> bool:
    """Whether we are in virtual env or not"""
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


def main() -> None:
    """Display information about the current Python environment."""
    in_venv = is_in_venv()

    if in_venv:
        print("\nMATRIX STATUS: Welcome to the construct\n")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")

    if in_venv:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print(r"matrix_env\Scripts\activate  # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
