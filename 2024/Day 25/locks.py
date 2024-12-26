import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        schematics = [section.splitlines() for section in file.read().split("\n\n")]

    # Parse lock and key data
    locks: list[list[int]] = []
    keys: list[list[int]] = []
    for schem in schematics:
        heights = [0 for _ in range(len(schem[0]))]
        for i in range(1, len(schem) - 1):
            for j in range(len(schem[0])):
                if schem[i][j] == "#":
                    heights[j] += 1

        if schem[0][0] == "#":
            locks.append(heights)
        else:
            keys.append(heights)

    # Try every key with every lock and count the number of non-overlapping pairs
    pairs = 0
    for lock in locks:
        for key in keys:
            if all(lh + kh <= 5 for lh, kh in zip(lock, key)):
                pairs += 1

    # Display results
    print(f"Pairs: {pairs}")


if __name__ == "__main__":
    main()
