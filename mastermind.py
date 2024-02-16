import os

print("Welcome partners!")
decide=True

while(decide):
    guess=input("Pick one to put in set of number to guess = ")
    guessed=str(guess)

    os.system('cls')

    chances=len(guessed)+2

    print("Now let the other player guess them, you have ", chances, "chances")
    option=""
    while(chances>0):
        print("chances = ",chances)
        chances-=1
        wrong=0
        opt=str(input("Your guess = "))
        option+=opt


        for char in guessed:
            if char in option:
                print(char, end=' ')
            else:
                print("x", end=' ')
                wrong+=1
        
        print(" ")

        if(wrong==0):
            print("You won! Congratulations")
            break
        
        if(chances==0):
            print("Sorry! You ran out of chances, the digits are", guessed)
            break

    
    again=str(input("Care to play again? (y/n)"))
    if(again=="n" or again=="N"):
        decide=False


