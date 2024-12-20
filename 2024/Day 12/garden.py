import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read garden data
    with open(infile) as file:
        garden = {(row, col): plot for row, line in enumerate(file.read().splitlines()) for col, plot in enumerate(line)}

    # Calculate total price of fencing all sections
    price = 0
    searched: set[tuple[int, int]] = set()
    for pos in garden:
        if pos not in searched:
            area, perimeter, section = getSectionStats(garden, pos)
            price += area * perimeter
            searched.update(section)

    # Print results
    print(f"Price: {price}")


def getSectionStats(
    garden: dict[tuple[int, int], str], 
    pos: tuple[int, int],
    area: int = 0, 
    perimeter: int = 0,
    section: set[tuple[int, int]] | None = None,
) -> tuple[int, int, set[tuple[int, int]]]:
    """Returns the area, perimeter, and a set of positions in a section in a garden"""

    # Initialize set of section positions
    if section is None:
        section = set()

    # Mark this space as searched
    section.add(pos)

    # Keep track of number of sides needed to enclose this space
    sides = 4

    # Search adjacent spaces 
    for rowOffset, colOffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        # Calculate adjacent position coordinates
        row, col = pos
        adjacent = row + rowOffset, col + colOffset

        # Do not search spaces outside garden boundaries
        if adjacent not in garden:
            continue

        # Get data for adjacent spaces in this section
        if garden[adjacent] == garden[pos]:
            if adjacent not in section:
                area, perimeter, section = getSectionStats(garden, adjacent, area, perimeter, section.copy())

            sides -= 1

    return area + 1, perimeter + sides, section


if __name__ == "__main__":
    main()
