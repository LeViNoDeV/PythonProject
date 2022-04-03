import turtle
import random
import time



#window

wn = turtle.Screen()
wn.title("Cards War!")
wn.bgcolor("green")
wn.setup(width=1000, height=1200)



#addshapes:
#Heart
wn.addshape("1Heart.gif")
wn.addshape("2Heart.gif")
wn.addshape("3Heart.gif")
wn.addshape("4Heart.gif")
wn.addshape("5Heart.gif")
wn.addshape("6Heart.gif")
wn.addshape("7Heart.gif")
wn.addshape("8Heart.gif")
wn.addshape("9Heart.gif")
wn.addshape("10Heart.gif")
wn.addshape("jHeart.gif")
wn.addshape("qHeart.gif")
wn.addshape("kHeart.gif")

#Spade
wn.addshape("1Spade.gif")
wn.addshape("2Spade.gif")
wn.addshape("3Spade.gif")
wn.addshape("4Spade.gif")
wn.addshape("5Spade.gif")
wn.addshape("6Spade.gif")
wn.addshape("7Spade.gif")
wn.addshape("8Spade.gif")
wn.addshape("9Spade.gif")
wn.addshape("10Spade.gif")
wn.addshape("jSpade.gif")
wn.addshape("qSpade.gif")
wn.addshape("kSpade.gif")

#Diamond
wn.addshape("1Diamond.gif")
wn.addshape("2Diamond.gif")
wn.addshape("3Diamond.gif")
wn.addshape("4Diamond.gif")
wn.addshape("5Diamond.gif")
wn.addshape("6Diamond.gif")
wn.addshape("7Diamond.gif")
wn.addshape("8Diamond.gif")
wn.addshape("9Diamond.gif")
wn.addshape("10Diamond.gif")
wn.addshape("jDiamond.gif")
wn.addshape("qDiamond.gif")
wn.addshape("kDiamond.gif")

#Clover
wn.addshape("1Clover.gif")
wn.addshape("2Clover.gif")
wn.addshape("3Clover.gif")
wn.addshape("4Clover.gif")
wn.addshape("5Clover.gif")
wn.addshape("6Clover.gif")
wn.addshape("7Clover.gif")
wn.addshape("8Clover.gif")
wn.addshape("9Clover.gif")
wn.addshape("10Clover.gif")
wn.addshape("jClover.gif")
wn.addshape("qClover.gif")
wn.addshape("kClover.gif")

#more shapes

wn.addshape("back.gif")
wn.addshape("clickme.gif")
wn.addshape("autoplace.gif")

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
    
listT[0].shape("1Heart.gif")
listT[0].val = 14
listT[1].shape("2Heart.gif")
listT[1].val = 2
listT[2].shape("3Heart.gif")
listT[2].val = 3
listT[3].shape("4Heart.gif")
listT[3].val = 4
listT[4].shape("5Heart.gif")
listT[4].val = 5
listT[5].shape("6Heart.gif")
listT[5].val = 6
listT[6].shape("7Heart.gif")
listT[6].val = 7
listT[7].shape("8Heart.gif")
listT[7].val = 8
listT[8].shape("9Heart.gif")
listT[8].val = 9
listT[9].shape("10Heart.gif")
listT[9].val = 10
listT[10].shape("jHeart.gif")
listT[10].val = 11
listT[11].shape("qHeart.gif")
listT[11].val = 12
listT[12].shape("kHeart.gif")
listT[12].val = 13

#Spade setting shapes

listT[13].shape("1Spade.gif")
listT[13].val = 14
listT[14].shape("2Spade.gif")
listT[14].val = 2
listT[15].shape("3Spade.gif")
listT[15].val = 3
listT[16].shape("4Spade.gif")
listT[16].val = 4
listT[17].shape("5Spade.gif")
listT[17].val = 5
listT[18].shape("6Spade.gif")
listT[18].val = 6
listT[19].shape("7Spade.gif")
listT[19].val = 7
listT[20].shape("8Spade.gif")
listT[20].val = 8
listT[21].shape("9Spade.gif")
listT[21].val = 9
listT[22].shape("10Spade.gif")
listT[22].val = 10
listT[23].shape("jSpade.gif")
listT[23].val = 11
listT[24].shape("qSpade.gif")
listT[24].val = 12 
listT[25].shape("kSpade.gif")
listT[25].val = 13

#Colver setting shapes

listT[26].shape("1Clover.gif")
listT[26].val = 14
listT[27].shape("2Clover.gif")
listT[27].val = 2
listT[28].shape("3Clover.gif")
listT[28].val = 3
listT[29].shape("4Clover.gif")
listT[29].val = 4
listT[30].shape("5Clover.gif")
listT[30].val = 5
listT[31].shape("6Clover.gif")
listT[31].val = 6
listT[32].shape("7Clover.gif")
listT[32].val = 7
listT[33].shape("8Clover.gif")
listT[33].val = 8
listT[34].shape("9Clover.gif")
listT[34].val = 9
listT[35].shape("10Clover.gif")
listT[35].val = 10
listT[36].shape("jClover.gif")
listT[36].val = 11
listT[37].shape("qClover.gif")
listT[37].val = 12
listT[38].shape("kClover.gif")
listT[38].val = 13

#Diamond setting shapes

