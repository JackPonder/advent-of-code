import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        firstSection, secondSection = file.read().split("\n\n")

    # Parse map and movements
    map = {(row, col): val for row, line in enumerate(firstSection.splitlines()) for col, val in enumerate(line)}
    movements = secondSection.replace("\n", "")

    # Execute movements
    directions = {"v": (1, 0), ">": (0, 1), "^": (-1, 0), "<": (0, -1)}
    for movement in movements:
        # Calculate next position
        row, col = next(pos for pos, val in map.items() if val == "@")
        rowOffset, colOffset = directions[movement]
        rowNext, colNext = row + rowOffset, col + colOffset

        # Get all obstacles in front of robot until a wall or empty space is reached
        obstacles = [map[row, col]]
        while obstacles[-1] not in (".", "#"):
            obstacles.append(map[rowNext, colNext])
            rowNext += rowOffset
            colNext += colOffset

        # Obstacles are not moved if there is a wall at the end
        if obstacles[-1] == "#":
            continue

        # Move all obstacles in front of robot forward 1 space
        for i in range(len(obstacles)):
            map[row, col] = obstacles[i - 1]
            row += rowOffset
            col += colOffset

    # Calculate sum of boxes' GPS coordinates
    coords = sum(100 * row + col for (row, col), val in map.items() if val == "O")

    # Print results
    print(f"Sum: {coords}")


if __name__ == "__main__":
    main()
