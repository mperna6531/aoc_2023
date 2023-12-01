#! /usr/bin/python

WORDS = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

sum = 0

for line in lines:
    for idx, char in enumerate(line):
        if char.isdigit():
            firstDigitIndex = idx
            firstDigit = char
            break

    for idx, char in enumerate(reversed(line)):
        if char.isdigit():
            lastDigitIndex = len(line) -1 - idx
            lastDigit = char
            break
    
    for word, value in WORDS.items():
        first_idx = line.find(word)
        last_idx = line.rfind(word)

        if first_idx == -1 and last_idx == -1:
            continue

        if (first_idx < firstDigitIndex):
            firstDigitIndex = first_idx
            firstDigit = value

        if (last_idx > lastDigitIndex):
            lastDigitIndex = last_idx
            lastDigit = value

    lineValue = firstDigit + lastDigit
    sum += int(lineValue)

print(sum)
