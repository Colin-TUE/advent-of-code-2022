import array


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    calories_array = array.array('i', [0])

    for line in lines:
        match (line):
            case "\n":
                # Go to the new elf and start counting from 0
                calories_array.append(0)
            case _:
                # add calories to current elf
                calories_array[-1] = calories_array[-1] + int(line)

    topThree = sorted(calories_array)[-1: -4: -1]

    return max(calories_array), sum(topThree)