listT[39].shape("1Diamond.gif")
listT[39].val = 14
listT[40].shape("2Diamond.gif")
listT[40].val = 2
listT[41].shape("3Diamond.gif")
listT[41].val = 3
listT[42].shape("4Diamond.gif")
listT[42].val = 4
listT[43].shape("5Diamond.gif")
listT[43].val = 5
listT[44].shape("6Diamond.gif")
listT[44].val = 6
listT[45].shape("7Diamond.gif")
listT[45].val = 7
listT[46].shape("8Diamond.gif")
listT[46].val = 8
listT[47].shape("9Diamond.gif")
listT[47].val = 9
listT[48].shape("10Diamond.gif")
listT[48].val = 10
listT[49].shape("jDiamond.gif")
listT[49].val = 11
listT[50].shape("qDiamond.gif")
listT[50].val = 12
listT[51].shape("kDiamond.gif")
listT[51].val = 13

#להפוך לFOR


    

#click me button + auto place
click = turtle.Turtle(visible = False)
click.speed(0)
click.penup()
click.setpos(0,100)
click.shape("clickme.gif")

auto = turtle.Turtle(visible = False)
auto.speed(0)
auto.penup()
auto.setpos(0,0)
auto.shape("autoplace.gif")


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
fake1.shape("back.gif")
fake2.shape("back.gif")
fake1.setpos(-200,400)#computer
fake2.setpos(-200,-400)#player
fake1.st()
fake2.st()


fakep_1.speed(0)
fakep_1.penup()
fakep_1.shape("back.gif")
fakep_1.hideturtle() #player

fakep_2.speed(0)
fakep_2.penup()
fakep_2.shape("back.gif")
fakep_2.hideturtle() #player

fakep_3.speed(0)
fakep_3.penup()
fakep_3.shape("back.gif")
fakep_3.hideturtle() #player

fakec_1.speed(0)
fakec_1.penup()
fakec_1.shape("back.gif")
fakec_1.hideturtle() #computer

fakec_2.speed(0)
fakec_2.penup()
fakec_2.shape("back.gif")
fakec_2.hideturtle() #computer

fakec_3.speed(0)
fakec_3.penup()
fakec_3.shape("back.gif")
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
numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
#numcards2

numcards2 = turtle.Turtle(visible = False)
numcards2.speed(0)
numcards2.hideturtle()
numcards2.color("black")
numcards2.penup()
numcards2.setpos(-265,340)
numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))

auto.showturtle()
click.showturtle()

print("************************")


#winnername

win = turtle.Turtle(visible = False)
win.speed(0)
win.hideturtle()
win.color("Red")
win.penup()
win.setpos(-265,0)

s=True

while s==True:
    wn.update()
    
    def cardson(x,y):
                  
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
            win.setpos(-325,0)
            click.hideturtle()
            auto.hideturtle()
            win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
            s=False
        
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
                numcards1.clear()
                numcards2.clear()
                numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                print("Computer Won!!!")
                print("************************")
                
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
                numcards1.clear()
                numcards2.clear()
                numcards1.write(playerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                numcards2.write(computerc, move=False, align="left", font=("Aharoni", 105, "normal"))
                print("Player Won!!!")
                print("************************")

            
                    
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
                    numcards1.clear()
                    numcards2.clear()
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
                    numcards1.clear()
                    numcards2.clear()
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
                win.setpos(-300,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False

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
                win.setpos(-275,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Draw!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False            

                
        


    





    def forward(x,y):
        checkwhile = True
        x = True


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
                win.setpos(-325,0)
                click.hideturtle()
                auto.hideturtle()
                win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                s=False
                checkwhile=False
          
            
            
            

            
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
                    numcards1.clear()
                    numcards2.clear()
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
                    numcards1.clear()
                    numcards2.clear()
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
                        x = True
                        while x == True:
                            list1random = random.randint(4,len(list1)-1)
                            list2random = random.randint(4,len(list2)-1)
                            list1.insert(4,list1[list1random])
                            list2.insert(4,list2[list2random])
                            list1.pop(list1random+1)
                            list2.pop(list2random+1)
                            if(list1[4] != list2[4]):
                                    x = False
                            
                    
        
                             
                    list1[4].showturtle()
                    list2[4].showturtle()
                    
                    if(list1[4].val>list2[4].val):
                        list1.append(list2[1])
                        list1.append(list2[2])
                        list1.append(list2[3])
                        list1.append(list2[4])
                        list1.append(list2[0])


                        list2.remove(list2[3])
                        list2.remove(list2[4])
                        list2.remove(list2[0])
                        list2.remove(list2[1])
                        list2.remove(list2[2])
                        
                        
                        
                        
                        
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
                        numcards1.clear()
                        numcards2.clear()
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


                        list1.remove(list1[3])
                        list1.remove(list1[4])
                        list1.remove(list1[0])
                        list1.remove(list1[1])
                        list1.remove(list1[2])
                        
                          

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
                        numcards1.clear()
                        numcards2.clear()
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
                    win.setpos(-300,0)
                    click.hideturtle()
                    auto.hideturtle()
                    win.write("Player Won!", move=False, align="left", font=("Agency FB", 105, "normal"))
                    s=False
                    checkwhile=False

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
                    win.setpos(-275,0)
                    click.hideturtle()
                    auto.hideturtle()
                    win.write("Draw!", move=False, align="left", font=("Agency FB", 105, "normal"))
                    s=False            
                    checkwhile=False

                    
            
        
        

    
 



    
    turtle.listen()
    click.onclick(cardson, 1)
    auto.onclick(forward, 1)

    turtle.mainloop()  


    




                















