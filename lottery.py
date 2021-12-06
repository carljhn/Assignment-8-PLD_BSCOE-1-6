#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.
import random

print("-"*10, "Welcome to the 3-Digit Lottery", 10*"-")
name=input("Enter your name: ")
print("Are you ready to win,", name,"?") 
ready=input("Press 'y' if yes and press 'n' if no: ")
if ready=="y":
    print("Goodluck and may the odds be in your favor.")
    input("Press 'enter' to start")

    again="y"
    while again=="y":
        print(50*"-")
        userNumCount=[]
        for num in range(0, 3):
            userNum=int(input("Enter a number (0 through 9): "))
            while userNum in userNumCount or userNum<0 or userNum>9:
                print("Invalid: Your input may have been already entered or beyond the range of 0 through 9 ")
                userNum=int(input("Enter another number (0 through 9): "))
            userNumCount.append(userNum)

        winNumCount=[]
        for num in range(0, 3):
            lottoNum=random.randint(0, 9)
            while lottoNum in winNumCount:
                lottoNum=random.randint(0, 9)
            winNumCount.append(lottoNum)

        match=0
        for num in userNumCount:
            if num in winNumCount:
                    match+=1
        input("Press 'Enter' to show the results")
        print(50*"-")

        if match==3:
            print("Congratulations, you won the jackpot!")
            print("You picked the winning digits:", winNumCount)

        else:
            print("Sorry, you lose.")
            print("Your numbers did not match the winning numbers which are", winNumCount)
            print("You got", match,"correct digit(s)")

        again=input("Do you want to test your luck again? (y/n): ")
        if again=="n":
            print("Thank you for using this program")

elif ready=="n": 
    print("Thank you for using this program")
else:
    print("Unknown input, repeat the program")