from turtle import Turtle

FONT = ("New Times Roman", 24, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.goto(-235, 260)
		self.level = 1
		self.pencolor("black")
		self.write(arg=f"Level: {self.level}", align="center", font=FONT)

	def nextLevel(self):
		self.level += 1
		self.clear()
		self.write(arg=f"Level: {self.level}", align="center", font=FONT)

	def gameOver(self):
		self.goto(0, 0)
		self.write(arg="TURTLE DIED", align="center", font=FONT)
