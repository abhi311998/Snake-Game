import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Step 1: Getting Started

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)   # Turns of the screen updates

#Step 2: Snake Head
head = turtle.Turtle()
head.speed(0) # Animation Speed of the turtle module
head.shape("circle")
head.color("black")
head.penup()  # So that no drawing is there
head.goto(0, 0)
head.direction = "stop"

# Functions
def move():
    if head.direction=="up":
        head.sety(head.ycor() + 10)
    if head.direction=="down":
        head.sety(head.ycor() - 10)
    if head.direction=="right":
        head.setx(head.xcor() + 10)
    if head.direction=="left":
        head.setx(head.xcor() - 10)

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

# Snake food
food = turtle.Turtle()
food.speed(0) # Animation Speed of the turtle module
food.shape("circle")
food.color("red")
food.penup()  # So that no drawing is there
food.goto(0, 100)

# Step 4: Snake Body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  HighScore: 0",align = "center" , font=("Courier", 24, "normal"))



# Keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")



# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # CLear the segments list
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {}  HighScrore: {}".format(score,high_score),align = "center" , font=("Courier", 24, "normal"))    

        # Reset the delay
        delay = 0.1
    
    # Check for collsion for the food
    if head.distance(food) < 10:
        # Move the food to a random spot of the screen
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)
        

        # Add a segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.0001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  HighScrore: {}".format(score,high_score),align = "center" , font=("Courier", 24, "normal"))    
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move the segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    move()

    # Check for head collsion with the body segment
    for segment in segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segmetns
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  HighScrore: {}".format(score,high_score),align = "center" , font=("Courier", 24, "normal"))    

            # Reset the delay
            delay = 0.1


    time.sleep(delay)


wn.mainloop()
