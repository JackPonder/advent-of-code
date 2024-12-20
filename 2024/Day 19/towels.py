import sys
import functools


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        firstLine, remainingLines = file.read().split("\n\n")

    # Parse towel patterns and desired designs
    patterns = tuple(firstLine.split(", "))
    designs = remainingLines.splitlines()

    # Calculate number of possible designs and number of different arrangements
    numPossible = 0
    totalArrangements = 0
    for design in designs:
        arrangements = getNumArrangements(design, patterns)
        if arrangements != 0:
            numPossible += 1
            totalArrangements += arrangements

    # Print results
    print(f"Possible Designs: {numPossible}")
    print(f"Total Arrangements: {totalArrangements}")


@functools.cache
def getNumArrangements(design: str, patterns: tuple[str, ...]) -> int:
    """Returns the number of different arrangements of patterns that can be used to create a design"""

    if len(design) == 0:
        return 1

    total = 0
    for pattern in patterns:
        if design.startswith(pattern):
            total += getNumArrangements(design[len(pattern):], patterns)

    return total


if __name__ == "__main__":
    main()
