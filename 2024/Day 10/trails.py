import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        lines = file.read().splitlines()

    # Parse map and find all trail heads
    map = {(row, col): int(height) for row, line in enumerate(lines) for col, height in enumerate(line)}
    heads = [pos for pos, height in map.items() if height == 0]

    # Calculate sum of all trail head scores and ratings
    totalScore = sum(getNumHikingTrails(map, head) for head in heads)
    totalRating = sum(getNumHikingTrails(map, head, duplicatesEnds=True) for head in heads)

    # Print results
    print(f"Total Score: {totalScore}")
    print(f"Total Rating: {totalRating}")


def getNumHikingTrails(
    map: dict[tuple[int, int], int], 
    head: tuple[int, int], 
    endings: list[tuple[int, int]] | None = None,
    duplicatesEnds: bool = False,
) -> int:
    """Returns the number hiking trails for a given trailhead"""

    # Initialize list of trail endings on first recursion
    if endings is None:
        endings = []

    # Update list of endings if max height is reached
    if map[head] == 9:
        endings.append(head)

    # Iterate through each adjacent space looking for adjacent spaces with gradual height increase
    for rowOffset, colOffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        # Calculate adjacent space coordinates
        row, col = head
        adjacent = row + rowOffset, col + colOffset
        if adjacent not in map:
            continue

        # Traverse adjacent spaces with correct height until max height is reached
        if map[adjacent] == map[head] + 1:
            getNumHikingTrails(map, adjacent, endings)

    return len(endings if duplicatesEnds else set(endings))


if __name__ == "__main__":
    main()
