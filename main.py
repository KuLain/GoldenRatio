from golden_rectangle import draw_golden_rectangle
import turtle

from golden_spiral import draw_golden_spiral

pen = turtle.Turtle(visible=False)

current_base_height = 600
nb_iteration = 15

pen.speed(150)

draw_golden_rectangle(pen, current_base_height, nb_iteration)

pen.speed(10)

draw_golden_spiral(pen, current_base_height, nb_iteration)

turtle.Screen().exitonclick()
