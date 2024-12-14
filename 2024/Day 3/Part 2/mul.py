import re


def main() -> None:
    with open("data.txt") as file:
        # Read data
        data = file.read()
        
        # Search patterns
        mulPattern = "mul\([0-9]+,[0-9]+\)"
        doPattern = "do\(\)"
        dontPattern = "don't\(\)"

        # Find all pattern matches
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

        # Display sum
        print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
