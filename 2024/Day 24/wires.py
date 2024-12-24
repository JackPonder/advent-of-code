import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        first, second = file.read().split("\n\n")

    # Parse initial wire info
    wires: dict[str, int] = {}
    for line in first.splitlines():
        name, val = line.split(":")
        wires[name] = int(val)

    # Calculate gate outputs for each gate
    lines = second.splitlines()
    while len(lines) != 0:
        for line in lines[:]:
            # Parse gate info
            a, gate, b, _, out = line.split()

            # Do not attempt to calculate gate output if inputs are unknown
            if a not in wires or b not in wires:
                continue

            # Calculate output gate value
            if gate == "AND":
                wires[out] = wires[a] & wires[b]
            elif gate == "OR":
                wires[out] = wires[a] | wires[b]
            elif gate == "XOR":
                wires[out] = wires[a] ^ wires[b]

            # Mark this gate as complete
            lines.remove(line)

    # Calculate decimal number from wires starting with 'z'
    out = sum(wires[z] * 2 ** int(z[1:]) for z in wires if z.startswith("z"))

    # Display results
    print(f"Decimal: {out}")


if __name__ == "__main__":
    main()
