with open("day_7_input.txt") as file_contents:
    input = file_contents.read().splitlines()


###########################################################################
##### Part 1
###########################################################################

def calculate_hand(hand):
    temp_hand = [char for char in hand.split()[0]]
    print(char_replace(temp_hand))
    return


def char_replace(hand):
    for index, char in enumerate(hand):
        if char == "T": 
            hand[index] = "10"
        elif char == "J":
            hand[index]= "11"
        elif char == "Q":
            hand[index]= "12"
        elif char == "K":
            hand[index]= "13"
        elif char =="A":
            hand[index]= "14"
    return hand


for i in range(len(input)):
    calculate_hand(input[i])


