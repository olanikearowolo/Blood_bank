import time
import mysql.connector
import tkinter  as tk
from tkinter import *

root = Tk()
root.geometry("1200x750")
root.title("Blood Group Application")

def data():
    name_var = Name.get()
    age_var = Age.get()
    gen_var = Checkbutton1.get()
    if gen_var==1:
        n = "male"
    elif gen_var==2:
        n = "female"
    phone_var = Phone_number.get()
    blood_var = Blood_group.get()
    rh_var = Rh_factor.get()

    my_str3.set("Submitted Succesfully")
    

    mydb = mysql.connector.connect(user="root",host="localhost", password="",database="Blood_group_app")
    mycursor = mydb.cursor()
    sql1 = "INSERT INTO bloodbank(Name, Age, Checkbutton1, Phone_number, Blood_group, Rh_factor) values(%s,%s,%s,%s,%s,%s)"
    values = [(name_var, age_var, n, phone_var, blood_var, rh_var)]
    mycursor.executemany(sql1, values)

    mydb.commit()
    mydb.close()
    
def reset():
    Name.set("")
    Age.set("")
    Phone_number.set("")
    Blood_group.set("")
    Rh_factor.set("")
    Checkbutton1.set("")

def close():
    root.destroy()

def record():
    class Table:
        def __init__(self,r2):
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(r2, width=12, fg='Indian Red',font=('Arial',16,'bold')) 
                    self.e.grid(row=i+1, column=j+1) 
                    self.e.insert(END, lst[i][j]) 
    myconn = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "blood_group_app")
    cur = myconn.cursor()
    cur.execute("select * from bloodbank")
    lst = cur.fetchall()
    #print(lst)
    myconn.close()
    total_rows = len(lst) 
    total_columns = len(lst[0]) 
    myconn.close()
    r2 = Tk()
    t = Table(r2)



    
def my_details(id2):
    try:
        val = str(id2)
        try:
            my_cursor.execute("SELECT * FROM bloodbank where Phone_number ="+id2)
            student = my_cursor.fetchall()
            for row in student:
                #print("%s %s %s %s %s %s"%(row[0],row[1],row[2],row[3],row[4],row[5]))
                my_str.set(row)
        except :
            my_str.set("Database error")
    except:
        my_str.set("Check input")

def my_3(id3):
    try:
        id5 = '"{0}"'.format(id3)
        try:
            my_cursor.execute("SELECT * FROM bloodbank where Blood_group ="+id5)
            student = my_cursor.fetchall()
            for row in student:
                #print("%s %s %s %s %s %s"%(row[0],row[1],row[2],row[3],row[4],row[5]))
                my_str1.set(row)
        except:
            my_str1.set("Database error")
    except:
        my_str.set("Check input")
    

    
Name = StringVar()
Age = StringVar()
Phone_number = IntVar()
Blood_group = StringVar()
Rh_factor = StringVar()
Checkbutton1 = IntVar()
my_str = StringVar()
my_str3 = StringVar()



localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(font=('aria',30, 'bold' ),text="BLOOD GROUP APPLICATION",fg="Indian Red",bd=10,anchor='w')
lblinfo.place(x=350,y=0)
lblinfo = Label(font=('aria' ,20),text=localtime,fg="Light Coral",anchor=W)
lblinfo.place(x=480,y=50)

lblinfo = Label(font=('Times New Roman',15,'bold'),text="SEARCH RECORDS",fg="Black",anchor=W)
lblinfo.place(x=50,y=100)

my_connect = mysql.connector.connect(user="root",host="localhost", password="",database="Blood_group_app")
my_cursor = my_connect.cursor()
l1 = tk.Label(font=('aria' ,12,'bold'),text='Enter Phone number', width=25,fg='Indian Red')  
l1.place(x=0,y=140)
t1 = tk.Text(font=('aria' ,12,'bold'),  height=1, width=30,bg='Indian Red') 
t1.place(x=250,y=140)
b1 = tk.Button(text='Search',font=('aria' ,12,'bold'), width=15,fg='Indian Red',command=lambda: my_details(t1.get('1.0',END)))
b1.place(x=550,y=140)
l2 = tk.Label(font=('aria' ,12,'bold'),textvariable=my_str, width=60,fg='light coral')  
l2.place(x=720,y=140)
my_str.set("Search by Phone number")

