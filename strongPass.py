import sys

from random import randint

#generate strong char passwords

#limits (valid values are 0 or 1)
SpecialSet1_Upper=0
SpecialSet2_Lower=0
SpecialSet3_Number=0
SpecialSet4_SpecChar=0

#specialSetCounter must be >= 3 for password to be valid
specialSetCounter=0;

#for each char generated, increment its core set
upperCounter=0
lowerCounter=0
numberCounter=0
specCharCounter=0


def is_number(s):
    return s.isdigit()

if len(sys.argv) > 1:
    characters = sys.argv[1]

    if is_number(characters):
        password = ""
        numCharacters=int(characters)
        for intCounterJ in range(1,numCharacters + 1):
            remainingChars=numCharacters - intCounterJ
            randomNumber = randint(33,126)
            #print(chr(randomNumber))

            if randomNumber >= 65 and randomNumber <= 90:
            #uppercase
                upperCounter += 1
                SpecialSet1_Upper=1
            elif randomNumber >= 97 and randomNumber <= 122:
            #lowercase
                lowerCounter += 1
                SpecialSet2_Lower=1
            elif randomNumber >= 48 and randomNumber <= 57:
            #numeric
                numberCounter += 1
                SpecialSet3_Number=1
            else:
            #other special char
                specCharCounter += 1
                SpecialSet4_SpecChar=1
                
            #check to see if we still need to gen a character for a different set
            #a valid password will register a SpecialSetN sum of at least 3
            specSetValue=SpecialSet1_Upper + SpecialSet2_Lower + SpecialSet3_Number + SpecialSet4_SpecChar
            specSetsRemaining= 4 - specSetValue

            if specSetsRemaining <= 1 or specSetsRemaining < remainingChars:
                password = password + chr(randomNumber)
        print(password)
    else:
        print("{0} is not a number.".format(characters))
else:
    print("You must provide the length of the password you wish to generate.")
