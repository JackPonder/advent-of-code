import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        data = file.read()

        # Compact data
        data = compacted(data)

        # Calculate checksum
        checksum = sum(i * num for i, num in enumerate(data))

        # Print results
        print(f"Checksum: {checksum}")


def compacted(data: str) -> list[int]:
    """Returns the compacted version of filesystem"""

    # Expand data
    files: list[int] = []
    for i, num in enumerate(data):
        files += [i // 2 if i % 2 == 0 else -1] * int(num)

    # Compact data by filling in gaps
    i = 0
    while i < len(files):
        while files[i] == -1:
            files[i] = files.pop()

        i += 1

    return files


if __name__ == "__main__":
    main()
