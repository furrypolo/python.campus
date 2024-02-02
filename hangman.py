import random

print("Welcome to the arcade! You've come to the game of hangman")
name=input("What's your name traveler?")

words=['lemon', 'apple', 'watermelon', 'mango', 'tangerine']

word=random.choice(words)

chances=len(word)+2

guesses=''

while chances>0:
    print("You have ",chances," more chance(s)")
    guess=input("put your guess: ")
    
    guesses+=guess
    n=0

    for char in word:
        
        if char in guesses:
            print(char, " ", end=' ')
        
        else:
            print("_ ", end=' ')
            n+=1
    
    if n==0:
        print("You win!")
        break

    if chances==1 & n!=0:
        print(" ")
        print("You lose, the word is ", word)
        break
    
    chances -=1

    print(" ")



