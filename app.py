from tkinter import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import ImageTk,Image

# root=Tk()
# root.geometry("600x580")
# myimg= ImageTk.PhotoImage(Image.open("login.jpg"))
# mylabel= Label(root,image=myimg)
# mylabel.pack()

conn=sqlite3.connect('user.db')
cur=conn.cursor()
detaillist=['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
cats=["Hotel/Staying Facilities","Photography & Videography","Decoration","Transportation","Catering Services","Bridal Attire","Groom Attire","Ring","Music","Makeup","Ceremonies/Events"]
price=["0","0","0","0","0","0","0","0","0","0","0","0"]
totalvalue=0


def details2():
    child8.withdraw()

#DONE
def budget():
    global bud
    global days
    global child7
    child7=Toplevel()
    child7.geometry("400x370")
    myimg = ImageTk.PhotoImage(Image.open("home.jpg"))
    mylabel = Label(child7, image=myimg)
    mylabel.pack()
    daylb=Label(child7,text="No of Days: ",bg="#F8D7FD")
    daylb.pack()
    daylb.place(x=60, y=100)
    days=Entry(child7,bg="#F8D7FD")
    days.pack()
    days.place(x=160, y=100)
    budlb=Label(child7,text="Budget: ",bg="#F8D7FD")
    budlb.pack()
    budlb.place(x=60, y=140)
    bud=Entry(child7,bg="#F8D7FD")
    bud.pack()
    bud.place(x=160, y=140)
    submit=Button(child7,text="Submit",command=details,bg="#ab05e8", pady=10, padx=30)
    submit.pack()
    submit.place(x=160,y=180)
    child7.mainloop()

def changebudget():
    child8.withdraw()
    global child9
    global days2
    global bud2
    global mybudget
    child9 = Toplevel()
    child9.geometry("400x370")
    myimg = ImageTk.PhotoImage(Image.open("home.jpg"))
    mylabel = Label(child9, image=myimg)
    mylabel.pack()
    daylb = Label(child9, text="No of Days: ", bg="#F8D7FD")
    daylb.pack()
    daylb.place(x=60, y=100)
    days = Entry(child9, bg="#F8D7FD")
    days.pack()
    days.place(x=160, y=100)
    budlb = Label(child9, text="Budget: ", bg="#F8D7FD")
    budlb.pack()
    budlb.place(x=60, y=140)
    bud = Entry(child9, bg="#F8D7FD")
    bud.pack()
    bud.place(x=160, y=140)
    submit = Button(child9, text="Submit", command=lambda: calcpre(bud.get()), bg="#ab05e8", pady=10, padx=30)
    submit.pack()
    submit.place(x=160, y=180)
    child9.mainloop()

def calcpre(val):
    child9.withdraw()
    calc(val)

def store():
    listToStr = ''.join(map(str,detaillist))

    cur = conn.cursor()
    cur.execute("INSERT INTO category(user_id,list,title,price) VALUES(\"{id}\",\"{list}\",\"{title}\",\"{price}\");".format(id=user_id,list=listToStr,title=abt.get(),price=price))
    conn.commit()
    result()

def result():

    global mycategory1
    cur=conn.cursor()
    cur.execute("SELECT list FROM category WHERE user_id=\"{userid}\"".format(userid=user_id))
    mycategory=cur.fetchall()
    mycategory1=list(mycategory[-1][0])
    print(mycategory)
    result2()

def result2():
    result = Toplevel()
    result.geometry("400x400")
    a=0
    for x in range(0,11):
        if mycategory1[x]=="1":
            catlabel=Label(result,text=cats[x])
            catlabel.grid(sticky="W",row=a,column=0)
            pricelabel=Label(result,text=price[x])
            pricelabel.grid(row=a,column=1)
            a+=1
    totalline=Label(result,text="---------")
    totalline.grid(row=a,column=1)
    a+=1

    totalans=Label(result,text=price[11])
    totalans.grid(row=a,column=1)

def calc(mybudget):
    global child8
    global totalvalue
    child8=Toplevel()
    child8.geometry("400x400")
    myimg = ImageTk.PhotoImage(Image.open("price.jpg"))
    mylabel = Label(child8, image=myimg)
    mylabel.pack()
    mylabel.place(x=0, y=0)
    remaining=int(mybudget)
    print(remaining)
    if CheckVar1.get()==1:
        one=100000
        two=500000
        three=2000000
        five=4000000
        if hotel1.get()=="Delux":
            temp=one
            remaining=remaining-one
        elif hotel1.get()=="2 Star":
            temp=two
            remaining=remaining-two
        elif hotel1.get()=="3 Star":
            temp=three
            remaining=remaining-three
        elif hotel1.get()=="5 Star":
            temp=five
            remaining=remaining-five
        price[0]=str(temp)
        totalvalue=totalvalue+temp
    print(remaining)
    if CheckVar2.get()==1:
        if photo1.get()=="Basic":
            remaining=remaining-5000
            temp=5000
        elif photo1.get()=="Mid":
            remaining=remaining-10000
            temp=10000
        elif photo1.get()=="Top Professionals":
            remaining=remaining-20000
            temp=20000
        price[1]=str(temp)
        totalvalue = totalvalue + temp
    print(remaining)

    if CheckVar3.get()==1:
        if decoration1.get()=="Basic":
            remaining=remaining-500000
            temp=500000
        elif decoration1.get()=="Mid":
            remaining=remaining-2000000
            temp=2000000
        elif decoration1.get()=="Extraordinary":
            remaining=remaining-5000000
            temp=5000000
        price[2]=str(temp)
        totalvalue = totalvalue + temp
    print(remaining)

    if CheckVar4.get()==1:
        remaining=remaining-10000
        temp=10000
        price[3]=str(temp)
        totalvalue = totalvalue + temp
    print(remaining)

    if CheckVar5.get()==1:
        catguest1=int(catguest.get())
        no_of_days1=int(no_of_days)
        if catering1.get()=="Good":
            temp=catguest1*500*no_of_days1
            remaining=remaining-(temp)
        if catering1.get()=="Best":
            temp=catguest1*1000*no_of_days1
            remaining=remaining-(temp)
        if catering1.get()=="Premium":
            temp=catguest1*2000*no_of_days1
            remaining=remaining-(temp)
        price[4]=str(temp)
        totalvalue = totalvalue + temp
    print(remaining)

    if CheckVar6.get()==1:
        if bridal1.get()=="Classic Lehenga":
            remaining=remaining-250000
            temp=250000
        elif bridal1.get()=="Diamond Lehenga":
            remaining=remaining-500000
            temp=500000
        elif bridal1.get()=="Gowm":
            remaining=remaining-100000
            temp=100000
        elif bridal1.get()=="Saree":
            remaining=remaining-150000
            temp=150000
        price[5]=str(temp)
        totalvalue = totalvalue + temp
    print(remaining)

    if CheckVar7.get()==1:
        if groom1.get()=="Sherwani":
            temp=50000
            remaining=remaining-50000
        elif groom1.get()=="Tuxedo/Suit":
            temp=100000
            remaining=remaining-100000
        price[6]=str(temp)
        totalvalue = totalvalue + temp
    print(remaining)

    if CheckVar8.get()==1:
        if ring1.get()=="Gold":
            temp=100000
            remaining=remaining-100000
        elif ring1.get()=="Diamind":
            temp=200000
            remaining=remaining-200000
        elif ring1.get()=="Silver":
            temp=50000
            remaining=remaining-50000
        price[7]=str(temp)
        totalvalue = totalvalue + temp
        print(remaining)

    if CheckVar9.get()==1:
        temp=20000
        remaining=remaining-20000
        price[8]=str(temp)
        totalvalue = totalvalue + temp
        print(remaining)

    if CheckVar10.get()==1:
        temp=10000
        remaining=remaining-10000
        price[9]=str(temp)
        totalvalue = totalvalue + temp
        print(remaining)

    if CheckVar11.get()==1:
        if ev1.get()==1:
            temp=250000
            remaining=remaining-250000
        if ev2.get()==1:
            temp=50000
            remaining=remaining-50000
        if ev3.get()==1:
            temp=20000
            remaining=remaining-20000
        if ev4.get()==1:
            temp=20000
            remaining=remaining-20000
        price[10]=str(temp)
        totalvalue = totalvalue + temp
        print(remaining)
    price[11] = str(totalvalue)

    if remaining<0:

        print("You Have",-remaining," Less")
        mystr="You Have "+str(-remaining)+" Less"
        rem=Label(child8,text=mystr, pady=5,bg="#EFA5FD")
        rem.pack()
        rem.place(x=150,y=20)
        #do you want to increase budget or change your decisions?
        incbtn=Button(child8,text="Increase Budget",command=changebudget, pady=10, padx=20,bg="#ab05e8")
        incbtn.pack()
        incbtn.place(x=150,y=100)
        chgbtn=Button(child8,text="Change Decisions",command=details, pady=10, padx=20,bg="#ab05e8")
        chgbtn.pack()
        chgbtn.place(x=150,y=150)
    if remaining==0:
        print("Perfect bitchhhh")
        mystr="Perfect Bitchhhhh"
        mylbl=Label(child8,text=mystr,bg="#EFA5FD")
        mylbl.pack()
        mylbl.place(x=150,y=20)
        result=Button(child8,text="See Result",command=store, pady=10, padx=20,bg="#ab05e8")
        result.pack()
        result.place(x=150,y=100)
        mm=Button(child8,text="Main Menu",command=dashboard, pady=10, padx=20,bg="#ab05e8")
        mm.pack()
        mm.place(x=150,y=150)
        #result()
    if remaining>0:
        print("Congrats you still have ",remaining," amount left")
        mystr="Congrats you still have "+str(remaining)+" amount remaining"
        mylbl=Label(child8,text=mystr,bg="#EFA5FD")
        mylbl.pack()
        mylbl.place(x=50,y=20)
        #do you wnt to add any other things?
        addbtn=Button(child8,text="Add more things!",command=details2, pady=10, padx=20,bg="#ab05e8")
        addbtn.pack()
        addbtn.place(x=150,y=80)
        result = Button(child8, text="See Result", command=store, pady=10, padx=20,bg="#ab05e8")   #TODO DESIGN
        result.pack()
        result.place(x=150,y=150)
        mm = Button(child8, text="Main Menu", command=dashboard, pady=10, padx=20,bg="#ab05e8")
        mm.pack()
        mm.place(x=150,y=220)

        #no?result()
        #yes?changedecision
    child8.mainloop()


def details():
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
    child7.withdraw()
    no_of_days=days.get()
    mybudget=bud.get()
    child6=Toplevel()
    child6.geometry("450x450")
    child6.configure(bg="#EFA5FD")
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
    hotel = Checkbutton(child6, text="Hotel/Staying Facilities", variable=CheckVar1,onvalue=1, offvalue=0,command=hotelm,bg="#EFA5FD")
    photo = Checkbutton(child6, text="Photography & Videography", variable=CheckVar2,onvalue=1, offvalue=0,command=photom,bg="#EFA5FD")
    decoration = Checkbutton(child6, text="Decoration", variable=CheckVar3,onvalue=1, offvalue=0,command=decorationm,bg="#EFA5FD")
    transportation = Checkbutton(child6, text="Transportation", variable=CheckVar4,onvalue=1, offvalue=0,anchor="w",command=setup,bg="#EFA5FD")
    catering = Checkbutton(child6, text="Catering Services", variable=CheckVar5,onvalue=1, offvalue=0,command=cateringm,bg="#EFA5FD")
    bridal = Checkbutton(child6, text="Bridal Attire", variable=CheckVar6,onvalue=1, offvalue=0,command=bridalm,bg="#EFA5FD")
    groom = Checkbutton(child6, text="Groom Attire", variable=CheckVar7,onvalue=1, offvalue=0,command=groomm,bg="#EFA5FD")
    ring = Checkbutton(child6, text="Ring", variable=CheckVar8,onvalue=1, offvalue=0,command=ringm,bg="#EFA5FD")
    music = Checkbutton(child6, text="Music", variable=CheckVar9,onvalue=1, offvalue=0,command=setup,bg="#EFA5FD")
    makeup = Checkbutton(child6, text="Makeup", variable=CheckVar10,onvalue=1, offvalue=0,command=setup,bg="#EFA5FD")
    event = Checkbutton(child6, text="Ceremonies/Events", variable=CheckVar11, onvalue=1, offvalue=0,command=eventm,bg="#EFA5FD")
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
    but=Button(child6,text="Submit",pady=10,padx=30,bg="#ab05e8",command=lambda:calc(mybudget))
    but.grid(row=14,column=0)
    child6.mainloop()

def setup():
    if CheckVar4.get()==1:
        detaillist[3]="1"
    if CheckVar9.get()==1:
        detaillist[8]="1"
    if CheckVar10.get()==1:
        detaillist[9]="1"

def hotelm():
    if CheckVar1.get() == 1:
        detaillist[0]="1"
        global hotel1
        hotel1 = StringVar()
        hotel1.set("Select category")
        drop = OptionMenu(child6, hotel1, "Delux", "2 Star", "3 Star", "5 Star")
        drop.grid(row=0, column=1)
        drop.config(bg="#EFA5FD")
    else:
        pass

def photom():
    if CheckVar2.get() == 1:
        detaillist[1]="1"
        global photo1
        photo1 = StringVar()
        photo1.set("Select category")
        drop = OptionMenu(child6, photo1, "Basic", "Mid", "Top Professionals")
        drop.grid(row=1, column=1)
        drop.config(bg="#EFA5FD")
    else:
        pass
def decorationm():
    if CheckVar3.get() == 1:
        detaillist[2]="1"
        global decoration1
        decoration1 = StringVar()
        decoration1.set("Select category")
        drop = OptionMenu(child6, decoration1, "Basic", "Good", "Extraordinary")
        drop.grid(row=2, column=1)
        drop.config(bg="#EFA5FD")
    else:
        pass
def cateringm():
    if CheckVar5.get() == 1:
        detaillist[4]="1"
        global catguest
        global catering1
        catguest=Entry(child6)
        catguest.grid(row=4,column=1)
        catering1 = StringVar()
        catering1.set("Select category")
        drop = OptionMenu(child6, catering1, "Good", "Best", "Premium")
        drop.grid(row=4, column=2)
        drop.config(bg="#EFA5FD")
    else:
        pass

def bridalm():
    if CheckVar6.get() == 1:
        detaillist[5]="1"
        global bridal1
        bridal1 = StringVar()
        bridal1.set("Select category")
        drop = OptionMenu(child6, bridal1, "Classic Lehenga", "Diamond Lehenga", "Gowm", "Saree") # 2.5l 5l 1l 1.5l
        drop.grid(row=5, column=1)
        drop.config(bg="#EFA5FD")
    else:
        pass

def groomm():
    if CheckVar7.get() == 1:
        detaillist[6]="1"
        global groom1
        groom1 = StringVar()
        groom1.set("Select category")
        drop = OptionMenu(child6, groom1, "Sherwani", "Tuxedo/Suit") #50t 1l
        drop.grid(row=6, column=1)
        drop.config(bg="#EFA5FD")
    else:
        pass

def ringm():
    if CheckVar8.get() == 1:
        detaillist[7]="1"
        global ring1
        ring1 = StringVar()
        ring1.set("Select category")
        drop = OptionMenu(child6, ring1, "Gold", "Diamond", "Silver") #1l 2l 50t
        drop.grid(row=7, column=1)
        drop.config(bg="#EFA5FD")
    else:
        pass

def eventm():

    if CheckVar11.get() == 1:
        detaillist[10]="1"
        global ev1
        global ev2
        global ev3
        global ev4
        ev1=IntVar()
        ev2=IntVar()
        ev3=IntVar()
        ev4=IntVar()
        eve1=Checkbutton(child6,text="Sangeet",onvalue=1,offvalue=0,variable=ev1,bg="#EFA5FD") #2.5l
        eve1.grid(sticky="W",row=11,column=1)
        eve2=Checkbutton(child6,text="Cocktail Party",onvalue=1,offvalue=0,variable=ev2,bg="#EFA5FD") #50t
        eve3=Checkbutton(child6,text="Mehendi",onvalue=1,offvalue=0,variable=ev3,bg="#EFA5FD") #20t
        eve4=Checkbutton(child6,text="Haldi",onvalue=1,offvalue=0,variable=ev4,bg="#EFA5FD")#20t
        eve2.grid(sticky="W",row=12,column=1)
        eve3.grid(sticky="W",row=13,column=1)
        eve4.grid(sticky="W",row=10,column=1)



def addevent():
    child4.withdraw()
    cur=conn.cursor()
    cur.execute("INSERT INTO Event(user_id,Date,Title) VALUES(\"{id}\",\"{date}\",\"{title}\");".format(id=user_id,date=cal.get(),title=abt.get()))
    conn.commit()
    budget()

def add():
    child3.withdraw()
    global child4
    global cal
    global abt
    child4 = Toplevel()
    child4.geometry("400x370")
    # child4.configure(bg="#EFA5FD")
    myimg = ImageTk.PhotoImage(Image.open("home.jpg"))
    mylabel = Label(child4, image=myimg)
    mylabel.pack()
    mylabel.place(x=0,y=0)


    a=ttk.Label(child4, text='Choose date',background="#EFA5FD")
    a.pack()
    a.place(x=50,y=100)

    cal = DateEntry(child4, width=12, background='#ab05e8',foreground='white', borderwidth=2)
    cal.pack()
    cal.place(x=150,y=100)
    abtlb=Label(child4,text="Title of event",bg="#EFA5FD")
    abtlb.pack()
    abtlb.place(x=50,y=150)
    abt=Entry(child4)
    abt.pack()
    abt.place(x=150,y=150)
    eventsub=Button(child4,text="Submit",command=addevent, pady=10, padx=30,bg="#ab05e8")
    eventsub.pack()
    eventsub.place(x=100,y=200)


    child4.mainloop()

def Mywedding():
    global mycategory1
    global price
    titlechoosed=var.get()
    cur=conn.cursor()
    cur.execute("SELECT list,price FROM category WHERE title=\"{tit}\"".format(tit=titlechoosed))
    mycatreplica=cur.fetchall()
    mycategory1=mycatreplica[-1][0]
    pricereplica=mycatreplica[-1][1]
    price=eval(pricereplica)
    result2()


def check():
    child3.withdraw()
    global var
    global var
    child5=Toplevel()
    child5.geometry("1920x1080")
    child5.configure(bg="#EFA5FD")
    cur=conn.cursor()
    cur.execute("SELECT id,Date,Title FROM Event WHERE user_id=\"{userid}\"".format(userid=user_id))
    mylist=cur.fetchall()
    print(mylist)
    var = StringVar(child5,0)
    for x in mylist:
        myradio=Radiobutton(child5, text=x[2], variable=var, value=x[2],bg="#EFA5FD")
        myradio.pack(anchor=W)

    bttn=Button(child5,text="ok",command=Mywedding, pady=10, padx=30,bg="#ab05e8")
    bttn.pack()


def dashboard():
    global child3
    child3=Toplevel()
    child3.geometry("600x600")
    myimg = ImageTk.PhotoImage(Image.open("login.jpg"))
    mylabel = Label(child3, image=myimg)
    mylabel.pack()
    addbtn=Button(child3,text="ADD A Wedding",command=add,padx="50",pady="20",bg="#ab05e8")
    addbtn.pack()
    addbtn.place(x=100, y=300)
    chkbtn=Button(child3,text="Check My Weddings",command=check,padx="50",pady="20",bg="#ab05e8")
    chkbtn.pack()
    chkbtn.place(x=300,y=300)
    child3.mainloop()

def fillup():
    cur = conn.cursor()
    cur.execute("INSERT INTO User(Name,Email,Password) VALUES(\"{name}\",\"{email}\",\"{password}\");".format(name=name.get(),
                                                                                                 email=email.get(),
                                                                                                 password=password.get()))
    conn.commit()

def loggedin():
    child2.withdraw()
    global user_id
    cur=conn.cursor()
    cur.execute("SELECT userid,Name,Password FROM User WHERE Name=\"{name}\" and Password=\"{password}\"".format(name=name2.get(),password=password2.get()))
    ans=cur.fetchall()
    print(ans)
    if len(ans)==1:
        user_id=ans[0][0]
        dashboard()
    else:
        errorlabel=Label(child2,text="Wrong Details!")
        errorlabel.pack()

def login():
    global child2
    global name2
    global password2

    root.withdraw()

    child2 = Toplevel()
    child2.geometry("400x370")
    myimg = ImageTk.PhotoImage(Image.open("home.jpg"))
    mylabel = Label(child2, image=myimg)
    mylabel.pack()
    nlabel = Label(child2, text="Name: ",bg="#F8D7FD")
    nlabel.pack()
    nlabel.place(x=80, y=100)
    name2 = Entry(child2, width=30,bg="#F8D7FD")
    name2.pack()
    name2.place(x=150, y=100)
    plabel = Label(child2, text="Password: ",bg="#F8D7FD")
    plabel.pack()
    plabel.place(x=80, y=140)
    password2 = Entry(child2, width=30,show="*",bg="#F8D7FD")
    password2.pack()
    password2.place(x=150, y=140)
    submit = Button(child2, text="Login", command=loggedin, pady=10, padx=30,bg="#ab05e8")
    submit.pack()
    submit.place(x=160, y=180)
    child2.mainloop()


def signup():
    global name
    global email
    global password
    check=1
    child1=Toplevel()
    child1.geometry("400x370")
    myimg = ImageTk.PhotoImage(Image.open("home.jpg"))
    mylabel = Label(child1, image=myimg)
    mylabel.pack()
    nlabel=Label(child1,text="Name: ",bg="#F8D7FD")
    nlabel.pack()
    nlabel.place(x=80,y=110)
    name=Entry(child1,width=30,bg="#F8D7FD")
    name.pack()
    name.place(x=150,y=110)
    elabel = Label(child1, text="Email: ",bg="#F8D7FD")
    elabel.pack()
    elabel.place(x=80,y=150)
    email = Entry(child1,width=30,bg="#F8D7FD")
    email.pack()
    email.place(x=150,y=150)
    plabel = Label(child1, text="Password: ",bg="#F8D7FD")
    plabel.pack()
    plabel.place(x=80,y=190)
    password = Entry(child1,show="*",width=30,bg="#F8D7FD")
    password.pack()
    password.place(x=150,y=190)
    submit=Button(child1,text="Submit",command=fillup,pady=10,padx=30,bg="#ab05e8")
    submit.pack()
    submit.place(x=160,y=230)
    child1.mainloop()


root=Tk()
root.geometry("600x580")
myimg= ImageTk.PhotoImage(Image.open("login.jpg"))
mylabel= Label(root,image=myimg)
mylabel.pack()
logbtn=Button(root,text="Login",command=login,padx="50",pady="20",bg="#ab05e8")
logbtn.pack()
logbtn.place(x=140,y=300)
subtn=Button(root,text="Sign-Up",command=signup,padx="50",pady="20",bg="#ab05e8")
subtn.pack()
subtn.place(x=330,y=300)










root.mainloop()