import turtle
import random
import time
import tkinter 
import os


#window

wn = turtle.Screen()
wn.title("Cards War!")
wn.bgcolor("green")
wn.setup(width=1000, height=1300)



#addshapes:
#Heart
wn.addshape("projecy/Heart/1Heart.gif")
wn.addshape("projecy/Heart/2Heart.gif")
wn.addshape("projecy/Heart/3Heart.gif")
wn.addshape("projecy/Heart/4Heart.gif")
wn.addshape("projecy/Heart/5Heart.gif")
wn.addshape("projecy/Heart/6Heart.gif")
wn.addshape("projecy/Heart/7Heart.gif")
wn.addshape("projecy/Heart/8Heart.gif")
wn.addshape("projecy/Heart/9Heart.gif")
wn.addshape("projecy/Heart/10Heart.gif")
wn.addshape("projecy/Heart/jHeart.gif")
wn.addshape("projecy/Heart/qHeart.gif")
wn.addshape("projecy/Heart/kHeart.gif")

#Spade
wn.addshape("projecy/Spade/1Spade.gif")
wn.addshape("projecy/Spade/2Spade.gif")
wn.addshape("projecy/Spade/3Spade.gif")
wn.addshape("projecy/Spade/4Spade.gif")
wn.addshape("projecy/Spade/5Spade.gif")
wn.addshape("projecy/Spade/6Spade.gif")
wn.addshape("projecy/Spade/7Spade.gif")
wn.addshape("projecy/Spade/8Spade.gif")
wn.addshape("projecy/Spade/9Spade.gif")
wn.addshape("projecy/Spade/10Spade.gif")
wn.addshape("projecy/Spade/jSpade.gif")
wn.addshape("projecy/Spade/qSpade.gif")
wn.addshape("projecy/Spade/kSpade.gif")

#Diamond
wn.addshape("projecy/Diamond/1Diamond.gif")
wn.addshape("projecy/Diamond/2Diamond.gif")
wn.addshape("projecy/Diamond/3Diamond.gif")
wn.addshape("projecy/Diamond/4Diamond.gif")
wn.addshape("projecy/Diamond/5Diamond.gif")
wn.addshape("projecy/Diamond/6Diamond.gif")
wn.addshape("projecy/Diamond/7Diamond.gif")
wn.addshape("projecy/Diamond/8Diamond.gif")
wn.addshape("projecy/Diamond/9Diamond.gif")
wn.addshape("projecy/Diamond/10Diamond.gif")
wn.addshape("projecy/Diamond/jDiamond.gif")
wn.addshape("projecy/Diamond/qDiamond.gif")
wn.addshape("projecy/Diamond/kDiamond.gif")

#Clover
wn.addshape("projecy/Clover/1Clover.gif")
wn.addshape("projecy/Clover/2Clover.gif")
wn.addshape("projecy/Clover/3Clover.gif")
wn.addshape("projecy/Clover/4Clover.gif")
wn.addshape("projecy/Clover/5Clover.gif")
wn.addshape("projecy/Clover/6Clover.gif")
wn.addshape("projecy/Clover/7Clover.gif")
wn.addshape("projecy/Clover/8Clover.gif")
wn.addshape("projecy/Clover/9Clover.gif")
wn.addshape("projecy/Clover/10Clover.gif")
wn.addshape("projecy/Clover/jClover.gif")
wn.addshape("projecy/Clover/qClover.gif")
wn.addshape("projecy/Clover/kClover.gif")

#more shapes

wn.addshape("projecy/Fake and Bg/back.gif")
wn.addshape("projecy/Buttons/clickme.gif")
wn.addshape("projecy/Fake and Bg/fakeclickme.gif")
wn.addshape("projecy/Fake and Bg/fakerestart.gif")
wn.addshape("projecy/Fake and Bg/fakemore.gif")
wn.addshape("projecy/Fake and Bg/fakeless.gif")
wn.addshape("projecy/Fake and Bg/fakebet.gif")
wn.addshape("projecy/Fake and Bg/fakeauto.gif")
wn.addshape("projecy/Fake and Bg/fakeallin.gif")
wn.addshape("projecy/Buttons/autoplace.gif")
wn.addshape("projecy/Buttons/restart.gif")

#list of turtle and set shape
start1 = turtle.Turtle(visible=False)
start1.speed(0)
start1.penup()
start1.setpos(-200,0)
start1.write("Loading...", move=False, align="left", font=("Aharoni", 72, "normal"))




listT = []

for i in range(52):
  
    listT.append(turtle.Turtle(visible = False))
    listT[i].speed(0)
    listT[i].penup()
    listT[i].hideturtle()
start1.clear()    




