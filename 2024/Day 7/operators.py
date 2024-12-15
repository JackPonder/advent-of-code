import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        lines = file.read().splitlines()
        
        # Iterate over each line and calculate sum of possible test values 
        calibration = 0
        for line in lines:
            # Parse test value and operands
            div = line.index(":")
            test = int(line[:div])
            operands = [int(i) for i in line[(div + 1):].split()]

            # Add test value to calibration result if test value is possible 
            if isPossible(test, operands):
                calibration += test

        # Print results
        print(f"Calibration Result: {calibration}")


def isPossible(test: int, operands: list[int], curr: int | None = None) -> bool:
    """Returns True if test value is reachable from list of operands, otherwise returns False"""

    # On first recursion, set current value to first operand
    if curr is None:
        curr = operands.pop(0)

    # If current value matches test value, test value was reached
    if curr == test:
        return True

    # If current value goes over test value or all operands have been used, test value was not reached
    if curr > test or len(operands) == 0:
        return False

    # Recursively search all operator combinations to determine if test value is reachable
    return isPossible(test, operands[1:], curr + operands[0]) or isPossible(test, operands[1:], curr * operands[0])


if __name__ == "__main__":
    main()
