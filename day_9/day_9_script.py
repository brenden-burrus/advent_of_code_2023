with open("day_9_input.txt") as file_contents:
    input = file_contents.read().splitlines()


###########################################################################
##### Part 1
###########################################################################


lines = [list(map(int, line.split(" "))) for line in input]
# print(lines)

def get_pattern(input):
    current_pattern = input
    pattern_list=[]
    pattern_list.append(current_pattern)
    answer_found = False
    while not answer_found:
        ind_pattern=[]
        for i in range(len(current_pattern)-1):
            ind_pattern.append(current_pattern[i+1] - current_pattern[i])
        
        pattern_list.append(ind_pattern)
        current_pattern = ind_pattern

        if ind_pattern[0] == 0 and all(i == 0 for i in ind_pattern):
            answer_found = True
            break
    return pattern_list

def get_next_value(input):
    for i in range(len(input)-1):
        input[i+1].append(input[i+1][-1] + input[i][-1])
    
    return input[-1][-1]


    return

answer_array = []
for line in lines:
    answer_array.append(get_next_value(get_pattern(line)[::-1]))

print(f"Part 1 answer is {sum(answer_array)}")


##########################################################################
#### Part 2
##########################################################################


lines = [list(map(int, line.split(" "))) for line in input]
# print(lines)

def get_pattern(input):
    current_pattern = input
    pattern_list=[]
    pattern_list.append(current_pattern)
    answer_found = False
    while not answer_found:
        ind_pattern=[]
        for i in range(len(current_pattern)-1):
            ind_pattern.append(current_pattern[i+1] - current_pattern[i])
        
        pattern_list.append(ind_pattern)
        current_pattern = ind_pattern

        if ind_pattern[0] == 0 and all(i == 0 for i in ind_pattern):
            answer_found = True
            break
    return pattern_list

def get_previous_value(input):
    input[0].insert(0, 0)
    
    for i in range(len(input)- 1):
        input[i+1].insert(0, (input[i+1][0] - input[i][0]))
    
    return input[-1][0]


    return

answer_array = []
for line in lines:
    answer_array.append(get_previous_value(get_pattern(line)[::-1]))

print(f"Part 2 answer is {sum(answer_array)}")