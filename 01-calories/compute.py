import array


f = open("input.csv","r")
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

print(f"Highest value: {max(calories_array)}")

topThree = sorted(calories_array)[-1: -4: -1]

print(f"Highest three values summed: {sum(topThree)}")