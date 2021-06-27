import Tkinter as tk
top = tk.Tk()
top.title('Basic Calculator')
# top.columnconfigure(0, weight=1, minsize=75)
# top.rowconfigure(0, weight=1, minsize=50)
# frame = tk.Frame(master=top, width=150, height=150, bg="gray")
# frame.pack()
# frame.columnconfigure(0, weight=1, minsize=75)
# frame.rowconfigure(0, weight=1, minsize=50)
# title = tk.Label(master=frame,
#     text="Basic Calculator", 
#     fg="white", background="purple",
#     width="15",
#     height="1",)
entry = tk.Entry(top, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    entry.insert(tk.END, number)

first_number = None
second_number = None
comp_result = None

def get_result():
    entry.insert(0,comp_result)

def clear_result():
    content = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,content[:-1])

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
        entry.insert(0, the_sum)
        comp_result = the_sum
        first_number = None
        second_number = None    
    # print(first_number)
    # print(second_number)

button_1 = tk.Button(
        top,
        command=lambda:button_click(1),
        text="1",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_1.grid(padx=5, pady=5, row=1, column=0)
button_2 = tk.Button(
        top,
        command=lambda:button_click(2),
        text="2",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_2.grid(padx=5, pady=5, row=1, column=1)
button_3 = tk.Button(
        top,
        command=lambda:button_click(3),
        text="3",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_3.grid(padx=5, pady=5, row=1, column=2)
button_4 = tk.Button(
        top,
        command=lambda:button_click(4),
        text="4",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_4.grid(padx=5, pady=5, row=2, column=0)
button_5 = tk.Button(
        top,
        command=lambda:button_click(5),
        text="5",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_5.grid(padx=5, pady=5, row=2, column=1)
button_6 = tk.Button(
        top,
        command=lambda:button_click(6),
        text="6",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_6.grid(padx=5, pady=5, row=2, column=2)
button_7 = tk.Button(
        top,
        command=lambda:button_click(7),
        text="7",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_7.grid(padx=5, pady=5, row=3, column=0)
button_8 = tk.Button(
        top,
        command=lambda:button_click(8),
        text="8",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_8.grid(padx=5, pady=5, row=3, column=1)
button_9 = tk.Button(
        top,
        command=lambda:button_click(9),
        text="9",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_9.grid(padx=5, pady=5, row=3, column=2)

button_0 = tk.Button(
        top,
        command=lambda:button_click(0),
        text="0",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_0.grid(padx=5, pady=5, row=4, column=0)
button_dot = tk.Button(
        top,
        command=lambda:button_click('.'),
        text=".",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_dot.grid(padx=5, pady=5, row=4, column=1)    
button_equal = tk.Button(
        top,
        command=lambda:get_result(),
        text="=",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_equal.grid(padx=5, pady=5, row=4, column=2)
button_clear = tk.Button(
        top,
        command=lambda:clear_result(),
        text="Clear",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_clear.grid(padx=5, pady=5, row=0, column=3)    
button_add = tk.Button(
        top,
        command=lambda:add_nums(),
        text="+",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_add.grid(padx=5, pady=5, row=1, column=3)   
button_sub = tk.Button(
top,
        text="-",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_sub.grid(padx=5, pady=5, row=2, column=3)    
button_mult = tk.Button(
top,
        text="x",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_mult.grid(padx=5, pady=5, row=3, column=3) 
button_div = tk.Button(
top,
        text="/",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button_div.grid(padx=5, pady=5, row=4, column=3)       

top.mainloop()