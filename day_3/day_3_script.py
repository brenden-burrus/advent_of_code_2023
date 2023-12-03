with open("day_3_input.txt") as file_contents:
    input = file_contents.read().splitlines()

###################################################################
####### Part 1
###################################################################


# coordinates = set()


# for row_num, row in enumerate(input):
#     for col_num, col_content in enumerate(row):
#         if col_content == "." or col_content.isdigit():
#             continue
#         for adj_rows in [row_num - 1, row_num, row_num + 1]:
#             for adj_cols in [col_num -1, col_num, col_num + 1]:
#                 if adj_rows < 0 or adj_rows >= len(input) or adj_cols < 0 or adj_cols >= len(input[adj_rows]) or not input[adj_rows][adj_cols].isdigit():
#                     continue
#                 while adj_cols > 0 and input[adj_rows][adj_cols-1].isdigit():
#                     adj_cols -= 1
#                 coordinates.add((adj_rows, adj_cols))

# number_set = []

# for r, c in coordinates:
#     num = ""
#     while c < len(input[r]) and input[r][c].isdigit():
#         num += input[r][c]
#         c += 1
#     if num != "":
#         number_set.append(int(num))

# print(f"part 1 value = {sum(number_set)}")


###################################################################
####### Part 2
###################################################################


coordinate_sets = []


for row_num, row in enumerate(input):
    for col_num, col_content in enumerate(row):
        temp_coord = set()
        if col_content != "*":
            continue
        for adj_rows in [row_num - 1, row_num, row_num + 1]:
            for adj_cols in [col_num -1, col_num, col_num + 1]:
                if adj_rows < 0 or adj_rows >= len(input) or adj_cols < 0 or adj_cols >= len(input[adj_rows]) or not input[adj_rows][adj_cols].isdigit():
                    continue
                while adj_cols > 0 and input[adj_rows][adj_cols-1].isdigit():
                    adj_cols -= 1
                temp_coord.add((adj_rows, adj_cols))
        if len(temp_coord) == 2:
            coordinate_sets.append(temp_coord)    

ratios = []

for set in coordinate_sets:
    temp_num = 0
    for r, c in set:
        num = ""
        while c < len(input[r]) and input[r][c].isdigit():
            num += input[r][c]
            c += 1
        if num != "":
            if temp_num == 0:
                temp_num += int(num)
            else:
                ratios.append(temp_num*int(num))

print(f"part 2 value = {sum(ratios)}")