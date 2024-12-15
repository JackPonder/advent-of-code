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
    score: int = 0,
) -> int:
    """Returns the number of distinct hiking trails that begin at a given trailhead"""

    # Increment score if max height is reached
    if map[head] == 9:
        return score + 1

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
            score = getScore(map, adjacent, score)

    return score


if __name__ == "__main__":
    main()
