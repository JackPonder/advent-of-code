import sys
import re


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        lines = file.read().splitlines()

    # Initialize lights grid
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    # Execute each command
    for line in lines:
        # Parse command
        command = re.match(r"\D+", line).group()[:-1] # type: ignore

        # Parse start and end coords
        iStart, jStart, iEnd, jEnd = [int(i) for i in re.findall(r"[0-9]+", line)]

        # Execute command
        for i in range(iStart, iEnd + 1):
            for j in range(jStart, jEnd + 1):
                if command == "turn on":
                    lights[i][j] += 1
                elif command == "turn off":
                    lights[i][j] = max(lights[i][j] - 1, 0)
                elif command == "toggle":
                    lights[i][j] += 2
    
    # Count number on lights turned on
    brightness = sum(sum(row) for row in lights)

    # Display results
    print(f"Part 2: {brightness}")


if __name__ == "__main__":
    main()
