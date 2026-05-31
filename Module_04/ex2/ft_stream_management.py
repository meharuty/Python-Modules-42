import sys


if len(sys.argv) != 2:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write("Usage: python ft_ancient_text.py <file>\n")
else:
    filename = sys.argv[1]

    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")

    try:
        f = open(filename)

        sys.stdout.write("---\n\n")
        content = f.read()
        sys.stdout.write(content)
        sys.stdout.write("\n\n---\n")

        f.close()
        sys.stdout.write(f"File '{filename}' closed.\n\n")

        lines = content.split("\n")
        new_cont = ""
        i = 0
        while i < len(lines):
            new_cont += lines[i] + '#'
            if i != len(lines) - 1:
                new_cont += "\n"
            i += 1

        sys.stdout.write("Transform data:\n")
        sys.stdout.write("---\n\n")
        sys.stdout.write(new_cont)
        sys.stdout.write("\n\n---\n")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        user_input = sys.stdin.readline().rstrip("\n")

        if user_input == "":
            sys.stdout.write("\nNot saving data.\n")
        else:
            m = open(user_input, "w")
            m.write(new_cont)
            m.close()
            sys.stdout.write(f"Saving data to '{user_input}'\n")
            sys.stdout.write(f"Data saved in '{user_input}'.\n")
    except Exception as e:
        sys.stdout.write(f"Saving data to '{user_input}'\n")
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stdout.write("Data not saved.\n")
