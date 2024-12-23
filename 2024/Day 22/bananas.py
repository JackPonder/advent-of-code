import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        numbers = [int(line) for line in file.read().splitlines()]

    # Calculate 2000 new secret numbers for each buyer
    buyers: list[dict[tuple[int, ...], int]] = []
    for num in numbers:
        buyer: dict[tuple[int, ...], int] = {}
        last = num % 10
        changes = (None, None, None, None)
        for _ in range(2000):
            num = getNextSecretNumber(num)
            price = num % 10
            changes = changes[1], changes[2], changes[3], price - last

            if None not in changes and changes not in buyer: # type: ignore
                buyer[changes] = price # type: ignore

            last = price

        buyers.append(buyer)

    # Find all unique sequences that will earn bananas
    sequences = {seq for buyer in buyers for seq in buyer}

    # Iterate through each sequence and find the sequence that gets the most overall bananas
    highest = 0
    for seq in sequences:
        highest = max(sum(buyer.get(seq, 0) for buyer in buyers), highest)

    # Display results
    print(f"Bananas: {highest}")


def getNextSecretNumber(num: int) -> int:
    """Returns the next secret number given an initial number"""

    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216

    return num


if __name__ == "__main__":
    main()
