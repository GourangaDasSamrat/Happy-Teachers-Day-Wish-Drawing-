import turtle
import random
import colorsys


alphabet = {
    'A': ((0,0),(0.5,1),(0.75,0.5),(0.25,0.5),(0.75,0.5),(1,0)),
    'C': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'D': ((0,0),(0,1),(0.625 ,1),(0.75,0.875),(0.75,0.125),(0.625,0),(0,0)),
    'E': ((0.75,0),(0,0),(0,0.5),(0.75,0.5),(0,0.5),(0,1),(0.75,1)),
    'H': ((0,0),(0,1),(0,0.5),(0.75,0.5),(0.75,1),(0.75,0)),
    'P': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5)),
    'R': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.875,0)),
    'S': ((0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,0.375),(0.675,0.5),(0.125,0.5),(0,0.625),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'T': ((0,1),(0.5,1),(0.5,0),(0.5,1),(1,1)),
    'Y': ((0,1),(0.375,0.5),(0.375,0),(0.375,0.5),(0.75,1)),
}


screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(650,650)
screen.title('Teacher Day wishes -by Gouranga Das Samrat')
turtle.hideturtle()
    


myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed()

screen.bgcolor("#000000")
myPen.pensize(10)
n=200
chasers = []
for i in range(n):
    chasers.append(turtle.Turtle())

h = 0
for i in range(n):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    chasers[i].color(c)
    chasers[i].up()
    chasers[i].goto(random.uniform(-500,500), random.uniform(-500,500))
chasers[n-1].goto(0,-300)
chasers[n-1].shape('circle')
chasers[n-1].shapesize(0.1)

def chase():
    for i in range(n-1):
        angle = chasers[i].towards(chasers[i+1])
        chasers[i].seth(angle)
    chasers[n-1].left(2)
    chasers[n-1].fd(10)
    for i in range(n-1):
        chasers[i].fd(10)
    screen.update()
    screen.ontimer(chase,1000//20)
    
def slow():
    for i in range(500):
        turtle.speed(10)


def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      slow()

      for dot in letter:
        slow()
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        slow()
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#Main Program Starts Here
chase()

fontSize = 50
characterSpacing = 13
fontColor = "ivory"

message = "happy "
displayMessage(message,fontSize,fontColor,-150,60)

fontSize = 40
characterSpacing = 13
fontColor = "hot pink"

message = "Teachers "
displayMessage(message,fontSize,fontColor,-230,0)

fontSize = 45
characterSpacing = 7
fontColor = "gold"

message = "Day"
displayMessage(message,fontSize,fontColor,-80,-70)


def my_goto(x, y):
    turtle.pencolor("orange")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.pendown()
my_goto(-350, 450)
turtle.write('By:- Trick with Rahul', font=("Bradley Hand ITC", 10, "bold"))
turtle.done()