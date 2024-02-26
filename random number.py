import random

print("Hello! Welcome to number-guess arcade")
print("Please input your range ")
min=int(input("minimum value= "))
max=int(input("maximum value= "))

pick=(random.randint(min,max))

print("You have 10 chances!")
for x in range(10):
    guess=int(input("What's your guess? "))
    if(guess==pick):
        break
    elif(guess>pick):
        print("Sorry your guess is too high")
    else:
        print("Sorry your guess is too low")

if(guess==pick):
    print("Yes! You won!")
else:
    print("Sorry, you ran out of chances!")