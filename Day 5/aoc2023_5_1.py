import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_5_1.py <input_filepath>")
    exit(1)


def clean_list(numbers_list: list):
    index = 0
    while index < len(numbers_list):
        try:
            x = int(numbers_list[index])
            index += 1
        except ValueError:
            numbers_list.pop(index)


def convert_map(input_list: list, input_map: file):
    """Converts a list from one section to the next, given a file with a cursor placed before the section
    This will advance the cursor past the section, making the function usable multiple times in sequence"""

    # Go to the first line of the section
    line = input_map.readline()
    while len(line) == 0 or not line[0].isdigit():
        line = input_map.readline()

    # Convert the list
    output_list = []
    while len(line) > 0 and line[0].isdigit():
        map_line = line.split(' ')
        clean_list(map_line)
        map_line = [int(value) for value in map_line]
        input_index = 0
        while input_index < len(input_list):
            if map_line[1] <= input_list[input_index] < map_line[1] + map_line[2]:
                output_list.append(map_line[0] + input_list[input_index] - map_line[1])
                input_list.pop(input_index)
            else:
                input_index += 1
        line = input_map.readline()

    # Add the unchanged elements
    for elem in input_list:
        output_list.append(elem)

    return output_list


input_file = open(file, "r")
res = 0

# Seeds line
line = input_file.readline()
numbers = line.split(':')[1].split(' ')
clean_list(numbers)
numbers = [int(seed) for seed in numbers]
# Convert the list through the 7 maps
for section in range(7):
    numbers = convert_map(numbers, input_file)

res = sorted(numbers)[0]

print("Your Advent of code day 5 part 1 answer is : " + str(res))


