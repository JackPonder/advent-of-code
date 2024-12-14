import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Get map boundaries
    maxX = int(sys.argv[2])
    maxY = int(sys.argv[3])

    with open(infile) as file:
        # Read file data
        lines = file.read().splitlines()

        # Populate robot data
        robots: list[dict[str, int]] = []
        for line in lines:
            # Get initial position and velocity data
            pos, vel = line.split()
            posX, posY = [int(i) for i in pos[2:].split(",")]
            velX, velY = [int(i) for i in vel[2:].split(",")]

            # Add new robot to list
            robots.append({"posX": posX, "posY": posY, "velX": velX, "velY": velY})

        # Update robot positions every second
        t = 0
        while True:
            for robot in robots:
                robot["posX"] = (robot["posX"] + robot["velX"]) % maxX
                robot["posY"] = (robot["posY"] + robot["velY"]) % maxY
            
            positions: dict[tuple[int, int], int] = dict()
            for bot in robots:
                pos = (bot["posX"], bot["posY"])
                if pos in positions:
                    positions[pos] += 1
                else:
                    positions[pos] = 1

            t += 1
            if (t - 12) % 101 == 0 and (t - 88) % 103 == 0:
                writeRoom(positions, maxX, maxY)
                print(f"Time: {t} s")
                break


def writeRoom(positions: dict[tuple[int, int], int], maxX: int, maxY: int) -> None:
    with open("out.txt", "w") as file:
        for y in range(maxY):
            for x in range(maxX):
                num = positions.get((x, y), 0)
                file.write(str(num) if num != 0 else " ")
            
            file.write("\n")


if __name__ == "__main__":
    main()
