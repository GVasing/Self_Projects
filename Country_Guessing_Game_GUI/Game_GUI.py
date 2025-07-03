# Import modules
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# Create variable for reference convenience
root = Tk()

# Window Title
root.title("Country Guessing Game")

# Creating a label widget
myLabel1 = Label(root, text="Welcome To The Country Guessing Game!")

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

# Function for Button created/defined
def myClick():
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

# Positioning onto the screen
myLabel1.grid(row=0, column=0, pady=5)

# Output text box for player name
player_name = Entry(root, width=50)
player_name.grid(row=4, column=0, padx=5, pady=5)
player_name.insert(0, "Enter Your Name...")

# Button inserted/displayed 
myButton = Button(root, text="Press To Start", padx=50, pady=10, command=myClick)
myButton.grid(row=2, column=0)

# Background image created/defined
my_img = ImageTk.PhotoImage(Image.open("CartoonWorldMap.jpg"))
my_label = Label(image=my_img)

# Background image displayed
my_label.grid(row=5, column=0)

# Run code/Open window
root.mainloop()