import tkinter

root = tkinter.Tk()
root.title("Shae's a bitch")

expression = ""

# functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "You fucked up"
            expression = ""
    label_result.config(text=result)
    expression = str(result)

def key_handler(event):
    global expression
    if event.keysym in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        add(event.keysym)
    elif event.keysym == "plus":
        add("+")
    elif event.keysym == "minus":
        add("-")
    elif event.keysym == "asterisk":
        add("*")
    elif event.keysym == "slash":
        add("/")
    elif event.keysym in ("c", "C"):
        clear()
    elif event.keysym == "period":
        add(".")
    elif event.keysym in ("Return", "equal"):
        calculate()
    elif event.keysym == "BackSpace":
        expression = expression[0:len(expression)-1]
        label_result.config(text=expression)
        
    
root.bind("<Key>", key_handler)

#Frame
label_result = tkinter.Label(root, text="", width=16, height=1, background="spring green")
label_result.grid(row=0, column=0, columnspan=4)


pressme_1 = tkinter.Button(root, text="1", command=lambda: add("1"))
pressme_1.grid(row=1, column=0)

pressme_2 = tkinter.Button(root, text="2", command=lambda: add("2"))
pressme_2.grid(row=1, column=1)

pressme_3 = tkinter.Button(root, text="3", command=lambda: add("3"))
pressme_3.grid(row=1, column=2)

pressme_4 = tkinter.Button(root, text="4", command=lambda: add("4"))
pressme_4.grid(row=2, column=0)

pressme_5 = tkinter.Button(root, text="5", command=lambda: add("5"))
pressme_5.grid(row=2, column=1)

pressme_6 = tkinter.Button(root, text="6", command=lambda: add("6"))
pressme_6.grid(row=2, column=2)

pressme_multiply = tkinter.Button(root, text="*", command=lambda: add("*"))
pressme_multiply.grid(row=2, column=3)

pressme_7 = tkinter.Button(root, text="7", command=lambda: add("7"))
pressme_7.grid(row=3, column=0)

pressme_8 = tkinter.Button(root, text="8", command=lambda: add("8"))
pressme_8.grid(row=3, column=1)

pressme_9 = tkinter.Button(root, text="9", command=lambda: add("9"))
pressme_9.grid(row=3, column=2)

pressme_0 = tkinter.Button(root, text="0", command=lambda: add("0"))
pressme_0.grid(row=4, column=1)

pressme_clear = tkinter.Button(root, text="C", command=lambda: clear())
pressme_clear.grid(row=4, column=0)

pressme_divide = tkinter.Button(root, text="/", command=lambda: add("/"))
pressme_divide.grid(row=1, column=3)  

pressme_dot = tkinter.Button(root, text=".", command=lambda: add("."))
pressme_dot.grid(row=4, column=2)

pressme_add = tkinter.Button(root, text="+", command=lambda: add("+"))
pressme_add.grid(row=4, column=3)

pressme_equals = tkinter.Button(root, text="=", width=16, command=lambda: calculate())
pressme_equals.grid(row=5, column=0, columnspan=4)

pressme_subtract = tkinter.Button(root, text="-", command=lambda: add("-"))
pressme_subtract.grid(row=3, column=3)

root.mainloop()
