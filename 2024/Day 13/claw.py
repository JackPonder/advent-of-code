import sys
import re


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        machines = file.read().split("\n\n")

    # Iterate through each machine and count the number of tokens spent
    t1, t2 = 0, 0
    for machine in machines:
        # Parse button and prize data
        a, b, (px, py) = [tuple(int(i) for i in re.findall("[0-9]+", line)) for line in machine.splitlines()]

        # Add number of tokens spent at machine to the total
        t1 += getNumTokens(a, b, (px, py)) # type: ignore
        t2 += getNumTokens(a, b, (px + 10000000000000, py + 10000000000000)) # type: ignore

    # Print results
    print(f"Part 1: {t1}")
    print(f"Part 2: {t2}")


def getNumTokens(a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]) -> int:
    """Returns the number of tokens needed to reach the prize, or 0 if the prize is unreachable"""

    # Unpack button and prize data
    ax, ay = a
    bx, by = b
    px, py = prize

    # Calculate number of button presses to reach the prize 
    aPresses = ((px / bx) - (py / by)) / ((ax / bx) - (ay / by))
    bPresses = (px - ax * aPresses) / bx 

    # Prize is reachable if number of A and B presses are integers
    if abs(aPresses - round(aPresses)) < 0.001 and abs(bPresses - round(bPresses)) < 0.001:
        return 3 * round(aPresses) + round(bPresses)

    return 0


if __name__ == "__main__":
    main()
