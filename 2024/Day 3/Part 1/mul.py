import re


def main() -> None:
    with open("data.txt") as file:
        data = file.read()
        
        matches = re.findall("mul\([0-9]+,[0-9]+\)", data)
        sum = 0
        for match in matches:
            num1, num2 = match[4:-1].split(",")
            sum += int(num1) * int(num2)

        print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