l2 = tk.Label(font=('aria' ,12,'bold'),text='Enter Blood Group', width=25,fg='Indian Red')  
l2.place(x=-10,y=200)
t2 = tk.Text(font=('aria' ,12,'bold'),  height=1, width=30,bg='Indian Red') 
t2.place(x=250,y=200) 
b2 = tk.Button(text='Search',font=('aria' ,12,'bold'), width=15,fg='Indian Red',command=lambda: my_3(t2.get('1.0','end-1c')))
b2.place(x=550,y=200)
my_str1 = tk.StringVar()
l3 = tk.Label(font=('aria' ,12,'bold'),textvariable=my_str1, width=60,fg='light coral')  
l3.place(x=720,y=200)
my_str1.set("Search by Blood Group")


lblinfo = Label(font=('Times New Roman',15,'bold'),text="REGISTER TO BLOOD GROUP APP",fg="Black",anchor=W)
lblinfo.place(x=50,y=240)

lblname = Label(font=('aria',16,'bold'),text="Name ",fg="Indian Red",bd=10,anchor='w')
lblname.place(x=50,y=280)
txtname = Entry(font=('ariel',16,'bold'), textvariable=Name , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtname.place(x=250,y=280)

lblage = Label(font=('aria',16,'bold'),text="Age ",fg="Indian Red",bd=10,anchor='w')
lblage.place(x=50,y=340)
txtage = Entry(font=('ariel',16,'bold'), textvariable=Age , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtage.place(x=250,y=340)

lblgender = Label(font=('aria',16, 'bold'),text="Gender ",fg="Indian Red",anchor='w')
lblgender.place(x=55,y=400)
Button1 = Checkbutton(font=('aria',16,'bold'),fg="Indian Red",text = "Male",variable = Checkbutton1, onvalue= 1, offvalue = "") 
Button1.place(x=250,y=400)
Button2 = Checkbutton(font=('aria',16, 'bold'),fg="Indian Red",text = "Female",variable = Checkbutton1, onvalue = 2, offvalue = "")
Button2.place(x=400,y=400)


lblphone = Label(font=( 'aria' ,16, 'bold' ),text="Phone number ",fg="Indian Red",bd=10,anchor='w')
lblphone.place(x=50,y=460)
txtphone = Entry(font=('ariel' ,16,'bold'), textvariable=Phone_number , bd=6,insertwidth=4,bg="light coral" ,justify='right',)
txtphone.place(x=250,y=460)
lblbg = Label(font=( 'aria' ,16, 'bold' ),text="Blood Group ",fg="Indian Red",bd=10,anchor='w')
lblbg.place(x=50,y=520)
txtbg = Entry(font=('ariel' ,16,'bold'), textvariable=Blood_group , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtbg.place(x=250,y=520)

lblrh = Label(font=( 'aria' ,16, 'bold' ),text="Rh factor ",fg="Indian Red",bd=10,anchor='w')
lblrh.place(x=50,y=580)
txtrh = Entry(font=('ariel' ,16,'bold'), textvariable=Rh_factor, bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtrh.place(x=250,y=580)

l3 = tk.Label(font=('aria' ,12,'bold'),textvariable=my_str3, width=60,fg='light coral')  
l3.place(x=50,y=630)
my_str3.set(" ")

btnsubmit=Button(padx=8,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="Submit", bg="light coral",command=data)
btnsubmit.place(x=50,y=680)

btnreset=Button(padx=8,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="Reset", bg="light coral",command=reset)
btnreset.place(x=230,y=680)

btnexit=Button(padx=8,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=8, text="Exit", bg="light coral",command=close)
btnexit.place(x=410,y=680)

btnrcd=Button(padx=8,pady=4, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=12, text="View All Records", bg="light coral",command = record)
btnrcd.place(x=590,y=680)

root.mainloop()
