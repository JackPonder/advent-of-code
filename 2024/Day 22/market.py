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
            num = ((num * 64) ^ num) % 16777216
            num = ((num // 32) ^ num) % 16777216
            num = ((num * 2048) ^ num) % 16777216
        total += num

    # Display results
    print(f"Sum: {total}")


if __name__ == "__main__":
    main()