start2 = turtle.Turtle(visible=False)
start2.speed(0)
start2.hideturtle()
start2.color("blue")
start2.penup()
start2.setpos(-50,0)
start2.write("3", move=False, align="left", font=("Aharoni", 150, "normal"))
time.sleep(0.5)
start2.clear()
start2.write("2", move=False, align="left", font=("Aharoni", 150, "normal"))
time.sleep(0.5)
start2.clear()
start2.write("1", move=False, align="left", font=("Aharoni", 150, "normal"))
time.sleep(0.5)
start2.clear()
start2.setpos(-200,0)
start2.write("Have fun!", move=False, align="left", font=("Aharoni", 72, "normal"))
time.sleep(0.5)
start2.clear()
    










    
#Heart setting shapes
    
#Heart setting shapes
    
listT[0].shape("projecy/Heart/1Heart.gif")
listT[0].val = 14
listT[1].shape("projecy/Heart/2Heart.gif")
listT[1].val = 2
listT[2].shape("projecy/Heart/3Heart.gif")
listT[2].val = 3
listT[3].shape("projecy/Heart/4Heart.gif")
listT[3].val = 4
listT[4].shape("projecy/Heart/5Heart.gif")
listT[4].val = 5
listT[5].shape("projecy/Heart/6Heart.gif")
listT[5].val = 6
listT[6].shape("projecy/Heart/7Heart.gif")
listT[6].val = 7
listT[7].shape("projecy/Heart/8Heart.gif")
listT[7].val = 8
listT[8].shape("projecy/Heart/9Heart.gif")
listT[8].val = 9
listT[9].shape("projecy/Heart/10Heart.gif")
listT[9].val = 10
listT[10].shape("projecy/Heart/jHeart.gif")
listT[10].val = 11
listT[11].shape("projecy/Heart/qHeart.gif")
listT[11].val = 12
listT[12].shape("projecy/Heart/kHeart.gif")
listT[12].val = 13

#Spade setting shapes

listT[13].shape("projecy/Spade/1Spade.gif")
listT[13].val = 14
listT[14].shape("projecy/Spade/2Spade.gif")
listT[14].val = 2
listT[15].shape("projecy/Spade/3Spade.gif")
listT[15].val = 3
listT[16].shape("projecy/Spade/4Spade.gif")
listT[16].val = 4
listT[17].shape("projecy/Spade/5Spade.gif")
listT[17].val = 5
listT[18].shape("projecy/Spade/6Spade.gif")
listT[18].val = 6
listT[19].shape("projecy/Spade/7Spade.gif")
listT[19].val = 7
listT[20].shape("projecy/Spade/8Spade.gif")
listT[20].val = 8
listT[21].shape("projecy/Spade/9Spade.gif")
listT[21].val = 9
listT[22].shape("projecy/Spade/10Spade.gif")
listT[22].val = 10
listT[23].shape("projecy/Spade/jSpade.gif")
listT[23].val = 11
listT[24].shape("projecy/Spade/qSpade.gif")
listT[24].val = 12 
listT[25].shape("projecy/Spade/kSpade.gif")
listT[25].val = 13

#Colver setting shapes
listT[26].shape("projecy/Clover/1Clover.gif")
listT[26].val = 14
listT[27].shape("projecy/Clover/2Clover.gif")
listT[27].val = 2
listT[28].shape("projecy/Clover/3Clover.gif")
listT[28].val = 3
listT[29].shape("projecy/Clover/4Clover.gif")
listT[29].val = 4
listT[30].shape("projecy/Clover/5Clover.gif")
listT[30].val = 5
listT[31].shape("projecy/Clover/6Clover.gif")
listT[31].val = 6
listT[32].shape("projecy/Clover/7Clover.gif")
listT[32].val = 7
listT[33].shape("projecy/Clover/8Clover.gif")
listT[33].val = 8
listT[34].shape("projecy/Clover/9Clover.gif")
listT[34].val = 9
listT[35].shape("projecy/Clover/10Clover.gif")
listT[35].val = 10
listT[36].shape("projecy/Clover/jClover.gif")
listT[36].val = 11
listT[37].shape("projecy/Clover/qClover.gif")
listT[37].val = 12
listT[38].shape("projecy/Clover/kClover.gif")
listT[38].val = 13

#Diamond setting shapes

listT[39].shape("projecy/Diamond/1Diamond.gif")
listT[39].val = 14
listT[40].shape("projecy/Diamond/2Diamond.gif")
listT[40].val = 2
listT[41].shape("projecy/Diamond/3Diamond.gif")
listT[41].val = 3
listT[42].shape("projecy/Diamond/4Diamond.gif")
listT[42].val = 4
listT[43].shape("projecy/Diamond/5Diamond.gif")
listT[43].val = 5
listT[44].shape("projecy/Diamond/6Diamond.gif")
listT[44].val = 6
listT[45].shape("projecy/Diamond/7Diamond.gif")
listT[45].val = 7
listT[46].shape("projecy/Diamond/8Diamond.gif")
listT[46].val = 8
listT[47].shape("projecy/Diamond/9Diamond.gif")
listT[47].val = 9
listT[48].shape("projecy/Diamond/10Diamond.gif")
listT[48].val = 10
listT[49].shape("projecy/Diamond/jDiamond.gif")
listT[49].val = 11
listT[50].shape("projecy/Diamond/qDiamond.gif")
listT[50].val = 12
listT[51].shape("projecy/Diamond/kDiamond.gif")
listT[51].val = 13

