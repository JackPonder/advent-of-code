import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Get number of fallen bytes
    bytesFallen = int(sys.argv[2])

    # Get map bounds
    bound = int(sys.argv[3])

    with open(infile) as file:
        # Read file data
        bytes: list[tuple[int, int]] = []
        for line in file.read().splitlines():
            x, y = line.split(",")
            bytes.append((int(x), int(y)))
            
        # Set up memory space
        map = {(x, y): "#" if (x, y) in bytes[:bytesFallen] else "." for x in range(bound + 1) for y in range(bound + 1)}

        # Calculate minimum number of steps to reach exit
        steps = getFewestSteps(map, (0, 0), (bound, bound))

        # Add more bytes until exit is unreachable
        byte = None
        for i in range(bytesFallen, len(bytes)):
            map[bytes[i]] = "#"
            if getFewestSteps(map, (0, 0), (bound, bound)) == sys.maxsize:
                byte = bytes[i]
                break

        # Print results
        print(f"Steps: {steps}")
        print(f"Byte: {byte}")


def getFewestSteps(map: dict[tuple[int, int], str], start: tuple[int, int], end: tuple[int, int]) -> int:
    """Returns the minimum number of steps to reach the bottom right corner of the given area"""

    # Set inital steps for each node
    unvisited = [start]
    steps = {pos: 0 if pos == start else sys.maxsize for pos, val in map.items() if val != "#"}

    # Traverse each node, calculating the shortest path to each adjacent node until all nodes have been searched
    while len(unvisited) != 0:
        # Get next unvisited node
        node = unvisited.pop(0)
        
        # Search all adjacent nodes
        for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            # Calculate adjacent node coordinates
            row, col = node
            rowOffset, colOffset = offset
            adjacent = row + rowOffset, col + colOffset

            # Ignore adjacent nodes that are outside map boundaries
            if adjacent not in steps:
                continue

            # Update adjacent node if a shorter path is found
            if steps[node] + 1 < steps[adjacent]:
                steps[adjacent] = steps[node] + 1
                unvisited.append(adjacent)

    return steps[end]


if __name__ == "__main__":
    main()
