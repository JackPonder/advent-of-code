import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        numbers = [int(line) for line in file.read().splitlines()]

    # Calculate 2000th new secret number for each intial number
    total = 0
    for num in numbers:
        for _ in range(2000):
            num = getNextSecretNumber(num)
        total += num

    # Display results
    print(f"Sum: {total}")


def getNextSecretNumber(num: int) -> int:
    """Returns the next secret number given an initial number"""

    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216

    return num


if __name__ == "__main__":
    main()
