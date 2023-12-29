import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
import about_us as abus

con = sq.connect("Details.db")
c = con.cursor()

class main_page(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.pack()
		self.master.title("Blood Donors")
		self.text1 = tk.Text(self, height=2, width=45,bg='blue')


		self.text1.grid(row=4, column=7)

		self.button_1 = tk.Button(self, text='Register',bg='red', command = self.register)
		self.button_1.grid(row=7, column=7)
		self.button_2 = tk.Button(self, text='Get info',bg='red', command = self.get_info)
		self.button_2.grid(row=9, column=7)
		self.button_3 = tk.Button(self, text='About Us',bg='red',command = abus.about_us_display)
		self.button_3.grid(row=11, column=7)
		self.button_4 = tk.Button(self, text='Exit',bg='red',command = self.close_win)
		self.button_4.grid(row=13, column=7)
	
	def close_win(self):
		self.destroy()
		quit()

	def confirm_win(self):
		self.rname = self.name1.get()
		self.g = self.radioval.get()
		print(self.g)
		self.rgender="F"
		if (self.g==1):
			self.rgender="F"
		elif(self.g==2):
			self.rgender="M"
		self.dob1 = self.day.get()
		self.dob2 = self.month.get()
		self.dob3 = self.year.get()
		self.rdob = str(self.dob1+"-"+self.dob2[:3]+"-"+self.dob3)
		self.rbgp = str(self.blood_group1.get())
		self.rcont = self.phone1.get()
		self.raddr = str(self.address1.get())
		self.i=0
		self.li = c.execute('SELECT * FROM REG')
		for row in self.li:
			self.i = row[0]
		self.i+=1
		self.info = (self.i, self.rgender, self.rname, self.rbgp, self.rcont, self.raddr, self.rdob)
		self.inserting = c.execute('INSERT INTO REG VALUES(?,?,?,?,?,?,?)', self.info)
		con.commit()
    
		self.win2 = tk.Tk()
		self.win2.title("Notification Window")
		self.text = tk.Text(self.win2)
		text1 = 'Information inserted! Your Donor ID is '+str(self.i)
		self.text.insert(tk.END, text1)
		self.button1 = tk.Button(self.win2,text = 'Exit',command = self.close_win)
		self.text.grid(row = 1,column = 2)
		self.button1.grid(row = 2,column = 2)
		self.win2.mainloop()

	def register(self):
		self.years = []
		for i in range(2019,1930,-1):
			self.years.append(i)

		self.days = []
		for i in range(1,32):
			self.days.append(i)

		self.win = tk.Tk()
		self.win.title( "Register")
		self.name = tk.Label(self.win, text='Name:')
		self.gen = tk.Label(self.win, text='Gender:')
		self.dob = tk.Label(self.win, text='Date of Birth:')
		self.radioval = tk.IntVar()
		self.r1 = tk.Radiobutton(self.win, text="Female", variable=self.radioval, value=1)
		self.r2 = tk.Radiobutton(self.win, text='Male', variable=self.radioval, value=2)
		self.blood_group = tk.Label(self.win, text='Blood group:')
		self.phone = tk.Label(self.win, text='Contact No.:')
		self.address = tk.Label(self.win, text='Address:')

		self.name1 = tk.StringVar()

		self.name1 = tk.Entry(self.win)
		self.phone1 = tk.Entry(self.win)
		self.address1 = tk.Entry(self.win)
		self.blood_group1 = ttk.Combobox(self.win, values=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
		self.day = ttk.Combobox(self.win, values=self.days)
		self.month = ttk.Combobox(self.win,values=['January','February','March','April','May','June','July','August','September','October','November','December'])
		self.year = ttk.Combobox(self.win,values = self.years)
		self.day.current()
		self.month.current()
		self.year.current()
		self.blood_group1.current()
		self.sub = tk.Button(self.win, text='Submit', command=self.confirm_win)
		self.name.grid(row = 1,column=1)
		self.name1.grid(row=1, column=2,columnspan = 2)
		self.gen.grid(row=2, column=1)
		self.r1.grid(row=2, column=2)
		self.r2.grid(row=2, column=3)
		self.dob.grid(row = 3,column = 1)
		self.day.grid(row=3,column = 2)
		self.month.grid(row = 3,column = 3)
		self.year.grid(row = 3,column = 4)
		self.blood_group.grid(row=4, column=1)
		self.blood_group1.grid(row=4,column=2)
		self.phone.grid(row=5, column=1)
		self.phone1.grid(row=5, column=2)
		self.address.grid(row=6, column=1)
		self.address1.grid(row=6, column=2)
		self.sub.grid(row=10, column=2,columnspan = 2)
		self.win.mainloop()

	def print_data(self):
		self.recv_bg = self.e2.get()
		self.recv_city = self.e3.get()
		self.printing = c.execute('SELECT ID, NAME, GENDER, BLOODGROUP, PHONE, CITY, DOB FROM REG R JOIN COMPAT C WHERE C.RBGRP=? AND R.BLOODGROUP=C.DBGRP AND CITY=?;', (self.recv_bg, self.recv_city,))
		count = 0
		row1 = ()
		for row in self.printing:
			row1+=row
			#print(row)
			count+=1
		if(count==0):
			self.C = tk.Tk()
			self.C.title('Donor Details')
			tk.Label(self.C, text='''Sorry!!
Seems like a rare blood group in your city!!
    Try searching in any other city!!''').grid(row=0, column=0)
			self.c1 = tk.Button(self.C, text = "Exit", command = self.close_win)
			self.c1.grid(row=1, column=0)
			self.C.mainloop()
		else:
			self.C = tk.Tk()
			self.C.title('Donor Details')
			tk.Label(self.C, text="ID").grid(row=0, column=0)
			tk.Label(self.C, text="Gender").grid(row=0, column=1)
			tk.Label(self.C, text="Name").grid(row=0, column=2)
			tk.Label(self.C, text="Blood Group").grid(row=0, column=3)
			tk.Label(self.C, text="Phone").grid(row=0, column=4)
			tk.Label(self.C, text="City").grid(row=0, column=5)
			tk.Label(self.C, text="DOB").grid(row=0, column=6)
			self.c1 = tk.Button(self.C, text = "          Exit          ", command = self.close_win)
			j=0
			for i in range(1, count+1):
				tk.Label(self.C, text=row1[i+j-1]).grid(row=i, column=0)
				tk.Label(self.C, text=row1[i+j+1-1]).grid(row=i, column=1)
				tk.Label(self.C, text=row1[i+j+2-1]).grid(row=i, column=2)
				tk.Label(self.C, text=row1[i+j+3-1]).grid(row=i, column=3)
				tk.Label(self.C, text=row1[i+j+4-1]).grid(row=i, column=4)
				tk.Label(self.C, text=row1[i+j+5-1]).grid(row=i, column=5)
				tk.Label(self.C, text=row1[i+j+6-1]).grid(row=i, column=6)
				j+=6
			self.c1.grid(row=count+1, column=2, columnspan = 3)
			self.C.mainloop()
	

	def get_info(self):
		self.B = tk.Tk()
		self.B.title('Recipient Details')
		tk.Label(self.B, text="Recipient Blood Group:").grid(row=0)
		tk.Label(self.B, text="Recipient City:").grid(row=1)
		self.e3 = tk.Entry(self.B)
		self.e2 = ttk.Combobox(self.B, values=['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
		self.b1 = tk.Button(self.B,text = "Go",command = self.print_data)
		self.e2.grid(row=0, column=1)
		self.e3.grid(row=1, column=1)
		self.b1.grid(row=3,column =1,columnspan = 2)
		self.B.mainloop()


if __name__== '__main__':
	main_page().mainloop()
