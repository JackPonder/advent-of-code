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

    # Parse gate info
    gates: list[tuple[str, str, str, str]] = []
    for line in second.splitlines():
        a, gate, b, _, out = line.split()
        gates.append((a, gate, b, out))

    # Calculate gate outputs for each gate
    while len(gates) != 0:
        # Get next gate to evaluate
        a, gate, b, out = gates.pop(0)

        # Do not attempt to calculate gate output if inputs are unknown
        if a not in wires or b not in wires:
            gates.append((a, gate, b, out))
            continue

        # Calculate output gate value
        if gate == "AND":
            wires[out] = wires[a] & wires[b]
        elif gate == "OR":
            wires[out] = wires[a] | wires[b]
        elif gate == "XOR":
            wires[out] = wires[a] ^ wires[b]

    # Calculate decimal number from wires starting with 'z'
    out = sum(wires[wire] * 2 ** int(wire[1:]) for wire in wires if wire.startswith("z"))

    # Display results
    print(f"Decimal: {out}")


if __name__ == "__main__":
    main()
