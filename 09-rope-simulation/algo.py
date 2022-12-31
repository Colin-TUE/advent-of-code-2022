from enum import Enum
import re


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    head = Position(0, 0)
    tail = Position(0, 0)
    knots = [Position(0, 0) for _ in range(0, 10)]
    visitedPositions: set[Position] = set()
    visitedPositionsRope: set[Position] = set()

    for line in lines:
        steps: int
        direction: Direction

        normLine = line.strip('\n')
        if (re.fullmatch(r'R (\d+)', normLine)):
            steps = int(re.findall(r'R (\d+)', normLine)[0])
            direction = Direction.R
        elif (re.fullmatch(r'L (\d+)', normLine)):
            steps = int(re.findall(r'L (\d+)', normLine)[0])
            direction = Direction.L
        elif (re.fullmatch(r'U (\d+)', normLine)):
            steps = int(re.findall(r'U (\d+)', normLine)[0])
            direction = Direction.U
        elif (re.fullmatch(r'D (\d+)', normLine)):
            steps = int(re.findall(r'D (\d+)', normLine)[0])
            direction = Direction.D
        else:
            raise ValueError("unknown line: ", normLine)

        for n in range(0, steps):
            simulateStep(head, tail, visitedPositions, direction)
            simulateStepRope(knots, visitedPositionsRope, direction)

    # print([(pos.i, pos.j) for pos in visitedPositions])

    result1 = len(visitedPositions)
    result2 = len(visitedPositionsRope)

    return result1, result2


def simulateStep(head: 'Position', tail: 'Position', visitedPositions: set['Position'], direction: 'Direction'):
    head.step(direction)
    stepDirection = computeDirection(head, tail)
    tail.step(stepDirection)
    visitedPositions.add(Position(tail.i, tail.j))


def simulateStepRope(knots: list['Position'], visitedPositionsRope: set['Position'], direction: 'Direction'):
    head = knots[0]
    tail = knots[9]

    # Move the head knot as instructed
    head.step(direction)

    # Compute for each knot which direction they will go
    # based on the updated position of the previous knot
    # including the tail at the end
    for i in range(1, 10):
        prevKnot = knots[i-1]
        currKnot = knots[i]
        stepDirection = computeDirection(prevKnot, currKnot)
        currKnot.step(stepDirection)

    visitedPositionsRope.add(Position(tail.i, tail.j))


def computeDirection(prevKnot, currKnot):
    (areTouching, diffI, diffJ) = computeDistance(prevKnot, currKnot)
    stepDirection: Direction
    if (areTouching):
        stepDirection = Direction.S
    elif (diffI == 0 and diffJ < 0):
        # same row, head is on the left
        stepDirection = Direction.L
    elif (diffI == 0 and diffJ > 0):
        # same row, head is on the right
        stepDirection = Direction.R
    elif (diffI < 0 and diffJ == 0):
        # same column, head is below
        stepDirection = Direction.D
    elif (diffI > 0 and diffJ == 0):
        # same column, head is above
        stepDirection = Direction.U
    elif (diffI < 0 and diffJ < 0):
        # head is below left
        stepDirection = Direction.LD
    elif (diffI < 0 and diffJ > 0):
        # head is below right
        stepDirection = Direction.RD
    elif (diffI > 0 and diffJ < 0):
        # head is above left
        stepDirection = Direction.LU
    elif (diffI > 0 and diffJ > 0):
        # head is above right
        stepDirection = Direction.RU
    else:
        raise ValueError("Case not considered: ", diffI, diffJ)

    return stepDirection


def computeDistance(pos1: 'Position', pos2: 'Position'):
    diffI = pos1.i - pos2.i
    diffJ = pos1.j - pos2.j
    return (abs(diffI) <= 1 and abs(diffJ) <= 1, diffI, diffJ)


class Position:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    i: int
    j: int

    def __eq__(self, other) -> bool:
        if isinstance(other, Position):
            return self.i == other.i and self.j == other.j
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.i, self.j))

    def step(self, direction: 'Direction'):
        match (direction):
            case Direction.R:
                self.j += 1
            case Direction.L:
                self.j -= 1
            case Direction.U:
                self.i += 1
            case Direction.D:
                self.i -= 1
            case Direction.RU:
                self.j += 1
                self.i += 1
            case Direction.RD:
                self.j += 1
                self.i -= 1
            case Direction.LU:
                self.j -= 1
                self.i += 1
            case Direction.LD:
                self.j -= 1
                self.i -= 1
            # case Direction.S:
                # do nothing, same position


class Direction(Enum):
    R = 1
    L = 2
    U = 3
    D = 4
    RU = 5
    RD = 6
    LU = 7
    LD = 8
    S = 9
