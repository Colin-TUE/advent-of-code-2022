import array


def toInt(s):
    return int(s)


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    containedSections = array.array('i', [])
    overlappingPairs = array.array('i', [])

    for line in lines:
        assignments = line.strip("\n").split(",")
        elfOne = list(map(toInt, assignments[0].split("-")))
        elfTwo = list(map(toInt, assignments[1].split("-")))

        elfOneSections = range(elfOne[0], elfOne[1]+1)
        elfTwoSections = range(elfTwo[0], elfTwo[1]+1)

        elfTwoLow = elfTwo[0]
        elfTwoUpp = elfTwo[1]
        isOneCOntainedInTwo = all(section >= elfTwoLow and section <=
                                  elfTwoUpp for section in elfOneSections)

        elfOneLow = elfOne[0]
        elfOneUpp = elfOne[1]
        isTwoContainedInOne = all(section >= elfOneLow and section <=
                                  elfOneUpp for section in elfTwoSections)

        containedSections.append(
            isOneCOntainedInTwo or isTwoContainedInOne if 1 else 0)

        overlap = set(elfOneSections) & set(elfTwoSections)

        overlappingPairs.append(len(overlap) > 0 if 1 else 0)

    return sum(containedSections), sum(overlappingPairs)
