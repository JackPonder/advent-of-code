import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        lines = file.read().splitlines()

    # Iterate through each space and count the number of times XMAS appears
    xmas = 0
    for row, line in enumerate(lines):
        for col in range(len(line)):
            xmas += getNumXmas(lines, row, col)

    # Iterate through each space and count the number of times an X-MAS appears
    crossMas = 0
    for row, line in enumerate(lines[:-2]):
        for col in range(len(line[:-2])):
            area = [line[col:col+3] for line in lines[row:row + 3]]
            if hasXmas(area):
                crossMas += 1

    # Display results
    print(f"XMAS: {xmas}")
    print(f"X-MAS: {crossMas}")


def getNumXmas(grid: list[str], row: int, col: int) -> int:
    """Returns the number of times 'XMAS' appears horizontally, vertically, or diagonally in a grid at a given point"""

    # Calculate grid boundaries
    rowMax = len(grid) 
    colMax = len(grid[0])

    # Test each direction and count the number of times XMAS appears
    xmas = 0
    for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        for i in range(4):
            rowNext, colNext = row + rowOffset * i, col + colOffset * i
            if not (0 <= rowNext < rowMax) or not (0 <= colNext < colMax):
                break

            if grid[rowNext][colNext] != ("XMAS")[i]:
                break
        else:
            xmas += 1

    return xmas


def hasXmas(area: list[str]) -> bool:
    """Returns True if a 3x3 area has an X-MAS, otherwise returns False"""

    line1 = "".join(area[i][i] for i in range(3))
    line2 = "".join(area[i][2 - i] for i in range(3))
    
    return line1 in ("MAS", "SAM") and line2 in ("MAS", "SAM")


if __name__ == "__main__":
    main()
