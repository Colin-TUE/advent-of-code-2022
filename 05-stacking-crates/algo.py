import array
import math
import re


def getTopContainers(stacks: list[list[str]]):
    result = ""
    for containers in stacks:
        if len(containers) > 0:
            result += containers[len(containers) - 1]

    return result


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    stacks: list[list[str]] = [[],  # Remains empty, since the stack numbers are 1 based
                               [], [], [], [], [], [], [], [], []]
    stacksManyMove: list[list[str]] = [[],  # Remains empty, since the stack numbers are 1 based
                                       [], [], [], [], [], [], [], [], []]

    for line in lines:
        line = line.strip("\n")
        matchContainers = re.match(r'( ){0,}(\[\w\])', line)
        matchAction = re.fullmatch(r'move (\d+) from (\d) to (\d)', line)
        matchStackNrs = re.fullmatch(r'(( \d )( )?){2,}', line)
        # at least 2 times so the digit does not match the action line

        if (matchContainers is not None):
            # container line so add the containers to the right stack (1 based)
            for index in range(1, len(line), 4):
                container = line[index]
                stackNr = math.floor(index / 4) + 1
                if container != " ":
                    stacks[stackNr].append(container)
                    stacksManyMove[stackNr].append(container)

        elif (matchAction is not None):
            # action line, so find all numbers and use them to move containers
            groups = re.findall(r'move (\d+) from (\d) to (\d)', line)[0]

            amount = int(groups[0])
            source = int(groups[1])
            target = int(groups[2])
            for item in range(0, amount):
                stacks[target].append(stacks[source].pop())

            movedContainers = []
            for item in range(0, amount):
                movedContainers.append(stacksManyMove[source].pop())

            for cont in movedContainers[::-1]:
                stacksManyMove[target].append(cont)

        elif (matchStackNrs is not None):
            # Done reading the container stacks, so revert the insertion order
            for index in range(0, len(stacks)):
                stacks[index] = stacks[index][::-1]
                stacksManyMove[index] = stacksManyMove[index][::-1]

        else:
            print(f"Line not matched: {line}")

    return getTopContainers(stacks), getTopContainers(stacksManyMove)
