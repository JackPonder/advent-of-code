import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        lines = file.read().splitlines()

    # Iterate over each line and calculate sum of possible test values 
    c1, c2 = 0, 0
    for line in lines:
        # Parse test value and operands
        div = line.index(":")
        test = int(line[:div])
        operands = [int(i) for i in line[(div + 1):].split()]

        # Add test value to calibration result if test value is possible 
        if isPossible(test, operands):
            c1 += test
        if isPossible(test, operands, concat=True):
            c2 += test

    # Print results
    print(f"Calibration: {c1}")
    print(f"Calibration (w/ Concat): {c2}")


def isPossible(test: int, operands: list[int], concat: bool = False) -> bool:
    """Returns True if test value is reachable from list of operands, otherwise returns False"""

    # If current value is over test value, test value will not be reached
    if operands[0] > test:
        return False

    # Once all operands have been used, check if test value was reached
    if len(operands) == 1:
        return operands[0] == test

    # Recursively search all operator combinations to determine if test value is reachable
    return (
        isPossible(test, [operands[0] + operands[1], *operands[2:]], concat) or 
        isPossible(test, [operands[0] * operands[1], *operands[2:]], concat) or
       (isPossible(test, [int(str(operands[0]) +  str(operands[1])), *operands[2:]], concat) if concat else False)
    )


if __name__ == "__main__":
    main()
