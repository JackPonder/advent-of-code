def main() -> None:
    with open("data.txt") as file:
        lines = file.read().splitlines()

        matches = 0
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != "X":
                    continue
                matches += findMatches(lines, i, j)

        print(f"Matches: {matches}")
        

def findMatches(grid: list[str], i: int, j: int) -> int:
    numMatches = 0

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

    iMax, jMax = len(grid), len(grid[0])
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
