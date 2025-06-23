import tkinter as tk

root = tk.Tk()

# Creating a label widget
myLabel1 = tk.Label(root, text="Country Guessing Game")
myLabel2 = tk.Label(root, text="Welcome To The Country Guessing Game!")
# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

def myClick():
    myLabel = tk.Label(root, text="Let's Begin!")
    myLabel.grid(row=3, column=0)

myButton = tk.Button(root, text="Press To Start", padx=50, pady=10, command=myClick, fg="blue", bg="#000000")
myButton.grid(row=2, column=0)

root.mainloop()