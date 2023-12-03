import re
from io import TextIOWrapper

"""
Nolan Gregory
Advent of Code 2023
Day 3

- Solved: Yes
- Stars gained: 2
- Difficulty: 5/10
"""


def one(data: TextIOWrapper) -> int:
    """
    Prompt: You are given the engine schematic consists of a visual representation of the engine. There are lots 
    of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, 
    is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.). Return the sum of all 
    of the part numbers in the engine schematic.

    Solution: 551094

    Explaination: Think of the schematic as a 2-d array of data. If you perform a check on all neighboring cells in the
    2-D array, you can just determine if any of the chars are a valid symbol. If so, add it to total. Bounds checks must
    be implemented to avoid going out of bounds of the array.

    Caveats: A bit tricky at first since a symbol can occur adjacent to any character in the string. Think of it like any
    2-D cellular automata and it should fall into place.

    Alternate Solution: N/a. 
    """
    total_sum = 0
    for row, line in enumerate(data):
        line += '.'
        concat_output = ''
        for col, element in enumerate(line):
            if element.isdigit():
                concat_output += element
            elif concat_output:
                neighbors = [data[row_i][col_i] for row_i in range(max(0, row-1), min(len(data), row+2))
                             for col_i in range(max(0, col-1-len(concat_output)), min(len(line)-1, col+1))]
                if any(neighbor not in '.0123456789' for neighbor in neighbors):
                    total_sum += int(concat_output)
                concat_output = ''
    return total_sum


def two(data: TextIOWrapper) -> int:
    """
    Prompt: TODO

    Solution: 80179647

    Explaination: TODO

    Caveats: TODO.

    Alternate Solution: N/a. 
    """
    coordinates = {}
    concat_output = ''
    for row, line in enumerate(data):
        line += '.'
        for col, element in enumerate(line):
            if element.isdigit():
                concat_output += element
            elif concat_output:
                for row_i in range(max(0, row-1), min(len(data), row+2)):
                    for col_i in range(max(0, col-1-len(concat_output)), min(len(line)-1, col+1)):
                        if data[row_i][col_i] == '*' and (row_i, col_i) not in coordinates:
                            coordinates[(row_i, col_i)] = [int(concat_output)]
                        elif data[row_i][col_i] == '*':
                            coordinates[(row_i, col_i)].append(
                                int(concat_output))
                concat_output = ''

    return sum(ab[0]*ab[1] for ab in coordinates.values() if len(ab) == 2)


def main():
    with open("./data.txt", "r") as file:
        data = file.read().splitlines()
        solution_one = one(data)
        print(solution_one)
        solution_two = two(data)
        print(solution_two)


if __name__ == "__main__":
    main()
