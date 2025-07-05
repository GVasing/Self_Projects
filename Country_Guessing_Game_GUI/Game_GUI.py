# Import modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

# Create variable for reference convenience
root = Tk()

# Window Title
root.title("Country Guessing Game")

# Creating a label widget
welcome_title = Label(root, text="Welcome To The Country Guessing Game!")

# Positioning welcome onto the screen
welcome_title.grid(row=0, column=0, pady=5)

# Define database for user accounts/info
conn = sqlite3.connect("player_data.db")

# Create/Define cursor
c = conn.cursor()

# Create table for data in database
# c.execute(""" CREATE TABLE players (
#           user_name TEXT NOT NULL
#           )
# """)

# Commit changes
conn.commit()

# Close connection
conn.close()

# Entry textbox colour change function
def text_colour_change(event):
    current_text=player_name.get()
    if current_text.lower():
        player_name.config(fg="black")
    else:
        player_name.config(fg="grey")

def game_message():    

    # Define variable for opening message text
    opening_message = """Let's quickly go over the rules of the game.
A country will be randomly selected, and you will have to guess which country it is.
With the help of hints, you'll be able to narrow down the possibilities.
If you're a beginner, start with EASY mode, where the hints are plenty, and the guesses are endless.
If you're a bit more confident, play INTERMEDIATE.  Here you'll be given plenty of hints, but the guesses are limited to 10, so choose wisely.
If you think you're a pro, play HARD. It'll be the same format, but hints will limited and obscure, while guesses will be capped at 5.
OR, if you're 'FEELING LUCKY', try and guess the Country in one, with no hint(s).
""" 
    # Create/Define label for message
    opening_message_label = Label(root, text=opening_message)

    # Display label(message)
    opening_message_label.grid(row=4, column=0)


# Function for Player start button created/defined
def myClick():
    # Disable button once pressed
    if player_name.get():
        myButton["state"] = DISABLED
    else:
        myButton["state"] = ACTIVE

    # Print 'hello' with player name
    hello = "Let's Begin "+ player_name.get() + "!"
    myLabel = Label(root, text=hello)
    myLabel.grid(row=3, column=0)

    # Connect to database
    conn = sqlite3.connect("player_data.db")

    # Create/Define cursor
    c = conn.cursor()

    # Insert data into table
    c.execute("INSERT INTO players VALUES (:user_name)",
              {
                  "user_name" : player_name.get()
              })

    # Commit changes
    conn.commit()

     # Close connection
    conn.close()

    # Clear textbox
    player_name.delete(0, END)

    # Run opening message function
    game_message()

# New window for scores option function
def open_scores():
    scores_window = Toplevel()
    scores_window.title("Scores")
    scores_window.geometry("400x400")
    scores_label = Label(scores_window, text="Player Scores:").pack()
    back_button = Button(scores_window, text="Back to Main", command=scores_window.destroy).pack()

# Confirm button function
def confirm_difficulty():
    # message = "You have selected: " + # add difficulty.get() once defined.
    # difficulty_label = Label(settings_window, text=message).pack()
    pass

# New window for settings/difficulty option function
def open_settings():
    settings_window = Toplevel()
    settings_window.title("Settings")
    settings_window.geometry("400x400")
    settings_label = Label(settings_window, text="Choose a difficulty:").pack()
    save_button = Button(settings_window, text="Confirm").pack() # Add command=settings_window.confirm_difficulty once function is complete.
    back_button = Button(settings_window, text="Back to Main", command=settings_window.destroy).pack()


# Pop-up for close window confirmation
def exit_pop_up():
    response = messagebox.askquestion("", "Are you sure you want to exit?")

    if response == "yes":
        close_window()
    else:
        pass

# Close Window function
def close_window():
    root.destroy()

# Create/Define MenuButton
dropdown = Menubutton(root, text="Options", relief=RAISED)
dropdown.place(x=0, y=0)

# Create menu and associate to MenuButton
dropdown.menu = Menu(dropdown, tearoff=0)
dropdown["menu"] = dropdown.menu

# Add commands to menu
dropdown.menu.add_command(label="Exit", command=exit_pop_up)
dropdown.menu.add_command(label="Settings/Difficulty", command=open_settings)
dropdown.menu.add_command(label="Scores", command=open_scores)

# Output text box for player name
player_name = Entry(root, width=50, fg="grey")
player_name.grid(row=4, column=0, padx=5, pady=5)
player_name.insert(0, "Enter Your Name...")

# Button inserted/displayed 
myButton = Button(root, text="Press To Start", padx=50, pady=10, command=myClick)
myButton.grid(row=2, column=0)

# Background image created/defined
map = ImageTk.PhotoImage(Image.open("CartoonWorldMap.jpg"))
map_label = Label(image=map)

# Background image displayed
map_label.grid(row=5, column=0)

# Bind text colour change function
player_name.bind("<KeyRelease>", text_colour_change)

# Run code/Open window
root.mainloop()