import turtle
from tkinter import*
import time
import random
import tkinter as tk





turtle.TurtleScreen._RUNNING = True

#window
mainwn = turtle.Screen()
mainwn.title("Main Screen!")
mainwn.bgcolor("White")
mainwn.setup(width=800, height=800)



#shapes
mainwn.addshape("ButtonsMainScreen/start.gif")
mainwn.addshape("ButtonsMainScreen/horseracebutton.gif")
mainwn.addshape("ButtonsMainScreen/machinebutton.gif")
mainwn.addshape("ButtonsMainScreen/cardwarbutton.gif")
mainwn.addshape("ButtonsMainScreen/roulettebutton.gif")


#text
text=turtle.Turtle(visible=False)
text.speed(0)
text.penup()
text.setpos(-325,200)
text.color("red")
text.write("Casino Games", move=False, align="left", font=("Aharoni", 72, "normal"))

#card war = work
cardwarb = turtle.Turtle(visible=False)
cardwarb.speed(0)
cardwarb.penup()
cardwarb.shape("ButtonsMainScreen/cardwarbutton.gif")
cardwarb.setpos(-200,-0)

startcardwarb = turtle.Turtle(visible=False)
startcardwarb.speed(0)
startcardwarb.penup()
startcardwarb.shape("ButtonsMainScreen/start.gif")
startcardwarb.setpos(-200,-100)

#horse race = work

roulette1 = turtle.Turtle(visible=False)
roulette1.speed(0)
roulette1.penup()
roulette1.shape("ButtonsMainScreen/roulettebutton.gif")
roulette1.setpos(-65,0)

startroulette1 = turtle.Turtle(visible=False)
startroulette1.speed(0)
startroulette1.penup()
startroulette1.shape("ButtonsMainScreen/start.gif")
startroulette1.setpos(-65,-100)

#lmachine = work
lmachine = turtle.Turtle(visible=False)
lmachine.speed(0)
lmachine.penup()
lmachine.shape("ButtonsMainScreen/machinebutton.gif")
lmachine.setpos(65,-0)

startlmachine = turtle.Turtle(visible=False)
startlmachine.speed(0)
startlmachine.penup()
startlmachine.shape("ButtonsMainScreen/start.gif")
startlmachine.setpos(65,-100)

#horserace = in progress
horserace = turtle.Turtle(visible=False)
horserace.speed(0)
horserace.penup()
horserace.shape("ButtonsMainScreen/horseracebutton.gif")
horserace.setpos(200,-0)

starthorserace = turtle.Turtle(visible=False)
starthorserace.speed(0)
starthorserace.penup()
starthorserace.shape("ButtonsMainScreen/start.gif")
starthorserace.setpos(200,-100)

#images
horserace.st()
lmachine.st()
roulette1.st()
cardwarb.st()
def showstarthorse(x,y):
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    starthorserace.st()
    
    

def showstartcard(x,y):
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    startcardwarb.st()
     

def showstartmachine(x,y):
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    startlmachine.st()
    
    
    
def showstartroulette1(x,y):
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    startroulette1.st()
    
    
    

#function to start game


def startbuttonlmachine1(x,y):
    text.undo()
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    lmachine.ht()
    cardwarb.ht()
    horserace.ht()
    roulette1.ht()
    
    import runpy
    file_globals = runpy.run_path('lmachine.py')

 



def startbuttoncardwar(x,y):
    text.undo()
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    horserace.ht()
    lmachine.ht()
    cardwarb.ht()
    roulette1.ht()
    import runpy
    file_globals = runpy.run_path("cardwar.py")
    
    

def startbuttonroulettegame(x,y):
    text.undo()
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    roulette1.ht()
    lmachine.ht()
    horserace.ht()
    cardwarb.ht()
    mainwn.setup(width=1200, height=1200)
    
    

    from roulette import Game, Table, Roulette, Chip, Button, Score, Ball
    a=Game()
    a.run()

    
    
def startbuttonhorsegame(x,y):
    text.undo()
    startcardwarb.ht()
    startroulette1.ht()
    startlmachine.ht()
    starthorserace.ht()
    
    
    roulette1.ht()
    lmachine.ht()
    cardwarb.ht()
    horserace.ht()
    
    turtle.bye()

    import runpy
    file_globals = runpy.run_path("gameprorace.py")
    
    
#call
turtle.listen()
startcardwarb.onclick(startbuttoncardwar, 1)

turtle.listen()
startlmachine.onclick(startbuttonlmachine1, 1)

turtle.listen()
startroulette1.onclick(startbuttonroulettegame, 1)

turtle.listen()
starthorserace.onclick(startbuttonhorsegame, 1)

#*************

turtle.listen()
cardwarb.onclick(showstartcard, 1)

turtle.listen()
lmachine.onclick(showstartmachine, 1)

turtle.listen()
roulette1.onclick(showstartroulette1, 1)

turtle.listen()
horserace.onclick(showstarthorse, 1)

turtle.mainloop()
































































