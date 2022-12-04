import re
file = open("day4/input.txt")
lines = file.readlines()

subset_count = 0
overlap_count = 0

for line in lines:
    line = line.replace('\\n', '')
    pairs = line.split(",")
    pair1 = pairs[0].split("-")
    pair2 = pairs[1].split("-")
    pair2[1] = pair2[1].replace('\\n', '')
    x = range(int(pair1[0]), int(pair1[1])+1)
    y = range(int(pair2[0]), int(pair2[1])+1)
    if set(x).issubset(y) or set(y).issubset(x):
        print(pairs)
        subset_count += 1
    if len(set(x).intersection(y)) != 0:
        overlap_count += 1

print(subset_count)
print(overlap_count)
