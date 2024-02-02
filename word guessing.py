import random

name=input("Welcome! \nWhat's your name? ")
print("Attaboy! Hi " + name + "! Welcome to a word guess")

words=['cabbage', 'book', 'bottle', 'oven', 'pencil']

word=random.choice(words)

turns=12

guesses=''

while turns>0:
    guess=input("Put in your guess \n")
    guesses+=guess

    fail=0
    for char in word:

        if char in guesses:
            print(char, "\n")
        
        else:
            fail+=1
            print("_ \n")
    
    if fail==0:
        print("You win!")
        break

    if turns==1 & fail!=0:
        print("Sorry you lose")
        break

    turns-=1