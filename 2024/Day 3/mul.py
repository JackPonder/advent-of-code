import sys
import re


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        memory = file.read()

    # Search through memory and execute instructions
    s1, s2 = 0, 0
    enabled = True
    for i in range(len(memory)):
        if match := re.match(r"mul\([0-9]+,[0-9]+\)", memory[i:]):
            num1, num2 = match.group()[4:-1].split(",")
            s1 += int(num1) * int(num2)
            if enabled:
                s2 += int(num1) * int(num2)
        elif re.match(r"do\(\)", memory[i:]):
            enabled = True
        elif re.match(r"don't\(\)", memory[i:]):
            enabled = False

    # Display results
    print(f"Part 1: {s1}")
    print(f"Part 2: {s2}")


if __name__ == "__main__":
    main()
