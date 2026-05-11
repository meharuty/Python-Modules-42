import sys

print("=== Command Quest ===")
print("Program name:", sys.argv[0])
lens = len(sys.argv)
if (lens == 1):
    print("No arguments provided!")
else:
    print("Arguments received:", lens - 1)
    i = 1
    while (i < lens):
        print(f"Argument {i}:", sys.argv[i])
        i += 1
print("Total arguments:", lens)
