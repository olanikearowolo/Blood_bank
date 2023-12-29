import tkinter as tk

def about_us_display():
    A = tk.Tk()
    A.title("About Us")

    def this_list1():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.grid(row=1, column=1)
        top.mainloop()

    def this_list2():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.insert(2, "O+")
        Lb1.grid(row=1, column=1)
        top.mainloop()

    def this_list3():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.insert(2, "A-")

        Lb1.grid(row=1, column=1)
        top.mainloop()

    def this_list4():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.insert(2, "O+")
        Lb1.insert(3, "A-")
        Lb1.insert(4, "A+")
        Lb1.grid(row=1, column=1)
        top.mainloop()


    def this_list5():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.insert(3, "B-")

        Lb1.grid(row=1, column=1)
        top.mainloop()


    def this_list6():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.insert(2, "O+")
        Lb1.insert(3, "B-")
        Lb1.insert(4, "B+")
        Lb1.grid(row=1, column=1)
        top.mainloop()


    def this_list7():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.insert(2, "B-")
        Lb1.insert(3, "A-")
        Lb1.insert(4, "AB-")
        Lb1.grid(row=1, column=1)
        top.mainloop()


    def this_list8():
        top = tk.Tk()

        Lb1 = tk.Listbox(top)
        Lb1.insert(1, "O-")
        Lb1.insert(2, "O+")
        Lb1.insert(3, "A-")
        Lb1.insert(4, "A+")
        Lb1.insert(1, "B-")
        Lb1.insert(1, "B+")
        Lb1.insert(1, "AB-")
        Lb1.insert(1, "AB+")

        Lb1.grid(row=1, column=1)
        top.mainloop()


    # ro=tk.Tk()
    # self.canvas = tk.Canvas(self.A, width=300, height=300)
    # self.canvas.grid(row = 1,column = 2)
    # self.img = tk.PhotoImage(file="do.png")
    # self.canvas.create_image(20, 20, image=self.img)
    #start_info = tk.Label(A,text='We would like you to know which blood groups are realted.here is a table you can refer.')
    info_ = tk.Label(A, text="Click the blood group,you want blood for:")
    g1 = tk.Button(A, text="O-", command=this_list1)
    g2 = tk.Button(A, text="O+", command=this_list2)
    g3 = tk.Button(A, text="A-", command=this_list3)
    g4 = tk.Button(A, text="A+",command = this_list4)
    g5 = tk.Button(A,text = 'B-',command = this_list5)
    g6 = tk.Button(A,text = 'B+',command = this_list6)
    g7 = tk.Button(A,text = 'AB-',command = this_list7)
    g8 = tk.Button(A,text = 'AB-',command = this_list8)
    g1.grid(row = 4,column = 1)
    g2.grid(row=5, column=1)
    g3.grid(row=6, column=1)
    g4.grid(row=7, column=1)
    g5.grid(row=8, column=1)
    g6.grid(row=9, column=1)
    g7.grid(row=10, column=1)
    g8.grid(row=11, column=1)


    #start_info.grid(row=1, column=1)
    info_.grid(row=3, column=1)
    A.mainloop()

