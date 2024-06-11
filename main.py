import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Sates Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    
    if answer_state == "Exit":
        missing_state =[state for state in all_states if state not in guess_states]
        # for state in all_states:
        #     if state not in guess_states:
        #         missing_state.append(state)
        new_csv = pandas.DataFrame(missing_state)
        new_csv.to_csv("missing_state.csv")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup() 
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



