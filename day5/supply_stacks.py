stack_file = open("day5/stack_input.txt")
instruction_file = open("day5/input.txt")
stacks = []
lines = stack_file.readlines()
for x in lines:
    stacks.append(x.split(","))
instructions = instruction_file.readlines()
# solution1
# for line in instructions:
#     instruction = line.split(" ")
#     for i in range(0, int(instruction[1])):
#         pop_stack = stacks[int(instruction[3])-1].pop()
#         stacks[int(instruction[5])-1].append(pop_stack)

# solution2
for line in instructions:
    instruction = line.split(" ")
    stack_len = len(stacks[int(instruction[3])-1])
    for i in range(stack_len - int(instruction[1]), stack_len):
        print(stack_len - int(instruction[1]))
        pop_stack = stacks[int(
            instruction[3])-1].pop(stack_len - int(instruction[1]))
        stacks[int(instruction[5])-1].append(pop_stack)
# print array
for i in range(0, len(stacks)):
    print(stacks[i])
