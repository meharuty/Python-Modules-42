import sys


if len(sys.argv) != 2:
    sys.stdout.write("Usage: python ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]

    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===")
    sys.stdout.write(f"Accessing file '{filename}'")

    try:
        f = open(filename)

        sys.stdout.write("---\n")
        content = f.read()
        sys.stdout.write(content)
        sys.stdout.write("\n---")

        f.close()

        lines = content.split("\n")
        new_cont = ""
        i = 0
        while i < len(lines):
            new_cont += lines[i] + '#'
            if i != len(lines) - 1:
                new_cont += "\n"
            i += 1

        sys.stdout.write("---\n")
        sys.stdout.write(new_cont)
        sys.stdout.write("\n---")

        sys.stdout.write(f"File '{filename}' closed.")

        sys.stdout.write("Transform data:")
        sys.stdout.write("---\n")

        user_input = sys.stdin.read()
        if user_input == "":
            sys.stdout.write("Not saving data.")
        else:
            m = open(user_input, "w")
            m.write(new_cont)
            m.close()
            sys.stdout.write(f"Saving data to '{user_input}'")
            sys.stdout.write(f"Data saved in '{user_input}'.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}")
