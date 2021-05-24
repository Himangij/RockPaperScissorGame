import turtle
import random
import os

###change shape
def rock(): #..i rock gets rock, no score update for both players
    global scoreP, scoreC
    player.shape(rock_img)
    ind=random.randint(0,2)
    computer.shape(images[ind])
    if ind==1: #paper
        penC.clear()
        scoreC=scoreC+1   
        penC.write('Computer: %d'%scoreC, align='center', font=(None,20))
    elif ind==2: #scissor
        penP.clear()
        scoreP=scoreP+1   
        penP.write('You: %d'%scoreP, align='center', font=(None,20))   
        
def paper():
    global scoreP, scoreC
    player.shape(paper_img)
    ind=random.randint(0,2)
    computer.shape(images[ind])
    if ind==2: #scissor
        penC.clear()
        scoreC=scoreC+1   
        penC.write('Computer: %d'%scoreC, align='center', font=(None,20))
    elif ind==0: #rock
        penP.clear()
        scoreP=scoreP+1   
        penP.write('You: %d'%scoreP, align='center', font=(None,20)) 
        
def scissor():
    global scoreP, scoreC
    player.shape(scissor_img)
    ind=random.randint(0,2)
    computer.shape(images[ind])
    if ind==0: #rock
        penC.clear()
        scoreC=scoreC+1   
        penC.write('Computer: %d'%scoreC, align='center', font=(None,20))
    elif ind==1: #paper
        penP.clear()
        scoreP=scoreP+1   
        penP.write('You: %d'%scoreP, align='center', font=(None,20)) 
        
##set screen
win=turtle.Screen()
win.bgcolor('yellow')
win.setup(width=1000, height=600)
win.title('Rock-Paper-Scissor Game')

##draw centre line to make 2 partitions for player and computer
t=turtle.Turtle()
t.speed(0)
t.pensize(3) ##..tll here it start with arrow at middle position
t.color('yellow')   #>.so a point is set
t.up()
t.setposition(0,-250)
t.down()
t.left(90) ##..take arrow to down position and turn upward
t.forward(800) ##..draw line upwards

##set rock -paper - scissor
os.chdir(r'C:\Users\hjalgaon\Desktop\projects\Rock-Paper-Scissor')
rock_img="img/rock.gif" ##..gif extension preferred
paper_img="img/paper.gif"
scissor_img="img/scissor.gif"
images=[rock_img,paper_img,scissor_img]

turtle.register_shape(rock_img)
turtle.register_shape(paper_img)
turtle.register_shape(scissor_img)

##create player
player=turtle.Turtle()
player.shape(rock_img)
player.speed(0)
player.up()
player.setposition(-150,-50) #..3rd quadrant

##create computer player
computer=turtle.Turtle()
computer.shape(rock_img)
computer.speed(0)
computer.up()
computer.setposition(350,-50) #..4th quadrant

##get input from keyboard..keyboard binding
win.listen()
win.onkey(rock,'r')

win.onkey(paper,'p')

win.onkey(scissor,'s')

##initialise score
scoreP=0
scoreC=0

penP=turtle.Turtle()
penP.speed(0)
penP.up()
penP.hideturtle()
penP.goto(-150,150)
penP.write("You: 0", align='center', font=(None,20))

penC=turtle.Turtle()
penC.speed(0)
penC.up()
penC.hideturtle()
penC.goto(350,150)
penC.write("Computer: 0", align='center', font=(None,20))

##to prevent screen from hanging
turtle.done()
turtle.bye() 
