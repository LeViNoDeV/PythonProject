import random
import time


global casinochips
casinochips = 1000
global bet
bet = int(input("Bet value: "))
casinochips -= bet



def randomize():
    global num1
    global num2
    global num3
    num1 = random.randint(1, 7)
    num2 = random.randint(1, 7)
    num3 = random.randint(1, 7)
    print(num1, num2, num3)



def jackpot():
    global bet
    global casinochips
    randomize()
    print(bet)
    if num1 == num2 and num2 == num3:
        print("You won 3x")
        bet = bet * 3
        casinochips += bet
        print(casinochips)
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print("You lost")
        print(casinochips)
    else:
        print("You won 2x")
        bet = bet * 2
        casinochips += bet
        print(casinochips)
jackpot()