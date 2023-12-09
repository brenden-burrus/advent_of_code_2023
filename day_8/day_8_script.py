from itertools import cycle

with open("day_8_input.txt") as file_contents:
    input = file_contents.read().splitlines()


###########################################################################
##### Part 1
###########################################################################

# instructions = input[0]
# network = input[2::]
# network_map = {}
# for line in network:
#     network_map[line.split("=")[0].strip()] = line.split("=")[1].strip().replace("(", "").replace(")", "").split(", ")

# instruction_cycle = cycle(instructions)

# num_steps = 0

# current_key = "AAA"

# while current_key != "ZZZ":
#     instruction = next(instruction_cycle)
    
#     if instruction == "L":
#         current_key = network_map[current_key][0]
#     elif instruction == "R":
#         current_key = network_map[current_key][1]
    
#     num_steps += 1


# print(f"Part 1 answer is: {num_steps} steps")


###########################################################################
##### Part 2
###########################################################################

instructions = input[0]
network = input[2::]
network_map = {}
for line in network:
    network_map[line.split("=")[0].strip()] = line.split("=")[1].strip().replace("(", "").replace(")", "").split(", ")

instruction_cycle = cycle(instructions)

num_steps = 0

current_keys = []
for key in network_map:
    if key[2] == "A":
        current_keys.append(key)

print(current_keys)

solution_found = False

while not solution_found:
    num_steps += 1
    instruction = next(instruction_cycle)
    for index, key in enumerate(current_keys):
        if instruction == "L":
            current_keys[index] = network_map[current_keys[index]][0]
        elif instruction == "R":
            current_keys[index] = network_map[current_keys[index]][1]
    
    # print(f"new keys: {current_keys}")
    temp_num = 0
    for key in current_keys:
        if key[2] == "Z":
            continue
        else:
            temp_num += 1
    
    if temp_num == 0:
        solution_found = True


print(f"Part 2 answer is: {num_steps} steps")