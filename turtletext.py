import turtle
from turtle import Screen, Turtle
import math
t = turtle.Pen()

count = 0

def intro():
    global count
    t.reset()
    Screen().setup(1920,1080)
    t.penup()
    t.left(180)
    t.forward(940)
    t.right(90)
    t.forward(480)
    t.left(90)
    t.pendown()
    t.left(180)
    count = 0

intro()

#forward and left functions
def f(amt):
    t.forward(amt)

def l(deg):
    t.left(deg)

#text input
x = input("Text : ")

#letter functions
def A():
    l(90);f(40);l(270);f(20);l(270);f(20);l(270);f(20);l(180);f(20);l(270);f(20);l(90);t.penup();f(10);t.pendown()

def B():
    l(90);f(40);l(180);f(20);l(90);f(20);l(270);f(20);l(270);f(20);l(180);f(20);t.penup();f(10);t.pendown()

def C():
    l(90)
    f(40)
    l(270)
    f(20)
    t.penup()
    l(270)
    f(40)
    t.pendown()
    l(270)
    f(20)
    l(180)
    t.penup()
    f(30)
    t.pendown()

def D():
    f(20)
    l(90)
    f(40)
    l(180)
    f(20)
    l(270)
    f(20)
    l(90)
    f(20)
    l(90)
    f(20)
    t.penup()
    f(10)
    t.pendown()

def E():
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    t.penup()
    l(270)
    f(40)
    l(90)
    f(10)
    t.pendown()

def F():
    l(90)
    f(20)
    l(270)
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    t.penup()
    l(270)
    f(40)
    l(90)
    f(10)
    t.pendown()

def G():
    l(90)
    f(40)
    l(270)
    f(20)
    t.penup()
    l(270)
    f(40)
    t.pendown()
    l(270)
    f(20)
    l(180)
    f(20)
    l(90)
    f(20)
    l(90)
    f(10)
    t.backward(10)
    l(90)
    f(20)
    l(90)
    t.penup()
    f(10)
    t.pendown()

def H():
    l(90)
    f(40)
    l(180)
    f(20)
    l(90)
    f(20)
    l(90)
    f(20)
    l(180)
    f(40)
    l(90)
    t.penup()
    f(10)
    t.pendown()
    
def I():
    f(10)
    l(90)
    f(40)
    l(90)
    f(10)
    l(180)
    f(20)
    l(180)
    f(10)
    l(90)
    f(40)
    l(90)
    f(10)
    t.penup()
    f(10)
    t.pendown()

def J():
    f(10)
    l(90)
    f(40)
    l(90)
    f(10)
    l(180)
    f(20)
    l(180)
    f(10)
    l(90)
    f(40)
    l(90)
    t.penup()
    f(20)
    t.pendown()

def K():
    l(90)
    f(40)
    l(180)
    f(20)
    l(90)
    l(45)
    f(math.sqrt(800))
    l(180)
    f(math.sqrt(800))
    l(90)
    f(math.sqrt(800)) 
    l(45)
    t.penup()
    f(10)
    t.pendown()

def L():
    l(90)
    f(40)
    l(180)
    f(40)
    l(90)
    f(20)
    t.penup()
    f(10)
    t.pendown()

def M():
    l(90)
    f(40)
    l(180)
    l(45)
    f(math.sqrt(800))
    l(90)
    f(math.sqrt(800)) 
    l(45)
    l(180)
    f(40)
    l(90)
    t.penup()
    f(10)
    t.pendown()

def N():
    l(90)
    f(40)
    l(180)
    l(26.5650511771)
    f(math.sqrt(2000))
    l(180-26.5650511771)
    f(40)
    l(180)
    f(40)
    l(90)
    t.penup()
    f(10)
    t.pendown()

def O():
    l(90)
    f(40)
    l(270)
    f(20)
    l(270)
    f(40)
    l(270)
    f(20)
    l(180)
    f(20)
    t.penup()
    f(10)
    t.pendown()

def P():
    l(90)
    f(40)
    l(270)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    l(90)
    f(20)
    l(90)
    t.penup()
    f(30)
    t.pendown()

def Q():
    l(90)
    f(40)
    l(270)
    f(20)
    l(270)
    f(40)
    l(270)
    f(20)
    l(180)
    f(20)
    l(90)
    l(45)
    f(20)
    l(180)
    f(30)
    l(180)
    f(10)
    l(45)
    l(180)
    t.penup()
    f(10)
    t.pendown()
    
