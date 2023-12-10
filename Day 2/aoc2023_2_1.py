import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_2_1.py <input_filepath>")
    exit(1)

red = 12
green = 13
blue = 14

def color_check(value, color):
    match color:
        case "blue":
            return value <= blue
        case "red":
            return value <= red
        case "green":
            return value <= green
        case _:
            return False


text = open(file, "r")
id_finder = re.compile("Game (\d*):*")
ball_counter = re.compile(" (\d*) (blue|red|green)[,|;]?")
res = 0
for line in text:
    m = id_finder.match(line)
    game_id = int(m.groups()[0])
    stripped_line = line[m.span()[1]:]
    ball_match = ball_counter.match(stripped_line)
    game_valid = True
    while ball_match:
        number = int(ball_match.groups()[0])
        color = ball_match.groups()[1]
        if not color_check(number, color):
            game_valid = False
            break

        stripped_line = stripped_line[ball_match.span()[1]:]
        ball_match = ball_counter.match(stripped_line)

    if game_valid:
        res += game_id

print("Your Advent of code day 2 part 1 answer is : " + str(res))


