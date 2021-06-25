from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Welcome to LearningWhilePracticing")
window.geometry("400x150")

lbl = Label(window, text="Hello World", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Please enter your name")
lbl2.grid(column=0, row=1)

txt = Entry(window, width=20)
txt.grid(column=1, row=1)

def GreetUser():
    userName = txt.get()
    messagebox.showinfo("LearingWhilePracticing", "Hello, " + userName)


btn = Button(window, text="Click Me",bg="yellow",fg="red",command=GreetUser)
btn.grid(column=2, row=1)


window.mainloop()

#evey line in here would be blocked
#until the window is closed