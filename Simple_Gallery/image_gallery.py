# Relevant Modules imported
from tkinter import *
from PIL import ImageTk, Image

# Create/Define window
root = Tk()

# Create/Define and display title
root.title("Learn To Code")

# Create/Define images
my_img1 = ImageTk.PhotoImage(Image.open("Wojak_cropped-8.png"))
my_img2 = ImageTk.PhotoImage(Image.open("CartoonWorldMap.png"))
my_img3 = ImageTk.PhotoImage(Image.open("contentwojak.jpg"))

# Create/Define list for images
image_list = [my_img1, my_img2, my_img3]

# Create/Define status bar
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

# Create/Define container for image
my_label = Label(image=my_img1)

# Display container with image in it
my_label.grid(row=0, column=0, columnspan=3)

# Create function for forward button
def forward(image_num):

    # Global Variable created to operate outside of funtion
    global my_label
    global back_button
    global forward_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num])
    forward_button = Button(root, text=">>", command= lambda: forward(image_num+1))
    back_button = Button(root, text="<<", command= lambda: backward(image_num-1))

    # Conditional statement to disable button at end
    if image_num == 2:
        forward_button = Button(root, text=">>", state=DISABLED)

    # Display image and buttons
    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)
    
    # Status Bar
    status = Label(root, text="Image " + str(image_num + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    # Display status bar
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Create function for back button
def backward(image_num):

    # Global Variable created to operate outside of funtion
    global my_label
    global back_button
    global forward_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num])
    forward_button = Button(root, text=">>", command= lambda: forward(image_num+1))
    back_button = Button(root, text="<<", command= lambda: backward(image_num-1))

    # Conditional statement to disable button at end
    if image_num == 0:
        back_button = Button(root, text="<<", state=DISABLED)
    
    # Display image and buttons
    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    # Status Bar
    status = Label(root, text="Image " + str(image_num + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    # Display status bar
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Create/Define directional buttons
back_button = Button(root, text='<<', command=lambda: backward(1), state=DISABLED)
exit_button = Button(root, text='Exit Program', command=root.quit)
forward_button = Button(root, text='>>', command=lambda: forward(1))

# Display directional buttons
back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2, pady=10)

# Display status bar
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Run code/Open window
root.mainloop()