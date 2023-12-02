#! /usr/bin/python

# 12 red cubes, 13 green cubes, and 14 blue cubes
CUBE_COUNTS = { 'red': 12, 'green': 13, 'blue': 14 }

with open('/home/michael/src/projects/aoc_2023/Day02/input.txt') as f:
    games = [game.rstrip() for game in f]

sum = 0

for game in games:
    valid_game = True

    split = game.split(': ')
    game_num = int(split[0].replace('Game ', ''))
    sets_array = split[1].split(';')

    for set in sets_array:
        colors = set.split(',')

        for color in colors:
            color_split = color.strip().split(' ')
            color_value = int(color_split[0])
            color_name = color_split[1]

            if color_value > CUBE_COUNTS[color_name]:
                valid_game = False
                break

        if (not valid_game):
            break
    
    if (valid_game):
        sum += game_num

print(sum)
