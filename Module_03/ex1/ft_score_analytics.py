import sys


def main():
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return

    args_list = []
    args_str = sys.argv[1:]
    for x in args_str:
        try:
            args_list += [int(x)]
        except ValueError:
            print("Invalid parameter:", x)
    if (len(args_list) == 0):
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return

    print("Scores processed:", args_list)
    print("Total players:", len(args_list))
    print("Total score:", sum(args_list))
    print("Average score:", sum(args_list) / len(args_list))
    print("High score:", max(args_list))
    print("Low score:", min(args_list))
    print("Score range:", max(args_list) - min(args_list))


main()
