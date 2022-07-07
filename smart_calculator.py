import math
from tkinter import *
import tkinter as tk
from pygame import mixer


mixer.init()


def mic_audio():
    print("Ok!")

def click(value):
    ent = char_entry.get()
    answer = ""
    try:
        if value=="C":
            ent = ent[0: len(ent)-1]
            char_entry.delete(0, END)
            char_entry.insert(0, ent)
            return

        elif value=="CE":
            char_entry.delete(0, END)

        elif value=="√":
            answer = math.sqrt(eval(ent))

        elif value== "π":
            answer = math.pi

        elif value== "cosθ":
            answer = math.cos(math.radians(eval(ent)))

        elif value== "tanθ":
            answer = math.tan(math.radians(eval(ent)))

        elif value == "sinθ":
            answer = math.sin(math.radians(eval(ent)))

        elif value == "2π":
            answer = 2 * math.pi

        elif value=="cosh":
            answer = math.cosh(eval(ent))

        elif value == "sinh":
            answer = math.sinh(eval(ent))

        elif value=="tanh":
            answer = math.tanh(eval(ent))

        elif value== chr(8731):
            answer = eval(ent)**(1/3)

        elif value== "x\u02b8":
            char_entry.insert(END, "**")
            return

        elif value== "x\u00B3":
            answer = eval(ent)**3

        elif value== "x\u00B2":
            answer = eval(ent)**2

        elif value== "ln":
            answer = math.log2(eval(ent))

        elif value== "deg":
            answer = math.degrees(eval(ent))

        elif value== "rad":
            answer = math.radians(eval(ent))

        elif value== "e":
            answer = math.e

        elif value == "log₁₀":
            answer = math.log10(eval(ent))

        elif value == "x!":
            answer = math.factorial(eval(ent))

        elif value == chr(247):
            char_entry.insert(END, "/")
            return

        elif value == "=":
            answer = eval(ent)

        else:
            char_entry.insert(END, value)
            return


        char_entry.delete(0, END)
        char_entry.insert(0, answer)

    except SyntaxError:
        pass

root = tk.Tk()
root.title("Smart Calculator")
root.iconbitmap('calculator-icon.ico')
root.config(bg='#54f542')
root.geometry('680x480')


micImage = PhotoImage(file='line_drawing_cal_image.png')
miclabel = Label(root, image=micImage, bg='#54f542', bd=0)
miclabel.grid(row=0, column=0)

char_entry = Entry(root, font=('arial', 20, 'bold'), bg='#54f542', fg='white', bd=10, relief= SUNKEN, width=33)
char_entry.grid(row=0, column=0, columnspan=9)

logoImage = PhotoImage(file='mic.png')
imagebutton = Button(root, image=logoImage, bg='#54f542', bd=0, command= mic_audio)
imagebutton.grid(row=0, column=7, pady=2)


button_texts = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                "0", ".", "%", "=", 'log₁₀', "(", ")", "x!"
                ]
rowval = 1
columnval = 0
for i in button_texts:

    button = Button(root, bg='#54f542', fg='white', bd=2, relief=SUNKEN,
                          font=('arial', 18, 'bold'), width=5, height=2,
                    text= i, activebackground='#54f542',
                    command= lambda button=i: click(button))
    button.grid(row=rowval, column=columnval)
    columnval+=1
    if columnval>7:
        rowval+=1
        columnval=0

root.mainloop()
