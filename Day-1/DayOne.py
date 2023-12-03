import re
from io import TextIOWrapper

"""
Nolan Gregory
Advent of Code 2023
Day 1

- Solved: Yes
- Stars gained: 2
- Difficulty: 2/10
"""

mapping: dict[str, int] = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def part_one(file: TextIOWrapper) -> int:
    """
    Prompt: On each line, the calibration value can be found by combining the first digit and the 
    last digit (in that order) to form a single two-digit number.

    Solution: 53334

    Explaination: We know each line must have 1 or more digits, therefore we can simply create a list of all digits,
    appending them as we encounter them, and concat. the zeroth and n-1 char, adding the int representation to a running
    total.

    Alternate Solution: Use two pointers, one at the head, and one at the tail. Walk each pointer closer together until a
    leftmost digit is found, a rightmost digit is found, or idx == idx of both ptrs. 
    """
    # # Part One (Normal)
    # total: int = 0
    # for line in file:
    #     if x := re.findall(r'[0-9]', line):
    #         total += int(x[0] + x[-1])
    # # return total

    # # Part One (epic)
    return sum(int(x[0] + x[-1]) for line in file if (x := re.findall(r'\d', line)))


def part_two(file: TextIOWrapper) -> int:
    """
    Prompt: Identical to part one, except that "one", "two", etc. map to their corresponding integer values.

    Solution: 52834

    Explaination: Pretty simple, we just need to create an ordered mapping of the start indexes of each substring, as well
    as the index of all digits. Using an array of arrays (inner array storing the index and the associated value), we can
    just concat all arrays, sort by n[0], and calculate via the first index of the inner array (as that stores the value).

    Caveats: Duplicates exist, so a simple "find()" function will not work, unless attempts were made to brute through the
    find until it returned a -1 for each possible digit. Regex is really supreme here.

    Alternate Solution: You can use a complex regex to find all possibilties, returning the matches, but that would look nasty.
    Addditionally, you could use a similar technique to part_one and then just use the regex return to perform similar logic to
    what is done below. 
    """
    # Part Two (Normal)
    total: int = 0
    for line in file:
        coords = sorted([[iter.start(), str(key)] for char, key in mapping.items()
                         for iter in re.finditer(char, line)] + [[idx, val] for idx, val in enumerate(line) if val.isdigit()])
        total += int(coords[0][1] + coords[-1][1])
    return total

    # Part Two (Epic)
    return sum(int(str(positions[0][1]) + str(positions[-1][1])) if positions else 0 for line in file for positions in [sorted([(int(char), int(line[char])) for char in range(
        len(line)) if line[char].isdigit()] + [(iter.start(), key) for char, key in mapping.items() for iter in re.finditer(re.escape(char), line)], key=lambda x: x[0])])


def DayOne():
    with open("./data.txt", "r") as file:
        file = file.read().splitlines()
        one = part_one(file)
        two = part_two(file)
        print(f"Solution to part one: {one}\nSolution to part two: {two}")


if __name__ == "__main__":
    DayOne()
