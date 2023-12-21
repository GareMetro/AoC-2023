import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_4_1.py <input_filepath>")
    exit(1)


def clean_list(numbers_list: list):
    index = 0
    while index < len(numbers_list):
        try:
            x = int(numbers_list[index])
            index += 1
        except ValueError:
            numbers_list.pop(index)


lines = open(file, "r").readlines()
res = 0

for line in lines:
    # Get the numbers
    numbers = line.split(':')[1].split('|')

    winning_numbers = numbers[0].split(' ')
    clean_list(winning_numbers)
    winning_numbers = [int(number) for number in winning_numbers]

    your_numbers = numbers[1].split(' ')
    clean_list(your_numbers)
    your_numbers = [int(number) for number in your_numbers]

    # Get the intersection
    matches = set(winning_numbers) & set(your_numbers)
    if len(matches) > 0:
        res += pow(2, len(matches) - 1)

print("Your Advent of code day 4 part 1 answer is : " + str(res))


