def secure_archive(filename: str, mode: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(filename) as f:
                return (True, f.read())

        elif mode == "write":
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")

    except FileNotFoundError:
        return (False, f"[Errno 2] No such file or directory: '{filename}'")
    except PermissionError:
        return (False, f"[Errno 13] Permission denied: '{filename}'")
    if (mode == "read"):
        return (True, f.read())
    else:
        f.write(content)
        return (True, "Content successfully written to file")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    tp = secure_archive("c.txt", 'read')
    print(tp)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    tp = secure_archive("mn", "read")
    print(tp)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    tp = secure_archive("a.txt", "read")
    print(tp)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    tp = secure_archive("a.txt", "write", "Melin")
    print(tp)
