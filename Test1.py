import turtle
fred = turtle.Pen()
fred.forward(100)
fred.left(90)
fred.forward(100)
fred.left (90)
fred.forward(100)
fred.left(90)
fred.forward(100)
fred.left (90)
fred.reset()
for i in range(4):
	fred.forward(100)
	fred.left(90)


for i in range(8):
	fred.forward(50)
	fred.left(45)

fred.reset()
for i in range(8):
	fred.forward(75)
	fred.left(45)


fred.color("green")
for i in range(8):
	fred.forward(100)
	fred.left(45)


fred.width(10)
for i in range(8):
	fred.forward(50)
	fred.left(45)


fred.circle(100)
