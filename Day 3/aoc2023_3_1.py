import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_3_1.py <input_filepath>")
    exit(1)


lines = open(file, "r").readlines()
number_finder = re.compile("[^\d]*(\d+)", re.DOTALL) #Parses everything up to the first number
symbol_finder = re.compile("[\d.]*[^\d.\n]", re.DOTALL) #Parses averything up to the first non-number non-dot character
res = 0

previous_line = ""
current_line = lines[0]
next_line = lines[1]
line_length = len(current_line)

#First line
match = number_finder.match(current_line)
current_char = 0
while match:
    for elem in [current_line, next_line]:
        check_symbol = elem[max(current_char + match.span()[1] - len(match.groups()[0]) - 1, 0):min(current_char + match.span()[1] + 1, line_length)]
        if symbol_finder.match(check_symbol):
            res += int(match.groups()[0])
            break
    current_char += match.span()[1]
    match = number_finder.match(current_line[current_char:])

#Middle lines
for line in lines[2:]:
    previous_line = current_line
    current_line = next_line
    next_line = line

    match = number_finder.match(current_line)
    current_char = 0
    while match:
        for elem in [previous_line, current_line, next_line]:
            check_symbol = elem[max(current_char + match.span()[1] - len(match.groups()[0]) - 1, 0):min(current_char + match.span()[1] + 1, line_length)]
            if symbol_finder.match(check_symbol):
                res += int(match.groups()[0])
                break
        current_char += match.span()[1]
        match = number_finder.match(current_line[current_char:])

previous_line = current_line
current_line = next_line

#Last line
match = number_finder.match(current_line)
current_char = 0
while match:
    for elem in [previous_line, current_line]:
        check_symbol = elem[max(current_char + match.span()[1] - len(match.groups()[0]) - 1, 0):min(current_char + match.span()[1] + 1, line_length)]
        if symbol_finder.match(check_symbol):
            res += int(match.groups()[0])
            break
    current_char += match.span()[1]
    match = number_finder.match(current_line[current_char:])

print("Your Advent of code day 3 part 1 answer is : " + str(res))


