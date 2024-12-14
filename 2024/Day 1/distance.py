import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        lines = file.read().splitlines()

        # Populate left and right lists
        left: list[int] = []
        right: list[int] = []
        for line in lines:
            leftNum, rightNum = [int(i) for i in line.split()]
            left.append(leftNum)
            right.append(rightNum)

        # Sort both lists
        left.sort()
        right.sort()

        # Calculate distance between both lists
        distance = sum(abs(leftNum - rightNum) for leftNum, rightNum in zip(left, right))

        # Display results
        print(f"Distance: {distance}")


if __name__ == "__main__":
    main()
