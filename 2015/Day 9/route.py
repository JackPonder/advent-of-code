import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        lines = file.read().splitlines()

    # Initialize graph of cities
    graph: dict[str, dict[str, int]] = {}
    for line in lines:
        n1, _, n2, _, dist = line.split()
        if n1 not in graph:
            graph[n1] = {}
        if n2 not in graph:
            graph[n2] = {}

        graph[n1][n2] = int(dist)
        graph[n2][n1] = int(dist)

    # Calculate shortest and longest distances to reach each city
    shortest = getShortestDistance(graph)
    longest = getLongestDistance(graph)

    # Display results
    print(f"Shortest: {shortest}")
    print(f"Longest: {longest}")


def getShortestDistance(
    graph: dict[str, dict[str, int]], 
    path: list[str] | None = None,
) -> int:
    """Returns the shortest possible distance to visit each node in a graph once"""

    # Initialize path on first recursion
    if path is None:
        path = []

    # Calculate distnace traveled once all nodes have been reached
    if len(path) == len(graph):
        return sum(graph[curr][next] for curr, next in zip(path[:-1], path[1:]))

    # Recursively search all possible paths
    shortest = sys.maxsize
    for node in (graph if len(path) == 0 else graph[path[-1]]):
        if node not in path:
            shortest = min(shortest, getShortestDistance(graph, [*path, node]))

    return shortest


def getLongestDistance(
    graph: dict[str, dict[str, int]], 
    path: list[str] | None = None,
) -> int:
    """Returns the longest possible distance to visit each node in a graph once"""

    # Initialize path on first recursion
    if path is None:
        path = []

    # Calculate distnace traveled once all nodes have been reached
    if len(path) == len(graph):
        return sum(graph[curr][next] for curr, next in zip(path[:-1], path[1:]))

    # Recursively search all possible paths
    longest = 0
    for node in (graph if len(path) == 0 else graph[path[-1]]):
        if node not in path:
            longest = max(longest, getLongestDistance(graph, [*path, node]))

    return longest


if __name__ == "__main__":
    main()
