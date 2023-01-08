import array
import math

decryptionKey = 811589153
amountOfMixRounds = 10


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    prio = 0
    numbers: list[Number] = []
    processingOrder: list[Number] = []
    zero = None

    for line in lines:
        line.strip("\n")
        number = Number(int(line), prio)

        if number.number == 0:
            zero = number
        numbers.append(number)
        processingOrder.append(number)

        prio += 1

    if (zero is None):
        raise ValueError("Zero not found")

    # for n in numbers:
    #     print(f"Number: {n.number} at {n.prio}")

    # printList(numbers)

    for n in processingOrder:
        move(numbers, n, n.number)

    result1 = 0
    startingCount = numbers.index(zero)
    for x in [1000, 2000, 3000]:
        result1 += get(numbers, startingCount + x).number

    # Rest list back to initial order
    numbers.sort(key=lambda n: n.prio)
    for i in range(0, amountOfMixRounds):
        # print(f"=====Round {i}=====")
        # printList(numbers, decrypted=True)

        for n in processingOrder:
            move(numbers, n, n.number)

    result2 = 0
    startingCount = numbers.index(zero)
    for x in [1000, 2000, 3000]:
        result2 += get(numbers, startingCount + x).decrypted

    return result1, result2


def move(list, itemToMove, amountOfSteps):
    # print(f"Moving {itemToMove.number}")
    oldIndex = list.index(itemToMove)

    if (amountOfSteps < 0):
        amountOfSteps -= 1
    diff = oldIndex + amountOfSteps
    if (diff >= len(list)):
        diff += math.floor(diff/len(list))
    newIndex = (diff) % len(list)

    list.insert(newIndex, list.pop(oldIndex))
    # printList(list)


def get(list, index):
    normalizedIndex = index % len(list)
    return list[normalizedIndex]


def printList(list, decrypted=False):
    string = ""
    for n in list:
        if decrypted:
            string += f"{n.decrypted}, "
        else:
            string += f"{n.number}, "

    print(string)


class Number():
    def __init__(self, number: int, prio: int) -> None:
        self.number = number
        self.decrypted = number * decryptionKey
        self.prio = prio
