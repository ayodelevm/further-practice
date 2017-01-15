"""
State and Capital Game

The game generates a Nigerian state for you
and you are required to correctly input the capital of that state.

The game keeps generating a new state until you eventually input a wrong capital and then the game ends.
"""

d = {}
import random

with open("C:\Program Files (x86)\Python27\s and c.txt", "r") as f:
    for line in f:
        a = line.strip().split(' ' and '\t\t')
        k, v = a[0], a[1]
        d[str(k)] = v

    
    print("Hello, what's your name?")
    MyName = input()

    print("Welcome " + MyName + "!")
    print("Ready to play? (yes/no)")

    yes = Yes = True
    no = No = False
    ready_or_not = input()
    

    for PlayerInput in ready_or_not:
        if PlayerInput == no:
            print("Thank you for your time. Try again another time")
            break
        if PlayerInput == yes:
            continue
        
        
        
        comp_guess = 0

        while comp_guess < 36:
            x = random.choice(list(d.items()))
            z = dict([(x)])
            for k, v in z.items():
                guess_key = k
                guess_value = v = v.lower()

                print("What is the capital of" + guess_key)
                player_guess = input()

                if player_guess == guess_value:
                    print("Correct!")

                if player_guess != guess_value:
                    break

        if player_guess != guess_value:
            print("Wrong")
            print("\nThe capital of" + guess_key + "is" + guess_value)
            print("Game Over!")
