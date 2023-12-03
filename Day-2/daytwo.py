import re
from io import TextIOWrapper

"""
Nolan Gregory
Advent of Code 2023
Day 2

- Solved: Yes
- Stars gained: 2
- Difficulty: 3/10
"""


def one(data: TextIOWrapper) -> int:
    """
    Prompt: You are given records for games (looks like Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green). Determine which 
    games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
    Return the sum of the IDs of games which satisfy the constraints.

    Solution: 2149

    Explaination: Use regex to split on the colons and semi colons of the string, which returns the game # as idx 0 and the
    colors as idx n-1. Use list unpacking to store the color values, then turn them into their own elements by splitting on
    commas, and determine if all the integers associated with each color is less than the threshold. Return the sum of the
    games that have colors <= threshold.

    Caveats: Initially read the problem wrong and thought that the sum was based on each game, not each subgame.

    Alternate Solution: N/a. 
    """
    thresholds: dict[str, int] = {"red": 12, "green": 13, "blue": 14}
    total_sum: int = 0
    for line in data:
        game, *bundle = re.split(': |;', line)
        bundle = [item.strip().split(',') for item in bundle]
        valid = all(int(value.split()[0]) <= thresholds.get(
            value.split()[1], 0) for item in bundle for value in item)
        total_sum += int(game.split()[1]) if valid else 0
    return total_sum


def two(data):
    """
    Prompt: The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The 
    power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding 
    up these five powers produces the sum 2286. For each game, find the minimum set of cubes that must have been present. 
    Return the sum of the power of these sets.

    Solution: 71274

    Explaination: Similar to above, just modified algorith to return the sum of the product of each rounds cubes.

    Caveats: N/a.

    Alternate Solution: N/a. 
    """
    total = 0
    for line in data:
        max_values = {"red": 0, "green": 0, "blue": 0}
        _, *data = re.split(': |;', line)
        values = [item.strip().split()
                  for sublist in data for item in sublist.split(',')]
        for value, color in values:
            value = int(value)
            max_values[color] = max(max_values[color], value)
        total += max_values["red"] * max_values["green"] * max_values["blue"]
    return total


def main():
    with open("./data.txt", "r") as file:
        data = file.read().splitlines()
        solution_one = one(data)
        print(solution_one)
        solution_two = two(data)
        print(solution_two)


if __name__ == "__main__":
    main()
