import sys
import json


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile, "r") as file:
        data = json.load(file)

    # Calculate sum of all numbers in document
    total = getSumOfAllNumbers(data)

    # Display results
    print(f"Total: {total}")


def getSumOfAllNumbers(data: object) -> int:
    """Returns the sum of all numbers in a JSON document"""

    if isinstance(data, int):
        return data
        
    if isinstance(data, list):
        return sum(getSumOfAllNumbers(i) for i in data)
        
    if isinstance(data, dict):
        return sum(getSumOfAllNumbers(i) for i in data.values())

    return 0


if __name__ == "__main__":
    main()
