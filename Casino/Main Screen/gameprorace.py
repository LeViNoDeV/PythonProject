
from tkinter import*
import time
import random
import sys
import os






helpc=0 




winner =False

horse1_x = 0
horse1_y = 20

horse2_x = 0
horse2_y = 120

horse3_x = 0
horse3_y = 220



def start_game():
    
    global horse2_x
    global horse1_x
    global horse3_x
    global winner
    global casinochips
    
    
    
    
    while winner ==False:
        time.sleep(0.03)
        random_move_horse_2 = random.randrange(0,20)
        random_move_horse_1 = random.randrange(0,20)
        random_move_horse_3 = random.randrange(0,20)
        #update x pos from both horses
        horse2_x += random_move_horse_2
        horse1_x += random_move_horse_1
        horse3_x +=random_move_horse_3

        move_horses(random_move_horse_1,random_move_horse_2,random_move_horse_3)
        main_screen.update()
        winner = chek_winner()
    if winner =="TIE":
        Label(main_screen,text=winner,font=('calibri',40),fg= 'red',bg ='white').place(x= 200,y= 290)
    if winner == 'your horse has won':
        Label(main_screen,text=winner,font=('calibri',40),fg = 'red',bg ='white').place(x= 250, y= 350)
        Label(main_screen,text=  casinochips*2,font=('calibri',20),fg = 'red',bg ='white').place(x= 100, y= 500)
    else:    Label(main_screen,text=winner + ' wins',font=('calibri',40),fg = 'red',bg ='white').place(x= 250, y= 350)




def move_horses(horse_1_random_move,horse_2_random_move,horse_3_random_move):
    Canvas.move(horse_1,horse_1_random_move,0)
    Canvas.move(horse_2,horse_2_random_move,0)
    Canvas.move(horse_3,horse_3_random_move,0)

def chek_winner():
    
    global helpc
    
    if horse2_x >= 550 and horse1_x >=550 and horse3_x >510:
        return "TIE"
    if horse2_x >= 550 and horse1_x >=550:
        return 'TIE'    
    if horse2_x >= 550 and horse3_x >=550:
        return 'TIE'        
    if horse3_x >= 550 and horse1_x >=550:
        return 'TIE'   
                   
    
    
    if horse1_x>=550 and helpc == 1 :
         return "your horse has won"
    if horse2_x>=550 and helpc==2 :       
         return "your horse has won"       
    if horse3_x>=550 and helpc ==3:
         return "your horse has won"  
    
    if horse2_x>=550:
        return"horse 2"  
    if horse1_x>=550:
        return"horse 1"
    if horse3_x>=550:
        return"horse 3"        
             
    return False  



def End_game():
    exit()



def new_round():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
#buttons
#main screen
main_screen =Tk()
main_screen.title('horse race')
main_screen.geometry('800x600')
main_screen.config(background='white')



#canvas setup
Canvas =Canvas(main_screen,width= 700, height=400,bg ='white')
Canvas.pack(pady = 20)

#adding images
horse_image = PhotoImage(file="racegameadam/horseimage222.jpg.png", master=main_screen)
horse_image2 = PhotoImage(file="racegameadam/horseimage222.jpg.png", master=main_screen)
horse_image3 = PhotoImage(file="racegameadam/horseimage222.jpg.png", master=main_screen)
#resizing images
horse_image = horse_image.zoom(5)
horse_image = horse_image.subsample(25)
horse_image2 = horse_image2.zoom(5)
horse_image2 = horse_image2.subsample(25)
horse_image3 = horse_image2.zoom(5)
horse_image3 = horse_image2.subsample(25)
  
