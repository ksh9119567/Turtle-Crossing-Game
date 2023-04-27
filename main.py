import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing game")
screen.tracer(0)

# Creating object
p1 = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p1.go_left, "Left")
screen.onkey(p1.go_right, "Right")

# Game logic
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.move_car()

    # Detecting collision
    for car in cars.all_cars:
        if car.distance(p1) < 20:
            game_is_on = False
            score.game_over()

    # Detect successful crossing
    if p1.is_at_finish_line():
        p1.go_to_start()
        cars.level_up()
        score.next_level()

screen.exitonclick()