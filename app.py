from tkinter import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk

root=Tk()
root.geometry("600x600")
conn=sqlite3.connect('user.db')
cur=conn.cursor()
lol=0
def budget():
    global bud
    global days
    child7=Toplevel()
    child7.geometry("100x100")
    days=Entry(child7)
    days.pack()
    bud=Entry(child7)
    bud.pack()
    submit=Button(child7,text="Submit",command=details)
    submit.pack()

def calc():
    remaining=int(mybudget)
    print(remaining)
    if CheckVar1.get()==1:
        one=100000
        two=500000
        three=2000000
        five=4000000
        if hotel1.get()=="Delux":
            remaining=remaining-one
        elif hotel1.get()=="2 Star":
            remaining=remaining-two
        elif hotel1.get()=="3 Star":
            remaining=remaining-three
        elif hotel1.get()=="5 Star":
            remaining=remaining-five
    print(remaining)
    if CheckVar2.get()==1:
        if photo1.get()=="Basic":
            remaining=remaining-5000
        elif photo1.get()=="Mid":
            remaining=remaining-10000
        elif photo1.get()=="Top Professionals":
            remaining=remaining-20000
    print(remaining)
    if CheckVar3.get()==1:
        if decoration1.get()=="Basic":
            remaining=remaining-50000
        elif decoration1.get()=="Mid":
            remaining=remaining-2000000
        elif decoration1.get()=="Extraordinary":
            remaining=remaining-5000000
    print(remaining)
    if CheckVar4.get()==1:
        remaining=remaining-10000
    print(remaining)
    if CheckVar5.get()==1:
        catguest1=int(catguest.get())
        no_of_days1=int(no_of_days)
        if catering1.get()=="Good":
            remaining=remaining-(catguest1*500*no_of_days1) #TODO no_of_days add
        if catering1.get()=="Best":
            remaining=remaining-(catguest1*1000*no_of_days1)
        if catering1.get()=="Premium":
            remaining=remaining-(catguest1*2000*no_of_days1)
    print(remaining)
    if CheckVar6.get()==1:
        if bridal1.get()=="Classic Lehenga":
            remaining=remaining-250000
        elif bridal1.get()=="Diamond Lehenga":
            remaining=remaining-500000
        elif bridal1.get()=="Gowm":
            remaining=remaining-100000
        elif bridal1.get()=="Saree":
            remaining=remaining-150000
    print(remaining)
    if CheckVar7.get()==1:
        if groom1.get()=="Sherwani":
            remaining=remaining-50000
        elif groom1.get()=="Tuxedo/Suit":
            remaining=remaining-100000
    print(remaining)
    if CheckVar8.get()==1:
        if ring1.get()=="Gold":
            remaining=remaining-100000
        elif ring1.get()=="Diamind":
            remaining=remaining-200000
        elif ring1.get()=="Silver":
            remaining=remaining-50000
        print(remaining)
    if CheckVar9.get()==1:
        remaining=remaining-20000
        print(remaining)
    if CheckVar10.get()==1:
        remaining=remaining-10000
        print(remaining)
    if CheckVar11.get()==1:
        if ev1.get()==1:
            remaining=remaining-250000
        if ev2.get()==1:
            remaining=remaining-50000
        if ev3.get()==1:
            remaining=remaining-20000
        if ev4.get()==1:
            remaining=remaining-20000
        print(remaining)

def details():
    global mybudget
    global CheckVar1
    global CheckVar2
    global CheckVar3
    global CheckVar4
    global CheckVar5
    global CheckVar6
    global CheckVar7
    global CheckVar8
    global CheckVar9
    global CheckVar10
    global CheckVar11
    global child6
    global no_of_days
    no_of_days=days.get()
    mybudget=bud.get()
    child6=Toplevel()
    child6.geometry("800x800")
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()
    CheckVar10 = IntVar()
    CheckVar11 = IntVar()
    hotel = Checkbutton(child6, text="Hotel/Staying Facilities", variable=CheckVar1,onvalue=1, offvalue=0,command=hotelm)
    photo = Checkbutton(child6, text="Photography & Videography", variable=CheckVar2,onvalue=1, offvalue=0,command=photom)
    decoration = Checkbutton(child6, text="Decoration", variable=CheckVar3,onvalue=1, offvalue=0,command=decorationm)
    transportation = Checkbutton(child6, text="Transportation", variable=CheckVar4,onvalue=1, offvalue=0,anchor="w")
    catering = Checkbutton(child6, text="Catering Services", variable=CheckVar5,onvalue=1, offvalue=0,command=cateringm)
    bridal = Checkbutton(child6, text="Bridal Attire", variable=CheckVar6,onvalue=1, offvalue=0,command=bridalm)
    groom = Checkbutton(child6, text="Groom Attire", variable=CheckVar7,onvalue=1, offvalue=0,command=groomm)
    ring = Checkbutton(child6, text="Ring", variable=CheckVar8,onvalue=1, offvalue=0,command=ringm)
    music = Checkbutton(child6, text="Music", variable=CheckVar9,onvalue=1, offvalue=0)
    makeup = Checkbutton(child6, text="Makeup", variable=CheckVar10,onvalue=1, offvalue=0)
    event = Checkbutton(child6, text="Ceremonies/Events", variable=CheckVar11, onvalue=1, offvalue=0,command=eventm)
    hotel.grid(sticky="W",row=0,column=0)
    photo.grid(sticky="W",row=1,column=0)
    decoration.grid(sticky="W",row=2,column=0)
    transportation.grid(sticky="W",row=3,column=0)
    catering.grid(sticky="W",row=4,column=0)
    bridal.grid(sticky="W",row=5,column=0)
    groom.grid(sticky="W",row=6,column=0)
    ring.grid(sticky="W",row=7,column=0)
    music.grid(sticky="W",row=8,column=0)
    makeup.grid(sticky="W",row=9,column=0)
    event.grid(sticky="W",row=10,column=0)
    but=Button(child6,text="2",command=calc)
    but.grid(row=11,column=0)


