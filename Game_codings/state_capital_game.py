"""
Hello, what's your name?
Steve
Welcome Steve!

Ready to play?

Yes

What is the capital of Bayelsa State?

Yenagoa

Correct!

What is the capital of Ondo State?

Ado - Ekiti

Wrong!

The capital of Ondo State is Akure

Game Over!

"""

d = {}
with open("C:\Program Files (x86)\Python27\s and c.txt", "r") as f:
    for line in f:
        a = line.strip().split(' ' and '\t\t')
        k, v = a[0], a[1]
        d[str(k)] = v

import random

print("Hello, what's your name?")
MyName = input()

print("Welcome " + MyName + "!")
print("Ready to play? (yes/no)")

ready_or_not = input()
ready_or_not = str(ready_or_not)

comp_guess = 0

while comp_guess < 36:

    if ready_or_not == yes == Yes:

        x = random.choice(d.items())
        guess_key = str(x.keys())
        guess_value = str(x.value())

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
