import tkinter
from tkinter import *
from fpdf import FPDF
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        font_amul = "DS Fette Gotisch"
        self.root.title("Dairy Bill")
        bg_color = "white"
        title = tkinter.Label(self.root, text="                                                                    Billing Management System                                                                    ", bd=5, relief=tkinter.GROOVE, bg=bg_color, fg="red",
                              font=(font_amul, 30, "bold"), pady=2).place(x=0,y=0)

        # ===========================================Variables============================#

        self.milk = IntVar()
        self.buffalo = IntVar()
        self.curd=IntVar()
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.c_bill = StringVar()
        self.m1_price = StringVar()

        # =====================================END OF VARIABLES=============================#

        F1 = tkinter.LabelFrame(self.root, bd=5, relief=GROOVE, text="Customer Details",
                                font=("times new roman", 15, "bold"), fg="red", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_label = Label(F1, text="Customer Name", bg=bg_color, fg="red", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=20, font="arial 15", textvariable=self.c_name, bd=3, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphn_label = Label(F1, text="Vehicle Number", bg=bg_color, fg="red", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20, font="arial 15", textvariable=self.c_phon, bd=3, relief=SUNKEN).grid(row=0,
                                                                                                            column=3,
                                                                                                            pady=5,
                                                                                                            padx=10)

        c_bill_label = Label(F1, text="Bill Number", bg=bg_color, fg="red", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=20, font="arial 15", textvariable=self.c_bill, bd=3, relief=SUNKEN).grid(row=0,
                                                                                                              column=5,
                                                                                                              pady=5,
                                                                                                              padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=3, font="arail 12 bold",command=self.search).grid(row=0, column=6, pady=10,
                                                                                        padx=10)

        # ================Products=========================#
        F2 = tkinter.LabelFrame(self.root, bd=5, relief=GROOVE, text="Products", font=("times new roman", 15, "bold"),
                                fg="red", bg=bg_color)
        F2.place(x=5, y=170, width=325, height=380)

        nutri_rich_label = Label(F2, text="Nutri Rich", font="poppins 16 bold", bg=bg_color, fg="black").grid(row=0,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10,
                                                                                                              sticky="w")
        nutri_rich_txt = Entry(F2, width=10, font="arial 16 bold", bd=3, relief=SUNKEN, textvariable=self.milk).grid(
            row=0, column=1, padx=10, pady=10)

        buffalo_lable = Label(F2, text="Full Fat", font="poppins 16 bold", bg=bg_color, fg="black").grid(row=1, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        buffalo_txt = Entry(F2, width=10, font="arial 16 bold", textvariable=self.buffalo, bd=3, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=10)


        curd_lable = Label(F2, text="Curd", font="poppins 16 bold", bg=bg_color, fg="black").grid(row=2, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="w")
        curd_txt = Entry(F2, width=10, font="arial 16 bold", textvariable=self.curd, bd=3, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=10)

        # ===============Bill Area==================#
        F5 = tkinter.LabelFrame(self.root, bd=5, relief=GROOVE)
        F5.place(x=500, y=170, width=900, height=380)

        bill_title = Label(F5, text="BILL",
                           font="arail 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # ==============Button Frame==============#
        F6 = tkinter.LabelFrame(self.root, bd=5, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                                fg="red", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Weight", bg=bg_color, fg="red", font="poppins 14 bold").grid(row=0, column=0,
                                                                                                    padx=20, pady=1,
                                                                                                    sticky="w")
        m1_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.m1_price, bd=3, relief=SUNKEN).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=1)

        btn_f = Frame(F6, bd=4, relief=GROOVE)
        btn_f.place(x=440, width=800, height=105)

        total_btn = Button(btn_f, text="Total", bg="red", bd=3, relief=GROOVE, fg="white", pady=15, width=15,
                           font="arail 10 bold", command=self.total).grid(row=0, column=0, padx=5, pady=5)

        bill_btn = Button(btn_f, text="Bill", bg="red", bd=3, relief=GROOVE, fg="white", pady=15, width=15,
                          font="arail 10 bold", command=self.bill_area).grid(row=0, column=1, padx=5, pady=15)

        clear_btn = Button(btn_f, text="Clear", bg="red", bd=3, relief=GROOVE, fg="white", pady=15, width=15,
                           font="arail 10 bold", command=self.clear).grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, text="Exit", bg="red", bd=3, relief=GROOVE, fg="white", pady=15, width=15,
                          font="arail 10 bold", command=self.exit).grid(row=0, column=3, padx=5, pady=5)

        info_btn = Button(btn_f, text="About (i)", bg="red", bd=3, fg="white", pady=15, width=15, font="arail 10 bold",
                           command=self.aboutus).grid(row=0, column=4, padx=5, pady=5)


    def aboutus(self):
        messagebox.showinfo("About US","Made by:- Ravinshu Makkar (11908152) & Sharanya Bharghavi (11903126)")

    def total(self):
        self.total_m1_price = float(
            (self.milk.get() * 10) +
            (self.buffalo.get() * 500)+
            (self.curd.get()*400)
        )
        self.m1_price.set(str(self.total_m1_price))

    def bill_line(self):
        
        self.textarea.delete('1.0', END)
        today = str(date.today())
        self.textarea.insert(END,
                             "\t\t\t\t\tBILL"
                             "\n\t\t\t\t  Dairy & Milk Farm Bill\n\t\t\t\t  Dispatch order slip")
        self.textarea.insert(END, f"\n Serial No. = {self.c_bill.get()}")
        self.textarea.insert(END, f"\n Party Name = {self.c_name.get()}\t\t\t\t\t\t\t\tDate:- "+today)
        self.textarea.insert(END, f"\n Vehicle Number = {self.c_phon.get()}")
        self.textarea.insert(END,
                             "\n "
                             "_______________________________________________________________________________________")
        self.textarea.insert(END, "\n\n Particular\t\t\tNOS\tWeight\t\tRemarks")
        self.textarea.insert(END,
                             "\n "
                             "_______________________________________________________________________________________")

    def clear(self):
        self.textarea.delete('1.0', END)

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            self.textarea.delete('1.0', END)
            self.textarea.insert(END, "Details are missing")
        else:
            self.total()
            self.bill_line()
            self.billfile()
            if self.milk.get() != 0:
                self.textarea.insert(END, f"\n\n Nutri Rich\t\t\t {self.milk.get()}\t {self.milk.get() * 10}")
            if self.buffalo.get() != 0:
                self.textarea.insert(END, f"\n\n Full Fat\t\t\t {self.buffalo.get()}\t {self.buffalo.get() * 500}")
            
            if self.curd.get() != 0:
                self.textarea.insert(END, f"\n\n Curd\t\t\t {self.curd.get()}\t {self.curd.get() * 400}")
            self.textarea.insert(END,
                                 "\n "
                                 "______________________________________________________________________________________")
            self.textarea.insert(END, f"\n\t\t\t\t\t\t  Total : {self.total_m1_price}")


#===============================File Text and PDF ============================#

    def billfile(self):
        b_bill = str(self.c_bill.get())
        b_buffalo = str(self.buffalo.get())
        b_curd = str(self.curd.get())
        b_milk = str(self.milk.get())
        bill = open(b_bill + ".txt", 'w')
        write = bill.write(f"\t  'BILL  \t\t\t\t Dairy & Milk Farm Bill \n\t\t\t\t  Dispatch order slip \n\n Serial No. = {self.c_bill.get()}\n Party Name = {self.c_name.get()}\t\t\t\t\t\tDate:- {date.today()} \n Vehicle Number = {self.c_phon.get()}")
        if b_milk != 0:                       
            bill=open(b_bill + ".txt",'a')
            append=bill.write("\n\n Nutri rich = " + b_milk)

        if b_buffalo != 0:                       
            bill=open(b_bill + ".txt",'a')
            append=bill.write("\n\n Full Fat = " + b_buffalo)

        if b_curd != 0:                       
            bill=open(b_bill + ".txt",'a')
            append=bill.write("\n\n Curd = " + b_curd)
        if b_milk != 0:                       
            bill=open(b_bill + ".txt",'a')
            append=bill.write("\n\n")


        self.createpdf()
        bill.close()

    def createpdf(self):
        b_bill = str(self.c_bill.get())
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        f = open(b_bill + ".txt", "r")
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='C')
        pdf.output(b_bill+ ".pdf")

    def exit(self):
        self.root.destroy()



    def search(self):
        b_bill = str(self.c_bill.get())
        self.textarea.delete('1.0', END)
        try:
            f=open(b_bill + ".txt",'r')
            for y in f:
                self.textarea.insert(END,"\n"+y)
            f.close()
            
        except FileNotFoundError:
            self.textarea.insert(END,"File Not Found")
            messagebox.showerror("Error","File not found")
            




root = tkinter.Tk()
image = Image.open('image.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image = photo_image)
label.pack()
p1 = tkinter.PhotoImage(file='invoice.png')
root.iconphoto(False, p1)
obj = Bill_App(root)
root.mainloop()