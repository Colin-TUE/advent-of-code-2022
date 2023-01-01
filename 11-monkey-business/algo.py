from copy import deepcopy
from enum import Enum
from functools import reduce
import math
import re


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    monkeys: list[Monkey] = []
    monkeyBuilder = MonkeyBuilder()

    for line in lines:
        normLine = line.strip('\n')
        if (normLine == ""):
            # empty line detected, finished parsing previous monkey
            monkeys.append(monkeyBuilder.build())

            # Reset monkey builder
            monkeyBuilder = MonkeyBuilder()
        elif (re.fullmatch(r'Monkey (\d+):', normLine)):
            monkeyNumber = int(re.findall(r'\d+', normLine)[0])
            monkeyBuilder.setMonkeyNr(monkeyNumber)
        elif (re.fullmatch(r'  Starting items: ((\d+)(, )?)+', normLine)):
            numbers = re.findall(r'\d+', normLine)

            items: list[int] = []
            for i in numbers:
                items.append(int(i))
            monkeyBuilder.setStartingItems(items)
        elif (re.fullmatch(r'  Operation: new = old \* (\d+)', normLine)):
            operationDelta = int(re.findall(r'\d+', normLine)[0])
            monkeyBuilder.setOperation(Operand.Multiply, operationDelta)
        elif (re.fullmatch(r'  Operation: new = old \+ (\d+)', normLine)):
            operationDelta = int(re.findall(r'\d+', normLine)[0])
            monkeyBuilder.setOperation(Operand.Addition, operationDelta)
        elif (re.fullmatch(r'  Operation: new = old \* old', normLine)):
            monkeyBuilder.setOperation(Operand.Squared, 0)
        elif (re.fullmatch(r'  Test: divisible by (\d+)', normLine)):
            testDivider = int(re.findall(r'\d+', normLine)[0])
            monkeyBuilder.setTestDivider(testDivider)
        elif (re.fullmatch(r'    If true: throw to monkey (\d+)', normLine)):
            monkeyNr = int(re.findall(r'\d+', normLine)[0])
            monkeyBuilder.setNextMonkeyTestPass(monkeyNr)
        elif (re.fullmatch(r'    If false: throw to monkey (\d+)', normLine)):
            monkeyNr = int(re.findall(r'\d+', normLine)[0])
            monkeyBuilder.setNextMonkeyTestFail(monkeyNr)
        else:
            raise ValueError("unknown line: ", normLine)

    # print(len(monkeys))
    # for m in monkeys:
    #     m.print()

    monkeysPartOne = deepcopy(monkeys)
    result1 = playMonkeyInTheMiddle(monkeysPartOne, 20, True, 3)

    monkeysPartTwo = deepcopy(monkeys)
    modulus = reduce(math.lcm, [m.testDivider for m in monkeysPartTwo])
    result2 = playMonkeyInTheMiddle(monkeysPartTwo, 10_000, False, modulus)

    return result1, result2


def playMonkeyInTheMiddle(monkeys, nrOfRounds, dampenWorries, value):
    for roundNr in range(0, nrOfRounds):
        for m in monkeys:
            while len(m.items) > 0:
                item = m.items.pop()
                newValue = m.inspect(item, dampenWorries, value)
                nextMonkey = m.test(newValue)
                monkeys[nextMonkey].items.append(newValue)

    monkeyInspections = sorted(monkeys, key=lambda m: m.nrOfInspections)

    for m in monkeys:
        print(f"Monkey {m.number}: {m.nrOfInspections}")

    return monkeyInspections[-1].nrOfInspections * \
        monkeyInspections[-2].nrOfInspections


class Monkey:
    def __init__(self, number: int, items: list[int], operation, testDivider: int, nextMonkeyTestPass: int, nextMonkeyTestFail: int) -> None:
        self.number = number
        self.items = items
        self.testDivider = testDivider
        self.nextMonkeyTestPass = nextMonkeyTestPass
        self.nextMonkeyTestFail = nextMonkeyTestFail
        self.operation = operation
        self.nrOfInspections = 0

    def inspect(self, item: int, dampenWorries: bool, dampenValue: int):
        self.nrOfInspections += 1
        if (dampenWorries):
            return math.floor((self.operation(item) / dampenValue))
        else:
            return self.operation(item) % dampenValue

    def test(self, item: int):
        if (item % self.testDivider == 0):
            return self.nextMonkeyTestPass
        else:
            return self.nextMonkeyTestFail

    def print(self):
        print(f"""Monkey {self.number}:
  Starting items: {self.items}
  Operation: {self.operation}
  Test: divisible by {self.testDivider}
    If true: throw to monkey {self.nextMonkeyTestPass}
    If false: throw to monkey {self.nextMonkeyTestFail}""")


class MonkeyBuilder:
    nr: int
    startingItems: list[int]
    operationDelta: int
    operationOperand: 'Operand'
    testDivider: int
    nextMonkeyTestPass: int
    nextMonkeyTestFail: int

    def setMonkeyNr(self, nr: int):
        self.nr = nr

    def setStartingItems(self, items: list[int]):
        self.startingItems = items

    def setOperation(self, op: 'Operand', delta: int):
        self.operationOperand = op
        self.operationDelta = delta

    def setTestDivider(self, divider: int):
        self.testDivider = divider

    def setNextMonkeyTestPass(self, nr: int):
        self.nextMonkeyTestPass = nr

    def setNextMonkeyTestFail(self, nr: int):
        self.nextMonkeyTestFail = nr

    def build(self):
        operation = defaultOperation
        match (self.operationOperand):
            case Operand.Multiply:
                def operation(old): return old * self.operationDelta
            case Operand.Addition:
                def operation(old): return old + self.operationDelta
            case Operand.Squared:
                def operation(old): return old * old

        return Monkey(self.nr, self.startingItems, operation, self.testDivider, self.nextMonkeyTestPass, self.nextMonkeyTestFail)


class Operand(Enum):
    Multiply = 1
    Addition = 2
    Squared = 3


def defaultOperation(old: int):
    raise ValueError("No operation defined")
