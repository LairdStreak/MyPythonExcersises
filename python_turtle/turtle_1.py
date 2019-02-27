import turtle
from math import sin, cos, radians as rad
from colorsys import hls_to_rgb

def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    turtle.colormode(255)
    turtle.bgcolor('#202020')

    t.speed(0)
    t.width(2)

    low = 125
    mid = low * 2
    high = mid * 2

    t.up()
    t.goto(low * sin(rad(0)), mid * cos(rad(0)))
    t.down()


    for i in range(360):
        t.pencolor(*map(lambda x: round(x * 255), hls_to_rgb(i / 120, 0.5, 0.5)))
        t.goto(low * sin(rad(i)), mid * cos(rad(i)))
        t.goto(mid * sin(rad(i)), high * cos(rad(i)))
        t.goto(high * sin(rad(i)), low * cos(rad(i)))

    s.exitonclick()



if __name__ == "__main__":
    main()