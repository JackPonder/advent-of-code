import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        data = file.read()

    # Expand file data
    blocks: list[int | None] = []
    for i, num in enumerate(data):
        blocks += [i // 2 if i % 2 == 0 else None] * int(num)

    # Compact data
    fragmentedFiles = fragmented(blocks)
    compactedFiles = compacted(blocks)

    # Calculate checksums
    fragmentedChecksum = sum(i * id for i, id in enumerate(fragmentedFiles) if id is not None)
    compactedChecksum = sum(i * id for i, id in enumerate(compactedFiles) if id is not None)

    # Print results
    print(f"Fragmented Checksum: {fragmentedChecksum}")
    print(f"Compacted Checksum: {compactedChecksum}")


def fragmented(blocks: list[int | None]) -> list[int | None]:
    """Returns list of file blocks after file fragmentation"""

    # Copy file blocks to prevent mutating original data
    blocks = blocks.copy()

    # Fragment data by moving individual blocks from the end to fill in empty spaces
    i = 0
    while i < len(blocks):
        while blocks[i] is None:
            blocks[i] = blocks.pop()

        i += 1

    return blocks


def compacted(blocks: list[int | None]) -> list[int | None]:
    """Returns list of file blocks after file compaction"""

    # Copy file blocks to prevent mutating original data
    blocks = blocks.copy()

    # Compact data by moving whole files from the end to fill in empty spaces
    for id in reversed(range(max(id for id in blocks if id is not None) + 1)):
        length = blocks.count(id)
        old = blocks.index(id)

        for new in range(old):
            if blocks[new:new + length] == [None] * length:
                blocks[new:new + length] = [id] * length
                blocks[old:old + length] = [None] * length
                break

    return blocks


if __name__ == "__main__":
    main()
