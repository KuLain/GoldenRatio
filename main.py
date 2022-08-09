from golden_rectangle import draw_golden_rectangle
import turtle

pen = turtle.Turtle(visible=False)
draw_golden_rectangle(pen, 300, 10)

turtle.Screen().exitonclick()
