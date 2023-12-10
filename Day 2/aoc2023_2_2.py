import sys
import logging
import re

logger = logging.getLogger()
try:
    file = sys.argv[1]
except IndexError:
    logger.warning("Usage : python aoc2023_2_1.py <input_filepath>")
    exit(1)


text = open(file, "r")
ball_counter = re.compile(" (\d*) (blue|red|green)[,|;]?")
res = 0
for line in text:
    line = line.split(":")[1]
    max_blue = 0
    max_red = 0
    max_green = 0
    ball_match = ball_counter.match(line)
    while ball_match:
        number = int(ball_match.groups()[0])
        color = ball_match.groups()[1]
        match color:
            case "blue":
                max_blue = max(max_blue, number)
            case "red":
                max_red = max(max_red, number)
            case "green":
                max_green = max(max_green, number)

        line = line[ball_match.span()[1]:]
        ball_match = ball_counter.match(line)

    res += max_blue * max_red * max_green

print("Your Advent of code day 2 part 2 answer is : " + str(res))


