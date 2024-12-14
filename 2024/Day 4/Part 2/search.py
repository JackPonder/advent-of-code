def main() -> None:
    with open("data.txt") as file:
        lines = file.read().splitlines()

        matches = 0
        for i, line in enumerate(lines[:-2]):
            for j, _ in enumerate(line[:-2]):
                area = [i[j:j+3] for i in lines[i:i + 3]]
                if hasXmas(area):
                    matches += 1

        print(f"Matches: {matches}")
        

def hasXmas(area: list[str]) -> bool:
    sub1 = "".join(area[i][i] for i in range(3))
    if sub1 not in ("MAS", "SAM"):
        return False
    
    sub2 = "".join(area[i][2 - i] for i in range(3))
    if sub2 not in ("MAS", "SAM"):
        return False
    
    return True


if __name__ == "__main__":
    main()
