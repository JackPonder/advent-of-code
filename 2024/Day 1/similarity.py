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
            leftNum, rightNum = [int(i) for i in line.split("   ")]
            left.append(leftNum)
            right.append(rightNum)

        # Calculate similarity between both lists
        similarity = sum(num * right.count(num) for num in left)

        # Display results
        print(f"Similarity: {similarity}")


if __name__ == "__main__":
    main()
