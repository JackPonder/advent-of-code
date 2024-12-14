from copy import copy


def main() -> None:
    with open("data.txt") as file:
        reports = file.read().splitlines()

        numSafe = 0
        for report in reports:
            levels = [int(i) for i in report.split(" ")]
            if isSafe(levels):
                numSafe += 1

        print(f"Safe Reports: {numSafe}")


def isSafe(levels: list[int], damp = False) -> bool:
    safe = True
    dir = sign(levels[1] - levels[0])

    for i, level in enumerate(levels[:-1]):
        if sign(levels[i + 1] - level) != dir:
            safe = False

        if abs(levels[i + 1] - level) > 3:
            safe = False

    if safe:
        return True
    if not damp:
        for i in range(len(levels)):
            new = levels[:i] + levels[(i + 1):]
            if isSafe(new, True):
                return True
            
        return False
    
    return False

def sign(num: int) -> int:
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0


if __name__ == "__main__":
    main()
