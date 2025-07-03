import sqlite3
from tkinter import *

# conn = sqlite3.connect("player_data.db")

# c = conn.cursor()

# c.execute("SELECT rowid, * FROM players")
# print(c.fetchall())

root = Tk()
root.geometry("400x400")

# user_name = "George"

# opening_message = (f"""
# Welcome {user_name}
# Let's quickly go over the rules of the game.
# A country will be randomly selected, and you will have to guess which country it is.
# With the help of hints, you'll be able to narrow down the possibilities.
# If you're a beginner, start with EASY mode, where the hints are plenty, and the guesses are endless.
# If you're a bit more confident, play INTERMEDIATE.  Here you'll be given plenty of hints, but the guesses are limited to 10, so choose wisely.
# If you think you're a pro, play HARD. It'll be the same format, but hints will limited and obscure, while guesses will be capped at 5.
# OR, if you're 'FEELING LUCKY', try and guess the Country in one, with no hint(s).
# Press Enter when you're ready(Or 'Quit' if you're not ready). Best of luck!.
# """)

# label = Label(root, text=opening_message)
# label.pack()

# def text_colour_change(event):
#     current_text=player_name.get()
#     if current_text.lower():
#         player_name.config(fg="black")
#     else:
#         player_name.config(fg="grey")

# def myClick():
#     if player_name.get():
#         myButton["state"] = DISABLED
#     else:
#         myButton["state"] = ACTIVE

#     # Print 'hello' with player name
#     hello = "Let's Begin "+ player_name.get() + "!"
#     myLabel = Label(root, text=hello)
#     myLabel.grid(row=1, column=0)

# # Output text box for player name
# player_name = Entry(root, width=50, fg="grey")
# player_name.grid(row=0, column=0, padx=5, pady=5)
# text = Text(root)
# player_name.insert(0, "Enter Your Name...")

# # Button inserted/displayed 
# myButton = Button(root, text="Press To Start", padx=50, pady=10, command=myClick)
# myButton.grid(row=2, column=0)

# # if "Enter Your Name..." not in player_name.get():
# #     myButton["state"] = ACTIVE
# # elif "Enter Your Name..." in player_name.get():
# #     myButton["state"] = DISABLED

# player_name.bind("<KeyRelease>", text_colour_change)

# Option list options
options = ["Settings/Difficulty", "Exit"]

# Define variable (Tkinter type variable)
clicked = StringVar(root)

# Set default value for variable
clicked.set("Options")

# Create/Define and display dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.config(indicatoron=0)
drop.pack()

root.mainloop()

