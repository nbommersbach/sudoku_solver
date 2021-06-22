def goto(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def square(t, size):
    t.pensize(5)
    for i in range(4):
        t.forward(size)
        t.right(90)

    t.pensize(1)


def line(t, bx, by, ex, ey):
    goto(t, bx, by)
    t.goto(ex, ey)


def grid(t, size):
    goto(t, -size / 2, size / 2)
    square(t, size)

    traveller_x = size / 2

    for i in range(8):
        if (i + 1) % 3 == 0:
            t.pensize(5)
        else:
            t.pensize(1)

        traveller_x -= size / 9
        line(t, traveller_x, size / 2, traveller_x, -size / 2)

    traveller_y = size / 2

    for i in range(8):
        if (i + 1) % 3 == 0:
            t.pensize(5)
        else:
            t.pensize(1)

        traveller_y -= size / 9
        line(t, -size / 2, traveller_y, size / 2, traveller_y)