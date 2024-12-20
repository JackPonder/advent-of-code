import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        first, second = file.read().split("\n\n")

    # Parse rules and updates
    rules = [[int(i) for i in line.split("|")] for line in first.splitlines()]
    updates = [[int(i) for i in line.split(",")] for line in second.splitlines()]

    # Calculate sum of middle page numbers of the updates
    correct, incorrect = 0, 0
    for update in updates:
        orderedUpdate = ordered(update, rules)
        if update == orderedUpdate:
            correct += orderedUpdate[len(orderedUpdate) // 2]
        else:
            incorrect += orderedUpdate[len(orderedUpdate) // 2]

    # Print results
    print(f"Sum of Correct Pages: {correct}")
    print(f"Sum of Incorrect Pages: {incorrect}")


def ordered(update: list[int], rules: list[list[int]]) -> list[int]:
    """Returns the correctly-ordered version of a given update"""

    # Iterate through each rule and check if the update violates any
    for rule in rules:
        # Ignore rules with pages the update does not have
        before, after = rule
        if before not in update or after not in update:
            continue

        # If a rule is broken, reorder the update to fix it, then recheck if the update is ordered correctly 
        bIndex, aIndex = update.index(before), update.index(after)
        if bIndex > aIndex:
            reorderd = update[:]
            reorderd[bIndex] = after
            reorderd[aIndex] = before
            return ordered(reorderd, rules)

    return update


if __name__ == "__main__":
    main()
