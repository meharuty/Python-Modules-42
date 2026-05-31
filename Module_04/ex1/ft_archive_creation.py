import sys


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename)

        print("---\n")
        content = f.read()
        print(content)
        print("\n---")

        f.close()

        lines = content.split("\n")
        new_cont = ""
        i = 0
        while i < len(lines):
            new_cont += lines[i] + '#'
            if i != len(lines) - 1:
                new_cont += "\n"
            i += 1
        print(f"File '{filename}' closed.\n")

        print("Transform data:")

        print("---\n")
        print(new_cont)
        print("\n---")

        user_input = input("Enter new file name (or empty):")
        if user_input == "":
            print("Not saving data.")
        else:
            m = open(user_input, "w")
            m.write(new_cont)
            m.close()
            print(f"Saving data to '{user_input}'")
            print(f"Data saved in file '{user_input}'.")
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
