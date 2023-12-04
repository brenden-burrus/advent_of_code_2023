with open("day_4_input.txt") as file_contents:
    input = file_contents.read().splitlines()


##############################################################################################
##### Part 1
##############################################################################################

total_value = 0

for card in input:
    cleansed_card = card.split(":")[1].strip()
    winning_numbers, drawn_numbers = [list(map(int, num.split())) for num in cleansed_card.split("|")]
    n = 0
    for number in winning_numbers:
        if number in drawn_numbers:
            n+=1
    if n > 0:
        total_value += (2**(n-1))

print(f"Part 1 value: {total_value}")


##############################################################################################
##### Part 2
##############################################################################################

total_value = 0

card_dict = {}

card_num = 0

def add_value_to_dict(dict, key, value):
    try:
        card_dict[f"{key}"] += value
    except KeyError:
        card_dict[f"{key}"] = value
    except:
        print("I don't know what happened... *shrug*")

    return

for card in input:
    card_num += 1
    add_value_to_dict(card_dict, card_num, 1)
    current_card_amt = card_dict[f"{card_num}"]
    cleansed_card = card.split(":")[1].strip()
    winning_numbers, drawn_numbers = [list(map(int, num.split())) for num in cleansed_card.split("|")]
    n = 0
    for number in winning_numbers:
        if number in drawn_numbers:
            n+=1
    if n > 0:
        for x in range(1, n+1):
            add_value_to_dict(card_dict, (card_num+x), (1*current_card_amt))

for key in card_dict:
    total_value += card_dict[key]

print(f" Part 2 value: {total_value}")