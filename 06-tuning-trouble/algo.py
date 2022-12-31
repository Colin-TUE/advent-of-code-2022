import array


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    startMarkerPositions = array.array('i', [])
    startMessagePositions = array.array('i', [])

    for line in lines:
        startMarker = findStartMarker(line)
        startMessage = findStartMessage(line)
        # add one, since the answer is 1 based
        startMarkerPositions.append(startMarker + 1)
        startMessagePositions.append(startMessage + 1)

    return startMarkerPositions, startMessagePositions


def findStartMarker(stream):
    # start at 3 since any shorter one cannot have 4 different chars
    for i in range(3, len(stream)):
        if (all_unique(stream[i-3:i+1])):
            return i
    return -1

def findStartMessage(stream):
    for i in range(13, len(stream)):
        if (all_unique(stream[i-13:i+1])):
            return i
    return -1

def all_unique(item):
    return len(set(item)) == len(item)
