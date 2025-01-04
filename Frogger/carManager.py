from turtle import Turtle
import random as r
import colorsys

STARTING_MOVE_DISTANCE = 1
MOVE_SPEED = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 0
        self.carSpeed = 0.1

    def spawnCar(self):
        if r.randint(1, 6) == 6:
            car = Turtle("square")
            # Give cars a random color that is not too light or else it will blend with the bg
            h = r.uniform(0, 1)  # Hue
            s = r.uniform(0.5, 1)  # Saturation with a minimum value
            l = r.uniform(0.5, 1)  # Lightness with a minimum value
            r_color, g_color, b_color = colorsys.hls_to_rgb(h, l, s)
            car.color(r_color, g_color, b_color)
            car.setheading(180)
            car.speed(0)
            car.penup()
            car.shapesize(1, 3, 0)
            car.goto(320, r.randint(-270, 270))
            self.cars.append(car)

    def carsMove(self):
        for car in self.cars:
            car.forward(MOVE_SPEED)

    def resetCars(self):
        # fix for the bug where all cars would be at the centre being a black square
        for car in self.cars:
            car.reset()
            car.color("white")
            car.goto(-999, -999)
        self.cars = []

    def speedUp(self):
        self.carSpeed /= 1.25