def R():
    P()
    t.penup()
    t.backward(10)
    l(90)
    l(45)
    t.pendown()
    f(math.sqrt(800))
    l(180)
    f(math.sqrt(800))
    l(45)
    t.penup()
    f(10)
    t.pendown()

def S():
    f(20)
    l(90)
    f(20)
    l(90)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    l(270)
    t.penup()
    f(40)
    l(90)
    f(10)
    t.pendown()

def T():
    t.penup()
    f(10)
    l(90)
    f(40)
    l(90)
    f(10)
    l(180)
    t.pendown()
    f(20)
    l(180)
    f(10)
    l(90)
    f(40)
    l(90)
    t.penup()
    f(20)
    t.pendown()

def U():
    l(90)
    f(40)
    l(180)
    f(40)
    l(90)
    f(20)
    l(90)
    f(40)
    l(180)
    f(40)
    l(90)
    t.penup()
    f(10)
    t.pendown()

def V():
    t.penup()
    l(90)
    f(40)
    l(180)
    l(26.5650511771)
    t.pendown()
    f(math.sqrt(2000))
    l(180-(26.5650511771+26.5650511771))
    f(math.sqrt(2000))
    l(180+26.5650511771)
    t.penup()
    f(40)
    l(90)
    f(10)
    t.pendown()

def W():
    l(90)
    f(40)
    l(180)
    f(40)
    l(90)
    l(45)
    f(math.sqrt(800))
    l(270)
    f(math.sqrt(800))
    l(45)
    l(90)
    f(40)
    l(180)
    f(40)
    l(90)
    t.penup()
    f(10)
    t.pendown()

def X():
    l(90-26.5650511771)
    f(math.sqrt(2000))
    l(270+180+26.5650511771)
    t.penup()
    f(20)
    t.pendown()
    l(90+26.5650511771)
    f(math.sqrt(2000))
    l(90-26.5650511771)
    t.penup()
    f(10)
    t.pendown()

def Y():
    t.penup()
    f(10)
    l(90)
    t.pendown()
    f(20)
    l(26.5650511771)
    f(math.sqrt(2000)/2)
    l(180)
    f(math.sqrt(2000)/2)
    l(180-(26.5650511771+26.5650511771))
    f(math.sqrt(2000)/2)
    l(180)
    f(math.sqrt(2000)/2)
    l(26.5650511771)
    f(20)
    l(90)
    t.penup()
    f(20)
    t.pendown()

def Z():
    f(20)
    l(180)
    f(20)
    l(270)
    l(360-26.5650511771)
    f(math.sqrt(2000))
    l(26.5650511771)
    l(90)
    f(20)
    l(180)
    f(20)
    l(270)
    t.penup()
    f(40)
    l(90)
    f(10)
    t.pendown()

def turtle_writer():
    global count
    for i in x.upper():
        if count < 187:
            #space
            if i == ' ':
                t.penup()
                f(20)
                t.pendown()
                count+=1
            #letters
            if i == 'A':
                A()
                count+=3
            if i == 'B':
                B()
                count+=3
            if i == 'C':
                C()
                count+=3
            if i == 'D':
                D()
                count+=3
            if i == 'E':
                E()
                count+=3
            if i == 'F':
                F()
                count+=3
            if i == 'G':
                G()
                count+=3
            if i == 'H':
                H()
                count+=3
            if i == 'I':
                I()
                count+=3
            if i == 'J':
                J()
                count+=3
            if i == 'K':
                K()
                count+=3
            if i == 'L':
                L()
                count+=3
            if i == 'M':
                M()
                count+=4
            if i == 'N':
                N()
                count+=3
            if i == 'O':
                O()
                count+=3
            if i == 'P':
                P()
                count+=3
            if i == 'Q':
                Q()
                count+=3
            if i == 'R':
                R()
                count+=3
            if i == 'S':
                S()
                count+=3
            if i == 'T':
                T()
                count+=3
            if i == 'U':
                U()
                count+=3
            if i == 'V':
                V()
                count+=4
            if i == 'W':
                W()
                count+=4
            if i == 'X':
                X()
                count+=3
            if i == 'Y':
                Y()
                count+=3
            if i == 'Z':
                Z()
                count+=3
        elif not count < 187:
            t.penup()
            l(180)
            f(count * 10)
            l(90)
            f(50)
            l(90)
            count = 0
            t.pendown()

    input()

turtle_writer()
input()