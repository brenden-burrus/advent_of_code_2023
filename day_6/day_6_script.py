from functools import reduce

with open("day_6_input.txt") as file_contents:
    input = file_contents.read().splitlines()


###########################################################################
##### Part 1
###########################################################################

times, distances = [list(map(int, line.split(":")[1].split())) for line in input]

value_array = []

for y in range(len(times)):
    amount = 0
    time = times[y]
    for x in range(time):
        distance = (time - x)*x
        if distance > distances[y]:
            amount+=1
    value_array.append(amount)

total_value = reduce(lambda x,y: x*y, value_array)

print(f"Part 1 Value: {total_value}")


###########################################################################
##### Part 2
###########################################################################

times, distances = [list(map(int, line.replace(" ","").split(":")[1].split())) for line in input]

value_array = []

for y in range(len(times)):
    amount = 0
    time = times[y]
    for x in range(time):
        distance = (time - x)*x
        if distance > distances[y]:
            amount+=1
    value_array.append(amount)

total_value = reduce(lambda x,y: x*y, value_array)

print(f"Part 2 Value: {total_value}")
