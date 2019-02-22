import turtle 
import os 

Wn = turtle.Screen()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('black')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
      border_pen.fd(600)
      border_pen.lt(90)
border_pen.hideturtle()


player = turtle.Turtle()
player.color('red')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

Wn.exitonclick() 