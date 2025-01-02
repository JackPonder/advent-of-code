import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        program = [(line[:3], line[4:].split(", ")) for line in file.read().splitlines()]

    # Initialize registers
    registers = {"a": 0, "b": 0}

    # Execute program
    pointer = 0
    while pointer < len(program):
        instruction, args = program[pointer]

        if instruction == "hlf":
            registers[args[0]] //= 2
            pointer += 1

        elif instruction == "tpl":
            registers[args[0]] *= 3
            pointer += 1

        elif instruction == "inc":
            registers[args[0]] += 1
            pointer += 1

        elif instruction == "jmp":
            pointer += int(args[0])

        elif instruction == "jie":
            pointer += int(args[1]) if registers[args[0]] % 2 == 0 else 1

        elif instruction == "jio":
            pointer += int(args[1]) if registers[args[0]] == 1 else 1

    # Display results
    print(f"Register B: {registers['b']}")


if __name__ == "__main__":
    main()
