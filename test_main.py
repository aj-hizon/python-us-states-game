import pandas as pd
from turtle import Turtle, Screen

turtle = Turtle()
MAP_IMAGE = r"python\us-states-game\us-states-game-start\blank_states_img.gif"

us_states = []
states = 0


data = pd.read_csv(r"python\us-states-game\us-states-game-start\50_states.csv")
states_list = data["state"].to_list()
x_coordinates = data["x"].to_list()
y_coordinates = data["y"].to_list()
x_y_coordinates = list(zip(x_coordinates, y_coordinates))





print(x_y_coordinates[0])





screen = Screen()
screen.setup(width = 745, height = 500)
screen.title("U.S States Game")
screen.addshape(MAP_IMAGE)
turtle.shape(MAP_IMAGE)


while states != 50:
    answer_state = screen.textinput(title = f"{states}/50 Guessed states", prompt = "What's another state's name?").title()

    for i in range(0, len(states_list)):
        listing = states_list[i]
        if answer_state == listing:
            states += 1 
            us_states += listing
            timmy = Turtle()
            index_of_state = states_list.index(f"{listing}")
            coordinates = x_y_coordinates[index_of_state]
            timmy.penup()
            timmy.goto(coordinates)
            timmy.write(arg = f"{listing}", align = "center", font = ["Arial", 10, "bold"])
        

screen.mainloop()

            
            