import Tkinter as tk
top = tk.Tk()
top.title('Basic Calculator')
top.configure(background='#555555')

entry = tk.Entry(top, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

first_number = None
second_number = None
comp_result = None
current_function = None
pending_function = None
is_compute = False
open_equation = False

def button_click(number):
    global is_compute
    global open_equation
    if is_compute:
        entry.delete(0, tk.END)
        is_compute = False
    entry.insert(tk.END, number)
    open_equation = False


def get_result():
    global first_number
    global second_number
    global comp_result
    global current_function
    global is_compute
    global open_equation
    if open_equation == False:
        pending_function()
        if comp_result.is_integer():
                entry.insert(0,int(comp_result))
        else:
                entry.insert(0, comp_result)
        first_number = None
        second_number = None
        comp_result = None
        is_compute = True

def clear_result():
    global first_number
    global second_number
    global comp_result
    content = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,content[:-1])

def reset_all():
    global first_number
    global second_number
    global comp_result
    global is_compute
    global current_function
    global pending_function
    global open_equation
    entry.delete(0,tk.END)
    first_number = None
    second_number = None
    comp_result = None
    is_compute = False
    current_function = None
    pending_function = None
    open_equation = False

def run_calc(the_function):
    global current_function
    global pending_function
    global open_equation
    open_equation = True
    if current_function ==None:
        current_function = the_function
    elif pending_function == None:
        pending_function = the_function
    else:
        current_function = pending_function
        pending_function = the_function
    current_function()


def add_nums():
    global first_number
    global second_number
    global comp_result
    if first_number==None:
        first_number = float(entry.get())
        entry.delete(0,tk.END)
    elif second_number==None:
        second_number = float(entry.get())
        the_sum = first_number + second_number
        entry.delete(0,tk.END)
        comp_result = the_sum
        first_number = the_sum
        second_number = None


def subtract_nums():
    global first_number
    global second_number
    global comp_result
    global current_function
    current_function = subtract_nums
    if first_number==None:
        first_number = float(entry.get())
        entry.delete(0,tk.END)
    elif second_number==None:
        second_number = float(entry.get())
        the_sum = first_number - second_number
        entry.delete(0,tk.END)
        comp_result = the_sum
        first_number = the_sum
        second_number = None  

def mult_nums():
    global first_number
    global second_number
    global comp_result
    global current_function
    current_function = mult_nums
    if first_number==None:
        first_number = float(entry.get())
        entry.delete(0,tk.END)
    elif second_number==None:
        second_number = float(entry.get())
        the_sum = first_number * second_number
        entry.delete(0,tk.END)
        comp_result = the_sum
        first_number = the_sum
        second_number = None  

def div_nums():
    global first_number
    global second_number
    global comp_result
    global current_function
    current_function = div_nums
    if first_number==None:
        first_number = float(entry.get())
        entry.delete(0,tk.END)
    elif second_number==None:
        second_number = float(entry.get())
        the_sum = first_number / second_number
        entry.delete(0,tk.END)
        comp_result = the_sum
        first_number = the_sum
        second_number = None  

button_1 = tk.Button(
        top,
        command=lambda:button_click(1),
        text="1",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_1.grid(padx=5, pady=5, row=2, column=0)
button_2 = tk.Button(
        top,
        command=lambda:button_click(2),
        text="2",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_2.grid(padx=5, pady=5, row=2, column=1)
button_3 = tk.Button(
        top,
        command=lambda:button_click(3),
        text="3",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_3.grid(padx=5, pady=5, row=2, column=2)
button_4 = tk.Button(
        top,
        command=lambda:button_click(4),
        text="4",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_4.grid(padx=5, pady=5, row=3, column=0)
button_5 = tk.Button(
        top,
        command=lambda:button_click(5),
        text="5",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_5.grid(padx=5, pady=5, row=3, column=1)
button_6 = tk.Button(
        top,
        command=lambda:button_click(6),
        text="6",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_6.grid(padx=5, pady=5, row=3, column=2)
button_7 = tk.Button(
        top,
        command=lambda:button_click(7),
        text="7",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_7.grid(padx=5, pady=5, row=4, column=0)
button_8 = tk.Button(
        top,
        command=lambda:button_click(8),
        text="8",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_8.grid(padx=5, pady=5, row=4, column=1)
button_9 = tk.Button(
        top,
        command=lambda:button_click(9),
        text="9",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_9.grid(padx=5, pady=5, row=4, column=2)

button_0 = tk.Button(
        top,
        command=lambda:button_click(0),
        text="0",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_0.grid(padx=5, pady=5, row=5, column=0)
button_dot = tk.Button(
        top,
        command=lambda:button_click('.'),
        text=".",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_dot.grid(padx=5, pady=5, row=5, column=1)    
button_equal = tk.Button(
        top,
        command=lambda:get_result(),
        text="=",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_equal.grid(padx=5, pady=5, row=5, column=2)
button_reset = tk.Button(
        top,
        command=lambda:reset_all(),
        text="Reset",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_reset.grid(padx=5, pady=5, row=1, column=0)    

button_clear = tk.Button(
        top,
        command=lambda:clear_result(),
        text="Clear",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_clear.grid(padx=5, pady=5, row=1, column=3)    
button_add = tk.Button(
        top,
        command=lambda:run_calc(add_nums),
        text="+",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_add.grid(padx=5, pady=5, row=2, column=3)   
button_sub = tk.Button(
top,
command=lambda: run_calc(subtract_nums),
        text="-",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_sub.grid(padx=5, pady=5, row=3, column=3)    
button_mult = tk.Button(
top,
command=lambda: run_calc(mult_nums),
        text="x",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_mult.grid(padx=5, pady=5, row=4, column=3) 
button_div = tk.Button(
top,
command=lambda: run_calc(div_nums),
        text="/",
        width=3,
        height=1,
        bg="black",
        fg="white",
        )
button_div.grid(padx=5, pady=5, row=5, column=3)       

top.mainloop()