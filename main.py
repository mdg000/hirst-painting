# 100 Days of Code
# Hirst Painting

import turtle as t
import random

# colors pulled from a Hirst Dot Painting using the cologram package
color_list = [(231, 206, 83), (229, 147, 85), (119, 166, 186), (160, 13, 19), (30, 110, 159), (235, 81, 44),
              (215, 222, 228), (5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144), (207, 62, 22),
              (23, 132, 41), (245, 201, 4), (10, 42, 77), (13, 64, 41), (137, 83, 98), (83, 17, 24), (46, 168, 74),
              (3, 66, 140), (173, 133, 149), (36, 25, 21), (45, 151, 198), (220, 63, 68), (227, 171, 162),
              (73, 135, 188), (172, 204, 174)]

# brush setup
t.colormode(255)
my_brush = t.Turtle()
my_brush.pencolor()
my_brush.penup()
my_brush.hideturtle()
my_brush.pensize(17)
my_brush.speed("fastest")
y = 230
x = -230

# paints 100 randomly colored dots, in a 10 by 10 grid
for i in range(10):
    my_brush.sety(y)
    my_brush.setx(x)
    y -= 50
    for j in range(10):
        my_brush.pendown()
        my_brush.fd(0)
        my_brush.penup()
        my_brush.fd(50)
        my_brush.pencolor(random.choice(color_list))

screen = t.Screen()
screen.exitonclick()