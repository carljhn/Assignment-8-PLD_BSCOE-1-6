#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.
import random
ranNum=random.randint(0, 100)
guessNum=int(input("Guess the number: "))

while guessNum!=ranNum:
    if guessNum>ranNum:
        print("Greater than")
        guessNum=int(input("Have another guess: "))
    elif guessNum<ranNum: 
        print("Less than")
        guessNum=int(input("Have another guess: "))
    if guessNum==ranNum:
        print("Congratulations, you got it! The number is", ranNum)
        break