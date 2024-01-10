from turtle import Turtle


class Snake:

    def __init__(self):
        self.xcor = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(self.xcor)
            self.segments.append(segment)
            self.xcor -= 20

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(20)

    def new_seg(self):
        segment = Turtle("square")
        segment.hideturtle()
        segment.color("white")
        segment.penup()
        self.segments.append(segment)
        # segment.showturtle()
        self.segments[-1].showturtle()
    #

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    #

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    #

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    #

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    # screen.listen()
    # screen.onkey(key="w", fun=up)
    # screen.onkey(key="a", fun=left)
    # screen.onkey(key="d", fun=right)
    # screen.onkey(key="s", fun=down)
    # if head.xcor() <= -400:
    #     new_seg()
