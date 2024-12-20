import sys

from collections import Counter


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        firstLine, remainingLines = file.read().split("\n\n")

    # Parse towel patterns and desired designs
    patterns = firstLine.split(", ")
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


def getNumArrangements(
    design: str, 
    patterns: list[str], 
    cache: Counter[str] | None = None,
) -> int:
    """Returns the number of different arrangements of patterns that can be used to create a design"""

    # Initialize cache if none is given
    if cache is None:
        cache = Counter({"": 1})

    # Return cached result if it exists
    if design in cache:
        return cache[design]

    # Recursively add up number of possible arrangements
    for pattern in patterns:
        if design.startswith(pattern):
            cache[design] += getNumArrangements(design[len(pattern):], patterns, cache)

    return cache[design]


if __name__ == "__main__":
    main()
