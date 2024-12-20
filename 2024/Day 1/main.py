import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        lines = file.read().splitlines()

    # Populate left and right lists
    left: list[int] = []
    right: list[int] = []
    for line in lines:
        leftNum, rightNum = line.split()
        left.append(int(leftNum))
        right.append(int(rightNum))

    # Sort both lists to calculate distance
    left.sort()
    right.sort()

    # Calculate distance and similarity between both lists
    distance = sum(abs(leftNum - rightNum) for leftNum, rightNum in zip(left, right))
    similarity = sum(num * right.count(num) for num in left)

    # Display results
    print(f"Distance: {distance}")
    print(f"Similarity: {similarity}")


if __name__ == "__main__":
    main()
