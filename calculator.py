from tkinter import *

def button(num):
    global entry
    entry = entry + str(num)
    equation_display.set(entry)

def equal():
    global entry
    try:
        answer = str(eval(entry))
        entry = answer
        equation_display.set(answer)
    except SyntaxError:
        equation_display.set("Syntax Error!")
        entry = ""
    except ZeroDivisionError:
        equation_display.set("Error! Cannot divided by zero!")
        entry = ""

def clearAll():
    global entry
    entry = ""
    equation_display.set("")

#window part
window = Tk()
window.title("My First Calculator")
window.geometry("600x600")
equation_display = StringVar()
entry = ""
label = Label(window, textvariable=equation_display, font=("Arial", 16, "bold"), bg="lightblue", width="30", height="2")
label.pack(pady=20)

#buttons
frame = Frame(window)
frame.pack()

button1 = Button(frame, text = 1, height = 3, width = 7, font = 30, command= lambda: button(1))
button1.grid(row=2, column=0)

button2 = Button(frame, text = 2, height = 3, width = 7, font = 30, command= lambda: button(2))
button2.grid(row=2, column=1)

button3 = Button(frame, text = 3, height = 3, width = 7, font = 30, command= lambda: button(3))
button3.grid(row=2, column=2)

button4 = Button(frame, text = 4, height = 3, width = 7, font = 30, command= lambda: button(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text = 5, height = 3, width = 7, font = 30, command= lambda: button(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text = 6, height = 3, width = 7, font = 30, command= lambda: button(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text = 7, height = 3, width = 7, font = 30, command= lambda: button(7))
button7.grid(row=0, column=0)

button8 = Button(frame, text = 8, height = 3, width = 7, font = 30, command= lambda: button(8))
button8.grid(row=0, column=1)

button9 = Button(frame, text = 9, height = 3, width = 7, font = 30, command= lambda: button(9))
button9.grid(row=0, column=2)

button0 = Button(frame, text = 0, height = 3, width = 7, font = 30, command= lambda: button(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=3, width=7, font=30, command=lambda: button('+'))
plus.grid(row=0, column=3)

minus = Button(frame,text='-', height=3, width=7, font=30, command=lambda: button('-'))
minus.grid(row=1, column=3)

multiply = Button(frame,text='*', height=3, width=7, font=30, command=lambda: button('*'))
multiply.grid(row=2, column=3)

divide = Button(frame,text='/', height=3, width=7, font=30, command=lambda: button('/'))
divide.grid(row=3, column=3)

dot = Button(frame,text='.', height=3, width=7, font=30, command=lambda: button('.'))
dot.grid(row=3, column=1)

equal =  Button(frame,text='=', height=3, width=7, font=30, command=equal)
equal.grid(row=3, column=2)

clearButton = Button(window,text='Clear', height=3, width=31, font=40, command=clearAll)
clearButton.pack()


window.mainloop()