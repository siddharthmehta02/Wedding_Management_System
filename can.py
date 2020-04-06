from tkinter import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import ImageTk,Image
def addevent():
    pass

global child4
global cal
global abt
child4 = Tk()
child4.geometry("400x400")
myimg = ImageTk.PhotoImage(Image.open("login.jpg"))
mylabel = Label(child4, image=myimg)
mylabel.pack()
# ttk.Label(child4, text='Choose date').pack(padx=10, pady=10)
# cal = DateEntry(child4, width=12, background='darkblue',foreground='white', borderwidth=2)
# cal.pack(padx=10, pady=10)
# abtlb=Label(child4,text="Title of event")
# abtlb.pack()
abt=Entry(child4)
abt.pack()
eventsub=Button(child4,text="Submit",command=addevent)
eventsub.pack()
child4.mainloop()

