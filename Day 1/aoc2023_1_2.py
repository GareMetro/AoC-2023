import sys
import logging
import re

def letters_to_digit(letters):
    match letters:
        case "zero":
            return 0
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return -1

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_1_2.py <input_filepath>")
    exit(1)

text = open(file, "r").readlines()
res = 0
first_digit_finder = re.compile("[^\d]*(\d).*", re.DOTALL)
last_digit_finder = re.compile(".*(\d)[^\d]*", re.DOTALL)

first_digit_letters_finder = re.compile("(zero|one|two|three|four|five|six|seven|eight|nine)", re.DOTALL)
last_digit_letters_finder = re.compile(".*(zero|one|two|three|four|five|six|seven|eight|nine).*", re.DOTALL)

for elem in text:
    first_digit = first_digit_finder.match(elem)
    first_digit_index = elem.index(first_digit.groups(0)[0])

    last_digit = last_digit_finder.match(elem)
    last_digit_index = elem.rindex(last_digit.groups(0)[0])

    match = first_digit_letters_finder.search(elem)
    if match is not None:
        first_digit_letter_index = match.start()
        if first_digit_letter_index < first_digit_index:
            first_digit_int = letters_to_digit(elem[match.start():match.end()])
        else:
            first_digit_int = int(first_digit.groups(0)[0])
    else:
        first_digit_int = int(first_digit.groups(0)[0])

    match = last_digit_letters_finder.match(elem)
    if match is not None:
        last_digit_letter = match.groups(0)[0]
        last_digit_letter_index = elem.rindex(last_digit_letter)
        if last_digit_letter_index > last_digit_index:
            last_digit_int = letters_to_digit(last_digit_letter)
        else:
            last_digit_int = int(last_digit.groups(0)[0])
    else:
        last_digit_int = int(last_digit.groups(0)[0])

    res += 10 * first_digit_int + last_digit_int

print("Your Advent of code day 1 part 2 answer is : " + str(res))


