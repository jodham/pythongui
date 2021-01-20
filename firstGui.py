from tkinter import *
import tkinter.messagebox as mb

window = Tk()
window.title("login")
window.geometry("300x300")
label1 = Label(window, text="Welcome", font="times 15 bold")
label1.place(x=60, y=20)
label2 = Label(window, text="Username", font="times 10 bold")
label2.place(x=40, y=60)
user_ent = Entry(window)
user_ent.place(x=40,y=80)
label3 = Label(window, text="Password", font="times 10 bold")
label3.place(x=40, y=110)
pass_ent = Entry(window, show='*')
pass_ent.place(x=40, y=130)


def login():
    username = user_ent.get()
    password = pass_ent.get()
    if username == "jodham" and password == "1234":
        mb.showinfo("welcome", "login success")
    else:
        mb.showinfo("error", "wrong details")


btn = Button(window, text="Login", font="times 12 bold", command=login)
btn.place(x=70, y=160)

window.mainloop()