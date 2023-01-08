import array


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    signalPairs: list[SignalPair] = []

    pairNr = 1
    for i in range(0, len(lines), 3):
        first = Signal(lines[i])
        second = Signal(lines[i+1])
        pair = SignalPair(first, second, pairNr)

        print("==========")
        print(f"Processing pair {pairNr}")
        # print(pair.toString())

        pair.mark(verifyInOrder(pair.first.signal, pair.second.signal)[0])
        print(f"Is in order: {pair.isInOrder}")
        print("==========")

        signalPairs.append(pair)
        pairNr += 1

    def fold(acc, x): return acc + x.pairNr if x.isInOrder else acc
    accumulator = 0
    i = 0
    [accumulator := fold(accumulator, x) for x in signalPairs]
    result1 = accumulator
    result2 = 256

    return result1, result2


def verifyInOrder(leftList, rightList):
    for i in range(0, len(leftList)):
        left = leftList[i]
        right = rightList[i] if i < len(rightList) else None

        print(f"Comparing: {left} vs {right}")

        # second list has ran out of elements
        if right is None:
            return False, True

        if type(left) is int and type(right) is int:
            if left < right:  # Lower so in order
                return True, True
            elif left > right:  # Higher so out of order
                return False, True
            else:  # Same, so go to next
                continue
        elif type(left) is list and type(right) is list:
            isInOrder = verifyInOrder(left, right)
            if isInOrder[1] is None:
                continue
            else:
                return isInOrder
        elif type(left) is int and type(right) is list:
            return verifyInOrder([left], right)
        elif type(left) is list and type(right) is int:
            return verifyInOrder(left, [right])
        else:
            raise ValueError(f"Unknown case: {left} vs {right}")

    # Left list ran out if items
    if len(leftList) is len(rightList):
        # are equal length, so definitive decision could be made
        return True, None
    else:
        # left list must be larger, so decision can be made
        return True, True


class SignalPair():
    def __init__(self, first: 'Signal', second: 'Signal', pairNr: int) -> None:
        self.first = first
        self.second = second
        self.pairNr = pairNr
        self.isInOrder = None

    def mark(self, inOrder: bool):
        self.isInOrder = inOrder

    def toString(self):
        return f"Fir: {self.first.toString()}; \nSec: {self.second.toString()}; \nisInOrder: {self.isInOrder}"


class Signal():
    def __init__(self, input: str) -> None:
        signal = eval(input)
        self.signal = signal

    def toString(self):
        return str(self.signal)
