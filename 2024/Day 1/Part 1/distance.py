with open("data.txt") as file:
    lines = file.read().split("\n")
    l1: list[int] = []
    l2: list[int] = []

    for line in lines:
        nums = line.split("   ")
        l1.append(int(nums[0]))
        l2.append(int(nums[1]))

    l1.sort()
    l2.sort()

    distance = 0
    for i, j in zip(l1, l2):
        distance += abs(i - j)

    print(f"{distance = }")