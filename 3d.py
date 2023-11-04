# from turtle import *
# color('cyan')
# bgcolor('black')
# speed(11)
# right(45)
# for i in range(150):
#     if 7 < i < 62:
#         left(5)
#     if 80 < i < 133:
#         right(5)
#     circle(30)
#     if i < 80:
#         forward(10)
#     else:
#         forward(5)





# import turtle
# import math
# import random

# # Instatiate Turtle and Screen
# fred = turtle.Turtle()
# wn = turtle.Screen()

# # Dartboard coordinates
# wn.setworldcoordinates(-1,-1,1,1)

# # We don't want to leave lines by default
# fred.up()

# # Speed things up when placing darts on board.
# fred._tracer(100)

# # Highly accurate approximations with >= 1000 darts thrown
# numdarts = 1000
# insideCount = 0

# for i in range(numdarts):
#     # Generate random floating points within (-1, 1)
#     # Figured out two methods of achieving this.
    
#     # .uniform() allows a negative range, returns floating point ints.
#     randx = random.uniform(-1, 1)
#     # .random() * 2 = [0 ,2], -1 = [-1, 1]
#     randy = random.random() * 2 - 1

#     x = randx
#     y = randy
    
#     # Move to position
#     fred.goto(x, y)
    
#     # Determine how many darts actually fall within the dart board.
#     # Dartboard is centred on 0,0 with radius of 1. Therefore need
#     # to verify if dart is within 1 unit away from 0,0.
#     #
#     # Colour red if within dartboard and count. Otherwise colour blue.
#     if fred.distance(0,0) <= 1.0:
#         fred.color("red")
#         insideCount += 1
#     else:
#         fred.color("blue")
#     fred.dot()

# fred.hideturtle()

# # Consider the area of the circular dartboard. It has a radius of one so its area is pi. 
# # The area of the square piece of wood is 4 (2 x 2). 
# # The ratio of the area of the circle to the area of the square is pi/4. 
# # If we throw a whole bunch of darts and let them randomly land on the square piece of wood, 
# # some will also land on the dartboard. The number of darts that land on the dartboard, 
# # divided by the number that we throw total, will be in the ratio described above (pi/4).
# # Multiply by 4 and we have pi.

# print('Percentage of darts inside dartboard: {}'.format(insideCount / numdarts)) # requires Python3
# print('Pi Approximation: {}'.format(insideCount / numdarts * 4))                 # requires Python3
# print('Ratio of area of cirle to area of square: %f' % (math.pi / 4))
    

# wn.exitonclick()




from turtle import *
import turtle
color('cyan')
bgcolor('black')
loadWindow = turtle.Screen()
turtle.speed(7)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
 
turtle.exitonclick()