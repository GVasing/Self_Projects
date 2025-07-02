# Import modules
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3

# Define database for user accounts/info
conn = sqlite3.connect("player_data.db")

# Create/Define cursor
c = conn.cursor()

# Create table for data in database
c.execute(""" CREATE TABLE players (
          user_id serial PRIMARY KEY,
          user_name text NOT NULL
          )
""")

# Commit changes
conn.commit()

# Close connection
conn.close()

# Create variable for reference convenience
root = tk.Tk()

# Window Title
root.title("Country Guessing Game")

# Creating a label widget
myLabel1 = tk.Label(root, text="Welcome To The Country Guessing Game!")

# Shoving it onto the screen
myLabel1.grid(row=0, column=0, pady=5)

# Output text box
e = tk.Entry(root, width=50)
e.grid(row=4, column=0, padx=5, pady=5)
e.insert(0, "Enter Your Name...")

# Function for Button created/defined
def myClick():
    hello = "Let's Begin "+ e.get() + "!"
    myLabel = tk.Label(root, text=hello)
    # if True:
    #     myLabel.destroy()
    myLabel.grid(row=3, column=0)

# Button inserted/displayed 
myButton = tk.Button(root, text="Press To Start", padx=50, pady=10, command=myClick)
myButton.grid(row=2, column=0)

# Background image created/defined
my_img = ImageTk.PhotoImage(Image.open("CartoonWorldMap.jpg"))
my_label = tk.Label(image=my_img)

# Background image displayed
my_label.grid(row=5, column=0)


# Run code/Open window
root.mainloop()