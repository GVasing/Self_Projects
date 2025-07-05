import sqlite3
from tkinter import *

# # conn = sqlite3.connect("player_data.db")

# # c = conn.cursor()

# # c.execute("SELECT rowid, * FROM players")
# # print(c.fetchall())

root = Tk()
root.geometry("400x400")

# # user_name = "George"

# # opening_message = (f"""
# # Welcome {user_name}
# # Let's quickly go over the rules of the game.
# # A country will be randomly selected, and you will have to guess which country it is.
# # With the help of hints, you'll be able to narrow down the possibilities.
# # If you're a beginner, start with EASY mode, where the hints are plenty, and the guesses are endless.
# # If you're a bit more confident, play INTERMEDIATE.  Here you'll be given plenty of hints, but the guesses are limited to 10, so choose wisely.
# # If you think you're a pro, play HARD. It'll be the same format, but hints will limited and obscure, while guesses will be capped at 5.
# # OR, if you're 'FEELING LUCKY', try and guess the Country in one, with no hint(s).
# # Press Enter when you're ready(Or 'Quit' if you're not ready). Best of luck!.
# # """)

# # label = Label(root, text=opening_message)
# # label.pack()

# # def text_colour_change(event):
# #     current_text=player_name.get()
# #     if current_text.lower():
# #         player_name.config(fg="black")
# #     else:
# #         player_name.config(fg="grey")

# # def myClick():
# #     if player_name.get():
# #         myButton["state"] = DISABLED
# #     else:
# #         myButton["state"] = ACTIVE

# #     # Print 'hello' with player name
# #     hello = "Let's Begin "+ player_name.get() + "!"
# #     myLabel = Label(root, text=hello)
# #     myLabel.grid(row=1, column=0)

# # # Output text box for player name
# # player_name = Entry(root, width=50, fg="grey")
# # player_name.grid(row=0, column=0, padx=5, pady=5)
# # text = Text(root)
# # player_name.insert(0, "Enter Your Name...")

# # # Button inserted/displayed 
# # myButton = Button(root, text="Press To Start", padx=50, pady=10, command=myClick)
# # myButton.grid(row=2, column=0)

# # # if "Enter Your Name..." not in player_name.get():
# # #     myButton["state"] = ACTIVE
# # # elif "Enter Your Name..." in player_name.get():
# # #     myButton["state"] = DISABLED

# # player_name.bind("<KeyRelease>", text_colour_change)

# def exit():
#     root.destroy

# # Option list options
# # options = ["Settings/Difficulty", exit_button]

# # Define variable (Tkinter type variable)
# clicked = StringVar(root)

# # Set default value for variable
# clicked.set("Options")

# # Create/Define and display dropdown menu
# drop = OptionMenu(root, clicked, "Settings/Difficulty", "Exit")
# drop.config(indicatoron=0)
# drop.pack()

# Create/Define menu bar
menubar = Menu()

  
def close_window():
    root.destroy()

def open_scores():
    scores_window = Toplevel()
    scores_window.title("Scores")
    scores_window.geometry("400x400")
    scores_label = Label(scores_window, text="Player Scores:").pack()
    back_button = Button(scores_window, text="Back to Main", command=scores_window.destroy).pack()

def open_settings():
    settings_window = Toplevel()
    settings_window.title("Settings")
    settings_window.geometry("400x400")
    frame = LabelFrame(settings_window, padx=50, pady=50)
    frame.pack(padx=50, pady=50)
    settings_label = Label(frame, text="Choose a difficulty:")
    settings_label.grid(row=0, column=0)
    # settings_label.pack()
    save_button = Button(frame, text="Confirm") # Add command=settings_window.confirm_difficulty once function is complete.
    save_button.grid(row=5, column=0)
    # save_button.pack()
    back_button = Button(settings_window, text="Back to Main", command=settings_window.destroy).pack()

    # DIFFICULTY = [
    # ("Easy", "Easy"),
    # ("Intermediate", "Intermediate"),
    # ("Hard", "Hard"),
    # ("I'm Feeling Lucky", "I'm Feeling Lucky")
    # ]

    mode = StringVar()
    # mode.set("Choose a difficulty")

    # for text, level in DIFFICULTY:
    #     Radiobutton(frame, text=text, variable=mode, value=level).pack(anchor=W)

    easy_button = Radiobutton(frame, text="Easy", variable=mode, value=1)
    intermediate_button = Radiobutton(frame, text="Intermediate", variable=mode, value=2)
    hard_button = Radiobutton(frame, text="Hard", variable=mode, value=3)
    im_feeling_lucky_button = Radiobutton(frame, text="I'm Feeling Lucky", variable=mode, value=4)

    easy_button.grid(row=1, column=0, sticky="w")
    intermediate_button.grid(row=2, column=0, sticky="w")
    hard_button.grid(row=3, column=0, sticky="w")
    im_feeling_lucky_button.grid(row=4, column=0, sticky="w")



mb = Menubutton(root, text="Options", relief=RAISED)
mb.pack()

mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mb.menu.add_command(label="Exit", command=close_window)
mb.menu.add_command(label="Scores", command=open_scores)
mb.menu.add_command(label="Settings/Difficulty", command=open_settings)



root.mainloop()
