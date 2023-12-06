with open("day_5_input.txt") as file_contents:
    input = file_contents.read().splitlines()


##################################################################################################################
##### Part 1
##################################################################################################################

# seed_nums = input[0].split(":")[1].strip().split(" ")
# all_mappings = input[2::]

# ind_mappings = []

# for x in range(len(all_mappings)):
#     if all_mappings[x] == "":
#         continue
#     elif all_mappings[x][0].isalpha():
#         temp_array = []

#         n = x
#         temp_array.append(all_mappings[x])
#         # print(temp_array)
#         while n != (len(all_mappings) - 1):
#             n += 1
#             if all_mappings[n] == "" or all_mappings[n][0].isalpha():
#                 break
#             else:
#                 temp_array.append(all_mappings[n])
#         ind_mappings.append(temp_array)
#     else:
#         continue


# Brute Force Method, not going to work for large numbers lol
#
# def get_mapping(source_nums, dest_map):
#     map_nums = dest_map[1::]
#     source_array = []
#     dest_array = []
#     for map in map_nums:
#         temp_map = map.split(" ")
#         print(temp_map)
#         for x in range(int(temp_map[2])):
#             dest_array.append(int(temp_map[0])+x)
#             source_array.append(int(temp_map[1])+x)

#     mapping_array = []
#     for num in source_nums:
#         try:
#             temp_index = source_array.index(int(num))
#         except ValueError:
#             mapping_array.append(int(num))
#         else:
#             mapping_array.append(dest_array[temp_index])

#     print(mapping_array)

#     return mapping_array


# def get_mapping(source_nums, dest_maps):
#     map_nums = dest_maps[1::]
#     mapping = []
#     for num in source_nums:
#         for map in map_nums:
#             temp_map = map.split(" ")
#             if int(num) >= int(temp_map[1]) and int(num) <= int(temp_map[1])+int(temp_map[2]):
#                 mapping.append(int(temp_map[0]) + (int(num) - int(temp_map[1])))
#                 break
#             elif map == map_nums[len(map_nums)-1]:
#                 mapping.append(int(num))

#     return mapping


# soil_nums = get_mapping(seed_nums, ind_mappings[0])
# fertilizer_nums = get_mapping(soil_nums, ind_mappings[1])
# water_nums = get_mapping(fertilizer_nums, ind_mappings[2])
# light_nums = get_mapping(water_nums, ind_mappings[3])
# temp_nums = get_mapping(light_nums, ind_mappings[4])
# humid_nums = get_mapping(temp_nums, ind_mappings[5])
# location_nums = get_mapping(humid_nums, ind_mappings[6])

# print(f"Part 1 answer is: {min(location_nums)}")


##################################################################################################################
##### Part 2 (not finished)
##################################################################################################################

seed_nums = input[0].split(":")[1].strip().split(" ")
all_mappings = input[2::]

ind_mappings = []

def get_range_of_seeds(seed_nums):
    new_seed_array = []
    for x in range(len(seed_nums)):
        if x % 2 == 0 or x == 0:
            temp_array = [int(seed_nums[x]), int(seed_nums[x]) + int(seed_nums[x+1]) - 1]
            new_seed_array.append(temp_array)
    
    return new_seed_array


def overlap(x, y):
    if not range_overlapping(x, y):
        return set()
    return set(range(max(x.start, y.start), min(x.stop, y.stop)+1))


def range_overlapping(x, y):
    if x.start == x.stop or y.start == y.stop:
        return False
    return x.start <= y.stop and y.start <= x.stop


for x in range(len(all_mappings)):
    if all_mappings[x] == "":
        continue
    elif all_mappings[x][0].isalpha():
        temp_array = []

        n = x
        temp_array.append(all_mappings[x])
        # print(temp_array)
        while n != (len(all_mappings) - 1):
            n += 1
            if all_mappings[n] == "" or all_mappings[n][0].isalpha():
                break
            else:
                temp_array.append(all_mappings[n])
        ind_mappings.append(temp_array)
    else:
        continue


def get_mapping(source_array, dest_maps):
    map_nums = dest_maps[1::]
    mapping = []
    for array in source_array:
        for map in dest_maps:
            source = int(dest_maps[1])
            dest = int(dest_maps[0])
            range = int(dest_maps[2])

            temp_list = list()

    return mapping


# soil_nums = get_mapping(seed_nums, ind_mappings[0])
# fertilizer_nums = get_mapping(soil_nums, ind_mappings[1])
# water_nums = get_mapping(fertilizer_nums, ind_mappings[2])
# light_nums = get_mapping(water_nums, ind_mappings[3])
# temp_nums = get_mapping(light_nums, ind_mappings[4])
# humid_nums = get_mapping(temp_nums, ind_mappings[5])
# location_nums = get_mapping(humid_nums, ind_mappings[6])

# print(f"Part 1 answer is: {min(location_nums)}")