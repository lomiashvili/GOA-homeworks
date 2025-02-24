from turtle import *

#we want to paint a house

#step 1:  draw a square
speed(30)
width(5)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
penup()
goto(50, 150)
pendown()
left(30)
forward(100)
right(90)
forward(40)
right(90)
forward(100)
right(90)
forward(40)
penup()
goto(30, 150)
pendown()
right(90)
forward(100)
penup()
goto(10, 100)
pendown()
left(90)
forward(40)

penup()
goto(150, 50)
pendown()
forward(40)
left(90)
forward(100)
left(90)
forward(40)
left(90)
forward(100)
penup()
goto(170, 50)
pendown()
left(180)
forward(100)
penup()
goto(150, 100)
pendown()
right(90)
forward(40)






exitonclick()
