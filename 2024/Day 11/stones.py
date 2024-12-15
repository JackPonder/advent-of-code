import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Get number of blinks
    blinks = int(sys.argv[2])

    with open(infile) as file:
        # Read file data
        stones: dict[int, int] = {}
        for num in file.read().split():
            num = int(num)
            if num not in stones:
                stones[num] = 0
            stones[num] += 1

        # Update stones every blink
        for _ in range(blinks):
            stones = getNextStones(stones)

        # Count number of stones after blinking
        numStones = sum(i for i in stones.values())

        # Display results
        print(f"{numStones} Stones")


def getNextStones(stones: dict[int, int]) -> dict[int, int]:
    """Returns next set of stones after one blink"""

    # Iterate over each unique stone and update them according to blinking rules
    nextStones: dict[int, int] = {}
    for num, occurrences in stones.items():
        # Keep track of new stones created
        replacements: list[int] = []

        # Stones engraved with 0 are replaced with 1
        if num == 0:
            replacements.append(1)

        # Stones with even number of digits are split in half
        elif len(str(num)) % 2 == 0:
            mid = len(str(num)) // 2
            replacements.append(int(str(num)[:mid]))
            replacements.append(int(str(num)[mid:]))

        # Other stones are multiplied by 2024
        else:
            replacements.append(num * 2024)

        # Update new stones with replacements
        for newNum in replacements:
            if newNum not in nextStones:
                nextStones[newNum] = 0
            nextStones[newNum] += occurrences

    return nextStones


if __name__ == "__main__":
    main()
