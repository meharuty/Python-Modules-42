import sys


if len(sys.argv) != 2:
    print("Usage: python ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    f = open(filename)

    print("---\n")
    print(f.read())
    print("\n---")

    f.close()
    print(f"File '{filename}' closed.")
