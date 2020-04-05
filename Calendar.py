from tkinter import *
import sqlite3

root = Tk()
conn = sqlite3.connect("database.db")
cur = conn.cursor()
logged_in_user = None


def dashboard():
    dash = Toplevel()
    Label(dash, text="Username: ").grid(row=0, column=0)
    uname = Entry(dash)
    uname.grid(row=0, column=1)
    Label(dash, text="Password: ").grid(row=1, column=0)
    paass = Entry(dash)
    paass.grid(row=1, column=1)
    btn = Button(dash, text="Login", command=oldNew)
    btn.grid(row=2)


def oldNew():
    oldNewWindow = Toplevel()
    oldBtn = Button(oldNewWindow, text="Old Customer", command=old)
    newBtn = Button(oldNewWindow, text="New Customer", command=new)
    oldBtn.grid(row=0, column=0)
    newBtn.grid(row=0, column=1)


def old():
    global logged_in_user
    oldCust = Toplevel()
    Label(oldCust, text="Enter the phone number: ").grid(row=0, column=0)
    num = Entry(oldCust)
    phoneNum = int(num.get())
    # rows = cur.execute("SELECT * FROM customer c, car_dets cd, repair as r WHERE c.phone="+str(phoneNum)+" AND (cd.ownerId=c.id AND (cd.id=r.carId AND c.id=r.ownerId))")
    # print(rows)


def new():
    newCust = Toplevel()

    Label(newCust, text="Name: ").grid(row=0, column=0)
    Label(newCust, text="Phone Number: ").grid(row=1, column=0)
    Label(newCust, text="Email: ").grid(row=2, column=0)
    Label(newCust, text="License Number: ").grid(row=3, column=0)

    name = Entry(newCust)
    phNum = Entry(newCust)
    email = Entry(newCust)
    liceNum = Entry(newCust)
    name.grid(row=0, column=1)
    phNum.grid(row=1, column=1)
    email.grid(row=2, column=1)
    liceNum.grid(row=3, column=1)

    cmd = "CREATE TABLE IF NOT EXISTS 'customer' ( 'id' INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT, 'name' TEXT DEFAULT NULL, 'phone' NUMERIC DEFAULT NULL, 'email' TEXT DEFAULT NULL, 'licenseNum' TEXT DEFAULT NULL);"
    cmd1 = "CREATE TABLE IF NOT EXISTS 'car_det' ( 'id' INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT, 'ownerId' NUMERIC DEFAULT NULL REFERENCES 'customer' ('id'), 'type' TEXT DEFAULT NULL, 'name' TEXT DEFAULT NULL, 'kilometers' INTEGER DEFAULT NULL, 'new field' TEXT DEFAULT NULL, 'insurance' TEXT DEFAULT NULL, 'engineNum' TEXT DEFAULT NULL, 'chassisNum' TEXT DEFAULT NULL);"
    cmd2 = "CREATE TABLE IF NOT EXISTS 'repair' ( 'id' INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT, 'ownerId' NUMERIC DEFAULT NULL REFERENCES 'customer' ('id'), 'carId' NUMERIC DEFAULT NULL REFERENCES 'car_det' ('id'), 'engine' INTEGER DEFAULT NULL, 'carWash' TEXT DEFAULT NULL, 'tireChange' INTEGER DEFAULT NULL, 'bodyReshaping' INTEGER DEFAULT NULL, 'desc_engine' TEXT DEFAULT NULL, 'desc_tire' TEXT DEFAULT NULL, 'desc_body' TEXT DEFAULT NULL);"
    cur.execute(cmd)
    cur.execute(cmd1)
    cur.execute(cmd2)
    conn.commit()

    def insertCust():
        global logged_in_user
        cmd = "INSERT INTO customer(name, phone, email, licenseNum) VALUES (\"" + name.get() + "\", " + str(
            phNum.get()) + ", \"" + email.get() + "\", \"" + liceNum.get() + "\")"
        cur.execute(cmd)
        conn.commit()
        cur.execute("SELECT id FROM customer WHERE phone=" + str(phNum.get()))
        id = cur.fetchall()
        logged_in_user = id[0][0]
        carDetails()

    submitBtn = Button(newCust, text="Submit", command=insertCust)
    submitBtn.grid(row=4)


def carDetails():
    carDet = Toplevel()
    Label(carDet, text="Car Type: ").grid(row=0, column=0)
    Label(carDet, text="Name(Eg. Hyundai Santro Zls): ").grid(row=1, column=0)
    Label(carDet, text="Kilometers: ").grid(row=2, column=0)
    Label(carDet, text="Engine Number: ").grid(row=3, column=0)
    Label(carDet, text="Chassis Number: ").grid(row=4, column=0)
    Label(carDet, text="Insurance Number: ").grid(row=5, column=0)

    carType = StringVar()
    suv = Radiobutton(carDet, text="SUV", variable=carType, value="suv")
    hatch = Radiobutton(carDet, text="Hatchback", variable=carType, value="hatchback")
    sedan = Radiobutton(carDet, text="Sedan", variable=carType, value="sedan")
    suv.grid(row=0, column=1)
    hatch.grid(row=0, column=2)
    sedan.grid(row=0, column=3)

    carName = Entry(carDet)
    carName.grid(row=1, column=1)
    km = Entry(carDet)
    km.grid(row=2, column=1)
    engNum = Entry(carDet)
    engNum.grid(row=3, column=1)
    chasNum = Entry(carDet)
    chasNum.grid(row=4, column=1)
    insNum = Entry(carDet)
    insNum.grid(row=5, column=1)

    def insertCar():
        cmd = "INSERT INTO car_det(ownerId, type, name, kilometers, insurance, engineNum, chassisNum) VALUES (" + str(
            logged_in_user) + ", \"" + carType.get() + "\", \"" + carName.get() + "\", " + str(
            km.get()) + ", \"" + insNum.get() + "\", \"" + str(engNum.get()) + "\", \"" + chasNum.get() + "\")"
        cur.execute(cmd)
        conn.commit()
        repair()

    submitBtn = Button(carDet, text="Submit", command=insertCar)
    submitBtn.grid(row=6)


def repair():
    repair = Toplevel()
    desc_eng = desc_tire = desc_body = ""
    Label(repair, text="Engine Repair").grid(row=0, column=0)
    Label(repair, text="Car Wash").grid(row=1, column=0)
    Label(repair, text="Tires Change").grid(row=2, column=0)
    Label(repair, text="Body Reshaping").grid(row=3, column=0)

    engRep = IntVar()
    yes = Radiobutton(repair, text="Yes", variable=engRep, value=1)
    no = Radiobutton(repair, text="No", variable=engRep, value=0)
    yes.grid(row=0, column=1)
    no.grid(row=0, column=2)


dashboard()
root.mainloop()