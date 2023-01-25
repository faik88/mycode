#!/usr/bin/python3
"""Fau Test 1
  Conditionals - with a while True loop."""

round = 0 #max number of time going round is 5
answer = int()

while round < 7 and answer != 1000: #use 1000 as a secret number to exit
    round += 1     # increase the round counter by 1
    answer = int(input('Give me a number: '))
    #answer = answer.i()

    if answer >= 90: #based on the input, check what score it is.
        print("Here a WOW Award - Packet of Nuts")
    elif answer >= 80:
        print("Good.  Don't expect a Pay Rise better - B")
    elif answer >= 70:    # logic to ensure round has not yet reached 3
        print("You can do better - C")
    elif answer >= 60:
        print("That's a Pass - D")
    elif answer < 59:
        print("You are Fired - F")
    elif round >= 6:
        print("Ok! That's enough")
    else:                 # if answer was wrong
        print("Last Chance! use number 1000 to stop")

