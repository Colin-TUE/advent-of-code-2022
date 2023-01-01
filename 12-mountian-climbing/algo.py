from copy import deepcopy


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    maxY = len(lines)
    maxX = len(lines[0].strip("\n"))
    elevations: list[list[Vertex]] = [
        [Vertex(-1, -1, -1) for i in range(maxX)] for j in range(maxY)]
    target: Vertex = Vertex(-1, -1, -1)
    start: Vertex = Vertex(-1, -1, -1)

    x = 0
    y = 0

    for line in lines:
        for c in line.strip("\n"):
            if (c == 'S'):
                start = Vertex(y, x, ord('a'))
                elevations[y][x] = start
            elif (c == 'E'):
                target = Vertex(y, x, ord('z'))
                target.setParent(target)
                elevations[y][x] = target
            else:
                e = ord(c)
                if e <= 96 or e >= 123:
                    raise ValueError(
                        f"Unexpected elevation found: {e} for {c}")
                elevations[y][x] = Vertex(y, x, e)
            x += 1
        y += 1
        x = 0

    print(f"Start: {start.toString()}")
    print(f"Target: {target.toString()}")

    for row in elevations:
        for p in row:
            if p.x < 0 or p.y < 0 or p.elevation < 0:
                print(elevationsToString(elevations, start, target))
                raise ValueError(f"Uninitialized point")

    print("=====Elevations=====")
    print(elevationsToString(elevations, start, target))

    print("=====Route=====")
    elevationsFromS = deepcopy(elevations)
    shortestPath = computeShortestPath(
        elevationsFromS, target, elevationsFromS[start.x][start.y])
    pathStr = pathToString(elevations, shortestPath, start, target)
    print(pathStr)

    print("=====Optimal Route=====")
    allShortestPaths: list[list['Vertex']] = []
    for i in range(0, maxY):
        elevationsFromA = deepcopy(elevations)
        potentialStart = elevationsFromA[i][0]
        onePathToEastEdge = computeShortestPath(
            elevationsFromA, target, potentialStart)
        allShortestPaths.append(onePathToEastEdge)
    shortestToAnyA = sorted(allShortestPaths, key=lambda p: len(p))[0]
    optPathStr = pathToString(elevations, shortestToAnyA, start, target)
    print(optPathStr)

    result1 = len(shortestPath) - 1
    result2 = len(shortestToAnyA) - 1

    return result1, result2


def computeShortestPath(elevations: list[list['Vertex']], target: 'Vertex', start: 'Vertex'):
    allCurrentVertices: list[Vertex] = []
    allCurrentVertices.append(target)
    debugPrinting = False

    while len(allCurrentVertices) > 0 and start.parent == None:
        v = allCurrentVertices.pop(0)
        # print(f"Visiting - {v.toString()}")

        if v.x == -1 and v.y == -1:
            debugPrinting = True
            print("REACHED MY DEBUG STATEMENT")
            print(start.toString())
            print(target.toString())

        if (debugPrinting):
            print("CURRENT")
            print(v.toString())
            print("NEIGHBORS")

        # get all the neighbors
        northNeighbor = getVertex(elevations, v.x-1, v.y)
        southNeighbor = getVertex(elevations, v.x+1, v.y)
        westNeighbor = getVertex(elevations, v.x, v.y-1)
        eastNeighbor = getVertex(elevations, v.x, v.y+1)

        for n in [northNeighbor, southNeighbor, westNeighbor, eastNeighbor]:
            if (  # Check if there is actual neighbor
                n != None
                # and it is not visited yet
                and n.parent == None
                # and it is reachable from our current elevation
                and n.elevation + 1 >= v.elevation
            ):
                # print(f"Adding neighbor - {n.toString()}")
                n.setParent(v)
                allCurrentVertices.append(n)

                if (debugPrinting):
                    print(n.toString() if n != None else "")

    # print("Found shorted path, reconstructing it now!")

    shortestPath = [start]
    nextVertex = start.parent
    while nextVertex != None and nextVertex != target:
        shortestPath.append(nextVertex)
        nextVertex = nextVertex.parent
    shortestPath.append(target)

    return shortestPath


def getVertex(elevations: list[list['Vertex']], x: int, y: int):
    if (x < 0 or x >= len(elevations) or y < 0 or y >= len(elevations[0])):
        return None
    else:
        return elevations[x][y]


def elevationsToString(elevations: list[list['Vertex']], start: 'Vertex', target: 'Vertex'):
    map = ""
    for row in elevations:
        for p in row:
            if p.elevation == 96 or p == start:
                map += "S"
            elif p.elevation == 123 or p == target:
                map += "E"
            elif p.elevation < 96:
                map += "."
            else:
                map += chr(p.elevation)
        map += "\n"

    return map


def pathToString(elevations: list[list['Vertex']], path: list['Vertex'], start: 'Vertex', target: 'Vertex'):
    map = list(elevationsToString(elevations, start, target))

    for i in range(0, len(path) - 1):
        currentV = path[i]
        nextV = path[i+1]

        direction: str
        if currentV.y == nextV.y:
            if (currentV.x < nextV.x):
                direction = "V"
            else:
                direction = "^"
        else:
            if (currentV.y < nextV.y):
                direction = ">"
            else:
                direction = "<"

        strPos = currentV.x*(len(elevations[0]) + 1) + currentV.y
        map[strPos] = direction

        for i in range(0, len(map)):
            char = map[i]
            if char not in ["E", "\n", "<", ">", "^", "V"]:
                map[i] = "."

    return "".join(map)


class Vertex():
    def __init__(self, x: int, y: int, e: int) -> None:
        self.x = x
        self.y = y
        self.elevation = e
        self.parent = None

    def setParent(self, p: 'Vertex'):
        self.parent = p

    def toString(self):
        return f"position X:{self.x},Y:{self.y} at {self.elevation}/{chr(self.elevation)}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Vertex):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))
