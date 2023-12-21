import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_3_2.py <input_filepath>")
    exit(1)


lines = open(file, "r").readlines()
star_finder = re.compile("[^*]*\\*", re.DOTALL) #Parses everything up to the first star
res = 0

previous_line = ""
current_line = lines[0]
next_line = lines[1]
line_length = len(current_line)

#First line
match = star_finder.match(current_line)
current_char = 0
while match:
    numbers = []
    left = current_char + match.span()[1]-1
    right = current_char + match.span()[1]-1

    while left >= 0 and next_line[left].isdigit():
        left -= 1

    while right <= line_length - 1 and next_line[right].isdigit():
        right += 1

    if right != left: #Found a digit above/below the gear
        numbers.append(int(next_line[left + 1:right]))

    else: #No digit above/below the gear = check diagonals
        left -= 1
        right += 1

        while left >= 0 and next_line[left].isdigit():
            left -= 1

        while right <= line_length - 1 and next_line[right].isdigit():
            right += 1

        if left != current_char + match.span()[1] - 2:
            numbers.append(int(next_line[left + 1:current_char + match.span()[1]-1]))

        if right != current_char + match.span()[1]:
            numbers.append(int(next_line[current_char + match.span()[1]:right]))

    #Check current line before and after the gear
    left = current_char + match.span()[1] - 2
    right = current_char + match.span()[1]

    while left >= 0 and current_line[left].isdigit():
        left -= 1

    while right <= line_length - 1 and current_line[right].isdigit():
        right += 1

    if left != current_char + match.span()[1] - 2:
        numbers.append(int(current_line[left + 1:current_char + match.span()[1] - 1]))

    if right != current_char + match.span()[1]:
        numbers.append(int(current_line[current_char + match.span()[1]:right]))

    if len(numbers) == 2:
        res += numbers[0] * numbers[1]

    current_char += match.span()[1]
    match = star_finder.match(current_line[current_char:])

#Middle lines
for line in lines[2:]:
    previous_line = current_line
    current_line = next_line
    next_line = line

    match = star_finder.match(current_line)
    current_char = 0
    while match:
        numbers = []
        for elem in [next_line, previous_line]:
            left = current_char + match.span()[1] - 1
            right = current_char + match.span()[1] - 1

            while left >= 0 and elem[left].isdigit():
                left -= 1

            while right <= line_length - 1 and elem[right].isdigit():
                right += 1

            if right != left:  # Found a digit above/below the gear
                numbers.append(int(elem[left + 1:right]))

            else:  # No digit above/below the gear = check diagonals
                left -= 1
                right += 1

                while left >= 0 and elem[left].isdigit():
                    left -= 1

                while right <= line_length - 1 and elem[right].isdigit():
                    right += 1

                if left != current_char + match.span()[1] - 2:
                    numbers.append(int(elem[left + 1:current_char + match.span()[1] - 1]))

                if right != current_char + match.span()[1]:
                    numbers.append(int(elem[current_char + match.span()[1]:right]))

        # Check current line before and after the gear
        left = current_char + match.span()[1] - 2
        right = current_char + match.span()[1]

        while left >= 0 and current_line[left].isdigit():
            left -= 1

        while right <= line_length - 1 and current_line[right].isdigit():
            right += 1

        if left != current_char + match.span()[1] - 2:
            numbers.append(int(current_line[left + 1:current_char + match.span()[1] - 1]))

        if right != current_char + match.span()[1]:
            numbers.append(int(current_line[current_char + match.span()[1]:right]))

        if len(numbers) == 2:
            res += numbers[0] * numbers[1]

        current_char += match.span()[1]
        match = star_finder.match(current_line[current_char:])

#Last line
previous_line = current_line
current_line = next_line

match = star_finder.match(current_line)
current_char = 0
while match:
    numbers = []
    left = current_char + match.span()[1] - 1
    right = current_char + match.span()[1] - 1

    while left >= 0 and previous_line[left].isdigit():
        left -= 1

    while right <= line_length - 1 and previous_line[right].isdigit():
        right += 1

    if right != left:  # Found a digit above/below the gear
        numbers.append(int(previous_line[left + 1:right]))

    else:  # No digit above/below the gear = check diagonals
        left -= 1
        right += 1

        while left >= 0 and previous_line[left].isdigit():
            left -= 1

        while right <= line_length - 1 and previous_line[right].isdigit():
            right += 1

        if left != current_char + match.span()[1] - 2:
            numbers.append(int(previous_line[left + 1:current_char + match.span()[1] - 1]))

        if right != current_char + match.span()[1]:
            numbers.append(int(previous_line[current_char + match.span()[1]:right]))

    # Check current line before and after the gear
    left = current_char + match.span()[1] - 2
    right = current_char + match.span()[1]

    while left >= 0 and current_line[left].isdigit():
        left -= 1

    while right <= line_length - 1 and current_line[right].isdigit():
        right += 1

    if left != current_char + match.span()[1] - 2:
        numbers.append(int(current_line[left + 1:current_char + match.span()[1] - 1]))

    if right != current_char + match.span()[1]:
        numbers.append(int(current_line[current_char + match.span()[1]:right]))

    if len(numbers) == 2:
        res += numbers[0] * numbers[1]

    current_char += match.span()[1]
    match = star_finder.match(current_line[current_char:])

print("Your Advent of code day 3 part 2 answer is : " + str(res))


