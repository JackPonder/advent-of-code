import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    with open(infile) as file:
        # Read file data
        lines = file.read().splitlines()

        # Parse program data
        a, b, c = [int(line[12:]) for line in lines[:3]]
        program = [int(i) for i in lines[4][9:].split(",")]

        # Get program outputs
        outputs = getOutputs(program, a, b, c)

        # Print results
        print(f"Output: {','.join(str(i) for i in outputs)}")


def getOutputs(program: list[int], a: int, b: int, c: int) -> list[int]:
    """Returns the outputs of a given program"""
    
    pointer = 0
    outputs: list[int] = []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        pointer += 2

        if opcode == 0:
            a = a // (2 ** getComboOperand(operand, a, b, c))
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = getComboOperand(operand, a, b, c) % 8
        elif opcode == 3 and a != 0:
            pointer = operand
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            outputs.append(getComboOperand(operand, a, b, c) % 8)
        elif opcode == 6:
            b = a // (2 ** getComboOperand(operand, a, b, c))
        elif opcode == 7:
            c = a // (2 ** getComboOperand(operand, a, b, c))

    return outputs


def getComboOperand(operand: int, a: int, b: int, c: int) -> int:
    """Returns the combo operand value for a given operand"""

    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c

    return operand


if __name__ == "__main__":
    main()
