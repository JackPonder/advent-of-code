def main() -> None:
    with open("data.txt") as file:
        # Read map data into memory
        map = [list(line) for line in file.read().splitlines()]

        # Traverse map
        traverse(map)

        # Get number of guard-occupied positions
        distinctPositions = sum(row.count("X") for row in map)
        
        # Print findings
        print(f"Distinct Positions: {distinctPositions}")
        

def traverse(map: list[list[str]]) -> None:
    # Get guard starting position
    row, col = getGuardPosition(map)

    # Get map boundaries
    rowMax = len(map)
    colMax = len(map[0])

    # Set starting direction
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0

    # Move guard throughout the map until he moves offscreen
    while True:
        # Get next guard position
        rowOffset, colOffset = DIRECTIONS[direction]
        rowNext, colNext = row + rowOffset, col + colOffset

        # Stop if guard hits map boundary
        if not (0 <= rowNext < rowMax) or not (0 <= colNext < colMax):
            map[row][col] = "X"
            break

        if map[rowNext][colNext] == "#":
            # Turn guard if next space is blocked
            direction = (direction + 1) % 4
        else:
            # Move guard forward if next space is empty
            map[rowNext][colNext] = map[row][col]
            map[row][col] = "X"
        
            # Update guard position
            row, col = rowNext, colNext


def getGuardPosition(map: list[list[str]]) -> tuple[int, int]:
    for i, line in enumerate(map):
        for j, space in enumerate(line):
            if space == "^":
                return (i, j)

    raise ValueError("Item not found in list")


if __name__ == "__main__":
    main()
