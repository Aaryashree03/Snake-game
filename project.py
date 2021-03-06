# Simple Snake game using Turtle module 
import turtle
import time
import random

delay = 0.1

# score
score = 0
high_score = 0

# setting the screen
wn=turtle.Screen()
wn.title("Snake Game ")
wn.bgcolor("pink")
wn.setup(width=600,height=600)
wn.tracer(0)  

#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction ="stop"

# snake food
food=turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color ("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:00  High score:00" , align="center" , font =("Courier", 24, "normal"))

# functions
def go_up():
    if head.direction != "down":
       head.direction = "up"

def go_down():
     if head.direction != "up":
        head.direction = "down"

def go_left():
     if head.direction != "right":
        head.direction = "left"

def go_right():
     if head.direction != "left":
        head.direction = "right"    
def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction=="down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction=="left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction=="right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

# main game loop
while True:
    wn.update()
    # check for collision with border
    if head.xcor()>260 or head.xcor()<-260 or head.ycor()>260 or head.ycor()<-260:
         time.sleep(1)
         head.goto(0,0)
         head.direction = "stop"
        # hide segments
         for segment in segments:
             segment.goto(1000,1000)
        # clear the segments list
         segments.clear()
        # reset the score
         score= 0
        #  update the score display
         pen.clear()
         pen.write ("Score :{} High Score :{}".format (score , high_score),align="center" , font =("Courier", 24, "normal"))
     
     # check for a collison with the food
    if head.distance(food) < 20:
        # move the food into random spot
        x = random.randint(-260,260)
        y=random.randint(-260,260)
        food.goto(x , y)
        # increase the score
        score += 10
    # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    # shorten the delay
        delay -= 0.001

        if score > high_score:
          high_score= score
        pen.clear()
        pen.write ("Score :{} High Score :{}".format (score , high_score),align="center" , font =("Courier", 24, "normal"))
    # move the end segments first in reverse order
    for index in range (len(segments)-1, 0 ,-1):
        x = segments[index -1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
     
    # check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
    # Hide the segments
            for segment in segments:
             segment.goto(1000,1000)
        # clear the segments list
            segments.clear()
            # reset the score
            score= 0
            # update the display score
            pen.clear()
            pen.write ("Score :{} High Score :{}".format (score , high_score),align="center" , font =("Courier", 24, "normal"))
  
   time.sleep(delay)
wn.mainloop()
