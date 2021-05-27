import math
import turtle
bob = turtle.Turtle()

def square(length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)

def polygon(t, length, n, angle = 360):
    intn = round(n)
    for i in range(intn):
        t.fd(length)
        t.lt(angle/n)

def circle(t, r):
    polygon(t, ((2 * math.pi * r) / 50), 50)

def arc(t, r, angle):
    polygon(t, (((2 * math.pi * r) / 50) * (angle / 360)), 50, angle)



def flower(numberofPetals, angleInnerPetals, arcLength):
    for i in range(numberofPetals):
        arc(bob, arcLength, 78)
        bob.lt(angleInnerPetals)
        arc(bob, arcLength, 78)
        bob.lt(78)

flower(16, 103, 70)

turtle.mainloop()

# I don't actually know if this` works
