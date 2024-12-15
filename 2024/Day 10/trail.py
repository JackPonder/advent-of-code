import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read map data and find all trail heads
        map: dict[tuple[int, int], int] = {}
        heads: list[tuple[int, int]] = []
        for row, line in enumerate(file.read().splitlines()):
            for col, height in enumerate(line):
                height = int(height)
                map[(row, col)] = height

                if height == 0:
                    heads.append((row, col))

        # Calculate sum of all trail head scores
        score = sum(getScore(map, head) for head in heads)

        # Print results
        print(f"Score: {score}")


def getScore(
    map: dict[tuple[int, int], int], 
    head: tuple[int, int], 
    found: set[tuple[int, int]] | None = None
) -> int:
    """Returns the number of 9-height positions reachable by a trailhead"""

    # Initialize set of 9-height positions on first recursion
    if found is None:
        found = set()

    # Increment score if max height is reached
    if map[head] == 9:
        found.add(head)

    # Adjacent position ofsets
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Iterate through each adjacent space looking for adjacent spaces with gradual height increase
    row, col = head
    for rowOffset, colOffset in offsets:
        # Calculate adjacent space coordinates
        adjacent = row + rowOffset, col + colOffset
        if adjacent not in map:
            continue

        # Traverse adjacent spaces with correct height until max height is reached
        if map[adjacent] == map[head] + 1:
            getScore(map, adjacent, found)

    return len(found)


if __name__ == "__main__":
    main()
