import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Get number of blinks
    blinks = int(sys.argv[2])

    with open(infile) as file:
        # Read file data
        stones = [int(stone) for stone in file.read().split()]

        # Update stones every blink
        for _ in range(blinks):
            stones = getNewStones(stones)

        # Display results
        print(f"{len(stones)} Stones")


def getNewStones(stones: list[int]) -> list[int]:
    """Returns new stones after blinking once"""

    # Iterate over every stone and update them according to rules
    new: list[int] = []
    for stone in stones:
        # Stones engraved with 0 are replaced with 1
        if stone == 0:
            new.append(1)

        # Stones with even number of digits are split in half
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            new.append(int(str(stone)[:mid]))
            new.append(int(str(stone)[mid:]))

        # Other stones are multiplied by 2024
        else:
            new.append(stone * 2024)

    return new


if __name__ == "__main__":
    main()
