import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Get max cheat duration
    maxCheat = int(sys.argv[2])

    # Read file data
    with open(infile) as file:
        lines = file.read().splitlines()

    # Set map and find start and end spaces
    map = {(x, y): val for y, line in enumerate(lines) for x, val in enumerate(line)}
    start = next(pos for pos, val in map.items() if val == "S")
    end = next(pos for pos, val in map.items() if val == "E")

    # Find path from start to end
    path = getPath(map, start, end)

    # Iterate through each space in the path, counting the number of cheats that save 100 steps
    numCheats = sum(getNumCheats(path, pos, maxCheat) for pos in path)

    # Display results
    print(f"Cheats: {numCheats}")


def getPath(
    map: dict[tuple[int, int], str], 
    start: tuple[int, int], 
    end: tuple[int, int],
) -> list[tuple[int, int]]:
    """Returns the path between start and end spaces on a map"""

    # Path starts at beginning space
    path = [start]

    # Search adjacent spaces until end is reached
    while path[-1] != end:
        x, y = path[-1]
        for adjacent in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            # Ignore spaces already in path
            if adjacent in path:
                continue

            # Add next empty space to the path
            if map.get(adjacent) != "#":
                path.append(adjacent)
                break

    return path


def getNumCheats(
    path: list[tuple[int, int]],
    start: tuple[int, int],
    maxCheat: int,
) -> int:
    """Returns number of viable cheats that begin at a given start position on the map"""

    # Unpack start space
    x, y = start

    # Find all possible spaces a cheat can end
    numCheats = 0
    for dx in range(-maxCheat, maxCheat + 1):
        for dy in range(-maxCheat, maxCheat + 1):
            # Ending space must be reachable within max cheat duration
            duration = abs(dx) + abs(dy)
            if duration > maxCheat:
                continue

            # Cheats must end on the path
            end = (x + dx, y + dy)
            if end not in path:
                continue

            # Only include cheats that save 100 steps or more
            saved = path.index(end) - path.index(start) - duration
            if saved >= 100:
                numCheats += 1

    return numCheats


if __name__ == "__main__":
    main()