#adding images to canvas
horse_1 = Canvas.create_image(horse1_x,horse1_y, anchor = NW ,image = horse_image)
horse_2 = Canvas.create_image(horse2_x,horse2_y,anchor = NW ,image = horse_image )
horse_3 = Canvas.create_image(horse3_x,horse3_y,anchor = NW ,image = horse_image )
#adding labels to the screen (text)
l1 =Label(main_screen, text = 'select your horse (1,2,3)',font=('calibri',20),fg='red',bg='white' )
l1.place(x=310,y =380)
l2 =Label(main_screen, text = 'f\ni\nn\ni\ns\nh\n',font=('calibri',20),fg='red',bg='white' )
l2.place(x=735,y=385)



b1 =Button (main_screen,text='Play',height=2,width=15, bg ='white', font=('calibri',20),fg='red' ,command=start_game)
b1.place_forget()
b2 = Button(main_screen,text='Exit Game',height=2,width=10,bg='white',font=('calibri',10),fg='red',command= End_game)
b2.place(x=0,y=0)
b3 = Button(main_screen,text='New Round',height=2,width=10,bg='white',font=('calibri',10),fg='red',command= new_round )
b3.place(x=700,y=0)
#creating finish line
# Coordinates of the line
coordinates = 700,0,700,400
#dashed line!
Canvas.create_line(coordinates, dash=(5,3) , width=9, fill='red')
Canvas.pack()


#creating entery box 
def button_command():
    global helpc
    
    text = entery1.get()
    if text =='1':
        helpc = 1
        l5 =Label(main_screen, text = 'your horse is: horse 1',font=('calibri',20),fg='red',bg='white' )
        l5.place(x=70,y =420)
        
        l1.place_forget()
        entery1.pack_forget()
        b3.pack_forget()
        
        entery2.pack()
        b4.pack()
        l6 =Label(main_screen, text = 'place your bet',font=('calibri',20),fg='red',bg='white' )
        l6.place(x=330,y =380)
    if text =='2':
        helpc = 2
        l5 =Label(main_screen, text = 'your horse is: horse 2',font=('calibri',20),fg='red',bg='white' )
        l5.place(x= 70,y =420)
        entery1.delete(0,899) 
        l1.place_forget()   
        entery1.pack_forget()
        b3.pack_forget()
        entery2.pack()
        b4.pack()
        l6 =Label(main_screen, text = 'place your bet',font=('calibri',20),fg='red',bg='white' )
        l6.place(x=330,y =380)

    if text =='3':
        helpc = 3
        l5 =Label(main_screen, text = 'your horse is: horse 3',font=('calibri',20),fg='red',bg='white' )
        l5.place(x=70,y =420)
        
        l1.place_forget()  
        entery1.pack_forget()
        b3.pack_forget()
        entery2.pack()
        b4.pack()
        l6 =Label(main_screen, text = 'place your bet',font=('calibri',20),fg='red',bg='white' )
        l6.place(x=330,y =380)
    return None





#casino chips


casinochips =10000
chiptxt=Label(main_screen, text = 'chips: ' ,font=('calibri',20),fg='red',bg='white')
chiptxt.place(x=10 ,y=500)
lchip = Label(main_screen, text = casinochips ,font=('calibri',20),fg='red',bg='white')
lchip.place(x=100,y=500)

def button_command2():
    textbet = entery2.get()
    texthelp = int(textbet)
    if texthelp>0 and texthelp<=10000:
        lchip.place_forget()
        chips = casinochips-texthelp
        chip2 = Label(main_screen, text =  chips ,font=('calibri',20),fg='red',bg='white')
        chip2.place(x=100,y=500)
        
      
    b4.pack_forget()
    entery2.pack_forget()
    l7 =Label(main_screen, text = 'your bet is:   '+ textbet,font=('calibri',20),fg='red',bg='white' )
    l7.place(x=330,y =380)
    b1.place(x= 280,y=490)
    
        





entery1 = Entry(main_screen , width=20 )
entery1.pack()
text = entery1.get()

b3 = Button (main_screen,text='select', command = button_command)
b3.pack()
entery2 = Entry(main_screen , width=20 )
entery2.pack_forget()
textbet = entery2.get()

b4 = Button (main_screen,text='bet', command = button_command2)
b4.pack_forget()





main_screen.mainloop()
