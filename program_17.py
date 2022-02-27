from random import randint
for x in range(1,6):
    guessNumber=int(input("enter your number :"))
    randomNumber = randint(1,5)


    if guessNumber == randomNumber:
        print("you have won" , randomNumber)
    else:
        print("you have lost")
        print("random number was: ", randomNumber)