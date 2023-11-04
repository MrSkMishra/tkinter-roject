# import turtle

# my_screen = turtle.Screen()
# my_screen.bgcolor('black')
# my_pen = turtle.Turtle()

# def circle(radius):
#     my_pen.speed(20)
#     my_pen.pencolor('white')
#     for i in range(0, 360, 1):
#         my_pen.circle(radius=radius)
#         my_pen.right(1)

# def sea_shell():
#     my_pen.speed(20)
#     my_pen.pencolor('white')
#     for i in range(0, 360, 1):
#         my_pen.circle(i)
#         my_pen.right(1)


# def colour_spiral(radius):
#     my_pen.speed(20)
#     for i in range(0, 9, 1):
#         for color in ('red', 'green', 'blue', 'white'):
#             my_pen.circle(radius=radius)
#             my_pen.pencolor(color)
#             my_pen.right(10)

# def tree_pattern():
#     turtle.tracer(0)
#     my_pen.speed(20)
#     my_pen.pencolor('white')
#     my_pen.left(90)
#     for i in range(0, 4, 1):
#         my_pen.forward(10)
#         for l in range(0, 2, 1):
#             my_pen.left(40)
#             my_pen.forward(10)
#             for m in range(0, 2, 1):
#                 my_pen.left(40)
#                 my_pen.forward(10)
#                 tree()
#                 my_pen.backward(10)
#                 my_pen.right(80)
#                 my_pen.forward(10)
#                 tree()
#                 my_pen.backward(10)
#                 my_pen.left(40)
#             tree()
#             my_pen.backward(10)
#             my_pen.right(80)
#             my_pen.forward(10)
#             for n in range(0, 2, 1):
#                 my_pen.left(40)
#                 my_pen.forward(10)
#                 tree()
#                 my_pen.backward(10)
#                 my_pen.right(80)
#                 my_pen.forward(10)
#                 tree()
#                 my_pen.backward(10)
#                 my_pen.left(40)
#             tree()
#             my_pen.backward(10)
#             my_pen.left(40)
#         my_pen.backward(10)
#         my_pen.right(90)

# def tree():
#     for m in range(0, 2, 1):
#         my_pen.left(40)
#         my_pen.forward(10)
#         my_pen.backward(10)
#         my_pen.right(80)
#         my_pen.forward(10)
#         my_pen.backward(10)
#         my_pen.left(40)

# colour_spiral(100)

# turtle.done()

from turtle import * 
import cv2
import turtle

# Binary Image
color('cyan')
bgcolor('yellow')
img = cv2.imread('image.jpg', 2)
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
width = int(img.shape[1])
height = int(img.shape[0])


# Turtle Setup

my_screen = turtle.Screen()
my_screen.screensize(width, height)
my_pen = turtle.Turtle()
my_screen.tracer(0)


# Printing Loop

for i in range(int(height/2), int(height/-2),  -1):
    my_pen.penup()
    my_pen.goto(-(width / 2), i)

    for l in range(-int(width/2), int(width/2), 1):
        pix_width = int(l + (width/2))
        pix_height = int(height/2 - i)
        if bw_img[pix_height, pix_width] == 0:
            my_pen.pendown()
            my_pen.forward(1)
        else:
            my_pen.penup()
            my_pen.forward(1)
    my_screen.update()

my_pen.hideturtle()

turtle.done()