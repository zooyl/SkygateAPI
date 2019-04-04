# There are 383 valid Skyphrases

with open('Skyphrase_list.txt') as file:
    text = file.readlines()

total = 0
for line in text:
    b = line.split()
    c = set(b)
    if len(b) == len(c):
        total += 1

print(total)
