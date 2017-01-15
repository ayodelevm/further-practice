"""
State and Capital Game

The game generates a Nigerian state for you
and you are required to correctly input the capital of that state.

The game keeps generating a new state until you eventually input a wrong capital and then the game ends.

NOTE: Download the s and c.txt file and save it to a folder of choice in your pc
Then replace "C:\Program Files (x86)\Python27\s and c.txt" in open 
with the path to where you saved the s and c.txt file in your pc.
Also, this program was written for python 3. to use in python 2, change all instances of input() to raw_input()
"""

d = {}
import random

with open(r"C:\Program Files (x86)\Python27\s and c.txt", "r") as f:
    for line in f:
        a = line.strip().split(' ' and '\t\t')
        k, v = a[0], a[1]
        d[str(k)] = v

    
    print("Hello, what's your name?")
    MyName = input()

    to_input = ''
    while to_input != 'yes' and to_input != 'no':
        print("\nWelcome " + MyName + "!")
        print("\nReady to play? (yes/no)")

                
        ready_or_not = []
        to_input = input().lower()
        ready_or_not.append(str(to_input))


        for user_input in ready_or_not:
            if user_input == 'yes' or user_input == "Yes":

                comp_guess = 0
            
                while comp_guess < 36:
                    t = random.choice(list(d.items()))
                    z = dict([(t)])
                    for k, v in z.items():
                        guess_v_list = []
                        guess_key = k
                        guess_lower = v.lower()
                        remove_hyphen = guess_lower.replace("-"," ")
                        remove_hyphen2 = v.replace("-"," ")
                        guess_v_list.append(str(v))
                        guess_v_list.append(str(guess_lower))
                        guess_v_list.append(str(remove_hyphen))
                        guess_v_list.append(str(remove_hyphen2))
                        guess_v_set = set(guess_v_list)


                        print("\nWhat is the capital of " + guess_key + "")
                        player_guess = input()

                        comp_guess += 1

                        if player_guess in guess_v_set:
                            print("\nCorrect!")
                            del d[k]

                        if player_guess not in guess_v_set:
                            break

                    if player_guess not in guess_v_set:
                        print("\nWrong!")
                        print("\nThe capital of " + guess_key + " is " + v + "")
                        print("\nGame Over!")

                        print("\nYour score is: " + str(comp_guess))
                        break

                print("\nThanks for playing, you can try again later!")

            if user_input != 'yes' and user_input != "Yes":
                break

    if user_input != 'yes' and user_input != "Yes":
        print("\nThanks!, you can try again later, if you change your mind!")
               

