import sys
import re


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        data = file.read()
        
        # Search patterns
        mulPattern = r"mul\([0-9]+,[0-9]+\)"
        doPattern = r"do\(\)"
        dontPattern = r"don't\(\)"

        # Find all pattern matches in file data
        matches = ["".join(i) for i in re.findall(f"({mulPattern})|({doPattern})|({dontPattern})", data)]

        # Execute matches
        sum = 0
        enabled = True
        for match in matches:
            if match.startswith("mul") and enabled:
                num1, num2 = match[4:-1].split(",")
                sum += int(num1) * int(num2)
            elif match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False

        # Display results
        print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