#להפוך לFOR


    

#click me button + auto place + restart
click = turtle.Turtle(visible = False)
click.speed(0)
click.penup()
click.setpos(0,100)
click.shape("projecy/Buttons/clickme.gif")

fakeclickme = turtle.Turtle(visible = False)
fakeclickme.speed(0)
fakeclickme.penup()
fakeclickme.setpos(0,100)
fakeclickme.shape("projecy/Fake and Bg/fakeclickme.gif")

fakerestart = turtle.Turtle(visible = False)
fakerestart.speed(0)
fakerestart.penup()
fakerestart.setpos(0,-50)
fakerestart.shape("projecy/Fake and Bg/fakerestart.gif")

fakemore = turtle.Turtle(visible = False)
fakemore.speed(0)
fakemore.penup()
fakemore.setpos(200,-100)
fakemore.shape("projecy/Fake and Bg/fakemore.gif")

fakeless = turtle.Turtle(visible = False)
fakeless.speed(0)
fakeless.penup()
fakeless.setpos(-200,-100)
fakeless.shape("projecy/Fake and Bg/fakeless.gif")

fakebet = turtle.Turtle(visible = False)
fakebet.speed(0)
fakebet.penup()
fakebet.setpos(0,0)
fakebet.shape("projecy/Fake and Bg/fakebet.gif")

fakeauto = turtle.Turtle(visible = False)
fakeauto.speed(0)
fakeauto.penup()
fakeauto.setpos(0,0)
fakeauto.shape("projecy/Fake and Bg/fakeauto.gif")

fakeallin = turtle.Turtle(visible = False)
fakeallin.speed(0)
fakeallin.penup()
fakeallin.setpos(0,-100)
fakeallin.shape("projecy/Fake and Bg/fakeallin.gif")

auto = turtle.Turtle(visible = False)
auto.speed(0)
auto.penup()
auto.setpos(0,0)
auto.shape("projecy/Buttons/autoplace.gif")

restart = turtle.Turtle(visible = False)
restart.speed(0)
restart.penup()
restart.setpos(0,-50)
restart.shape("projecy/Buttons/restart.gif")

#fake card
fake1 = turtle.Turtle(visible = False)
fake2 = turtle.Turtle(visible = False)
fakep_1 = turtle.Turtle(visible = False)
fakec_1 = turtle.Turtle(visible = False)
fakep_2 = turtle.Turtle(visible = False)
fakec_2 = turtle.Turtle(visible = False)
fakep_3 = turtle.Turtle(visible = False)
fakec_3 = turtle.Turtle(visible = False)



fake1.speed(0)
fake2.speed(0)
fake1.penup()
fake2.penup()
fake1.shape("projecy/Fake and Bg/back.gif")
fake2.shape("projecy/Fake and Bg/back.gif")
fake1.setpos(-200,400)#computer
fake2.setpos(-200,-400)#player


fakep_1.speed(0)
fakep_1.penup()
fakep_1.shape("projecy/Fake and Bg/back.gif")
fakep_1.hideturtle() #player

fakep_2.speed(0)
fakep_2.penup()
fakep_2.shape("projecy/Fake and Bg/back.gif")
fakep_2.hideturtle() #player

fakep_3.speed(0)
fakep_3.penup()
fakep_3.shape("projecy/Fake and Bg/back.gif")
fakep_3.hideturtle() #player

fakec_1.speed(0)
fakec_1.penup()
fakec_1.shape("projecy/Fake and Bg/back.gif")
fakec_1.hideturtle() #computer

fakec_2.speed(0)
fakec_2.penup()
fakec_2.shape("projecy/Fake and Bg/back.gif")
fakec_2.hideturtle() #computer

fakec_3.speed(0)
fakec_3.penup()
fakec_3.shape("projecy/Fake and Bg/back.gif")
fakec_3.hideturtle() #computer





#cards of each player(26)



list1 = [] #computer(200,400)

list2 = [] #player(200,-400)


for i in range(5):
    random.shuffle(listT)


for i in range(26):
    
    list1.append(listT[i])
    random.shuffle(list1)
    
for i in range(26,52):
    
    list2.append(listT[i])
    random.shuffle(list2)






             
            
           
           






  



playerc = len(list2)
computerc = len(list1)
#numcards1

