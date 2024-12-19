import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        firstLine, remainingLines = file.read().split("\n\n")

    # Parse towel patterns and desired designs
    patterns = firstLine.split(", ")
    designs = remainingLines.splitlines()

    # Calculate number of possible designs
    numPossible = len([design for design in designs if isPossible(design, patterns)])

    # Print results
    print(f"Possible Designs: {numPossible}")


def isPossible(design: str, patterns: list[str], curr: str = "") -> bool:
    """Returns True is a design is possible to create from a list of patterns, otherwise returns False"""

    if curr == design:
        return True
    
    if not design.startswith(curr):
        return False
    
    return any(isPossible(design, patterns, curr + pattern) for pattern in patterns)


if __name__ == "__main__":
    main()
