import sys
import math


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        reports = [[int(level) for level in report.split()] for report in file.read().splitlines()]

    # Iterate through reports and count how many are safe
    safe, dampened = 0, 0
    for report in reports:
        if isSafe(report):
            safe += 1

        for i in range(len(report)):
            if isSafe(report[:i] + report[(i + 1):]):
                dampened += 1
                break

    # Display results
    print(f"Safe Reports: {safe}")
    print(f"Dampened Reports: {dampened}")


def isSafe(report: list[int]) -> bool:
    """Returns True if a report is safe and False if a report is unsafe"""

    # Determine if levels are increasing or decreasing
    slope = math.copysign(1, report[1] - report[0])

    # Iterate through levels checking if each level is safe
    for i, level in enumerate(report[:-1]):
        # Calculate difference between current level and next level
        diff = report[i + 1] - level

        # Report is unsafe if levels are not all increasing or decreasing 
        if math.copysign(1, diff) != slope:
            return False

        # Report is unsafe if adjacent levels differ by less than 1 or more than 3 
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True


if __name__ == "__main__":
    main()
