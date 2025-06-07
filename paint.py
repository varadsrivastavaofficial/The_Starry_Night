# this program is made to be use3d in Stanford Code in Place IDE

from graphics import Canvas
import math
import random

# do not change these
CANVAS_WIDTH = 525
CANVAS_HEIGHT = 400

# background default


def bg(canvas):
    recangle = canvas.create_rectangle(
        0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "#3b74c5")

# blue dashed background


def bg1(canvas):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    while y1 < CANVAS_HEIGHT:
        x1 = 0
        while x1 < CANVAS_WIDTH:
            line = canvas.create_line(x1, y1, x1 + 5, y1, "#0a1c72")
            x1 += 7
        y1 += 4

# black dashed background


def bg2(canvas, y1, y2):
    if y2 <= CANVAS_HEIGHT:
        while y1 < y2:
            x1 = 0
            while x1 < CANVAS_WIDTH:
                line = canvas.create_line(x1, y1, x1 + 10, y1, "black")
                x1 += 7
            y1 += 4

# sky suns


def suns(canvas, x1, y1, size):
    copy = size
    colors1 = ['#9ebce5', '#d4d98c', '#c2d1b8']
    colors2 = ['#af8f4b', '#b6b53d']
    while size > 0:
        oval = canvas.create_oval(
            x1, y1, x1+size, y1+size, random.choice(colors1), random.choice(colors1))
        size -= 5
    oval2 = canvas.create_oval(x1+copy*0.25, y1+copy*0.25, x1+copy*0.75,
                               y1+copy*0.75, random.choice(colors2), random.choice(colors2))

# full sky


def sky(canvas):
    suns(canvas, 20, 0, 50)  # 1
    suns(canvas, 90, 3, 25)  # 2
    suns(canvas, 140, 1, 35)  # 3
    suns(canvas, 185, 20, 25)  # 4
    suns(canvas, 270, 25, 55)  # 5
    suns(canvas, 390, 20, 120)  # 6
    suns(canvas, 335, 100, 50)  # 7
    suns(canvas, 110, 55, 40)  # 8
    suns(canvas, 160, 130, 25)  # 9
    suns(canvas, 5, 160, 20)  # 10
    suns(canvas, 55, 165, 30)  # 11
    suns(canvas, 145, 195, 75)  # 12

# mountains parabola


def pb(canvas, x1, y1, color):
    a = 0.001  # positive → opens downward; increase to make it narrower
    while y1 < CANVAS_HEIGHT:
        for x in range(x1 - 150, x1 + 150):  # width of the curve
            dx = x - x1
            y_current = int(y1 + a * dx ** 2)
            dx_next = (x + 1) - x1
            y_next = int(y1 + a * dx_next ** 2)
            canvas.create_line(x, y_current, x + 1, y_next, "blue")
        y1 += 3

# full mountains


def mountains(canvas):
    colors1 = ['#3364b2', '#b3cfe4']
    colors2 = ['#182faa', '#1733ae']
    colors3 = ['#12245b', '#1d445b']
    colors4 = ['#1e3d85', '#172f45']

    pb(canvas, 20, 225, random.choice(colors1))  # white mountains
    pb(canvas, 185, 245, random.choice(colors1))
    pb(canvas, 297, 233, random.choice(colors1))
    pb(canvas, 450, 165, random.choice(colors1))

    pb(canvas, 465, 225, random.choice(colors4))  # black mountains

    pb(canvas, 55, 310, random.choice(colors2))  # blue mountains
    pb(canvas, 220, 290, random.choice(colors2))
    pb(canvas, 285, 265, random.choice(colors2))
    pb(canvas, 450, 260, random.choice(colors2))

    pb(canvas, -50, 310, random.choice(colors3))  # green mountains
    pb(canvas, 85, 315, random.choice(colors3))

# front tree


def tree(canvas, base_start_x, base_width, height):
    colors = ['#000000', '#02500f', '#0e3d16', '#073d10']
    base_end_x = base_start_x + base_width
    apex_x = base_start_x + base_width // 2
    apex_y = CANVAS_HEIGHT - height
    base_y = CANVAS_HEIGHT

    for x in range(base_start_x, base_end_x + 1):
        if x < apex_x:
            top_y = base_y - ((x - base_start_x) /
                              (apex_x - base_start_x)) * height
        else:
            top_y = base_y - ((base_end_x - x) /
                              (base_end_x - apex_x)) * height
        canvas.create_line(x, base_y, x, top_y, random.choice(colors))

# single house


def house(canvas, x, y, sizefactor):
    colors = ['#0b2131', '#0e2859', '#3f8181', '#3a7abd', '#000000']

    polygon = canvas.create_polygon(x*sizefactor, y*sizefactor, (x + 50)*sizefactor, y*sizefactor, (x + 50)*sizefactor, (y + 50)*sizefactor, (x - 25)*sizefactor, (y + 50)*sizefactor, (x - 25)*sizefactor, (y + 25)*sizefactor,
                                    color=random.choice(colors), outline=random.choice(colors))
    rectangle = canvas.create_rectangle(x+20, y+30, x+30, y+40, color="yellow")

# full village


def village(canvas):
    house(canvas, 220, 275, 1)
    house(canvas, 250, 325, 1)
    house(canvas, 300, 350, 1)
    house(canvas, 350, 365, 1)
    house(canvas, 310, 280, 1)
    house(canvas, 415, 300, 1)
    house(canvas, 470, 350, 1)

# single shrubs


def shrubs(canvas, x, y, size):
    colors = ['#000000', '#02500f', '#0e3d16', '#073d10']
    circle = canvas.create_oval(
        x, y, x+size, y+size, random.choice(colors), random.choice(colors))

# full bushes


def bushes(canvas):
    shrubs(canvas, -25, CANVAS_HEIGHT-40, 70)
    shrubs(canvas, 25, CANVAS_HEIGHT-60, 45)
    shrubs(canvas, 50, CANVAS_HEIGHT-25, 45)
    shrubs(canvas, 60, CANVAS_HEIGHT-60, 50)
    shrubs(canvas, 75, CANVAS_HEIGHT-40, 45)

# all trees


def trees(canvas):
    tree(canvas, 55, 80, 275)
    tree(canvas, 80, 70, 375)
    tree(canvas, 110, 90, 140)
    tree(canvas, 150, 70, 80)


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    bg(canvas)
    # bg1(canvas)
    # bg2(canvas,0,20)
    # bg2(canvas,300,400
    sky(canvas)
    # mountains(canvas)
    village(canvas)
    bushes(canvas)
    trees(canvas)


if __name__ == '__main__':
    main()
