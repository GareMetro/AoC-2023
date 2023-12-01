import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_1_1.py <input_filepath>")
    exit(1)

text = open(file, "r").readlines()
res = 0
first_digit_finder = re.compile("[^\d]*(\d).*", re.DOTALL)
last_digit_finder = re.compile(".*(\d)[^\d]*", re.DOTALL)
for elem in text:
    first_digit = first_digit_finder.match(elem)
    last_digit = last_digit_finder.match(elem)
    res += int(first_digit.groups(0)[0] + last_digit.groups(0)[0])

print("Your Advent of code day 1 part 1 answer is : " + str(res))


