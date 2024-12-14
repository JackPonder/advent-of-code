import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        reports = file.read().splitlines()

        # Iterate through reports and count the number of safe reports
        numSafe = 0
        for report in reports:
            levels = [int(i) for i in report.split()]
            if isSafe(levels):
                numSafe += 1

        # Display results
        print(f"Safe Reports: {numSafe}")


def isSafe(report: list[int]) -> bool:
    """Returns True if a report is safe, otherwise returns False"""

    # Determine if levels are increasing or decreasing
    change = sign(report[1] - report[0])

    # Iterate through levels checking if each level is safe
    for i, level in enumerate(report[:-1]):
        # Report is unsafe if levels are not all increasing or decreasing 
        if sign(report[i + 1] - level) != change:
            return False

        # Report is unsafe if adjacent levels differ by less than 1 or more than 3 
        if not (1 <= abs(report[i + 1] - level) <= 3):
            return False

    return True


def sign(n: int) -> int:
    """Returns 1 is n is positive, -1 if n is negative, and 0 if n is 0"""

    if n > 0:
        return 1
    if n < 0:
        return -1

    return 0


if __name__ == "__main__":
    main()