def hotelm():

    if CheckVar1.get() == 1:
        global hotel1
        hotel1 = StringVar()
        hotel1.set("Select category")
        drop1 = OptionMenu(child6, hotel1, "Delux", "2 Star", "3 Star", "5 Star")
        drop1.grid(row=0, column=1)
    else:
        drop.destroy()
def photom():
    if CheckVar2.get() == 1:
        global photo1
        photo1 = StringVar()
        photo1.set("Select category")
        drop2 = OptionMenu(child6, photo1, "Basic", "Mid", "Top Professionals")
        drop2.grid(row=1, column=1)
    else:
        drop.destroy()
def decorationm():
    if CheckVar3.get() == 1:
        global decoration1
        decoration1 = StringVar()
        decoration1.set("Select category")
        drop3 = OptionMenu(child6, decoration1, "Basic", "Good", "Extraordinary")
        drop3.grid(row=2, column=1)
    else:
        drop.destroy()
def cateringm():
    if CheckVar5.get() == 1:
        global catguest
        global catering1
        catguest=Entry(child6)
        catguest.grid(row=4,column=1)
        catering1 = StringVar()
        catering1.set("Select category")
        drop4 = OptionMenu(child6, catering1, "Good", "Best", "Premium")
        drop4.grid(row=4, column=2)
    else:
        drop.destroy()

def bridalm():
    if CheckVar6.get() == 1:
        global bridal1
        bridal1 = StringVar()
        bridal1.set("Select category")
        drop5 = OptionMenu(child6, bridal1, "Classic Lehenga", "Diamond Lehenga", "Gowm", "Saree") # 2.5l 5l 1l 1.5l
        drop5.grid(row=5, column=1)
    else:
        drop.destroy()

def groomm():
    if CheckVar7.get() == 1:
        global groom1
        groom1 = StringVar()
        groom1.set("Select category")
        drop6 = OptionMenu(child6, groom1, "Sherwani", "Tuxedo/Suit") #50t 1l
        drop6.grid(row=6, column=1)
    else:
        drop.destroy()

def ringm():
    if CheckVar8.get() == 1:
        global ring1
        ring1 = StringVar()
        ring1.set("Select category")
        drop7 = OptionMenu(child6, ring1, "Gold", "Diamond", "Silver") #1l 2l 50t
        drop7.grid(row=7, column=1)
    else:
        drop.destroy()

def eventm():

    if CheckVar11.get() == 1:
        global ev1
        global ev2
        global ev3
        global ev4
        ev1=IntVar()
        ev2=IntVar()
        ev3=IntVar()
        ev4=IntVar()
        eve1=Checkbutton(child6,text="Sangeet",onvalue=1,offvalue=0,variable=ev1) #2.5l
        eve1.grid(row=11,column=1)
        eve2=Checkbutton(child6,text="Cocktail Party",onvalue=1,offvalue=0,variable=ev2) #50t
        eve3=Checkbutton(child6,text="Mehendi",onvalue=1,offvalue=0,variable=ev3) #20t
        eve4=Checkbutton(child6,text="Haldi",onvalue=1,offvalue=0,variable=ev4)#20t
        eve2.grid(row=12,column=1)
        eve3.grid(row=13,column=1)
        eve4.grid(row=10,column=1)



def addevent():
    cur=conn.cursor()
    cur.execute("INSERT INTO Event(user_id,Date,Title) VALUES(\"{id}\",\"{date}\",\"{title}\");".format(id=user_id,date=cal.get(),title=abt.get()))
    conn.commit()
    budget()

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

def Mywedding():
    pass


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