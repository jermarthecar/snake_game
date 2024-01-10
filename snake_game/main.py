from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)

scoreboard.present_score()

on = True
while on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom")
        food.refresh()
        scoreboard.present_score()
        snake.new_seg()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        on = False
        scoreboard.game_over()

    # Detect collision with tail
    for i in snake.segments[1:]:
        if snake.head.position() == i.position():
            on = False
            scoreboard.game_over()

screen.exitonclick()
