import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_4_2.py <input_filepath>")
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
cards = [1 for index in range(len(lines))]

for index in range(len(lines)):
    line = lines[index]
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
        card_number = cards[index]
        for card_index in range(index + 1, index + 1 + len(matches)):
            cards[card_index] += card_number

res = sum(cards)
print("Your Advent of code day 4 part 2 answer is : " + str(res))


