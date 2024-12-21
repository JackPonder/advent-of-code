import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read map data
    with open(infile) as file:
        map = {(row, col): val for row, line in enumerate(file.read().splitlines()) for col, val in enumerate(line)}

    # Calculate the number of antinodes on the map
    antinodes = getAntinodes(map)
    updatedAntinodes = getAntinodes(map, extended=True)

    # Print results
    print(f"Antinodes: {antinodes}")
    print(f"Updated Antinodes: {updatedAntinodes}")


def getAntinodes(map: dict[tuple[int, int], str], extended: bool = False) -> int:
    """Returns the number of antinodes on a map"""

    # Get all antenna locations
    antennas = [pos for pos, val in map.items() if val != "."]

    # Iterate through each antenna location add up the number of unique antinodes 
    antinodes: set[tuple[int, int]] = set()
    for l1 in antennas:
        for l2 in antennas:
            # Antennas do not form antinodes with themselves
            if l1 == l2:
                continue

            # Antennas with different frequencies do not form antinodes
            if map[l1] != map[l2]:
                continue

            # Calculate antinode locations until antinodes fall outside map boundaries
            r1, c1 = l1
            r2, c2 = l2
            dr, dc = r2 - r1, c2 - c1
            magnitude = 0
            while True:
                a1 = r1 - dr * magnitude, c1 - dc * magnitude
                a2 = r2 + dr * magnitude, c2 + dc * magnitude

                if a1 not in map and a2 not in map:
                    break

                if magnitude == 1 or extended:
                    if a1 in map:
                        antinodes.add(a1)
                    elif a2 in map:
                        antinodes.add(a2)

                magnitude += 1

    return len(antinodes)


if __name__ == "__main__":
    main()