numcards1 = turtle.Turtle(visible = False)
numcards1.speed(0)
numcards1.hideturtle()
numcards1.color("black")
numcards1.penup()
numcards1.setpos(-265,-460)
#numcards2

numcards2 = turtle.Turtle(visible = False)
numcards2.speed(0)
numcards2.hideturtle()
numcards2.color("black")
numcards2.penup()
numcards2.setpos(-265,340)

#back
wn.addshape("projecy/Buttons/returntomain.gif")
backmain = turtle.Turtle(visible = False)
backmain.speed(0)
backmain.penup()
backmain.setpos(-400,-600)
backmain.shape("projecy/Buttons/returntomain.gif")

    

def back(x,y):
    border.ht()
    more.hideturtle()
    fakemore.ht()
    moneytext.undo()
    chipsnum.undo()
    chipsnum2.undo()
    less.hideturtle()
    fakeless.hideturtle()
    allin.hideturtle()
    fakeallin.hideturtle()
    bet.ht()
    fakebet.hideturtle()
    win.undo()
    click.hideturtle()
    numcards2.undo()
    numcards1.undo()
    fakep_1.hideturtle()
    fakep_2.hideturtle()
    fakep_3.hideturtle()
    fake1.hideturtle()
    fake2.hideturtle()
    fakeauto.hideturtle()
    auto.hideturtle()
    fakeclickme.hideturtle()
    restart.ht()
    fakerestart.ht()
    backmain.hideturtle()
    
    import runpy
    file_globals = runpy.run_path(r"..\ex.py")
    
    
#betsystem

chips = 10000
betmoney = 100
wn.addshape("projecy/Buttons/less.gif")
wn.addshape("projecy/Buttons/more.gif")
wn.addshape("projecy/Buttons/bet.gif")
wn.addshape("projecy/Buttons/allin.gif")
allin = turtle.Turtle()
bet = turtle.Turtle()
less = turtle.Turtle()
more = turtle.Turtle()
allin.speed(0)
bet.speed(0)
more.speed(0)
less.speed(0)
allin.penup()
more.penup()
less.penup()
bet.penup()
more.shape("projecy/Buttons/more.gif")
bet.shape("projecy/Buttons/bet.gif")
less.shape("projecy/Buttons/less.gif")
allin.shape("projecy/Buttons/allin.gif")
allin.setpos(0,-100)
more.setpos(200,-100)
bet.setpos(0,0)
less.setpos(-200,-100)
more.showturtle()
less.showturtle()
bet.showturtle()
allin.showturtle()
backmain.showturtle()
wn.addshape("projecy/Fake and Bg/border.gif")
border = turtle.Turtle()
border.speed(0)
border.penup()
border.shape("projecy/Fake and Bg/border.gif")
border.setpos(0,200)
border.showturtle()



#moneytext

moneytext = turtle.Turtle(visible = False)
moneytext.speed(0)
moneytext.hideturtle()
moneytext.color("black")
moneytext.penup()
moneytext.setpos(-150,150)
moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))

#chipsnum
chipsnum = turtle.Turtle(visible = False)
chipsnum.speed(0)
chipsnum.hideturtle()
chipsnum.color("Red")
chipsnum.penup()
chipsnum.setpos(-480,580)
chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))

#chipsnum2
chipsnum2 = turtle.Turtle(visible = False)
chipsnum2.speed(0)
chipsnum2.hideturtle()
chipsnum2.color("Red")
chipsnum2.penup()
chipsnum2.setpos(-125,580)
chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))



turtle.listen()
backmain.onclick(back, 1)
    
def moremoney(x,y):
    
    more.hideturtle()
    fakemore.showturtle()
    global betmoney
    global chips

    if(betmoney<chips):
        betmoney+=100
        time.sleep(0.25)
        moneytext.undo()
        moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))
        
    elif(betmoney==chips):
        betmoney=chips
        moneytext.undo()
        moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))
        tkinter.messagebox.showwarning("ChipSystem","You dont have enough chips!", )
    elif(betmoney==0):
        betmoney=0
        moneytext.undo()
        moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))
        tkinter.messagebox.showwarning("ChipSystem","You dont have enough chips to play the game!", )
    fakemore.hideturtle()
    more.showturtle()
           
def lessmoney(x,y):
    less.hideturtle()
    fakeless.showturtle()
    time.sleep(0.25)
    
    global betmoney 
    if(betmoney==100):
        betmoney=100
        moneytext.undo()
        moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))
        tkinter.messagebox.showwarning("ChipSystem","You cannot enter less than 100 Chips!", )
    elif(betmoney>100):
        betmoney-=100
        moneytext.undo()
        moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))
    elif(betmoney==0):
        betmoney=0
        moneytext.undo()
        moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))
        tkinter.messagebox.showwarning("ChipSystem","You cannot enter less than 0 Chips!", )
    fakeless.hideturtle()
    less.showturtle()
        
