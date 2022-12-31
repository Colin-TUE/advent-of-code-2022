

def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    trees: list[list[Tree]] = []

    lineNr = -1
    for line in lines:
        lineNr += 1
        trees.append([])
        for treeHeight in line.strip('\n'):
            trees[lineNr].append(Tree(int(treeHeight)))

    nrOfRows: int = len(trees)
    nrOfColumns: int = len(trees[0])

    for i in range(0, nrOfRows):
        # Per row:
        # Compare tree heights in east wards direction
        maxHeight: int = -1
        for j in range(0, nrOfColumns):
            maxHeight = compareTreeHeight(trees, i, j, maxHeight)

        # Compare tree heights in west wards direction
        maxHeight: int = -1
        for j in range(nrOfColumns-1, -1, -1):
            maxHeight = compareTreeHeight(trees, i, j, maxHeight)

    for j in range(0, nrOfColumns):
        # Per column:
        # Compare tree heights in south wards direction
        maxHeight: int = -1
        for i in range(0, nrOfRows):
            maxHeight = compareTreeHeight(trees, i, j, maxHeight)

        # Compare tree heights in north wards direction
        maxHeight: int = -1
        for i in range(nrOfRows-1, -1, -1):
            maxHeight = compareTreeHeight(trees, i, j, maxHeight)

    nrOfVisibleTrees = 0
    for i in range(0, nrOfRows):
        for j in range(0, nrOfColumns):
            if (trees[i][j].isVisible):
                nrOfVisibleTrees += 1

    maxScenicScore = 0
    for i in range(0, nrOfRows):
        for j in range(0, nrOfColumns):
            tree = trees[i][j]
            treeHeight = tree.height

            northScore = computeScenicScore(
                trees, treeHeight, i, j, i-1, -1, -1, True)
            southScore = computeScenicScore(
                trees, treeHeight, i, j, i+1, nrOfRows, 1, True)
            westScore = computeScenicScore(
                trees, treeHeight, i, j, j-1, -1, -1, False)
            eastScore = computeScenicScore(
                trees, treeHeight, i, j, j+1, nrOfColumns, 1, False)

            tree.scenicScore = northScore * southScore * westScore * eastScore
            maxScenicScore = max(tree.scenicScore, maxScenicScore)

    # print([[t.isVisible for t in i] for i in trees])
    # print([[t.scenicScore for t in i] for i in trees])

    result1 = nrOfVisibleTrees
    result2 = maxScenicScore

    return result1, result2


def computeScenicScore(trees, treeHeight, i, j, start, stop, step, isRowDirection):
    nrOfTreesVisible = 0
    for d in range(start, stop, step):
        if (trees
            [d if isRowDirection else i]
                [j if isRowDirection else d]
                .height >= treeHeight):
            nrOfTreesVisible += 1
            break
        else:
            nrOfTreesVisible += 1
    return nrOfTreesVisible


def compareTreeHeight(trees, i, j, maxHeight):
    tree = trees[i][j]
    treeHeight = tree.height

    if (treeHeight > maxHeight):
        tree.isVisible = True
        maxHeight = treeHeight

    return maxHeight


class Tree:
    def __init__(self, height: int):
        self.height = height
        self.isVisible = False
        self.scenicScore = 0

    height: int
    isVisible: bool
    scenicScore: int
