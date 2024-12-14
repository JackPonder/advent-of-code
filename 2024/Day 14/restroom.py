import sys


def main() -> None:
    # Get input file name
    infile = sys.argv[1]

    # Get map boundaries
    maxX = int(sys.argv[2])
    maxY = int(sys.argv[3])

    # Set quadrant boundaries
    boundX = (maxX - 1) / 2
    boundY = (maxY - 1) / 2

    # Count number of robots in each quadrant
    q1, q2, q3, q4 = 0, 0, 0, 0

    with open(infile) as file:
        # Read file data
        lines = file.read().splitlines()

        for line in lines:
            # Get initial position and velocity data
            pos, vel = line.split()
            posX, posY = [int(i) for i in pos[2:].split(",")]
            velX, velY = [int(i) for i in vel[2:].split(",")]

            # Calculate final robot position after 100 seconds
            finalPosX = (posX + velX * 100) % maxX
            finalPosY = (posY + velY * 100) % maxY
            
            # Count which quadrant the robot ends in
            if finalPosX < boundX and finalPosY < boundY:
                q1 += 1
            elif finalPosX > boundX and finalPosY < boundY:
                q2 += 1
            elif finalPosX < boundX and finalPosY > boundY:
                q3 += 1
            elif finalPosX > boundX and finalPosY > boundY:
                q4 += 1            

        # Calculate safety factor by multiplying number of robots in each quadrant
        safetyFactor = q1 * q2 * q3 * q4

        # Display results
        print(f"Safety Factor: {safetyFactor}")


if __name__ == "__main__":
    main()
