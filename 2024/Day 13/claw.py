import sys
import re
import math


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        machines = file.read().split("\n\n")

        # Iterate through each machine and count the number of tokens spent at each
        total = 0
        for machine in machines:
            # Parse button and prize data
            a, b, prize = [tuple(int(i) for i in re.findall("[0-9]+", line)) for line in machine.splitlines()]

            # Add number of tokens spent at machine to the total if prize is reachable
            tokens = getTokens(a, b, prize) # type: ignore
            if tokens is not None:
                total += tokens

        # Display results
        print(f"Tokens: {total}")


def getTokens(a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]) -> int | None:
    """Returns the minimum number of tokens needed to reach the prize, or None if the prize is unreachable"""

    # Button and prize data
    px, py = prize
    dxa, dya = a
    dxb, dyb = b

    # Look for prize solutions until each button has been pressed 100 times
    minTokens = math.inf
    for i in range(101):
        if (px % dxb == 0) and (px / dxb) == (py / dyb):
            minTokens = min(minTokens, i * 3 + px // dxb)

        px, py = px - dxa, py - dya

    return int(minTokens) if minTokens != math.inf else None


if __name__ == "__main__":
    main()
