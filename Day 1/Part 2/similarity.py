with open("data.txt") as file:
    lines = file.read().split("\n")
    left: dict[int, int] = dict()
    right: dict[int, int] = dict()

    for line in lines:
        nums = line.split("   ")

        leftNum = int(nums[0])
        if leftNum in left:
            left[leftNum] += 1
        else:
            left[leftNum] = 1
        
        rightNum = int(nums[1])
        if rightNum in right:
            right[rightNum] += 1
        else:
            right[rightNum] = 1

    similarity = 0
    for i in left.keys():
        occurances = right.get(i, 0)
        similarity += i * occurances

    print(f"{similarity = }")