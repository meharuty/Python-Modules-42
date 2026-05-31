import sys


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename)
        print("---\n")
        print(f.read())
        print("\n---")
        f.close()
        print(f"File '{filename}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
