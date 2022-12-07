import array


def computePrio(item):
    asciiValue = ord(item)
    if (asciiValue > 64 and asciiValue < 91):
        # item is from A to Z and should have prio 27 to 52
        return asciiValue - 64 + 26
    elif (asciiValue > 96 and asciiValue < 123):
        # item is from a to z and should have prio 1 to 26
        return asciiValue - 96
    else:
        # Error, not one of the expected items
        raise ValueError(
            f"Item was out side of expected range: {item} - {asciiValue}")


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    prios = array.array('i', [])
    badgePrios = array.array('i', [])

    for line in lines:
        rucksack = line.strip("\n")
        n = len(rucksack)
        if n % 2 != 0:
            raise ValueError("Odd length found")

        # Assume strings lengths are always even
        compartOne = rucksack[0:n//2]
        compartTwo = rucksack[n//2:]

        commonItems = list(set(compartOne) & set(compartTwo))

        priosOfItems = list(map(computePrio, commonItems))
        if len(priosOfItems) > 1:
            raise ValueError("Multiple common items found")

        prios.append(priosOfItems[0])

    for group in range(0, len(lines), 3):
        rucksack1 = lines[group].strip("\n")
        rucksack2 = lines[group+1].strip("\n")
        rucksack3 = lines[group+2].strip("\n")

        groupBadges = list(set(rucksack1) & set(rucksack2) & set(rucksack3))
        prioOfBadge = list(map(computePrio, groupBadges))
        if len(prioOfBadge) > 1:
            raise ValueError("Multiple group badges found")

        badgePrios.append(prioOfBadge[0])
        

    return sum(prios), sum(badgePrios)