def allin1(x,y):
    allin.hideturtle()
    fakeallin.showturtle()
    global betmoney
    global chips
    betmoney=chips
    moneytext.undo()
    moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))
    time.sleep(0.25)
    fakeallin.hideturtle()
    allin.showturtle()
    
def betsystem(x,y):
    bet.st()
    global betmoney
    global chips
    if(betmoney==0):
        tkinter.messagebox.showwarning("ChipSystem","You dont have enough chips to play!", )
        fakebet.hideturtle()

    
        
    elif(betmoney!=0):
        bet.hideturtle()
        allin.hideturtle()
        more.hideturtle()
        less.hideturtle()
        fakebet.showturtle()

        chips-=betmoney
        chipsnum.clear()
        chipsnum2.clear()
        chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))
        chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))
        print("betted: ",betmoney)
        moneytext.clear()
        border.hideturtle()
        fakebet.hideturtle()

        allin.hideturtle()
        more.hideturtle()
        less.hideturtle()

        fake1.showturtle()
        fake2.showturtle()
        auto.showturtle()
        click.showturtle()
        numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
        numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
        s=True
        

    
print("************************")


#winnername

win = turtle.Turtle(visible = False)
win.speed(0)
win.hideturtle()
win.color("Red")
win.penup()
win.setpos(-265,550)


def restart1(x,y):
    fakerestart.showturtle()
    restart.ht()
    global betmoney
    global chips
    win.clear()
    list1.clear()
    list2.clear()
    print("************************")
    for i in range(5):
        random.shuffle(listT)  
    for i in range(26):
        list1.append(listT[i])
        random.shuffle(list1)
        
    for i in range(26,52):
        list2.append(listT[i])
        random.shuffle(list2)
    restart.hideturtle()
    border.showturtle()
    bet.showturtle()
    allin.showturtle()
    more.showturtle()
    less.showturtle()
    fakerestart.hideturtle()

    if(chips>0):
        betmoney = 100
    elif(chips<=0):
        betmoney=0
    moneytext.write(betmoney, move=False, align="left", font=("Aharoni", 105, "normal"))



s=True

