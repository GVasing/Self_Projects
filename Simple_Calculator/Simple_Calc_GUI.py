# Import module
import tkinter as tk

# Create variable for reference convenience
root = tk.Tk()

# Window Title
root.title("Simple Calculator")

# Total Output Box
e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Function to calculate
def button_calc(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))  

def button_clear():
    e.delete(0, tk.END)

def button_plus():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, tk.END)

def button_sub():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, tk.END)

def button_times():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, tk.END)

def button_divi():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, tk.END)

def button_total():
    second_num = e.get()
    e.delete(0, tk.END)
    if math == "addition":
        e.insert(0, f_num + int(second_num))
    if math == "subtraction":
        e.insert(0, f_num - int(second_num))
    if math == "multiplication":
        e.insert(0, f_num * int(second_num))
    if math == "division":
        e.insert(0, f_num / int(second_num)) 

# Buttons defined/created
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_calc(1))
button_2 = tk.Button(root, text="2", padx=42, pady=20, command=lambda: button_calc(2))
button_3 = tk.Button(root, text="3", padx=42, pady=20, command=lambda: button_calc(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_calc(4))
button_5 = tk.Button(root, text="5", padx=42, pady=20, command=lambda: button_calc(5))
button_6 = tk.Button(root, text="6", padx=42, pady=20, command=lambda: button_calc(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_calc(7))
button_8 = tk.Button(root, text="8", padx=42, pady=20, command=lambda: button_calc(8))
button_9 = tk.Button(root, text="9", padx=42, pady=20, command=lambda: button_calc(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_calc(0))

# Non-numeric buttons define/created
button_add = tk.Button(root, text="+", padx=39, pady=20, command= button_plus)
button_subtract = tk.Button(root, text="-", padx=39, pady=20, command= button_sub)
button_multiply = tk.Button(root, text="x", padx=42, pady=20, command= button_times)
button_divide = tk.Button(root, text="÷", padx=42, pady=20, command= button_divi)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_total)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command= button_clear)

# Buttons inserted onto screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)

# Run code/Open window
root.mainloop()