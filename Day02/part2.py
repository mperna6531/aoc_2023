#! /usr/bin/python
from functools import reduce

reducer = lambda x, y: x * y

with open('/home/michael/src/projects/aoc_2023/Day02/input.txt') as f:
    games = [game.rstrip() for game in f]

sum = 0

for game in games:
    max_counts = {}

    split = game.split(': ')
    game_num = int(split[0].replace('Game ', ''))
    sets_array = split[1].split(';')

    for set in sets_array:
        colors = set.split(',')

        for color in colors:
            color_split = color.strip().split(' ')
            color_value = int(color_split[0])
            color_name = color_split[1]

            if color_name not in max_counts or color_value > max_counts[color_name]:              
                max_counts[color_name] = color_value
    
    power = reduce(reducer, max_counts.values())
    sum += power
                
print(sum)
