import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

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
    numCheats = 0
    for i, (x, y) in enumerate(path):
        for (c1x, c1y) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if map.get((c1x, c1y)) != "#":
                continue

            for (c2x, c2y) in [(c1x + 1, c1y), (c1x, c1y + 1), (c1x - 1, c1y), (c1x, c1y - 1)]:
                if (c2x, c2y) not in path:
                    continue

                saved = (path.index((c2x, c2y)) - i) - 2
                if saved >= 100:
                    numCheats += 1

    # Display results
    print(f"Cheats: {numCheats}")


def getPath(
    map: dict[tuple[int, int], str], 
    start: tuple[int, int], 
    end: tuple[int, int],
) -> list[tuple[int, int]]:
    """Returns a list of spaces that represents a path between start and end spaces on a map"""

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


if __name__ == "__main__":
    main()
