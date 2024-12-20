import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        lines = file.read().splitlines()

        # Iterate through each row and column and count the number of times XMAS appears
        matches = 0
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != "X":
                    continue

                matches += getNumXmas(lines, i, j)

        # Display results
        print(f"Matches: {matches}")
        

def getNumXmas(grid: list[str], i: int, j: int) -> int:
    """Returns the number of times 'XMAS' appears horizontally, vertically, or diagonally in a grid at the point (i, j)"""

    # Search patterns
    patterns = [
        (0, 1), # Horizontal
        (0, -1),
        (1, 0), # Vertical
        (-1, 0),
        (1, 1), # Diagonal
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    # Calculate grid boundaries
    iMax, jMax = len(grid), len(grid[0])

    # Test each pattern and count the number of times XMAS appears
    numMatches = 0
    for iOffset, jOffset in patterns:
        sub = ""
        for magnitude in range(4):
            iNext, jNext = i + (iOffset * magnitude), j + (jOffset * magnitude)
            if not (0 <= iNext < iMax) or not (0 <= jNext < jMax):
                break

            sub += grid[iNext][jNext]
        
        if sub == "XMAS":
            numMatches += 1

    return numMatches


if __name__ == "__main__":
    main()
