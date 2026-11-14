#---Imports

import tkinter as Tk

#---Var Setup

calstring = []

#---define function

def add_1_string(x):
    global calstring
    calstring.append(x)
    print(calstring)
    display.config(text="".join(calstring))

def calculate():
    try:
        expression = "".join(calstring)
        result = eval(expression)
        display.config(text=result)
    except:
        display.config(text="Error")

def clear():
    global calstring
    calstring = []
    display.config(text="")

#---Setup Window

window = Tk.Tk()
window.geometry("500x600")
window.title("Ocysc")
window.columnconfigure((0,1,2,3), weight=1, uniform ='a')
window.rowconfigure((0,1,2,3,4), weight=1, uniform='a')

#---Numpad

#--Setup(subpart of numpad)

numpad_1 = Tk.Button(window, text="1", command= lambda: add_1_string("1"))  
numpad_2 = Tk.Button(window, text="2", command= lambda: add_1_string("2")) 
numpad_3 = Tk.Button(window, text="3", command= lambda: add_1_string("3")) 
numpad_4 = Tk.Button(window, text="4", command= lambda: add_1_string("4")) 
numpad_5 = Tk.Button(window, text="5", command= lambda: add_1_string("5")) 
numpad_6 = Tk.Button(window, text="6", command= lambda: add_1_string("6")) 
numpad_7 = Tk.Button(window, text="7", command= lambda: add_1_string("7")) 
numpad_8 = Tk.Button(window, text="8", command= lambda: add_1_string("8")) 
numpad_9 = Tk.Button(window, text="9", command= lambda: add_1_string("9")) 
numpad_0 = Tk.Button(window, text="0", command= lambda: add_1_string("0")) 

#--Placement(subpart of numpad)

numpad_1.grid(row=1, column=0, sticky= "nsew")
numpad_2.grid(row=1, column=1, sticky= "nsew")
numpad_3.grid(row=1, column=2, sticky= "nsew")
numpad_4.grid(row=2, column=0, sticky= "nsew")
numpad_5.grid(row=2, column=1, sticky= "nsew")
numpad_6.grid(row=2, column=2, sticky= "nsew")
numpad_7.grid(row=3, column=0, sticky= "nsew")
numpad_8.grid(row=3, column=1, sticky= "nsew")
numpad_9.grid(row=3, column=2, sticky= "nsew")
numpad_0.grid(row=4, column=1, sticky= "nsew")

#---Oprators

#--Setup(subpart of oprators)

oprator_add = Tk.Button(window, text="+", command= lambda: add_1_string("+"))
oprator_sub = Tk.Button(window, text="-", command= lambda: add_1_string("-"))
oprator_mul = Tk.Button(window, text="x", command= lambda: add_1_string("*"))
oprator_div = Tk.Button(window, text="/", command= lambda: add_1_string("/"))

#--Placement(subpart of oprators)

oprator_add.grid(row=1, column=3, sticky= "nsew")
oprator_sub.grid(row=2, column=3, sticky= "nsew")
oprator_mul.grid(row=3, column=3, sticky= "nsew")
oprator_div.grid(row=4, column=3, sticky= "nsew")

#---Display

display = Tk.Label(window, text="", font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, sticky="nsew")
equals = Tk.Button(window, text="=",
                   command=calculate)

#---Equal and Clear

equals.grid(row=4, column=2, sticky="nsew")
clear_button = Tk.Button(window, text="C",
                         command=clear)
 
clear_button.grid(row=4, column=0, sticky="nsew")

#---End

window.mainloop()
