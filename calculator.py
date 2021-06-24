import Tkinter as tk
top = tk.Tk()
top.columnconfigure(0, weight=1, minsize=75)
top.rowconfigure(0, weight=1, minsize=50)
frame = tk.Frame(master=top, width=150, height=150, bg="gray")
frame.pack()
frame.columnconfigure(0, weight=1, minsize=75)
frame.rowconfigure(0, weight=1, minsize=50)
title = tk.Label(master=frame,
    text="Basic Calculator", 
    fg="white", background="purple",
    width="15",
    height="1",)
entry = tk.Entry(master=frame)
title.pack()
entry.pack()
entry.insert(0, "clicked button")
btn_frame = tk.Frame(
    master=frame, width=150, bg="gray", borderwidth=1, relief=tk.RIDGE)
# name = entry.get()
# for i in range(1, 10):
btn_frame.pack()
count = 1
for row in range(0,3):
    # top.columnconfigure(row, weight=1, minsize=75)
    # top.rowconfigure(row, weight=1, minsize=50)
    for col in range(0,3):
        button = tk.Button(
            
            master=btn_frame,
        text=count,
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
        button.grid(padx=5, pady=5, row=row, column=col)
        count += 1
button = tk.Button(
    
            master=btn_frame,
        text="0",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button.grid(padx=5, pady=5, row=3, column=0)
button = tk.Button(
    
            master=btn_frame,
        text=".",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button.grid(padx=5, pady=5, row=3, column=1)    
button = tk.Button(
    
            master=btn_frame,
        text="=",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button.grid(padx=5, pady=5, row=3, column=2)    
button = tk.Button(
    
            master=btn_frame,
        text="+",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button.grid(padx=5, pady=5, row=0, column=3)   
button = tk.Button(
    
            master=btn_frame,
        text="-",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button.grid(padx=5, pady=5, row=1, column=3)    
button = tk.Button(
    
            master=btn_frame,
        text="x",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button.grid(padx=5, pady=5, row=2, column=3) 
button = tk.Button(
    
            master=btn_frame,
        text="/",
        width=3,
        height=1,
        bg="black",
        fg="yellow",
        )
button.grid(padx=5, pady=5, row=3, column=3)       

top.mainloop()