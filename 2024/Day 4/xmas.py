import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        lines = file.read().splitlines()

        # Iterate through each row and column and count the number of times an X-MAS appears
        matches = 0
        for i, line in enumerate(lines[:-2]):
            for j, _ in enumerate(line[:-2]):
                area = [i[j:j+3] for i in lines[i:i + 3]]
                if hasXmas(area):
                    matches += 1

        # Display results
        print(f"Matches: {matches}")
        

def hasXmas(area: list[str]) -> bool:
    """Returns True if a 3x3 area has an X-MAS, otherwise False"""

    sub1 = "".join(area[i][i] for i in range(3))
    if sub1 not in ("MAS", "SAM"):
        return False
    
    sub2 = "".join(area[i][2 - i] for i in range(3))
    if sub2 not in ("MAS", "SAM"):
        return False
    
    return True


if __name__ == "__main__":
    main()