while s==True:
    wn.update()
    
    
    def cardson(x,y):
        backmain.ht()
        click.hideturtle()
        fakeclickme.showturtle()
        global  chips
        global betmoney
        yes=True         
        playerc = len(list2)
        computerc = len(list1)

        if(len(list1)==52):

            playerc = len(list2)
            computerc = len(list1)
            numcards1.clear()
            numcards2.clear()
            fake1.hideturtle()
            fake2.hideturtle()
            print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            print("   Computer Won The Game!    ")
            print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            win.setpos(-325,0)
            click.hideturtle()
            auto.hideturtle()
            win.write("Computer Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
            s=False
            restart.showturtle()
            backmain.st()
            
        elif(len(list2)==52):

            playerc = len(list2)
            computerc = len(list1)
            numcards1.clear()
            numcards2.clear()
            fake1.hideturtle()
            fake2.hideturtle()
            print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            print("   Player Won The Game!    ")
            print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
            chips=chips+2*betmoney
            chipsnum.clear()
            chipsnum2.clear()
            chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))
            chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))
            win.setpos(-325,0)
            click.hideturtle()
            auto.hideturtle()
            win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
            s=False
            restart.showturtle()
            backmain.st()
        
        elif(len(list1)>0 and len(list2)>0):
            
            list2[0].setpos(200,-400)
            list2[0].showturtle()
            list1[0].setpos(200,400)
            list1[0].showturtle()
            
            if(list1[0].val>list2[0].val):
                list1.append(list2[0])
                list2.remove(list2[0])
                time.sleep(1)
                list1[len(list1)-1].hideturtle()
                list1[0].hideturtle()
                list1.append(list1[0])
                list1.remove(list1[0])
                playerc = len(list2)
                computerc = len(list1)
                numcards1.undo()
                numcards2.undo()
                numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                print("Computer Won!!!")
                print("************************")
                fakeclickme.hideturtle()
                click.showturtle()
            elif(list1[0].val<list2[0].val):
                list2.append(list1[0])
                list1.remove(list1[0])
                time.sleep(1)
                list2[len(list2)-1].hideturtle()
                list2[0].hideturtle()
                list2.append(list2[0])
                list2.remove(list2[0])
                playerc = len(list2)
                computerc = len(list1)
                numcards1.undo()
                numcards2.undo()
                numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                print("Player Won!!!")
                print("************************")
                fakeclickme.hideturtle()
                click.showturtle()

            
                    
            elif(list1[0].val==list2[0].val and  len(list1) >= 5 and len(list2)>=5 ):
                
                print("WAR!!!")
                print("************************")
                
                

                
                   
                    
                time.sleep(1)
                fakep_1.setpos(200,-400)
                fakep_1.showturtle()
                fakec_1.setpos(200,400)
                fakec_1.showturtle()

                fakep_2.setpos(200,-425)
                fakep_2.showturtle()
                fakec_2.setpos(200,425)
                fakec_2.showturtle()
                
                fakep_3.setpos(200,-450)
                fakep_3.showturtle()
                fakec_3.setpos(200,450)
                fakec_3.showturtle()

                
                list1[0].hideturtle()
                list2[0].hideturtle()
                time.sleep(1)


                
                fakep_2.hideturtle()
                fakec_2.hideturtle()
                fakep_3.hideturtle()
                fakec_3.hideturtle()

                time.sleep(0.75)

                fakep_1.hideturtle()
                fakec_1.hideturtle()

                if(list1[4].val == list2[4].val):
                    yes = True
                    while yes == True:
                        list1random = random.randint(4,len(list1)-1)
                        list2random = random.randint(4,len(list2)-1)
                        list1.insert(4,list1[list1random])
                        list2.insert(4,list2[list2random])
                        list1.pop(list1random+1)
                        list2.pop(list2random+1)
                        if(list1[4] != list2[4]):
                            yes = False
                
                list1[4].setpos(200,400)
                list2[4].setpos(200,-400)
                list1[4].showturtle()
                list2[4].showturtle()
                
                
                if(list1[4].val>list2[4].val):
                    
                    list1.append(list2[1])
                    list1.append(list2[2])
                    list1.append(list2[3])
                    list1.append(list2[4])
                    list1.append(list2[0])
                    
                    list2.remove(list2[0])
                    list2.remove(list2[1])
                    list2.remove(list2[2])
                    list2.remove(list2[3])
                    list2.remove(list2[4])
                    
                    time.sleep(1)
                    
                    list1[len(list1)-1].hideturtle()
                    list1[len(list1)-2].hideturtle()

                    list1[0].hideturtle()
                    list1[4].hideturtle()
                    
                    list1.append(list1[1])
                    list1.append(list1[2])
                    list1.append(list1[3])
                    list1.append(list1[0])
                    list1.append(list1[4])

                    list1.remove(list1[1])
                    list1.remove(list1[2])
                    list1.remove(list1[3])
                    list1.remove(list1[0])
                    list1.remove(list1[4])

                    
                    
                    
                    playerc = len(list2)
                    computerc = len(list1)
                    numcards1.undo()
                    numcards2.undo()
                    numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    print("Computer Won!!!")
                    print("************************")
                    fakeclickme.hideturtle()
                    click.showturtle()
                    
                elif(list1[4].val<list2[4].val):
                    
                    list2.append(list1[1])
                    list2.append(list1[2])
                    list2.append(list1[3])
                    list2.append(list1[4])
                    list2.append(list1[0])
                    
                    list1.remove(list1[0])
                    list1.remove(list1[1])
                    list1.remove(list1[2])
                    list1.remove(list1[3])
                    list1.remove(list1[4])

                    
                    time.sleep(1)
                    
                    list2[len(list2)-1].hideturtle()
                    list2[len(list2)-2].hideturtle()

                    list2[0].hideturtle()
                    list2[4].hideturtle()

                    
                    list2.append(list2[1])
                    list2.append(list2[2])
                    list2.append(list2[3])
                    list2.append(list2[4])
                    list2.append(list2[0])

                    list2.remove(list2[0])
                    list2.remove(list2[1])
                    list2.remove(list2[2])
                    list2.remove(list2[3])
                    list2.remove(list2[4])
                    
                    
                    
                    playerc = len(list2)
                    computerc = len(list1)
                    numcards1.undo()
                    numcards2.undo()
                    numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    print("Player Won!!!")
                    print("************************")
                    fakeclickme.hideturtle()
                    click.showturtle()

            elif(list1[0].val==list2[0].val and  len(list1) < 5):
                list1[0].hideturtle()
                list2[0].hideturtle()

                playerc = len(list2)
                computerc = len(list1)
                numcards1.clear()
                numcards2.clear()
                fake1.hideturtle()
                fake2.hideturtle()
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                print("   Player Won The Game!    ")
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                chips=chips+2*betmoney
                chipsnum.clear()
                chipsnum2.clear()
                chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))
                chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))
                win.setpos(-300,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False
                restart.showturtle()
                backmain.showturtle()
                
            elif(list1[0].val==list2[0].val and len(list2) < 5 ):
                list1[0].hideturtle()
                list2[0].hideturtle()
                
                playerc = len(list2)
                computerc = len(list1)
                numcards1.clear()
                numcards2.clear()
                fake1.hideturtle()
                fake2.hideturtle()
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                print("   Computer Won The Game!    ")
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                win.setpos(-325,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Computer Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False
                restart.showturtle()
                backmain.showturtle()

            elif(list1[0].val==list2[0].val and  len(list1) < 5 and len(list2) < 5 ):
                list1[0].hideturtle()
                list2[0].hideturtle()
               
                playerc = len(list2)
                computerc = len(list1)
                numcards1.clear()
                numcards2.clear()
                fake1.hideturtle()
                fake2.hideturtle()
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                print("            Draw!           ")
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                chips=chips+betmoney
                chipsnum.clear()
                chipsnum2.clear()
                chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))
                chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))
                win.setpos(-275,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Draw!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False
                restart.showturtle()
                backmain.showturtle()


                
        


    





    def forward(x,y):
        backmain.hideturtle()
        auto.hideturtle()
        fakeauto.showturtle()
        time.sleep(0.25)
        fakeauto.hideturtle()
        
        fakeclickme.hideturtle()
        auto.hideturtle()
        click.hideturtle()
        global betmoney
        global chips
        checkwhile = True
        yes = True


        while checkwhile==True:

            playerc = len(list2)
            computerc = len(list1)
            
            if(len(list1)==52):
                               
                playerc = len(list2)
                computerc = len(list1)
                numcards1.clear()
                numcards2.clear()
                fake1.hideturtle()
                fake2.hideturtle()
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                print("   Computer Won The Game!    ")
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                win.setpos(-325,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Computer Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False
                checkwhile=False
                restart.showturtle()
                backmain.st()
            elif(len(list2)==52):
                            
                playerc = len(list2)
                computerc = len(list1)
                numcards1.clear()
                numcards2.clear()
                fake1.hideturtle()
                fake2.hideturtle()
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                print("   Player Won The Game!    ")
                print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                chips=chips+2*betmoney
                chipsnum.clear()
                chipsnum2.clear()
                chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))
                chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))
                win.setpos(-325,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False
                checkwhile=False
                restart.showturtle()
                backmain.st()
          
            
            
            

            
            elif(len(list1)>0 and len(list2)>0):
                
                list2[0].setpos(200,-400)
                list2[0].showturtle()
                list1[0].setpos(200,400)
                list1[0].showturtle()
                
                if(list1[0].val>list2[0].val):
                    list1.append(list2[0])
                    list2.remove(list2[0])
                    list1[len(list1)-1].hideturtle()
                    list1[0].hideturtle()
                    list1.append(list1[0])
                    list1.remove(list1[0])
                    playerc = len(list2)
                    computerc = len(list1)
                    numcards1.undo()
                    numcards2.undo()
                    numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    print("Computer Won!!!")
                    print("************************")
                    
                elif(list1[0].val<list2[0].val):
                    list2.append(list1[0])
                    list1.remove(list1[0])
                    list2[len(list2)-1].hideturtle()
                    list2[0].hideturtle()
                    list2.append(list2[0])
                    list2.remove(list2[0])
                    playerc = len(list2)
                    computerc = len(list1)
                    numcards1.undo()
                    numcards2.undo()
                    numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                    print("Player Won!!!")
                    print("************************")

                
                        
                elif(list1[0].val==list2[0].val and  len(list1) >= 5 and len(list2)>=5 ):
                    
                    print("WAR!!!")
                    print("************************")
                    
                            
                    
                    

                    
                       
                        
                    fakep_1.setpos(200,-400)
                    fakep_1.showturtle()
                    fakec_1.setpos(200,400)
                    fakec_1.showturtle()

                    fakep_2.setpos(200,-425)
                    fakep_2.showturtle()
                    fakec_2.setpos(200,425)
                    fakec_2.showturtle()
                    
                    fakep_3.setpos(200,-450)
                    fakep_3.showturtle()
                    fakec_3.setpos(200,450)
                    fakec_3.showturtle()
                    
                    list1[0].hideturtle()
                    list2[0].hideturtle()


                    
                    fakep_2.hideturtle()
                    fakec_2.hideturtle()
                    fakep_3.hideturtle()
                    fakec_3.hideturtle()


                    fakep_1.hideturtle()
                    fakec_1.hideturtle()

                    
                    
                    list1[4].setpos(200,400)
                    list2[4].setpos(200,-400)
                    
                    
                    if(list1[4].val == list2[4].val):
                        yes = True
                        while yes == True:
                            list1random = random.randint(4,len(list1)-1)
                            list2random = random.randint(4,len(list2)-1)
                            list1.insert(4,list1[list1random])
                            list2.insert(4,list2[list2random])
                            list1.pop(list1random+1)
                            list2.pop(list2random+1)
                            if(list1[4] != list2[4]):
                                    yes = False
                            
                    
        
                             
                    list1[4].showturtle()
                    list2[4].showturtle()
                    
                    if(list1[4].val>list2[4].val):
                        list1.append(list2[1])
                        list1.append(list2[2])
                        list1.append(list2[3])
                        list1.append(list2[4])
                        list1.append(list2[0])


                        list2.remove(list2[4])
                        list2.remove(list2[3])
                        list2.remove(list2[2])
                        list2.remove(list2[1])
                        list2.remove(list2[0])
                        
                        
                        
                        
                        
                        list1[len(list1)-1].hideturtle()
                        list1[len(list1)-2].hideturtle()

                        list1[0].hideturtle()
                        list1[4].hideturtle()
                        
                        list1.append(list1[1])
                        list1.append(list1[2])
                        list1.append(list1[3])
                        list1.append(list1[0])
                        list1.append(list1[4])

                        list1.remove(list1[4])
                        list1.remove(list1[3])
                        list1.remove(list1[2])
                        list1.remove(list1[1])
                        list1.remove(list1[0])

                        
                        
                        
                        playerc = len(list2)
                        computerc = len(list1)
                        numcards1.undo()
                        numcards2.undo()
                        numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                        numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                        print("Computer Won!!!")
                        print("************************")
                        
                    elif(list1[4].val<list2[4].val):
                        
                        list2.append(list1[1])
                        list2.append(list1[2])
                        list2.append(list1[3])
                        list2.append(list1[4])
                        list2.append(list1[0])


                        list1.remove(list1[4])
                        list1.remove(list1[3])
                        list1.remove(list1[2])
                        list1.remove(list1[1])
                        list1.remove(list1[0])
                        
                          

                        list2[len(list2)-1].hideturtle()
                        list2[len(list2)-2].hideturtle()

                        list2[0].hideturtle()
                        list2[4].hideturtle()

                        
                        list2.append(list2[1])
                        list2.append(list2[2])
                        list2.append(list2[3])
                        list2.append(list2[4])
                        list2.append(list2[0])

                        list2.remove(list2[4])
                        list2.remove(list2[3])
                        list2.remove(list2[2])
                        list2.remove(list2[1])
                        list2.remove(list2[0])
                        
                        
                        
                        playerc = len(list2)
                        computerc = len(list1)
                        numcards1.undo()
                        numcards2.undo()
                        numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                        numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                        print("Player Won!!!")
                        print("************************")
                        
                    





                elif(list1[0].val==list2[0].val and  len(list1) < 5):
                    list1[0].hideturtle()
                    list2[0].hideturtle()

                    playerc = len(list2)
                    computerc = len(list1)
                    numcards1.clear()
                    numcards2.clear()
                    fake1.hideturtle()
                    fake2.hideturtle()
                    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                    print("   Player Won The Game!    ")
                    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                    chips=chips+2*betmoney
                    chipsnum.clear()
                    chipsnum2.clear()
                    chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))
                    chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))
                    win.setpos(-300,0)
                    click.hideturtle()
                    auto.hideturtle()
                    win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                    s=False
                    checkwhile=False
                    restart.showturtle()
                    backmain.st()

                elif(list1[0].val==list2[0].val and len(list2) < 5 ):
                    list1[0].hideturtle()
                    list2[0].hideturtle()
                                
                    playerc = len(list2)
                    computerc = len(list1)
                    numcards1.clear()
                    numcards2.clear()
                    fake1.hideturtle()
                    fake2.hideturtle()
                    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                    print("   Computer Won The Game!    ")
                    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                    win.setpos(-325,0)
                    click.hideturtle()
                    auto.hideturtle()
                    win.write("Computer Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                    s=False
                    checkwhile=False
                    restart.showturtle()
                    backmain.st()


                elif(list1[0].val==list2[0].val and  len(list1) < 5 and len(list2) < 5 ):
                    list1[0].hideturtle()
                    list2[0].hideturtle()
                    
                    playerc = len(list2)
                    computerc = len(list1)
                    numcards1.clear()
                    numcards2.clear()
                    fake1.hideturtle()
                    fake2.hideturtle()
                    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                    print("            Draw!           ")
                    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                    chips=chips+betmoney
                    chipsnum.clear()
                    chipsnum2.clear()
                    chipsnum.write("Number of chips: ", move=False, align="left", font=("Aharoni", 32, "normal"))
                    chipsnum2.write(chips, move=False, align="left", font=("Aharoni", 32, "normal"))
                    win.setpos(-275,0)
                    click.hideturtle()
                    auto.hideturtle()
                    win.write("Draw!", move=False, align="left", font=("Agency FB", 105, "normal"))
                    s=False            
                    checkwhile=False
                    restart.showturtle()
                    backmain.st()

        

    
 



    
    turtle.listen()
    #chips system
    less.onclick(lessmoney, 1)
    more.onclick(moremoney, 1)
    allin.onclick(allin1, 1)
    bet.onclick(betsystem, 1)
    #gameplay
    click.onclick(cardson, 1)
    auto.onclick(forward, 1)
    restart.onclick(restart1, 1)

    

    turtle.mainloop()  


    




                















