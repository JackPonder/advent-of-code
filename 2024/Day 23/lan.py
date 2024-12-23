import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        pairs = [line.split("-") for line in file.read().splitlines()]

    # Create graph of all computer connections  
    connections: dict[str, set[str]] = {}
    for (c1, c2) in pairs:
        if c1 not in connections:
            connections[c1] = set()
        if c2 not in connections:
            connections[c2] = set()

        connections[c1].add(c2)
        connections[c2].add(c1)

    # Find all sets of 3 inter-connected computers
    sets: set[tuple[str, ...]] = set()
    for c1 in connections:
        for c2 in connections[c1]:
            for c3 in connections[c2]:
                # Only include sets where all 3 computers are connected to each other
                if c3 not in connections[c1]:
                    continue
                
                # Only include sets where at least one computer's name starts with 't'
                if not any(c.startswith("t") for c in (c1, c2, c3)):
                    continue

                sets.add(tuple(sorted((c1, c2, c3))))

    # Display results
    print(f"Sets: {len(sets)}")


if __name__ == "__main__":
    main()
