file = open("day3/input.txt")
lines = file.readlines()
sum = 0

file2 = open("day3/input2.txt")


def find_intersection(left, right):
    item = set(left).intersection(right)
    print(item)
    return find_priority(item)


def find_priority(item):
    item_sum = 0
    while len(item) != 0:
        item_value = ord(item.pop())
        if item_value >= 97:
            item_sum += item_value - 96
        else:
            item_sum += item_value - 38
    return item_sum


def find_intersection(one, two, three):
    set1 = set(one).intersection(two)
    return find_priority(set1.intersection(three))


# for line in lines:
#     # print(line[0:int(len(line)/2)-1]+" "+line[int(len(line)/2)-1:len(line)])
#     sum += find_intersection(
#         line[0:int(len(line)/2)], line[int(len(line)/2):len(line)])
#     print(line[0:int(len(line)/2)] + " "+line[int(len(line)/2):len(line)])
# print(sum)

sum = 0
for i in range(3, len(lines)+1, 3):
    sum += find_intersection(lines[i-3].replace('\n', ''),
                             lines[i-2].replace('\n', ''), lines[i-1].replace('\n', ''))
print(sum)

# print()
