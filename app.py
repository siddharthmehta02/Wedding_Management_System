from tkinter import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk

root=Tk()
root.geometry("600x600")
conn=sqlite3.connect('user.db')
cur=conn.cursor()

def addevent():
    cur=conn.cursor()
    cur.execute("INSERT INTO Event(user_id,Date,Title) VALUES(\"{id}\",\"{date}\",\"{title}\");".format(id=user_id,date=cal.get(),title=abt.get()))
    conn.commit()

def add():
    global cal
    global abt
    child4 = Tk()
    child4.geometry("400x400")
    ttk.Label(child4, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(child4, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    abtlb=Label(child4,text="Title of event").pack()
    abt=Entry(child4)
    abt.pack()
    eventsub=Button(child4,text="Submit",command=addevent)
    eventsub.pack()




def check():
    global var
    child5=Toplevel()
    cur=conn.cursor()
    cur.execute("SELECT id,Date,Title FROM Event WHERE user_id=\"{userid}\"".format(userid=user_id))
    mylist=cur.fetchall()
    print(mylist)
    var = IntVar(child5, 0)
    for x in mylist:
        Radiobutton(child5, text=x[2], variable=var, value=x[0]).pack()
    bttn=Button(child5,text="ok",command=Mywedding)
    bttn.pack()

def dashboard():
    child3=Toplevel()
    child3.geometry("800x800")
    addbtn=Button(child3,text="ADD A Wedding",command=add)
    addbtn.pack()
    chkbtn=Button(child3,text="Check My Weddings",command=check)
    chkbtn.pack()

def fillup():
    cur = conn.cursor()
    cur.execute("INSERT INTO User(Name,Email,Password) VALUES(\"{name}\",\"{email}\",\"{password}\");".format(name=name.get(),
                                                                                                 email=email.get(),
                                                                                                 password=password.get()))
    conn.commit()

def loggedin():
    global user_id
    cur=conn.cursor()
    cur.execute("SELECT userid,Name,Password FROM User WHERE Name=\"{name}\" and Password=\"{password}\"".format(name=name2.get(),password=password2.get()))
    ans=cur.fetchall()
    print(ans)
    if len(ans)==1:
        user_id=ans[0][0]
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