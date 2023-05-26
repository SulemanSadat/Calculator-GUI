import tkinter
from tkinter import *

calc = Tk()
calc.geometry('320x500')
calc.resizable(False, False)
calc.title("Calculator")


# ======================Start==========================
# ======================Functions======================


def button1():
    num1.insert(END, 1)


print("Calculator Started!")


def button2():
    num1.insert(END, 2)


def button3():
    num1.insert(END, 3)


def button4():
    num1.insert(END, 4)


def button5():
    num1.insert(END, 5)


def button6():
    num1.insert(END, 6)


def button7():
    num1.insert(END, 7)


def button8():
    num1.insert(END, 8)


def button9():
    num1.insert(END, 9)


def button0():
    num1.insert(END, 0)


def adds():
    add.delete(0, END)
    add.insert(END, '+')


def mines():
    add.delete(0, END)
    add.insert(END, '-')


def multiple():
    add.delete(0, END)
    add.insert(END, '*')


def divide():
    add.delete(0, END)
    add.insert(END, '/')
def percentage():
    add.delete(0, END)
    add.insert(END, '%')


def input1():
    num1.insert(input())
    num2.insert(input())


def delete():
    try:
        num1.delete(0, END)
        num2.delete(0, END)
        add.delete(0, END)
        result.delete(0, END)
    except:
        print("Deleted")


def equals():
    result.delete(0, END)
    a = num1.get()
    b = num2.get()
    if add.get() == '+':
        c = int(a) + int(b)
        result.insert(END, c)
    elif add.get() == '-':
        c = int(a) - int(b)
        result.insert(END, c)
    elif add.get() == '*':
        c = int(a) * int(b)
        result.insert(END, c)
    elif add.get() == '/':
        c = int(a) / int(b)
        result.insert(END, c)
    if add.get() == '%':
        c = int(a) * int(b) //100
        result.insert(END, c)


calc.config(bg="white")
F1 = Frame(calc, width=350, height=50)
F1.pack()
F1.config(bg="white")

name = Label(F1, text="SULEMAN SADAT", font="Calibri 12 bold")
Python = Label(F1, text="Python Programmer", font="Calibri 12 bold")
name.config(bg="white")
Python.config(bg="white")

# ---------------------inputs--------------------------
number1Label = Label(text="Number 1: ", bg="white")
title_text = IntVar
num1 = Entry(calc, textvariable=title_text, width=45)
num1.pack()
number2Label = Label(text="Number 2: ", bg="white")
num2 = Entry(calc, width=45)
num2.pack()

resultLabel = Label(text="  Result  ", bg="red")
result = Entry(calc, width=20)
result.pack()

add = Entry(calc, width=2)
add.pack()
sulemanjan = Label(text="", bg="white")

# Img1 = PhotoImage(file="suliman.png")
# now = Label(calc, image=Img1, bg="white", ).place(x=110, y=150)

# ---------------------Buttons--------------------------
one = Button(calc, text="1", width=9, height=3, command=lambda: button1())
two = Button(calc, text="2", width=9, height=3, command=button2)
three = Button(calc, text="3", width=9, height=3, command=button3)
four = Button(calc, text="4", width=9, height=3, command=button4)
five = Button(calc, text="5", width=9, height=3, command=button5)
six = Button(calc, text="6", width=9, height=3, command=button6)
seven = Button(calc, text="7", width=9, height=3, command=button7)
eight = Button(calc, text="8", width=9, height=3, command=button8)
nine = Button(calc, text="9", width=9, height=3, command=button9)
zero = Button(calc, text="0", width=9, height=3, command=button0)
point = Button(calc, text=".", width=9, height=3)
plusmines = Button(calc, text="+_", width=9, height=3)
average = Button(calc, text="%", width=9, height=3,command=percentage)
backspace = Button(calc, text="backspace", width=9, height=3)
C = Button(calc, text="C", width=9, height=3, command=delete)

plus = Button(calc, text="+", width=13, height=3, command=adds)
mines = Button(calc, text="_", width=13, height=3, command=mines)
multi = Button(calc, text="X", width=13, height=3, command=multiple)
divide = Button(calc, text="/", width=13, height=3, command=divide)


equal = Button(calc, text="=", width=13, height=3, command=lambda: equals())
equal.config(bg="#EEE", activebackground="GRAY")
equal.pack()

# ---------------------location--------------------------

one.place(y=392, x=0)
two.place(y=392, x=75)
three.place(y=392, x=150)
four.place(y=342, x=0)
five.place(y=342, x=75)
six.place(y=342, x=150)
seven.place(y=292, x=0)
eight.place(y=292, x=75)
nine.place(y=292, x=150)
zero.place(y=450, x=75)
plusmines.place(y=450, x=0)
zero.place(y=450, x=75)

equal.place(y=450, x=224)
point.place(y=450, x=150)

plus.place(y=392, x=224)
mines.place(y=342, x=224)
multi.place(y=292, x=224)
divide.place(y=235, x=224)
average.place(y=235, x=0)
backspace.place(y=235, x=150)
C.place(y=235, x=75)

add.place(y=95, x=156)
number1Label.place(x=0, y=50)
number2Label.place(x=0, y=80)

num1.place(y=50, x=67)
num2.place(y=80, x=67)

resultLabel.place(x=140, y=115)

result.place(x=105, y=135)
sulemanjan.place(x=150, y=180)
F1.place()
name.place(x=100, y=0)
Python.place(x=90, y=20)
calc.mainloop()