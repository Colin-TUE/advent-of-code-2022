import re


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    cycleNumbers = [20, 60, 100, 140, 180, 220]
    register = Register()
    crt = Crt(register)

    for line in lines:
        normLine = line.strip('\n')
        if (re.fullmatch(r'noop', normLine)):
            crt.noop()
            register.noop()
        elif (re.fullmatch(r'addx (\d+)', normLine)):
            value = int(re.findall(r'addx (\d+)', normLine)[0])

            crt.addx(value)
            register.addx(value)
        elif (re.fullmatch(r'addx -(\d+)', normLine)):
            value = int(re.findall(r'addx -(\d+)', normLine)[0])

            crt.addx(-value)
            register.addx(-value)
        else:
            raise ValueError("unknown line: ", normLine)

    result1 = computeSignalStrengths(register, cycleNumbers)
    result2 = crt.screen

    crt.print()

    return result1, result2


class Register:
    def __init__(self) -> None:
        self.values = [1]
        self.current = 1

    def noop(self):
        self.values.append(self.current)

    def addx(self, value):
        self.values.append(self.current)
        self.values.append(self.current)
        self.current += value

    def getValue(self):
        return self.values[len(self.values) - 1]

    def getCycleNr(self):
        return len(self.values)


class Crt():
    def __init__(self, register: 'Register') -> None:
        self.rows = [1, 41, 81, 121, 161, 201, 241]
        self.screen = str("")
        self.spritePosition = [1, 2, 3]
        self.cycleNr = 0

    def noop(self):
        self.cycleNr += 1
        self.cycle()

    def addx(self, value):
        self.cycleNr += 1
        self.cycle()
        self.cycleNr += 1
        self.cycle()
        self.updateSprite(value)

    def updateSprite(self, value):
        currentValue = self.spritePosition[1]
        newValue = currentValue + value
        self.spritePosition = [newValue - 1, newValue, newValue + 1]

    def cycle(self, ):
        if (self.cycleNr in self.rows):
            # cycle nr is where a new row starts
            self.screen += "\n"
            # self.screen += f"{self.register.getCycleNr()}"

        if ((self.cycleNr % 40) in self.spritePosition):
            # cycle nr is where the sprite is located, so light up pixel
            self.screen += "#"
        else:
            # cycle nr is not where the sprite is located, keep pixel off
            self.screen += '.'

    def print(self):
        print("====START CRT====================")
        print(self.screen)
        print("====END CRT======================")


def computeSignalStrengths(register: 'Register', cycleNumbers: list[int]):
    signalStrengths: list[int] = []

    for nr in cycleNumbers:
        signalStrengths.append(nr * register.values[nr])

    totalSignalStrength = sum(signalStrengths)

    return (signalStrengths, totalSignalStrength)
