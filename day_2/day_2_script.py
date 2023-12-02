with open("day_2_input.txt") as file_contents:
    input = file_contents.read().splitlines()


#######################################################################
##### Part 1
#######################################################################

red_amount = 12
green_amount = 13
blue_amount = 14

total_value = 0

for game in input:
    game_number = game.split()[1].replace(":","")
    sets = game.split(":")[1].split(";")
    viability_list = []
    for handfuls in sets:
        handfuls.split(",")
        for cubes in handfuls.split(","):
            cube_num = cubes.split()[0]
            cube_color = cubes.split()[1]
            if cube_color == "red" and int(cube_num) > red_amount:
                viability = False
                break
            elif cube_color == "green" and int(cube_num) > green_amount:
                viability = False
                break
            elif cube_color == "blue" and int(cube_num) > blue_amount:
                viability = False
                break
            else:
                viability = True
            
        viability_list.append(viability)

    if False not in viability_list:
        total_value += int(game_number)

print(f"Part 1 Value: {total_value}")


#######################################################################
##### Part 1
#######################################################################

total_value = 0

for game in input:
    sets = game.split(":")[1].split(";")
    red_max = 0
    blue_max = 0
    green_max = 0
    for handfuls in sets:
        handfuls.split(",")
        for cubes in handfuls.split(","):
            cube_num = cubes.split()[0]
            cube_color = cubes.split()[1]
            if cube_color == "red" and int(cube_num) > red_max:
                red_max = int(cube_num)
            elif cube_color == "green" and int(cube_num) > green_max:
                green_max = int(cube_num)
            elif cube_color == "blue" and int(cube_num) > blue_max:
                blue_max = int(cube_num)

    total_value += (blue_max*red_max*green_max)

print(f"Part 2 Value: {total_value}")