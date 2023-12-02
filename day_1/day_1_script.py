import re

with open("day_1_input.txt") as file_contents:
    input = file_contents.read().splitlines()

###############################################################################
#### PART 1
###############################################################################

def part_1(input):
    total_value = 0

    for string in input:
        left_found = False
        left_value = 0
        right_found = False
        right_value = 0
        for x in range(len(string)):
            if string[x].isdigit() and not left_found:
                left_value = string[x]
                left_found = True
            if string[-x-1].isdigit() and not right_found:
                right_value = string[-x-1]
                right_found = True
            if left_found and right_found:
                break
        total_value += int(str(left_value) + str(right_value))

    return total_value

print(part_1(input))

###############################################################################
#### PART 2
###############################################################################

number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def search_for_number(string: str, number_strings: list, right_side: bool):
    if right_side == True:
        string = string[::-1]

    for y in range(len(number_strings)):
        if re.search(number_strings[y], string) != None:
            return (y+1)
    
    return None
        


def get_left_value(string):
    number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    value = 0
    number_found = False
    working_string = ""

    for x in range(len(string)):
        if string[x].isdigit():
            value = string[x]
            number_found = True
        elif string[x].isalpha():
            working_string = working_string + string[x]
            string_value = search_for_number(working_string, number_strings, False)
            if string_value != None:
                value = string_value
                number_found = True

        if number_found:
            break

    return value


def get_right_value(string):
    number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    value = 0
    number_found = False
    working_string = ""

    for x in range(len(string)):
        if string[-x-1].isdigit():
            value = string[-x-1]
            number_found = True
        elif string[-x-1].isalpha():
            working_string = working_string + string[-x-1]
            string_value = search_for_number(working_string, number_strings, True)
            if string_value != None:
                value = string_value
                number_found = True

        if number_found:
            break

    return value        
        

def part_2(input):
    total_value = 0
    
    for string in input:
        left_value = get_left_value(string)
        right_value = get_right_value(string)

        total_value += int(str(left_value) + str(right_value))
    
    return total_value

print(part_2(input))