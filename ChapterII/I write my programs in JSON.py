import re

# Sum of all numbers in document is 111754

with open('JSON-list.txt') as file:
    text = file.read()

numbers = re.findall(r'(-*\d+)', text)


def summary(input):
    return sum([int(n) for n in input])


print(summary(numbers))
