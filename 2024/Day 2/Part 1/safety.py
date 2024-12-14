def main() -> None:
    with open("data.txt") as file:
        reports = file.read().splitlines()

        numSafe = 0
        for report in reports:
            levels = [int(i) for i in report.split(" ")]
            if isSafe(levels):
                numSafe += 1

        print(f"Safe Reports: {numSafe}")


def isSafe(levels: list[int]) -> bool:
    dir = sign(levels[1] - levels[0])
    for i, level in enumerate(levels[:-1]):
        if sign(levels[i + 1] - level) != dir:
            return False

        if abs(levels[i + 1] - level) > 3:
            return False

    return True

def sign(num: int) -> int:
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0


if __name__ == "__main__":
    main()
