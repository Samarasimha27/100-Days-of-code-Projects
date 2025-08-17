from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

score = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        score.reset()
        snake.reset()

    for block in snake.python[1:]:
        if snake.head.distance(block) < 10:
            score.reset()

screen.exitonclick()