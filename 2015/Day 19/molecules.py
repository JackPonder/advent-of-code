import sys
import re


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        data, molecule = file.read().split("\n\n")

    # Parse replacements
    replacements: dict[str, set[str]] = {}
    for line in data.splitlines():
        atom, sub = line.split(" => ")
        if atom not in replacements:
            replacements[atom] = set()

        replacements[atom].add(sub)

    # Find number of distinct molecules that can be created
    distinct = getNumDistinctMolecules(molecule, replacements)

    # Display results
    print(f"Distinct Molecules: {distinct}")


def getNumDistinctMolecules(
    molecule: str,
    replacements: dict[str, set[str]],
) -> int:
    """Returns the number of distinct molecules that can be created after one replacement"""

    # Parse atoms in molecule
    atoms = re.findall(r"[A-Z][a-z]?", molecule)

    # Iterate through the molecule and do replacements on each atom
    distinct: set[str] = set()
    for i, atom in enumerate(atoms):
        if atom not in replacements:
            continue

        for sub in replacements[atom]:
            distinct.add(str().join(atom if i != j else sub for j, atom in enumerate(atoms)))

    return len(distinct)


if __name__ == "__main__":
    main()
