from tkinter import *
import sqlite3

root=Tk()
root.geometry("600x600")
conn=sqlite3.connect('user.db')
cur=conn.cursor()

def dashboard():
    child3=Toplevel()
    child3.geometry("800x800")
    addbtn=Button

def fillup():
    cur = conn.cursor()
    cur.execute("INSERT INTO User(Name,Email,Password) VALUES(\"{name}\",\"{email}\",\"{password}\");".format(name=name.get(),
                                                                                                 email=email.get(),
                                                                                                 password=password.get()))
    conn.commit()

def loggedin():
    cur=conn.cursor()
    cur.execute("SELECT Name,Password FROM User WHERE Name=\"{name}\" and Password=\"{password}\"".format(name=name2.get(),password=password2.get()))
    ans=cur.fetchall()
    print(ans)
    if len(ans)==1:
        dashboard()
    else:
        errorlabel=Label(child2,text="Wrong Details!").pack()

def login():
    global child2
    global name2
    global password2
    child2 = Toplevel()
    child2.geometry("400x400")
    nlabel = Label(child2, text="Name: ")
    nlabel.pack()
    nlabel.place(x=80, y=10)
    name2 = Entry(child2, width=30)
    name2.pack()
    name2.place(x=150, y=10)
    plabel = Label(child2, text="Password: ")
    plabel.pack()
    plabel.place(x=80, y=50)
    password2 = Entry(child2, width=30,show="*")
    password2.pack()
    password2.place(x=150, y=50)
    submit = Button(child2, text="Login", command=loggedin, pady=10, padx=30)
    submit.pack()
    submit.place(x=160, y=90)

def signup():
    global name
    global email
    global password
    check=1
    child1=Toplevel()
    child1.geometry("400x400")
    nlabel=Label(child1,text="Name: ")
    nlabel.pack()
    nlabel.place(x=80,y=10)
    name=Entry(child1,width=30)
    name.pack()
    name.place(x=150,y=10)
    elabel = Label(child1, text="Email: ")
    elabel.pack()
    elabel.place(x=80,y=50)
    email = Entry(child1,width=30)
    email.pack()
    email.place(x=150,y=50)
    plabel = Label(child1, text="Password: ")
    plabel.pack()
    plabel.place(x=80,y=90)
    password = Entry(child1,show="*",width=30)
    password.pack()
    password.place(x=150,y=90)
    submit=Button(child1,text="Submit",command=fillup,pady=10,padx=30)
    submit.pack()
    submit.place(x=160,y=140)
    check=0



logbtn=Button(root,text="Login",command=login,padx="50",pady="20")
logbtn.pack()
logbtn.place(x=120,y=200)
subtn=Button(root,text="Sign-Up",command=signup,padx="50",pady="20")
subtn.pack()
subtn.place(x=320,y=200)










root.mainloop()