import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("Indian States Game")
image="Mapa-de-India-color-scaled-1024x1024.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('indian_states_29_xy_cartesian.csv')
states = data['state'].tolist()

t = turtle.Turtle()
t.penup()
t.hideturtle()
guessed_states = []
correct = 0

game_on = True
while game_on:
    answer_state = screen.textinput(f'Guess the state {correct}/29', "What's another state name ?").title()
    if correct == 29:
        t.write("Good job kid",align='center',font=("Arial", 8, "normal"))
        break

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        record = data[data['state'] == answer_state]

        x = int(record.x_cor)
        y = int(record.y_cor)

        t.goto(x,y)
        t.write(answer_state,align='center',font=("Arial", 8, "normal"))
        correct+=1










turtle.mainloop()