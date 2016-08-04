from turtle import *
penup()
pencolor("spring green")
goto(-200, 0)
pendown()

fillcolor("plum")
begin_fill()
def shape(sides):
    for i in range(3):
        for i in range(sides):
            forward(40)
            right(360/sides)
        penup()
        forward(70)
        pendown()
shape(3)
end_fill()

def octagon(length):
    pendown()
    fillcolor("coral")
    begin_fill()
    for i in range(8):
        forward(length)
        right(45)
    end_fill()
    penup()
octagon(40)

