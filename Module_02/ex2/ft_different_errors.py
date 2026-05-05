def garden_operations(operation_number: int) -> str:
    if (operation_number == 0):
        int('abc')
    elif(operation_number == 1):
        x = 6 / 0
    elif (operation_number == 2):
        f = open("no.txt", "r")
        f.read()
        f.close()
    elif(operation_number == 3):
        "mel" + 5
    else:
        return "Operation completed successfully"


def test_error_types():
    for i in range (5):
        try:
            print(f"\nTesting operation {i}...")
            result = garden_operations(i)
            if result:
                print(result)
        except ValueError:
            print("Caught ValueError: invalid literal for int() with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'")
        except TypeError:
            print('Caught TypeError: can only concatenate str (not "int") to str')


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")