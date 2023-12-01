#! /usr/bin/python

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

sum = 0

for line in lines:
    for char in line:
        if char.isdigit():
            firstDigit = char
            break

    for char in reversed(line):
        if char.isdigit():
            lastDigit = char
            break
    
    lineValue = firstDigit + lastDigit
    sum += int(lineValue)

print(sum)
