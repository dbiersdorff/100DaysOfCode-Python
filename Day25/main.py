from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(800, 600)
screen.bgpic("Day25\\blank_states_img.gif")

data = pandas.read_csv("Day25\\50_states.csv")
states_list = data.state.to_list()
x_list = data.x.to_list()
y_list = data.y.to_list()


guessed_states = []


while len(guessed_states) < 50:

    answer = screen.textinput(f"Score: {len(guessed_states)}", "Name of State").title()

    if answer in states_list:
        if answer not in guessed_states:

            index = states_list.index(answer)
            x = x_list[index]
            y = y_list[index]

            name_turtle = Turtle()
            name_turtle.penup()
            name_turtle.speed("fastest")
            name_turtle.hideturtle()
            name_turtle.goto(x, y)
            name_turtle.write(answer)
            guessed_states.append(answer)
            print(guessed_states)


screen.exitonclick()