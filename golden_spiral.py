from turtle import Turtle
from math import sqrt
from enum import Enum

PHI = (1 + sqrt(5)) / 2


class Heading(Enum):
    """
    Enumeration used to choose the heading of the turtle
    """
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


def draw_golden_spiral(pen: Turtle, base_height: float, n: int) -> None:
    """
    Set up the turtle and draw the golden spiral
    :param pen: Turtle to use
    :param base_height: Height of the first rectangle
    :param n: Number of quarter of circle wanted
    :return: None : Draws the golden spiral
    """
    pen.up()
    pen.setposition(-(base_height * PHI) / 2, base_height / 2)
    pen.setheading(Heading.DOWN.value)
    pen.forward(base_height)
    pen.down()
    draw_quarter_circle_recursive(pen, base_height, n)


def draw_quarter_circle_recursive(pen: Turtle, base_height: float, n: int) -> None:
    """
    Draw a quarter of the golden spiral
    :param pen: Turtle
    :param base_height: Height of the first rectangle
    :param n: Current iteration
    :return: None: Draw a quarter of the golden spiral
    """
    if n > 0:
        print(f"------------------------Iteration n°{n}------------------------")
        new_base_height = base_height / PHI
        pen.circle(PHI * base_height - new_base_height, extent=-90)
        print(f"Drawing circle of radius {PHI * base_height - new_base_height} for rectangle with base height {base_height}")
        draw_quarter_circle_recursive(pen, new_base_height, n - 1)
