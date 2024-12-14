DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "V": (1, 0),
    "<": (0, -1),
}


def main() -> None:
    with open("data.txt") as file, open("out.txt", "w") as output:
        # Read mapa data into memory
        map = [list(line) for line in file.read().splitlines()]

        # Get new traversed map
        map = traversed(map)

        # Write new map to file
        output.writelines("".join(row) + "\n" for row in map)

        # Get number of guard-occupied positions
        distinctPositions = sum(row.count("X") for row in map)
        
        # Print finding
        print(f"Distinct Positions: {distinctPositions}")
        

def traversed(map: list[list[str]]) -> list[list[str]]:
    # Get guard starting position
    row, col = search(map)

    # Get map boundaries
    rowMax = len(map)
    colMax = len(map[0])

    # Move guard throughout the map until he moves offscreen
    while True:
        # Get next guard position
        rowOffset, colOffset = DIRECTIONS[map[row][col]]
        rowNext, colNext = row + rowOffset, col + colOffset

        # Stop if guard hits map boundary
        if not (0 <= rowNext < rowMax) or not (0 <= colNext < colMax):
            map[row][col] = "X"
            break

        if map[rowNext][colNext] == "#":
            # Turn guard if next space is blocked
            map[row][col] = getNextDirection(map[row][col])
        else:
            # Move guard forward if next space is empty
            map[rowNext][colNext] = map[row][col]
            map[row][col] = "X"
        
            # Update guard position
            row, col = rowNext, colNext
    
    return map


def getNextDirection(current: str) -> str:
    options = list(DIRECTIONS.keys())
    return options[(options.index(current) + 1) % 4]


def search(map: list[list[str]]) -> tuple[int, int]:
    for i, line in enumerate(map):
        for j, space in enumerate(line):
            if space == "^":
                return (i, j)

    raise ValueError("Item not found in list")


if __name__ == "__main__":
    main()
