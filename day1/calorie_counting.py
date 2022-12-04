f = open("day1/input.txt")
lines = f.readlines()
calories = 0
max = [0, 0, 0]


def max_calories(calories, max_values):
    temp = calories
    for max_value in reversed(max_values):
        if temp > max_value:
            max_values[max_values.index(max_value)] = temp
            temp = max_value
    return max_values


for x in lines:
    if x.strip():
        calories += int(x.strip())
        continue
    max = max_calories(calories, max)
    calories = 0

max = max_calories(calories, max)

print(sum(max))
