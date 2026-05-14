def get_player_pos() -> tuple:
    user_input = input()
    tp1 = tuple(user_input.split(','))
    """if (len(tp1) != 3):
        print("Enter coordinates as floats in format 'x,y,z':", user_input)
        print("Invalid syntax")
        return (get_player_pos())"""
    tp = ()
    for x in tp1:
        try:
            tp += (float(x),)   # type: ignore
        except ValueError:
            print("Enter coordinates as floats in format 'x,y,z':", user_input)
            print("Invalid syntax")
            return (get_player_pos())
    return tp


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    tp1 = get_player_pos()
    print("Got a first tuple:", tp1)
    print("It includes:", f"X={tp1[0]}, Y={tp1[1]}, Z={tp1[2]}")
    distance = (tp1[0]**2 + tp1[1]**2 + tp1[2]**2)**0.5
    print("Distance to center:", round(distance, 4))
    print()
    print("Get a second set of coordinates")
    tp2 = get_player_pos()
    distance2 = (
                (tp1[0] - tp2[0])**2 +
                (tp1[1] - tp2[1])**2 +
                (tp1[2] - tp2[2])**2
                )**0.5
    print("Distance between the 2 sets of coordinates:", round(distance2, 4))
