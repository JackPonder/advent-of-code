import sys

from collections import Counter


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Get number of blinks
    blinks = int(sys.argv[2])

    # Read file data
    with open(infile) as file:
        stones = Counter(int(i) for i in file.read().split())

    # Update stones every blink
    for _ in range(blinks):
        stones = getNextStones(stones)

    # Count number of stones after blinking
    numStones = stones.total()

    # Display results
    print(f"{numStones} Stones")


def getNextStones(stones: Counter[int]) -> Counter[int]:
    """Returns next set of stones after one blink"""

    # Iterate over each unique stone and update them according to blinking rules
    nextStones: Counter[int] = Counter()
    for num, occurrences in stones.items():
        # Stones engraved with 0 are replaced with 1
        if num == 0:
            nextStones[1] += occurrences

        # Stones with even number of digits are split in half
        elif len(str(num)) % 2 == 0:
            mid = len(str(num)) // 2
            nextStones[int(str(num)[mid:])] += occurrences
            nextStones[int(str(num)[:mid])] += occurrences

        # Other stones are multiplied by 2024
        else:
            nextStones[num * 2024] += occurrences

    return nextStones


if __name__ == "__main__":
    main()
