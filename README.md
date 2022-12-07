# advent-of-code-2022

This repo contains the code I used to solve the challenges for the
[Advent of Code 2022](https://adventofcode.com/2022/).

## Setup

I use Python as programming language for the challenges as it is easy to script
and get started with. I use [ASDF](https://asdf-vm.com/) to manage the my Python
install (and potentially other needed dependencies).

For each day a new folder is used that contains the code used for
the challenge of that day. Naming convention is
`{day number - leading 0}-{theme of the day - word separated by -}`.

In the `00-template` folder, one can find the basic file setup used:

- `algo.py` contains the function with the algorithm.
- `compute.py` calls the algo for the provided puzzle input and prints the result.
- `test.py` calls the algo with the example input and assert the result.
- `example.csv` contains the example input.
- `input.csv` contains the puzzle input.
