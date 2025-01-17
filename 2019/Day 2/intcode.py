import sys
import itertools


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Read file data
    with open(infile) as file:
        program = [int(i) for i in file.read().split(",")]

    # Run program with inputs 12, 2
    print(f"Part 1: {execute(program, 12, 2)}")

    # Test different program inputs until target output is found
    for noun, verb in itertools.product(range(100), range(100)):
        if execute(program, noun, verb) == 19690720:
            print(f"Part 2: {100 * noun + verb}")
            break


def execute(program: list[int], noun: int, verb: int) -> int:
    """Returns the value at address 0 of a given program after it has halted"""

    # Copy program to prevent mutating original data
    program = program[:]

    # Set program inputs
    program[1] = noun
    program[2] = verb

    # Execute program
    ptr = 0
    while True:
        # Get next opcode
        opcode = program[ptr]

        # Add
        if opcode == 1:
            a, b, out = program[ptr + 1:ptr + 4]
            program[out] = program[a] + program[b]
            ptr += 4

        # Multiply
        elif opcode == 2:
            a, b, out = program[ptr + 1:ptr + 4]
            program[out] = program[a] * program[b]
            ptr += 4

        # Halt
        elif opcode == 99:
            return program[0]


if __name__ == "__main__":
    main()
