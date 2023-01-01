import re


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    cycleNumbers = [20, 60, 100, 140, 180, 220]
    register = Register()

    for line in lines:
        normLine = line.strip('\n')
        if (re.fullmatch(r'noop', normLine)):
            register.noop()
        elif (re.fullmatch(r'addx (\d+)', normLine)):
            value = int(re.findall(r'addx (\d+)', normLine)[0])
            register.addx(value)
        elif (re.fullmatch(r'addx -(\d+)', normLine)):
            value = int(re.findall(r'addx -(\d+)', normLine)[0])
            register.addx(-value)
        else:
            raise ValueError("unknown line: ", normLine)

    result1 = computeSignalStrengths(register, cycleNumbers)
    result2 = 256

    return result1, result2


class Register:
    def __init__(self) -> None:
        self.values = [1]
        self.current = 1

    values: list[int]
    current: int

    def noop(self):
        self.values.append(self.current)

    def addx(self, value):
        self.values.append(self.current)
        self.values.append(self.current)
        self.current += value


def computeSignalStrengths(register: 'Register', cycleNumbers: list[int]):
    signalStrengths: list[int] = []

    for nr in cycleNumbers:
        signalStrengths.append(nr * register.values[nr])

    totalSignalStrength = sum(signalStrengths)

    return (signalStrengths, totalSignalStrength)
