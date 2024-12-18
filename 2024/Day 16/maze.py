import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read maze data 
        maze: dict[tuple[int, int], str] = {}
        start, end = (0, 0), (0, 0)
        for row, line in enumerate(file.read().splitlines()):
            for col, space in enumerate(line):
                maze[row, col] = space

                if space == "S":
                    start = (row, col)
                elif space == "E":
                    end = (row, col)

        # Calculate lowest possible score for maze
        score = getLowestScore(maze, start, end)

        # Print results
        print(f"Lowest Score: {score}")


def getLowestScore(
    maze: dict[tuple[int, int], str], 
    start: tuple[int, int],
    end: tuple[int, int],
) -> int:
    """Returns the lowest possible score to navigate from start to end in a given maze"""

    # Set initial scores and directions for each node
    unvisited = [pos for pos, val in maze.items() if val != "#"]
    scores = {node: 0 if node == start else sys.maxsize for node in unvisited}
    directions = {node: (0, 1) if node == start else None for node in unvisited}

    # Traverse each node, calculating the shortest path to each adjacent node until all nodes have been searched
    while len(unvisited) != 0:
        # Search unvisited node with lowest score 
        unvisited.sort(key=lambda node: scores[node])
        node = unvisited[0]

        # Iterate through adjacent nodes and update their scores
        for offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # Calculate adjacent node coordinates
            row, col = node
            rowOffset, colOffset = offset
            adjacent = row + rowOffset, col + colOffset

            # Ignore visited nodes
            if adjacent not in unvisited:
                continue

            # Update adjacent node if a shorter path is found
            edge = 1 if directions[node] == offset else 1001
            if scores[node] + edge < scores[adjacent]:
                scores[adjacent] = scores[node] + edge
                directions[adjacent] = offset

        # Mark current node as visited
        unvisited.remove(node)

    return scores[end]


if __name__ == "__main__":
    main()
