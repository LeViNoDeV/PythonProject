import random
import time
import turtle
from chips import casinochips

import sys
import os

def main():
    from chips import casinochips
    casinochips = int(casinochips)

    global yesorno
    yesorno = 'yes'

    resetthischips = 'reset'

    wn = turtle.Screen()
    height = 360
    width = 360
    wn.screensize(width, height)
    wn.addshape('bgpict.gif')
    backgroundpic = turtle.Turtle()
    backgroundpic.shape('bgpict.gif')

    wn.addshape('bananas.gif')
    wn.addshape('coins.gif')
    wn.addshape('cherries.gif')
    wn.addshape("king.gif")
    wn.addshape('gold.gif')
    wn.addshape('diamond.gif')
    wn.addshape('apple.gif')

    global i1
    global i2
    global i3
    global displaychips

    i1 = turtle.Turtle()
    i2 = turtle.Turtle()
    i3 = turtle.Turtle()
    textturtle = turtle.Turtle()
    displaychips = turtle.Turtle()

    i1.penup()
    i2.penup()
    i3.penup()
    textturtle.penup()
    displaychips.penup()

    textturtle.color('white')
    displaychips.color('white')

    i1.hideturtle()
    i2.hideturtle()
    i3.hideturtle()
    textturtle.hideturtle()
    displaychips.hideturtle()

    i1.speed(10000)
    i2.speed(10000)
    i3.speed(10000)
    textturtle.speed(10000)
    displaychips.speed(10000)

    i1.goto(-101,-55)
    i2.goto(-5,-55)
    i3.goto(89,-55)
    textturtle.goto(0, 280)
    displaychips.goto(-301, 240)
    displaychips.write("Chips: "+str(casinochips), font=('Courier',30), align="center")

    global bet
    bet = turtle.textinput("Choose your bet", "Bet value:")
    bet = bet
    if bet == resetthischips:
        file1 = open("chips.py", "w") 
        file1.write('casinochips = 10000')
        file1.close()
        bet = turtle.textinput("Choose your bet", "Bet value:")
        
    print(bet)
    while int(bet) > casinochips:
        bet = turtle.textinput("Choose your bet", "Bet value:")
        bet = int(bet)
        if bet > casinochips:
            print("The bet can't be bigger than the amount of chips")
    casinochips -= int(bet)

    def randomize():
        global num1
        global num2
        global num3
        num1 = random.randint(1, 7)
        num2 = random.randint(1, 7)
        num3 = random.randint(1, 7)
        print(num1, num2, num3)
        i1.showturtle()
        if num1 == 1:
            i1.shape('apple.gif')
        elif num1 == 2:
            i1.shape('bananas.gif')
        elif num1 == 3:
            i1.shape('cherries.gif')
        elif num1 == 4:
            i1.shape('coins.gif')
        elif num1 == 5:
            i1.shape('gold.gif')
        elif num1 == 6:
            i1.shape('diamond.gif')
        elif num1 == 7:
            i1.shape('king.gif')
        time.sleep(1)
        i2.showturtle()
        if num2 == 1:
            i2.shape('apple.gif')
        elif num2 == 2:
            i2.shape('bananas.gif')
        elif num2 == 3:
            i2.shape('cherries.gif')
        elif num2 == 4:
            i2.shape('coins.gif')
        elif num2 == 5:
            i2.shape('gold.gif')
        elif num2 == 6:
            i2.shape('diamond.gif')
        elif num2 == 7:
            i2.shape('king.gif')
        time.sleep(1)
        i3.showturtle()
        if num3 == 1:
            i3.shape('apple.gif')
        elif num3 == 2:
            i3.shape('bananas.gif')
        elif num3 == 3:
            i3.shape('cherries.gif')
        elif num3 == 4:
            i3.shape('coins.gif')
        elif num3 == 5:
            i3.shape('gold.gif')
        elif num3 == 6:
            i3.shape('diamond.gif')
        elif num3 == 7:
            i3.shape('king.gif')
        return True

    def jackpot():
        if randomize() == True:
            global bet
            global casinochips
            randomize()
            print(bet)
            if num1 == num2 and num2 == num3:
                textturtle.write("You won 3x", font=('Courier',30), align="center")
                bet =  float(bet) * 3
                casinochips += float(bet)
                casinochips = str(casinochips)
                print(casinochips)
                file1 = open("chips.py", "w") 
                file1.write('casinochips = ', casinochips)
                file1.close()
            elif num1 != num2 and num1 != num3 and num2 != num3:
                casinochips = int(casinochips)-int(bet)
                casinochips = str(casinochips)
                textturtle.write("You lost", True,font=('Courier',30) , align="center")
                print(casinochips)
                file1 = open("chips.py", "w") 
                file1.write('casinochips = '+casinochips)
                file1.close()
            else:
                textturtle.write("You won 1.5x", True,font=('Courier',30), align="center")
                bet =  float(bet) * 1.5
                casinochips = float(casinochips)+float(bet)
                casinochips = str(casinochips)
                file1 = open("chips.py", "w") 
                file1.write('casinochips = '+ casinochips)
                file1.close()

    jackpot()
main()
while True:
    restartprogram = turtle.textinput('Restart', 'Y/N')
    if restartprogram == 'Y':
        main()
    elif restartprogram == 'N':
        exit()
    else:
        print("Invalid input")
turtle.mainloop() 
