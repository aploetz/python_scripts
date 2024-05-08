import random

from random import randint

import sys

minDieValue = 1
maxDieValue = 6

def roll_dice(num_dice):
    dice = []
    
    for indexJ in range(0,num_dice):
        dice.append(roll_die())

    return dice

def roll_die():
    return random.randint(minDieValue,maxDieValue)

def decide(dice):
    diceLen = len(dice)
    rolledA = [0] * 7
    dieIndex = 0;

    #generate matrix of what was rolled
    for roll in dice:
        #testing
        #print roll
        dieIndex = roll
        count = rolledA[roll] + 1
        rolledA[dieIndex] = count

    #testing
    #print "len(dice) = %d" % (diceLen + 1)
    highVal = 0
    sndHighVal = 0
    for indexK in range(1,maxDieValue + 1):
        if (indexK > 0):
            value = rolledA[indexK]
            #testing
            print("%d = %d" % (indexK, value))

            if (value > highVal):
                sndHighVal = highVal
                highVal = value
            else:
                if (value > sndHighVal):
                    sndHighVal = value
            
    if (highVal == 5):
        print("Yahtzee!")
    else:
        if (rolledA[1] == rolledA[2] == rolledA[3] == rolledA[4] == rolledA[5]) or (rolledA[2] == rolledA[3] == rolledA[4] == rolledA[5] == rolledA[6]):
            print("Large Straight")
        else:
            if (highVal == 4):
                print("Four-of-a-Kind")
            else:
                if (rolledA[1] >= 1 and rolledA[2] >= 1 and rolledA[3] >= 1 and rolledA[4] >= 1) or \
                 (rolledA[2] >= 1 and rolledA[3] >= 1 and rolledA[4] >= 1 and rolledA[5] >= 1) or \
                 (rolledA[3] >= 1 and rolledA[4] >= 1 and rolledA[5] >= 1 and rolledA[6] >= 1):
                    print("Small Straight")
                else:
                    if (highVal == 3):
                        if (sndHighVal == 2):
                            print("Full House")
                        else:
                            print("Three-of-a-Kind")
            
#start by rolling all 5
hand = roll_dice(5)

#show your hand
print(hand)

hold = decide(hand)
