#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
print("please pick a number")
number = input()
number = int(number)

from random import seed
from random import randint

truenum = randint(0, 10)
x=1

while number != truenum:

    if number < truenum:
        print("that is to low please pick again")
        number = input()
        number = int(number)
    elif number > truenum:
        print("that is to high please pick again")
        number = input()
        number = int(number)
        #do I have to added number = intnum every time?
    x=x+1

print("thats correct!")

print("it only took you",x,"times")



