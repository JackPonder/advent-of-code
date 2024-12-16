import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        data = file.read()

        # Parse rules and updates
        sep = data.index("\n\n")
        rules = [[int(i) for i in line.split("|")] for line in data[:sep].splitlines()]
        updates = [[int(i) for i in line.split(",")] for line in data[(sep + 2):].splitlines()]

        # Calculate sum of middle page numbers of correctly ordered updates
        total = sum(update[len(update) // 2] for update in updates if isOrdered(update, rules))

        # Print results
        print(f"Sum of Correctly-Ordered Pages: {total}")


def isOrdered(update: list[int], rules: list[list[int]]) -> bool:
    """Returns True if a given update follow all rules, otherwise returns False"""

    # Iterate through each rule and check if the update violates any
    for rule in rules:
        # Ignore rules with pages the update does not have
        before, after = rule
        if before not in update or after not in update:
            continue

        # If a before page does not precede its after page, the update does is not in the correct order 
        if update.index(before) > update.index(after):
            return False

    return True


if __name__ == "__main__":
    main()
