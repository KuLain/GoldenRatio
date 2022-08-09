from turtle import Turtle
from math import sqrt

PHI = (1 + sqrt(5)) / 2


def draw_golden_rectangle(pen: Turtle, base_rectangle_height: float, n: int = 1) -> None:
    pen.up()
    pen.setposition(-(base_rectangle_height * PHI) / 2, base_rectangle_height / 2)
    draw_golden_rectangle_recursive(pen, base_rectangle_height, n)


def draw_golden_rectangle_recursive(pen: Turtle, base_rectangle_height: float, n: int = 1) -> None:
    if n > 0:
        print(f"------------------------Itération n°{n}------------------------")
        new_rectangle_height = base_rectangle_height / PHI
        pen.down()
        draw_rectangle(pen, base_rectangle_height, base_rectangle_height * PHI)
        pen.up()
        pen.forward(base_rectangle_height * PHI)
        pen.right(90)
        draw_golden_rectangle_recursive(pen, new_rectangle_height, n - 1)


def draw_rectangle(pen: Turtle, height: float, width: float) -> None:
    for _ in range(2):
        pen.forward(width)
        print(f"Going forward of {width} for width")
        pen.right(90)
        pen.forward(height)
        print(f"Going forward of {height} for height")
        pen.right(90)
