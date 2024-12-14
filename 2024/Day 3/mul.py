import sys
import re


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        data = file.read()
        
        # Find all occurances of multiplication functions
        matches = re.findall(r"mul\([0-9]+,[0-9]+\)", data)

        # Iterate through matches and add up result of multiplications 
        sum = 0
        for match in matches:
            num1, num2 = match[4:-1].split(",")
            sum += int(num1) * int(num2)

        # Display results
        print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
