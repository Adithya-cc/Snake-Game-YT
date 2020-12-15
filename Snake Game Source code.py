#========Snake Game ==========
import turtle
import time
import random

delay = 0.1

# Windows
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

#border
t = turtle.Turtle()

t.goto(-300, 300)
t.hideturtle()
t.fillcolor("white")
t.begin_fill()
for i in range(4):
    t.forward(590)
    t.right(90)
t.end_fill()

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(x = random.randint(-260, 260),y = random.randint(-260, 260))

segments = []

# Score
score = turtle.Turtle()
score.color("black")
score.penup()
score.hideturtle()
score.goto(-270, 265)
score.write("Score: 0", font=("Courier", 16, "bold"))
score_value = 0

# High score
hiscore = turtle.Turtle()
hiscore.color("black")
hiscore.penup()
hiscore.hideturtle()
hiscore.goto(270, 265)
hiscore.write("High Score: 0",align= "right", font=("Courier", 16, "bold"))
hidgh_score = 0


# direction of snake
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
def go_stop():
    head.direction = "stop"

# movement of snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#get controles
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")
win.onkeypress(go_stop,"space")

#collusion
def collusion():
    head.direction = "stop"
    time.sleep(1)
    head.goto(0, 0)
    food.goto(x, y)

    for i in segments:
        i.goto(1000, 1000)

    segments.clear()


while True:
    win.update()
    # random movement
    x = random.randint(-260, 260)
    y = random.randint(-260, 260)

    # make a border
    if head.xcor()<-270 or head.xcor()>260 or head.ycor()<-260 or head.ycor()>270:
        collusion()
        # delay time
        delay = 0.1
        # scores
        if score_value > hidgh_score:
            hidgh_score = score_value

        score_value = 0

        score.clear()
        score.write("Score: {}".format(score_value), font=("Courier", 16, "bold"))
        hiscore.clear()
        hiscore.write("High Score: {}".format(hidgh_score), align="right", font=("Courier", 16, "bold"))


    # eat food
    if head.distance(food)<20:
        food.goto(x,y)
        # snake's Body
        body = turtle.Turtle()
        body.shape("square")
        body.color("blue")
        body.penup()
        segments.append(body)

        # delay time
        delay -= 0.001
        # scores
        score_value += 10

        score.clear()
        score.write("Score: {}".format(score_value), font=("Courier", 16, "bold"))


    #move body in order
    for i in range (len(segments) -1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments [0].goto(x,y)



    move()
    # body collusion
    for i in segments:
        if i.distance(head) < 20:
            collusion()
            # delay time
            delay = 0.1
            # scores
            if score_value > hidgh_score:
                hidgh_score = score_value

            score_value = 0

            score.clear()
            score.write("Score: {}".format(score_value), font=("Courier", 16, "bold"))
            hiscore.clear()
            hiscore.write("High Score: {}".format(hidgh_score), align="right", font=("Courier", 16, "bold"))


    time.sleep(delay)


win.mainloop()