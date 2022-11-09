import time
from turtle import Turtle, Screen
import random

DIRECTIONS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.body_formation()
        self.head = self.segments[0]

    def body_formation(self):
        for i in DIRECTIONS:
            self.add(i)

    def add(self, i):
        t = Turtle(shape='circle')
        t.color('white')
        t.penup()
        t.goto(i)
        self.segments.append(t)

    def extend(self):
        self.add(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right_direction(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left_direction(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score_print()

    def score_print(self):
        self.write(f"score:{self.score}", align='center', font=('Arial', 15, "normal"))

    def game_over(self):
        self.color('white')
        self.goto(0, 0)
        self.write(f"Game over", align='center', font=('Arial', 15, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.score_print()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        x = random.randint(-280, 280)
        y = random.randint(-280, 250)
        self.goto(x, y)

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right_direction, 'Right')
screen.onkey(snake.left_direction, 'Left')
food = Food()
game = True
score = Score()
while game:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        score.increase()
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        game = False
        score.game_over()
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game = False
            score.game_over()
screen.exitonclick()

