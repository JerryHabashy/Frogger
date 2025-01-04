import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.carSpeed)
    screen.update()
    car_manager.spawnCar()
    car_manager.carsMove()

    # player reached the top
    if player.ycor() > 280:
        player.resetPos()
        car_manager.resetCars()
        scoreboard.nextLevel()
        car_manager.speedUp()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

screen.exitonclick()