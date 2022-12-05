import array

def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    pointLose = 0
    pointDraw = 3
    pointWin = 6

    pointRock = 1
    pointPaper = 2
    pointScissors = 3

    roundsBasedOnShape = array.array('i', [])
    roundsBasedOnOutcome = array.array('i', [])

    for line in lines:
        match (line.strip("\n")):
            case "A X":  # Rock - Rock - Lose
                roundsBasedOnShape.append(pointRock + pointDraw)
                roundsBasedOnOutcome.append(pointLose + pointScissors)
            case "A Y":  # Rock - Paper - Draw
                roundsBasedOnShape.append(pointPaper + pointWin)
                roundsBasedOnOutcome.append(pointDraw + pointRock)
            case "A Z":  # Rock - Scissors - Win
                roundsBasedOnShape.append(pointScissors + pointLose)
                roundsBasedOnOutcome.append(pointWin + pointPaper)
            case "B X":  # Paper - Rock - Lose
                roundsBasedOnShape.append(pointRock + pointLose)
                roundsBasedOnOutcome.append(pointLose + pointRock)
            case "B Y":  # Paper - Paper - Draw
                roundsBasedOnShape.append(pointPaper + pointDraw)
                roundsBasedOnOutcome.append(pointDraw + pointPaper)
            case "B Z":  # Paper - Scissors - Win
                roundsBasedOnShape.append(pointScissors + pointWin)
                roundsBasedOnOutcome.append(pointWin + pointScissors)
            case "C X":  # Scissors - Rock - Lose
                roundsBasedOnShape.append(pointRock + pointWin)
                roundsBasedOnOutcome.append(pointLose + pointPaper)
            case "C Y":  # Scissors - Paper - Draw
                roundsBasedOnShape.append(pointPaper + pointLose)
                roundsBasedOnOutcome.append(pointDraw + pointScissors)
            case "C Z":  # Scissors - Scissors - Win
                roundsBasedOnShape.append(pointScissors + pointDraw)
                roundsBasedOnOutcome.append(pointWin + pointRock)

    return sum(roundsBasedOnShape), sum(roundsBasedOnOutcome)
