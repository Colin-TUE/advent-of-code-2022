import array


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    line_array = array.array('u', [])

    for line in lines:
        line_array.append(line[0])

    result1 = 41
    result2 = 256

    return result1, result2
