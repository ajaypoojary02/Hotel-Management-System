from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
import webbrowser as wb
from fpdf import FPDF
import platform
import os
import tempfile
import datetime
import random
import time
from tkcalendar import *

def splash_win():
    splash_root=Tk()
    splash_scr=Splash_Screen(splash_root)
    splash_root.mainloop()

class Splash_Screen:
    def __init__(self, splash):
        self.splash=splash
        self.splash.title("Splash_screen")
        self.splash.overrideredirect(True)
        self.splash.resizable(0, 0)
        image = PhotoImage(file=r"img\splash_screen.png")
        height = 450
        width = 718
        x = (self.splash.winfo_screenwidth() // 2) - (width // 2)
        y = (self.splash.winfo_screenheight() // 2) - (height // 2)


        self.splash.geometry("{}x{}+{}+{}".format(width, height, x, y))

        # Label(self.splash, image=image).pack()

        bglbl = Label(self.splash, image=image)
        bglbl.image = image
        bglbl.pack()
        self.splash.after(2000, self.main)

    def main(self):
        self.splash.destroy()
        root = Tk()
        app = SystemLogin(root)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()

class SystemLogin:
    def __init__(self, master):
        self.master = master
        self.master.wm_iconbitmap("img/Coffee.ico")
        self.master.title("Hotel Management")
        self.master.geometry("1119x600+100+50")
        self.bg = PhotoImage(file="img/bg.png")
        self.bg_image=Label(self.master,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        Frame_login=Frame(self.master,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)


        #variables

        self.Username=StringVar()
        self.Password=StringVar()

        title = Label(Frame_login, text="Hotel Management System", bg='white', fg="#d77337",
                      font=("arial",20, "bold"), pady=6).place(x=90,y=30)

        lbl_user = Label(Frame_login, text="Username:",  fg="#d77337",bg="white", font=("arial", 16, "bold")).place(
            x=90,y=100)
        ent_user = Entry(Frame_login, textvariable=self.Username, font=("arial", 16),bg="lightgray").place(x=90, y=130, width=350, height=35)
        lbl_passwd = Label(Frame_login, text="Password:", height="1", fg="#d77337",bg="white",
                           font=("arial", 16, "bold")).place(x=90, y=200)
        ent_passwd = Entry(Frame_login, textvariable=self.Password, font=("arial", 16),bg="lightgray", show="*").place(x=90, y=230,width=350,height=35)

        login_btn = Button(self.master, text="Log In", command=self.Login_System, width=16, bd=4, bg="#d77337",
                           fg="white", font="arial 16 bold").place(x=300, y=470,height=40,width=180)


    def Login_System(self):
        user = (self.Username.get())
        passwd = (self.Password.get())

        if (user == "" or passwd == ""):
            messagebox.showinfo("Login System", "Fill the Login Details")
        else:
            try:
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("select * from login where Username=%s and Passwd=%s", (user, passwd))
                row = cur.fetchone()
                if row == None:
                    messagebox.showinfo("Login System", "Invalid Login Details")
                    self.Username.set("")
                    self.Password.set("")

                else:
                    self.master.withdraw()
                    self.Login_Window()
            except Exception as er:
                messagebox.showerror("Error", f"Error Due to:{str(er)}")

    def Login_Window(self):
        self.loginWindow = Toplevel(self.master)
        self.app = DashBoard(self.loginWindow)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.loginWindow.destroy()
                self.master.destroy()
                DashBoard.truncate_order(self)

        self.loginWindow.protocol("WM_DELETE_WINDOW", on_closing)
        self.loginWindow.mainloop()



class DashBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("Hotel Management System")
        self.master.wm_iconbitmap("img/Coffee.ico")
        master.geometry("1366x700+0+0")

        def hmenu():
            hide_all_frames()
            mn_frame.pack(fill=BOTH, expand=1)

        def BillGen():
            hide_all_frames()
            billgen.pack(fill=BOTH, expand=1)

        def staff():
            hide_all_frames()
            emp_Mgmt_Frame.pack(fill=BOTH, expand=1)

        def setting():
            hide_all_frames()
            set_frame.pack(fill=BOTH, expand=1)

        def hide_all_frames():
            mn_frame.pack_forget()
            billgen.pack_forget()
            emp_Mgmt_Frame.pack_forget()
            set_frame.pack_forget()

        self.bg = PhotoImage(file="img/two.png")
        self.bg_image = Label(self.master, image=self.bg).place(x=0, y=0,relwidth=1, relheight=1)

        #####variables###
        self.Item_Category_var = StringVar()
        self.Item_Price_var = StringVar()
        self.Item_Name_var = StringVar()
        self.Item_No_var = StringVar()

        self.Search_By_var = StringVar()
        self.Search_var = StringVar()

        self.Cust_Name_var= StringVar()
        self.Cust_Contact_var = StringVar()

        self.menu_Category_var = StringVar()
        self.menu_Search_var = StringVar()
        self.BItem_Category_var = StringVar()
        self.BItem_Name_var = StringVar()
        self.BItem_Rate_var = StringVar()
        self.BItem_Quantity_var = StringVar()
        self.Total_Price_var = StringVar()
        self.bill_no_var=StringVar()
        x=random.randint(100,10000000)
        self.bill_no_var.set(x)


        title = Label(self.master, text="Hotel Sainath", relief=RAISED, bg="#234e70", fg="#fbf8be",
                      font=("Castellar", 30, "bold"), ).pack(fill=X)
        btnframe = Frame(self.master, width=300, height=650, bd=0, relief=GROOVE, bg="#234e70")
        btnframe.pack(side=LEFT)
        logo=Frame(self.master,bg="black")
        # logo.place(x=0,y=0,height=150,width=300)
        logo.place(x=0, y=0, height=150, width=300)

        self.hg = PhotoImage(file="img/mlogo.png")
        bg_image = Label(logo,image=self.hg)
        bg_image.place(x=0,y=0,relwidth=1,relheight=1)



        menu = Button(btnframe, text="Menu", command=hmenu, bd=2,relief=GROOVE,  bg="#fbf8be",fg="#234e70",
                      font=("Times new roman", 20)).place(x=0,y=130,width=300)


        staff= Button(btnframe, text="Employee\n\tManagement",anchor="w", command=staff, bd=2,relief=GROOVE, bg="#fbf8be",fg="#234e70",
                      font=("Times new roman", 20)).place(x=0,y=230,width=300)


        bill = Button(btnframe, text="Bill Generation", command=BillGen,bd=2,relief=GROOVE, bg="#fbf8be",fg="#234e70",
                      font=("Times new roman", 20,)).place(x=0,y=360,width=300)

        setting = Button(btnframe, text="Setting", command=setting, bd=2, relief=GROOVE, bg="#fbf8be",fg="#234e70",
                         font=("Times new roman", 20,)).place(x=0,y=460,width=300)

        log = Button(self.master, text="Logout", command=self.logout, bd=2, relief=GROOVE, bg="#fbf8be",fg="#234e70",
                         font=("Times new roman", 20,)).place(x=1270, y=0, width=100)

        self.CUsername= StringVar()
        self.CPassword = StringVar()
        set_frame = Frame(self.master,bd=4,relief=GROOVE,bg="lightgrey",height=700)
        bill_title = Label(set_frame, text="Setting", bg="#ffa871", fg="#722620", bd=5, relief=GROOVE,
                           font=("times new roman", 25, "bold")).pack(fill=X)
        create_usr=Frame(set_frame,bg="#e9e9ff")
        create_usr.place(x=300,y=50,height=300,width=400)
        bill_title = Label(create_usr, text="Create New User", bg="#cacaff", fg="#722620", bd=5, relief=GROOVE,anchor=W,
                           font=("times new roman", 20, )).pack(fill=X)
        cr_usr_lbl=Label(create_usr,text="Username :", fg="#d77337", bg="#e9e9ff", font=("arial", 16, "bold")).place(x=10,y=50)

        cr_ent_user = Entry(create_usr, textvariable=self.CUsername, font=("arial", 16), bg="lightgray").place(x=150,y=50)
        cr_lbl_passwd = Label(create_usr, text="Password:", height="1", fg="#d77337", bg="#e9e9ff",
                           font=("arial", 16, "bold")).place(x=10, y=100)
        self.ent_passwd = Entry(create_usr, textvariable=self.CPassword, font=("arial", 16), bg="lightgray", show="*")
        self.ent_passwd.place(x=150, y=100)

        add_btn = Button(create_usr, text="Add",  bd=4,command=self.add_usr, bg="#d77337",
                         fg="white", font="arial 16 bold").place(x=30, y=170, height=40, width=150)

        btn_clear = Button(create_usr, text="Clear", bd=4, bg="#d77337", command=self.clear_user,
                           fg="white", font="arial 16 bold").place(x=220, y=170,height=40, width=150)
        btn_update = Button(create_usr, text="Update", bd=4, bg="#d77337", command=self.update_user,
                            fg="white", font="arial 16 bold").place(x=30,y=220,height=40, width=150)
        btn_delete = Button(create_usr, text="Delete", bd=4, bg="#d77337", command=self.delete_user,
                            fg="white", font="arial 16 bold").place(x=220, y=220, height=40, width=150)




        #######menu######
        mn_frame = Frame(self.master,bd=4,relief=GROOVE,bg="lightgrey",height=700)
        # mn_frame.pack(fill="both", expand=1)

        title = Label(mn_frame, text="Menu", bd=5,bg="#ffa871",fg="#722620", relief=GROOVE, font=("times new roman", 25, "bold")).pack(fill=X)


        ########Manage_frame#########
        manage_frame = Frame(mn_frame, bd=1, bg="#e9e9ff", relief=GROOVE)
        manage_frame.place(x=5, y=50, height=590, width=400)
        m_title = Label(manage_frame, text="Manage Menu", font=("times new roman", 20, "bold"), bd=2, relief=RIDGE,
                        bg="#cacaff", fg="#722620",anchor=W).grid(row=0, columnspan=5, pady=10)

        lbl_item_no = Label(manage_frame, text="Item No.",fg="#d77337", bg="#e9e9ff",
                            font=("Times new roman", 18, "bold")).grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_item_no = Entry(manage_frame, textvariable=self.Item_No_var, font=("Times new roman", 16, "bold"),
                            bg="lightgrey").grid(row=1, column=1,
                                                 pady=10, padx=10, sticky="w")

        lbl_item = Label(manage_frame, text="Item Name", fg="#d77337", bg="#e9e9ff",
                         font=("Times new roman", 18, "bold")).grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_item = Entry(manage_frame, textvariable=self.Item_Name_var, font=("Times new roman", 16, "bold"),
                         bg="lightgrey").grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_price = Label(manage_frame, text="Price", fg="#d77337", bg="#e9e9ff",
                          font=("Times new roman", 18, "bold")).grid(row=3, column=0, pady=10, padx=10, sticky="w")
        txt_price = Entry(manage_frame, textvariable=self.Item_Price_var, font=("Times new roman", 16, "bold"),
                          bg="lightgray").grid(row=3, column=1,
                                               pady=10, padx=10, sticky="w")

        lbl_category = Label(manage_frame, text="Category", fg="#d77337", bg="#e9e9ff",
                             font=("Times new roman", 18, "bold")).grid(row=4, column=0, pady=10, padx=10, sticky="w")

        combo_category = ttk.Combobox(manage_frame, textvariable=self.Item_Category_var,
                                      font=("Times new roman", 13, "bold"), state="readonly")

        combo_category['values'] = (
        "Tea & Coffee", "Beverages", "Fast Food", "South Indian", "Starters", "Main Course", "Dessert")
        combo_category.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        ########Button_frame########
        button_frame = Frame(manage_frame, bd=1, bg="#e9e9ff", relief=GROOVE)
        button_frame.place(x=0, y=300, width=400, height=160)
        Addbtn = Button(button_frame, text="Add",  bg="#d77337",fg="white",font="arial 18 " , bd=4, relief=RAISED,
                        command=self.add_items).place(x=20,y=10,width=150)

        updatebtn = Button(button_frame, text="Update",  bg="#d77337",fg="white", bd=4,
                          font="arial 18 ", command=self.update_data).place(x=220,y=10,width=150)

        deletebtn = Button(button_frame, text="Delete", bg="#d77337",fg="white", bd=4,
                           font="arial 18 ", command=self.delete_data).place(x=20,y=70,width=150)
        clearbtn = Button(button_frame, text="Clear",  bg="#d77337",fg="white", bd=4,
                          font="arial 18 ", command=self.clear).place(x=220,y=70,width=150)

        #########Menu_Frame#########
        menu_frame = Frame(mn_frame, bd=1, bg="#e9e9ff", relief=RIDGE)
        menu_frame.place(x=410, y=50,height=700, width=640)

        lbl_search = Label(menu_frame, text="Search By",fg="#d77337", bg="#e9e9ff",
                           font=("Times new roman", 18, "bold")).grid(row=0, column=0, pady=10, padx=5, sticky="w")
        combo_category = ttk.Combobox(menu_frame, textvariable=self.Search_By_var, font=("Times new roman",),
                                      state="readonly",width=15)
        combo_category['values'] = ("Item_No", "Item_Name", "Item_Price", "Item_Category")
        combo_category.grid(row=0, column=1, padx=5,)
        txt_search = Entry(menu_frame, textvariable=self.Search_var, font=("Times new roman",),
                           bg="lightgrey", width=15).grid(row=0, column=2, padx=5)
        search_btn = Button(menu_frame, text="Search", width=10,bg="#d77337",fg="white", font=("Times new roman",),
                            command=self.search_data).grid(row=0, column=3, padx=5)
        showall_btn = Button(menu_frame, text="Show All", width=10, bg="#d77337",fg="white", font=("Times new roman",),
                             command=self.fetch_data).grid(row=0, column=4, padx=5)

        ##########table_frame########
        table_frame = Frame(menu_frame, bd=4, relief=RIDGE, bg="#e9e9ff")
        table_frame.place(x=10, y=70, width=650, height=524)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        style = ttk.Style()
        style.configure("mstyle.Treeview", bd=10, font=("Times new roman", 13))
        style.configure("mstyle.Treeview.Heading", bd=10, font=("Calibri", 15, "bold"))
        style.layout("mstyle.Treeview", [('mstyle.Treeview.treearea', {'sticky': 'NWES'})])
        self.menu_table = ttk.Treeview(table_frame, style="mstyle.Treeview",
                                       columns=("Item No.", "Item Name", "Item Price", "Category"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.menu_table.xview)
        scroll_y.config(command=self.menu_table.yview)
        self.menu_table.heading("Item No.", text="Item No.")
        self.menu_table.heading("Item Name", text="Item Name")
        self.menu_table.heading("Item Price", text="Item Price")
        self.menu_table.heading("Category", text="Category")
        self.menu_table['show'] = 'headings'
        self.menu_table.column("Item No.",width=85,  minwidth=50, anchor=CENTER)
        self.menu_table.column("Item Name",width=100, minwidth=90, anchor=CENTER)
        self.menu_table.column("Item Price",width=100,  minwidth=90, anchor=CENTER)
        self.menu_table.column("Category",width=100,  minwidth=90, anchor=CENTER)
        self.menu_table.pack(fill=BOTH, expand=1)

        self.menu_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


        ################################## Employee Management ########################################

        emp_Mgmt_Frame = Frame(self.master, bd=4, relief=GROOVE, bg="#e9e9ff", height=600)
        e_title = Label(emp_Mgmt_Frame, text="Employee Management",bg="#ffa871",fg="#722620", bd=5, relief=GROOVE, font=("times new roman", 25, "bold")).pack(fill=X)

        #######Variables#############
        self.emp_code_var = StringVar()
        self.designation_var = StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()
        self.dob_var = StringVar()
        self.doj_var = StringVar()
        self.salaryemp_var = StringVar()
        self.contact_var = StringVar()

        self.emp_s_code_var = StringVar()
        self.month_var = StringVar()
        self.year_var = StringVar()
        self.salary_var = StringVar()
        self.days_var = StringVar()
        self.absent_var = StringVar()
        self.medical_var = StringVar()
        self.pf_var = StringVar()
        self.convence_var = StringVar()
        self.net_salary_var = StringVar()

        Frame1 = Frame(emp_Mgmt_Frame, bd=1, relief=RIDGE, bg="#e9e9ff")
        Frame1.place(x=0, y=50, width=620, height=592)

        title2 = Label(Frame1, text="Employee Details", font=("calibri", 25, "bold"), bd=2, relief=RIDGE, bg="#cacaff",
                       fg="#722620",  anchor=W, padx=10).place(x=0, y=0, relwidth=1)


        lbl_code = Label(Frame1, text="Employee Code", font=("calibri", 15), fg="#d77337", bg="#e9e9ff").place(x=2, y=60)

        self.txt_code = Entry(Frame1, font=("calibri", 15), bg="lightgrey", textvariable=self.emp_code_var)
        self.txt_code.place(x=170, y=65, width=110)
        btn_cSearch = Button(Frame1, text="Search", font=("calibri", 14),bg="#d77337",fg="white",
                             command=self.search_emp).place(x=320, y=55, width=150)

        # r1
        lbl_designation = Label(Frame1, text="Designation ", font=("calibri", 16),fg="#d77337", bg="#e9e9ff"
                                ).place(x=5, y=110)
        txt_designation = Entry(Frame1, font=("calibri", 14), bg="lightgrey", textvariable=self.designation_var).place(
            x=140, y=115, width=150)

        lbl_name = Label(Frame1, text="Name ", font=("calibri", 16), fg="#d77337", bg="#e9e9ff"
                         ).place(x=350, y=110)
        txt_name = Entry(Frame1, font=("calibri", 14), bg="lightgrey", textvariable=self.name_var).place(x=460, y=115,
                                                                                                         width=150)

        # r2
        lbl_age = Label(Frame1, text="Age ", font=("calibri", 16), fg="#d77337", bg="#e9e9ff",
                        ).place(x=5, y=150)
        txt_age = Entry(Frame1, font=("calibri", 14), bg="lightgrey", textvariable=self.age_var).place(x=140, y=155,
                                                                                                       width=150)

        lbl_doj = Label(Frame1, text="D.O.J ", font=("calibri", 16), fg="#d77337", bg="#e9e9ff"
                        ).place(x=350, y=150)
        txt_doj = DateEntry(Frame1, font=("calibri", 14), bg="lightgrey",format="%d-%b-%Y",
                            textvariable=self.doj_var).place(x=460, y=155, width=150)

        # r3
        lbl_gender = Label(Frame1, text="Gender ", font=("calibri", 16),fg="#d77337", bg="#e9e9ff",
                           ).place(x=5, y=190)
        combo_gender = ttk.Combobox(Frame1, font=("calibri", 14), state="readonly", textvariable=self.gender_var)
        combo_gender['values'] = ("Male", "Female")
        combo_gender.place(x=140, y=195, width=150)

        lbl_salary = Label(Frame1, text="Salary ", font=("calibri", 16), fg="#d77337", bg="#e9e9ff",
                           ).place(x=350, y=190)
        txt_salary = Entry(Frame1, font=("calibri", 14), bg="lightgrey", textvariable=self.salaryemp_var).place(
            x=460, y=195, width=150)

        # r4
        lbl_email = Label(Frame1, text="Email ", font=("calibri", 16), fg="#d77337", bg="#e9e9ff"
                          ).place(x=5, y=230)
        txt_email = Entry(Frame1, font=("calibri", 14), bg="lightgrey", textvariable=self.email_var).place(x=140, y=235,
                                                                                                           width=150)

        lbl_contact = Label(Frame1, text="Conatact ", font=("calibri", 16), fg="#d77337", bg="#e9e9ff"
                            ).place(x=350, y=230)
        txt_contact = Entry(Frame1, font=("calibri", 14), bg="lightgrey", textvariable=self.contact_var).place(x=460,
                                                                                                 y=235, width=150)
        # r6
        lbl_addrees = Label(Frame1, text="Address ", font=("calibri", 16), fg="#d77337", bg="#e9e9ff"
                            ).place(x=5, y=270)
        self.txt_address = Text(Frame1, font=("calibri", 14), bg="lightgrey")
        self.txt_address.place(x=140, y=275, width=470, height=70)


        self.btn_save = Button(Frame1, text="Save", font=("calibri", 14),  bg="#d77337",fg="white",
                               command=self.add_emp)
        self.btn_save.place(x=50, y=355, width=100)
        btn_clear = Button(Frame1, text="Clear", font=("calibri", 14), bg="#d77337",fg="white",
                           command=self.clear_emp).place( x=200, y=355, width=100)
        self.btn_update = Button(Frame1, text="Update", font=("calibri", 14), bg="#d77337", fg="white", command=self.update_emp,
                                 )
        self.btn_update.place(x=350, y=355, width=100)
        self.btn_delete = Button(Frame1, text="Delete", font=("calibri", 14), bg="#d77337", fg="white",
                                 command=self.delete_emp )
        self.btn_delete.place(x=500, y=355, width=100)

        emp_detail_table_frame=Frame(Frame1,bg="#e9e9ff")
        emp_detail_table_frame.place(x=0,y=410,height=190,width=617)

        title = Label(emp_detail_table_frame, text="Employee Detail", bd=1, bg="#cacaff", fg="#722620",
                      font=("times new roman", 15, "bold") ).pack(fill=X)

        scroll_x = Scrollbar(emp_detail_table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(emp_detail_table_frame, orient=VERTICAL)

        self.emp_table = ttk.Treeview(emp_detail_table_frame, columns=( "e_id", "designation", "name", "age", "gender",
        "email", "doj", "salary", "contact", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)
        self.emp_table.heading("e_id", text="Emp ID")
        self.emp_table.heading("designation", text="Designation")
        self.emp_table.heading("name", text="Name")
        self.emp_table.heading("age", text="Age")
        self.emp_table.heading("gender", text="Gender")
        self.emp_table.heading("email", text="Email")
        self.emp_table.heading("doj", text="DOJ")
        self.emp_table.heading("salary", text="Salary")
        self.emp_table.heading("contact", text="Contact")
        self.emp_table.heading("address", text="Address")
        self.emp_table["show"] = "headings"

        self.emp_table.column("e_id",width=50, anchor=CENTER)
        self.emp_table.column("designation",width=100, anchor=CENTER)
        self.emp_table.column("name",width=100, anchor=CENTER)
        self.emp_table.column("age", width=50,anchor=CENTER)
        self.emp_table.column("gender", width=50,anchor=CENTER)
        self.emp_table.column("email", width=150,anchor=CENTER)
        self.emp_table.column("doj", width=50,anchor=CENTER)
        self.emp_table.column("salary", width=100,anchor=CENTER)
        self.emp_table.column("contact", width=100,anchor=CENTER)
        self.emp_table.column("address", width=200,anchor=CENTER)
        self.emp_table.pack(fill=BOTH, expand=1)

        self.emp_table.bind("<ButtonRelease-1>", self.load_emp_data)
        self.show_emp_data()


        Frame2 = Frame(emp_Mgmt_Frame, bd=1, relief=RIDGE, bg="#e9e9ff")
        Frame2.place(x=620, y=50, width=440, height=303)

        title2 = Label(Frame2, text="Salary Details", font=("calibri", 18, "bold"), bd=2, relief=RIDGE,
                       bg="#cacaff", fg="#722620", anchor=W, padx=10).place(x=0, y=0, relwidth=1)
        self.btn_show_emp = Button(Frame2, text="Salary Records", font=("calibri", 12), bg="grey", fg="white",
                                   command=self.salary_record)
        self.btn_show_emp.place(x=325, y=0)
        lbl_s_code = Label(Frame2, text="Employee Code", font=("calibri", 15), fg="#d77337", bg="#e9e9ff"
                           ).place(x=2, y=40)

        self.txt_s_code = Entry(Frame2, font=("calibri", 15), bg="lightgrey", textvariable=self.emp_s_code_var)
        self.txt_s_code.place(x=170, y=45, width=110)
        btn_s_cSearch = Button(Frame2, text="Search", font=("calibri", 13), bg="#d77337",fg="white",
                             command=self.search_sal_record).place(x=320, y=40, width=100)

        lbl_month = Label(Frame2, text="Month", font=("calibri", 15), fg="#d77337", bg="#e9e9ff").place(x=0, y=90)
        combo_month = ttk.Combobox(Frame2, font=("calibri", 13), state="readonly", textvariable=self.month_var)
        combo_month['values'] = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        combo_month.place(x=70, y=95, width=80)


        lbl_year = Label(Frame2, text="Year", font=("calibri", 15), fg="#d77337", bg="#e9e9ff",).place(x=170, y=90)

        txt_year = Entry(Frame2, font=("calibri", 13), bg="lightgrey", textvariable=self.year_var).place(x=220, y=95,
                                                                                                         width=80)
        lbl_absent = Label(Frame2, text="Absent", font=("calibri", 15), fg="#d77337", bg="#e9e9ff").place(x=320, y=90)
        spin_absent = Spinbox(Frame2,font=("calibri", 13), bg="lightgrey", textvariable=self.absent_var,
                              from_=0,to=31).place(x=385,y=95,width=40)

        lbl_salary = Label(Frame2, text="Salary", font=("calibri", 15),fg="#d77337", bg="#e9e9ff").place(x=0, y=130)
        txt_salary = Entry(Frame2, font=("calibri", 13), bg="lightgrey", textvariable=self.salary_var).place(x=70,
                                                                                             y=135, width=120)

        lbl_days = Label(Frame2, text="Total Days", font=("calibri", 15), fg="#d77337", bg="#e9e9ff").place(x=220, y=130)

        spin_tdays = Spinbox(Frame2, font=("calibri", 13), bg="lightgrey", textvariable=self.days_var,
                              from_=0, to=31).place(x=320, y=135,width=100)
        self.days_var.set(30)

        lbl_medical = Label(Frame2, text="Medical", font=("calibri", 15), fg="#d77337", bg="#e9e9ff").place(x=0, y=170)
        txt_medical = Entry(Frame2, font=("calibri", 13), bg="lightgrey", textvariable=self.medical_var).place(x=100,
                                                                                                   y=175, width=100)
        lbl_pf = Label(Frame2, text="PF", font=("calibri", 15),fg="#d77337", bg="#e9e9ff").place(x=250, y=170)
        txt_pf = Entry(Frame2, font=("calibri", 13), bg="lightgrey", textvariable=self.pf_var).place(x=320, y=175,
                                                                                                     width=100)

        lbl_covence = Label(Frame2, text="Convence", font=("calibri", 15), fg="#d77337", bg="#e9e9ff").place(x=0, y=210)
        txt_convence = Entry(Frame2, font=("calibri", 13), bg="lightgrey", textvariable=self.convence_var).place(x=100,
                                                                                                      y=215, width=100)

        lbl_netsalary = Label(Frame2, text="Net Salary", font=("calibri", 15), fg="#d77337", bg="#e9e9ff"
                              ).place(x=220, y=210)
        txt_netsalary = Entry(Frame2, font=("calibri", 13), bg="lightgrey", textvariable=self.net_salary_var,
                              state=DISABLED).place(x=320, y=215, width=100)

        btn_calculate = Button(Frame2, text="Calculate", font=("calibri", 13), bg="#d77337",fg="white",
                               command=self.calculate).place(x=0, y=255,
                                                             width=80)
        self.btn_sal_save = Button(Frame2, text="Save", font=("calibri", 13), bg="#d77337",fg="white",
                                   command=self.add_sal_record)
        self.btn_sal_save.place(x=90, y=255, width=80)
        btn_clear = Button(Frame2, text="Clear", font=("calibri", 13), bg="#d77337",fg="white",
                           command=self.clear_sal_record).place(x=180, y=255, width=80)
        self.btn_sal_update = Button(Frame2, text="Update", font=("calibri", 13), bg="#d77337",fg="white",
                                     command=self.update_sal_record)
        self.btn_sal_update.place(x=270, y=255, width=80)
        self.btn_sal_delete = Button(Frame2, text="Delete", font=("calibri", 13), bg="#d77337",fg="white",
                                     command=self.delete_sal_record)
        self.btn_sal_delete.place(x=360, y=255, width=80)

        Frame3 = Frame(emp_Mgmt_Frame, bd=1, relief=RIDGE, bg="#e9e9ff")
        Frame3.place(x=620, y=352, width=440, height=293)

        self.salary_slip = f'''\t\tHotel Sainath \n\t\t  Vaithiwadi,\n\t\t   Thane(W)
\n\t\t  Salary Slip 
--------------------------------------------------------------------
Employee ID\t\t:  	
Salary Of\t\t:  Mon-YYYY	
Generated On\t\t:  DD-MM-YYYY HH:MM:SS
--------------------------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Basic Salary\t\t:  Rs.______/-
Convence\t\t:  Rs.______/-
Medical\t\t:  Rs.______/-
PF\t\t:  Rs.______/-
Net Salary\t\t:  Rs.______/
--------------------------------------------------------------------
        '''

        title3 = Label(Frame3, text="Salary Reciept", font=("calibri", 20, "bold"), bd=2, relief=RIDGE,
                        anchor=W, padx=10, bg="#cacaff", fg="#722620",).place(x=0, y=0, relwidth=1)
        sal_frame = Frame(Frame3, bg="#e9e9ff")
        sal_frame.place(x=0, y=40, width=430, height=210)

        scroll_sal_y = Scrollbar(sal_frame, orient=VERTICAL)
        scroll_sal_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_reciept = Text(sal_frame, font=("calibri", 15,), bg="lightgrey",
                                       yscrollcommand=scroll_sal_y.set)

        scroll_sal_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.pack(fill=BOTH, expand=1)
        self.txt_salary_reciept.insert(END, self.salary_slip)

        self.btn_print = Button(Frame3, text="Print", font=("calibri", 13), bg="#d77337",fg="white", bd=2,
                                command=self.print_emp_sal,
                                relief=RIDGE, state=DISABLED)
        self.btn_print.place(x=170, y=255, width=100)


        ################################# BillGen ####################################################

        billgen = Frame(self.master, bd=4, relief=GROOVE, bg="#e9e9ff",height=700)


        #######Customer########
        bill_title = Label(billgen,text="Bill Generation",bg="#ffa871",fg="#722620", bd=5, relief=GROOVE, font=("times new roman", 25, "bold")
                           ).pack(fill=X)
        cust_frame =LabelFrame(billgen, text="Customer Details", font=("times new roman", 15, "bold"),
                                bd=8, bg="#cacaff", fg="#722620", relief=GROOVE)
        cust_frame.pack(side=TOP, fill="x")

        cust_name_lbl = Label(cust_frame, text="Name",
                              font=("arial", 15, "bold"), fg="#d77337", bg="#cacaff")
        cust_name_lbl.grid(row=0, column=0)

        cust_name_txt = Entry(cust_frame, width=20, font="arial 15", bd=5, textvariable=self.Cust_Name_var)
        cust_name_txt.grid(row=0, column=1, padx=50)

        cust_contact_lbl = Label(cust_frame, text="Contact", font=("arial", 15, "bold"), fg="#d77337", bg="#cacaff")
        cust_contact_lbl.grid(row=0, column=2)

        cust_contact_txt = Entry(cust_frame, width=20, font="arial 15", bd=5, textvariable=self.Cust_Contact_var)
        cust_contact_txt.grid(row=0, column=3, padx=50)

        ###########Menu#############
        menu_frame = Frame(billgen, bd=1, bg="#e9e9ff", relief=GROOVE)
        menu_frame.place(x=0, y=118, height=522, width=600)

        menu_label = Label(menu_frame, text="Menu",
                           font=("times new roman", 20, "bold"), bg="#cacaff", fg="#722620", pady=0)
        menu_label.pack(side=TOP, fill="x")

        menu_category_frame = Frame(menu_frame, bg="#e9e9ff", pady=10)
        menu_category_frame.pack(fill="x")

        combo_lable = Label(menu_category_frame, text="Search By",
                            font=("arial", 12, "bold"), fg="#d77337", bg="#e9e9ff",)
        combo_lable.grid(row=0, column=0, padx=1)

        combo_menu = ttk.Combobox(menu_category_frame, textvariable=self.menu_Category_var, state="readonly")
        combo_menu['values'] = ("Item_No", "Item_Name", "Item_Price", "Item_Category")
        combo_menu.grid(row=0, column=1, padx=5)
        txt_csearch = Entry(menu_category_frame, textvariable=self.menu_Search_var, font=("arial", 12, "bold"),
                            bg="lightgrey").grid(row=0,
                                                 column=2, padx=5)

        show_button = Button(menu_category_frame, text="Show", width=9,bg="#d77337",fg="white",
                                 command=self.show_button_operation)
        show_button.grid(row=0, column=3, padx=5)
        show_all_button = Button(menu_category_frame, text="Show All", width=9,bg="#d77337",fg="white",
                                     command=self.bill_fetch_data)
        show_all_button.grid(row=0, column=4)

        ############### Menu Tabel ##############
        menu_table_frame = Frame(menu_frame,bg="#e9e9ff")
        menu_table_frame.pack(fill=BOTH, expand=1)

        scrollbar_menu_x = Scrollbar(menu_table_frame, orient=HORIZONTAL)
        scrollbar_menu_y = Scrollbar(menu_table_frame, orient=VERTICAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15, "bold"))
        style.configure("Treeview", font=("arial", 12), rowheight=25)

        self.menu_table1 = ttk.Treeview(menu_table_frame, style="Treeview",
                                        columns=("Item No.", "Item Name", "Item Price", "Item Category"),
                                        xscrollcommand=scrollbar_menu_x.set,
                                        yscrollcommand=scrollbar_menu_y.set)
        self.menu_table1.heading("Item No.", text="Item No.")
        self.menu_table1.heading("Item Name", text="Item Name")
        self.menu_table1.heading("Item Price", text="Item Price")

        self.menu_table1["displaycolumns"] = ("Item No.", "Item Name", "Item Price")
        self.menu_table1["show"] = "headings"
        self.menu_table1.column("Item No.", width=50, anchor='center')
        self.menu_table1.column("Item Name", width=200, anchor='center')
        self.menu_table1.column("Item Price", width=50, anchor='center')

        scrollbar_menu_x.pack(side=BOTTOM, fill=X)
        scrollbar_menu_y.pack(side=RIGHT, fill=Y)

        scrollbar_menu_x.configure(command=self.menu_table1.xview)
        scrollbar_menu_y.configure(command=self.menu_table1.yview)

        self.menu_table1.pack(fill=BOTH, expand=1)

        self.bill_fetch_data()
        self.menu_table1.bind("<ButtonRelease-1>", self.load_item_from_menu)

        ########Item Frame#########
        item_frame = Frame(billgen, bd=2, bg="#e9e9ff", relief=GROOVE)
        item_frame.place(x=602, y=118, height=230, width=455)

        item_title_label = Label(item_frame, text="Item",
                                 font=("times new roman", 20, "bold"), bd=2, relief=RIDGE,  bg="#cacaff", fg="#722620")
        item_title_label.pack(side=TOP, fill=X)

        item_frame2 = Frame(item_frame, bg="#e9e9ff")
        item_frame2.pack(fill=X)

        item_name_label = Label(item_frame2, text="Name",
                                font=("arial", 12, "bold"), fg="#d77337", bg="#e9e9ff")
        item_name_label.grid(row=0, column=0,  pady=30)

        item_name = Entry(item_frame2, font="arial 10", textvariable=self.BItem_Name_var, state=DISABLED, width=20)
        item_name.grid(row=0, column=1, padx=1, pady=30)

        item_rate_label = Label(item_frame2, text="Rate",
                                font=("arial", 12, "bold"), fg="#d77337", bg="#e9e9ff")
        item_rate_label.grid(row=0, column=2, padx=10, pady=30)

        item_rate = Entry(item_frame2, font="arial 12", textvariable=self.BItem_Rate_var, state=DISABLED, width=8)
        item_rate.grid(row=0, column=3, padx=5, pady=30)

        item_quantity_label = Label(item_frame2, text="Quantity",
                                    font=("arial", 12, "bold"), fg="#d77337", bg="#e9e9ff")
        item_quantity_label.grid(row=1, column=0, padx=30, pady=5)

        item_quantity = Entry(item_frame2, font="arial 12", textvariable=self.BItem_Quantity_var, width=10)
        item_quantity.grid(row=1, column=1, padx=0, pady=5)

        item_frame3 = Frame(item_frame, bg="#e9e9ff")
        item_frame3.pack(fill=X)

        add_button = Button(item_frame3, text="Add Item", command=self.add_button_operation)
        add_button.grid(row=0, column=0, padx=40, pady=15)

        remove_button = Button(item_frame3, text="Remove Item", command=self.remove_button_operation)
        remove_button.grid(row=0, column=1, padx=30, pady=15)

        update_button = Button(item_frame3, text="Update Quantity", command=self.update_button_operation)
        update_button.grid(row=0, column=2, padx=30, pady=15)

        clear_button = Button(item_frame3, text="Clear", width=15, command=self.clear_button_operation)
        clear_button.grid(row=0, column=3, padx=30, pady=15)

        ############Order Frame###########
        order_frame = Frame(billgen, bd=2, bg="#e9e9ff", relief=GROOVE)
        order_frame.place(x=602, y=350, height=292, width=455)

        order_title_label = Label(order_frame, text="Your Order",
                                  font=("times new roman", 20, "bold"),  bg="#cacaff", fg="#722620")
        order_title_label.pack(side=TOP, fill="x")

        ############# Order Tabel ##############
        order_tabel_frame = Frame(order_frame,bg="#e9e9ff")
        order_tabel_frame.place(x=0, y=40, height=190, width=450)

        scrollbar_order_x = Scrollbar(order_tabel_frame, orient=HORIZONTAL)
        scrollbar_order_y = Scrollbar(order_tabel_frame, orient=VERTICAL)

        self.order_tabel = ttk.Treeview(order_tabel_frame,
                                   columns=("Name", "Rate", "Quantity", "Price", "Category"),
                                   xscrollcommand=scrollbar_order_x.set,
                                   yscrollcommand=scrollbar_order_y.set)


        self.order_tabel.heading("Name", text="Name")
        self.order_tabel.heading("Rate", text="Rate")
        self.order_tabel.heading("Quantity", text="Quantity")
        self.order_tabel.heading("Price", text="Price")
        self.order_tabel["displaycolumns"] = ("Name", "Rate", "Quantity", "Price")
        self.order_tabel["show"] = "headings"

        self.order_tabel.column("Name", width=145, anchor='center', stretch=NO)
        self.order_tabel.column("Rate", width=85, anchor='center', stretch=NO)
        self.order_tabel.column("Quantity", width=100, anchor='center', stretch=NO)
        self.order_tabel.column("Price", width=100, anchor='center', stretch=NO)

        self.order_tabel.bind("<ButtonRelease-1>",self.load_item_from_order)


        scrollbar_order_x.pack(side=BOTTOM, fill=X)
        scrollbar_order_y.pack(side=RIGHT, fill=Y)

        scrollbar_order_x.configure(command=self.order_tabel.xview)
        scrollbar_order_y.configure(command=self.order_tabel.yview)

        self.order_tabel.pack(fill=BOTH, expand=1)


        ###########################################################################################

        total_price_label = Label(order_frame, text="Total Price",
                                  font=("arial", 12, "bold"), fg="#d77337", bg="#e9e9ff",)
        total_price_label.pack(side=LEFT, anchor=SW, padx=10, pady=10)

        total_price_entry = Entry(order_frame, font="arial 12", textvariable=self.Total_Price_var, state=DISABLED,
                                  width=15)
        total_price_entry.pack(side=LEFT, anchor=SW, padx=0, pady=10)

        bill_button = Button(order_frame, text="Bill", bg="#d77337",fg="white",width=10,command=self.print_bill)

        bill_button.pack(side=LEFT, anchor=SW, padx=10, pady=10)

        cancel_button = Button(order_frame, text="Cancel Order",bg="#d77337",fg="white", width=15, command=self.cancel_button_operation)
        cancel_button.pack(side=LEFT, anchor=SW, padx=10, pady=10)
        self.load_order()


    def add_items(self):
        ini = self.Item_No_var.get()
        itn = self.Item_Name_var.get()
        itp = self.Item_Price_var.get()
        itc = self.Item_Category_var.get()
        try:
            if ini == "" or itn == "" or itp == "" or itc == "":
                messagebox.showerror("Error", "ALl fields are required!!!")
            elif not ini.isdigit() or itn.isdigit() or not itp.isdigit():
                messagebox.showerror("Error","Enter valid Data")
            else:
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("select * from menu where Item_Name=%s", self.Item_Name_var.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Item is already present")
                else:
                    con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                    cur = con.cursor()
                    cur.execute("insert into menu values (%s,%s,%s,%s)", (ini, itn, itp, itc))
                    con.commit()
                    self.fetch_data()
                    con.close()
                    messagebox.showinfo("Success", "Item successfully added")
                    self.clear()

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("select * from menu")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.menu_table.delete(*self.menu_table.get_children())
            for row in rows:
                self.menu_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Item_No_var.set("")
        self.Item_Name_var.set("")
        self.Item_Price_var.set("")
        self.Item_Category_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.menu_table.focus()
        contents = self.menu_table.item(cursor_row)
        row = contents['values']
        self.Item_No_var.set(row[0])
        self.Item_Name_var.set(row[1])
        self.Item_Price_var.set(row[2])
        self.Item_Category_var.set(row[3])

    def update_data(self):
        ini = self.Item_No_var.get()
        itn = self.Item_Name_var.get()
        itp = self.Item_Price_var.get()
        itc = self.Item_Category_var.get()
        try:
            if ini == "" or itn == "" or itp == "" or itc == "":
                messagebox.showerror("Error", "ALl fields are required!!!")

            else:
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("update menu set Item_Name=%s,Item_Price=%s,Item_Category=%s where Item_No=%s",
                            (self.Item_Name_var.get(),
                             self.Item_Price_var.get(),
                             self.Item_Category_var.get(),
                             self.Item_No_var.get()
                             ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")


    def delete_data(self):
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("delete from menu where Item_No=%s", self.Item_No_var.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def search_data(self):
        if self.Search_By_var.get() == "" or self.Search_var.get() == "":
            messagebox.showerror("Error", "Please select something to search")
        else:
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from menu where " + str(self.Search_By_var.get()) + " LIKE '%" + str(
                self.Search_var.get()) + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.menu_table.delete(*self.menu_table.get_children())
                for row in rows:
                    self.menu_table.insert('', END, values=row)
                con.commit()
                con.commit()
                self.sclear()
            con.close()

    def sclear(self):
        self.Search_By_var.set("")
        self.Search_var.set("")

        ###############################################################################################################

    def bill_fetch_data(self):
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("select * from menu")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.menu_table1.delete(*self.menu_table1.get_children())
            for row in rows:
                self.menu_table1.insert('', END, values=row)
            con.commit()
        con.close()

    def show_button_operation(self):
        if self.menu_Category_var.get() == "" or self.menu_Search_var.get() == "":
            messagebox.showerror("Error", "Please select something to search")
        else:
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from menu where " + str(self.menu_Category_var.get()) + " LIKE '%" + str(
                self.menu_Search_var.get()) + "%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.menu_table1.delete(*self.menu_table1.get_children())
                for row in rows:
                    self.menu_table1.insert('', END, values=row)
                con.commit()
                self.sclear()
            con.close()

    def load_item_from_order(self,event):
        cursor_row = self.order_tabel.focus()
        contents = self.order_tabel.item(cursor_row)
        row = contents["values"]
        self.BItem_Name_var.set(row[0])
        self.BItem_Rate_var.set(row[1])
        self.BItem_Quantity_var.set(row[2])



    def load_order(self):
        self.order_tabel.delete(*self.order_tabel.get_children())
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("SELECT * FROM `order`")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.order_tabel.delete(*self.order_tabel.get_children())
            for row in rows:
                self.order_tabel.insert('', END, values=row)
            con.commit()
        con.close()
        self.update_total_price()

    def add_button_operation(self):
        name =self.BItem_Name_var.get()
        rate = self.BItem_Rate_var.get()
        category = self.BItem_Category_var.get()
        quantity = self.BItem_Quantity_var.get()

        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("SELECT Name FROM `order`")
        order = cur.fetchall()
        for i in order:
            if name in i:
                messagebox.showinfo("Error", "Item already exist in your order")
                return
        if not quantity.isdigit():
            messagebox.showinfo("Error", "Please Enter Valid Quantity")
            return
        else:
            price = str(int(float(rate)) * int(quantity))
            cur.execute("INSERT INTO `order`(`Name`, `Rate`, `Quantity`, `Price`) VALUES (%s,%s,%s,%s)", (name,rate,quantity,price))
            con.commit()
        con.close()
        self.load_order()

    def load_item_from_menu(self,ev):
        cursor_row = self.menu_table1.focus()
        contents = self.menu_table1.item(cursor_row)
        row = contents["values"]

        self.BItem_Name_var.set(row[1])
        self.BItem_Rate_var.set(row[2])
        self.BItem_Category_var.set(row[3])
        self.BItem_Quantity_var.set("1")


    def clear_button_operation(self):
        self.BItem_Name_var.set("")
        self.BItem_Rate_var.set("")
        self.BItem_Quantity_var.set("")


    def cancel_button_operation(self):
        # try:
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("SELECT * FROM `order`")
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Your order list is Empty")
            else:
                op = messagebox.askquestion("Cancel Order", "Are You Sure to Cancel Order?")
                if op == "no":
                    return
                cur.execute("TRUNCATE `order`")
                con.commit()
                con.close()
                self.clear_button_operation()
                self.update_total_price()
                self.load_order()
            self.Total_Price_var.set("")

    def update_button_operation(self):
        name = self.BItem_Name_var.get()
        rate = self.BItem_Rate_var.get()
        category = self.BItem_Category_var.get()
        quantity = self.BItem_Quantity_var.get()
        price = str(int(float(rate)) * int(quantity))
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("SELECT Name FROM `order`")
        order = cur.fetchall()
        if not quantity.isdigit():
            messagebox.showerror("Error","Please select valid quantity")
        else:
            cur.execute("update `order` set Quantity=%s,Price=%s where Name=%s",(quantity,price,name))
            con.commit()
        con.close()
        self.load_order()


    def remove_button_operation(self):
        try:
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from `order` where name=%s", self.BItem_Name_var.get())
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Item not present in your list")
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete ?")
                if op == True:
                    cur.execute("delete from `order` where Name=%s", self.BItem_Name_var.get())
                    con.commit()
                    con.close()
                    self.load_order()
                    messagebox.showinfo("Delete", "Item Removed")

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")


    def update_total_price(self):
        self.price = 0
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("SELECT SUM(Price) FROM `order`")
        self.rows = (cur.fetchall()[0][0])
        self.price =self.rows
        if self.rows == 0:
            self.Total_Price_var.set("")
        else:
            self.Total_Price_var.set("Rs. " +str(self.price) + " /-")

    def truncate_order(self):
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("TRUNCATE `order`")
        con.commit()
        con.close()
        # self.clear_button_operation()
        # self.update_total_price()
        # self.load_order()


    def print_bill(self):
        customer_name = self.Cust_Name_var.get()
        customer_contact = self.Cust_Contact_var.get()
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("SELECT * FROM `order`")
        rows = cur.fetchall()
        con.commit()


        if len(rows) == 0:
            messagebox.showerror("Error", "Your order list is Empty")
            return
        if customer_name == "" or customer_contact == "":
            messagebox.showinfo("Error", "Customer Details Required")
            return
        if not self.Cust_Contact_var.get().isdigit() or not len(self.Cust_Contact_var.get())==10:
            messagebox.showinfo("Error", "Invalid Customer Contact")
            return
        if customer_name.isdigit():
            messagebox.showinfo("Error","Please Enter valid Customer Name")
            return
        self.a=datetime.datetime.today()
        time=self.a.strftime("%d-%b-%Y %H:%M:%S")
        ans = messagebox.askquestion("Generate Bill", "Are You Sure to Generate Bill?")
        if ans == "yes":
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=25)
            pdf.cell(200, 8,  txt="Hotel Sainath",
                     ln=1, align='C')
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 8,  txt="Vaitywadi",
                     ln=1, align='C')
            pdf.cell(200, 8, txt="Thane (W)",
                     ln=1, align='C')
            pdf.cell(300, 15,
                     txt="----------------------------------------------- INVOICE -------------------------------------------------",
                     ln=1)
            pdf.cell(120, 10, txt="Bill Number : " + str(self.bill_no_var.get()),
                     ln=0)
            pdf.cell(100, 10, txt="Phone Number : " + str(self.Cust_Contact_var.get()),
                     ln=1)
            pdf.cell(120, 10, txt="Customer Name : " + str(self.Cust_Name_var.get()),
                     ln=0)
            pdf.cell(100, 10, txt=("Date : " + str(time)),
                     ln=1)

            pdf.cell(300, 1,
                     txt="--------------------------------------------------------------------------------------------------------------",
                     ln=1)
            pdf.cell(50, 10, txt="Name", ln=0,align="C")
            pdf.cell(50, 10, txt="Rate", ln=0,align="C")
            pdf.cell(50, 10, txt="Quantity", ln=0,align="C")
            pdf.cell(50, 10, txt="Price", ln=1,align="C")
            pdf.cell(300, 1,
                     txt="--------------------------------------------------------------------------------------------------------------",
                     ln=1)
            for line in self.order_tabel.get_children():

                for value in self.order_tabel.item(line)['values']:
                    pdf.set_font_size(12)
                    pdf.cell(50, 10, txt=f"{value}", align="C",
                             ln=0)
                pdf.cell(1, 8, ln=1)

            pdf.set_font_size(15)
            pdf.cell(300, 1,
                     txt="--------------------------------------------------------------------------------------------------------------",
                     ln=1)
            pdf.cell(120, 10,
                     ln=0)
            pdf.cell(100, 10, txt="Total Amount : " + str(self.Total_Price_var.get()),
                     ln=1)

            pdf.cell(300, 1,
                     txt="--------------------------------------------------------------------------------------------------------------",
                     ln=1)
            pdf.cell(200, 10, txt="Thank You!!!",align="C",
                     ln=1)
            pdf.cell(200, 10, txt="Visit Again!!!", align="C",
                     ln=1)

            pdf.cell(100, 10, txt="Printed At : "+str(platform.uname().node),
                     ln=1)

            pdf.cell(300, 1,  
                     txt="--------------------------------------------------------------------------------------------------------------",
                     ln=1 )

            pdf.output("Bill_Record\ "+str(self.bill_no_var.get())+".pdf")
            wb.open_new(r"Bill_Record\ "+str(self.bill_no_var.get())+".pdf")
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            self.bill_record()
            cur.execute("TRUNCATE `order`")
            self.load_order()
            con.commit()
            con.close()

        else:
            return True

    def bill_record(self):
        time=self.a.strftime("%Y-%m-%d %H:%M:%S")
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("SELECT SUM(Price) FROM `order`")
        rows = (cur.fetchall()[0][0])
        cur.execute("INSERT INTO `bill` values (%s,%s,%s,%s,%s)", (self.bill_no_var.get(),self.Cust_Name_var.get(),self.Cust_Contact_var.get(),rows,time))
        con.commit()
        con.close()


    ######Employee Management #####

    def add_sal_record(self):
        # try:
            if self.emp_s_code_var.get() == "" or self.net_salary_var.get() == "" :
                messagebox.showerror("Error", "All details are required")
            elif not self.medical_var.get().isdigit() or not self.pf_var.get().isdigit()  or not self.convence_var.get().isdigit() or not self.salary_var.get().isdigit():
                messagebox.showerror("Error", "Enter valid Data")
            else:
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("insert into sal_record values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.emp_s_code_var.get(),
                                                                                                   self.month_var.get(),
                                                                                                   self.year_var.get(),
                                                                                                   self.salary_var.get(),
                                                                                                   self.days_var.get(),
                                                                                                   self.absent_var.get(),
                                                                                                   self.pf_var.get(),
                                                                                                   self.medical_var.get(),
                                                                                                   self.convence_var.get(),
                                                                                                   self.net_salary_var.get(),
                                                                                                self.emp_s_code_var.get() + self.month_var.get()+self.year_var.get()+ ".txt"
                                                                                                   ))
                file_ = open('Salary_Reciept/' + str(self.emp_s_code_var.get()) + str(self.month_var.get()) + str(self.year_var.get()) +'.txt', 'w')
                file_.write(self.txt_salary_reciept.get('1.0', END))
                file_.close()
                messagebox.showinfo("Success", "Record inserted Successfully")
                con.commit()
                con.close()
                self.btn_print.config(state=NORMAL)
                self.clear_sal_record()

        #
        # except Exception as er:
        #     messagebox.showerror("Error", f"Error Due to:{str(er)}")

    def clear_sal_record(self):
        self.btn_print.config(state=DISABLED)

        self.emp_s_code_var.set("")
        self.month_var.set("")
        self.year_var.set("")
        self.salary_var.set("")
        self.days_var.set("")
        self.absent_var.set("")

        self.pf_var.set("")
        self.medical_var.set("")
        self.convence_var.set("")
        self.net_salary_var.set("")
        self.txt_salary_reciept.delete('1.0', END)
        self.txt_salary_reciept.insert(END, self.salary_slip)

    def calculate(self):
        if self.month_var.get() == "" or self.year_var.get() == "" or self.salary_var.get() == "" or self.days_var.get() == "" or self.absent_var.get() == "" or self.medical_var.get() == "" or self.pf_var.get() == "" or self.convence_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif not self.medical_var.get().isdigit() or not self.pf_var.get().isdigit() or not self.convence_var.get().isdigit() or not self.salary_var.get().isdigit():
            messagebox.showerror("Error", "Enter valid Data")
        else:
            per_day = int(self.salary_var.get()) / int(self.days_var.get())
            work_days = int(self.days_var.get()) - int(self.absent_var.get())
            sal = per_day * work_days
            deduct = int(self.medical_var.get()) + int(self.pf_var.get())
            add = int(self.convence_var.get())
            net_sal = sal - deduct + add
            self.net_salary_var.set(str(round(net_sal, 2)))

            up_salary_slip = f'''\t\tHotel Sainath \n\t\t  Vaithiwadi,\n\t\t   Thane(W)
\n\t\t  Pay Slip 
--------------------------------------------------------------------
Employee ID\t\t:  {self.emp_s_code_var.get()} 	
Salary Of\t\t:  {self.month_var.get()} - {self.year_var.get()}	
Generated On\t\t:  {str(time.strftime("%d-%b-%Y - %H:%M:%S"))}
--------------------------------------------------------------------
Total Days\t\t:  {self.days_var.get()}
Total Present\t\t:  {str(int(self.days_var.get()) - int(self.absent_var.get()))}
Total Absent\t\t:  {self.absent_var.get()}
Basic Salary\t\t:  Rs.{self.salary_var.get()}/-
Convence\t\t:  Rs.{self.convence_var.get()}/-
Medical\t\t:  Rs.{self.medical_var.get()}/-
PF\t\t:  Rs.{self.pf_var.get()}/-
Net Salary\t\t:  Rs.{self.net_salary_var.get()}/-

--------------------------------------------------------------------
This is computer generated Payslip and doesn't required any signature
'''
            self.txt_salary_reciept.delete('1.0', END)
            self.txt_salary_reciept.insert(END, up_salary_slip)

    def search_sal_record(self):
        try:
            if self.emp_s_code_var.get()=="" or self.month_var.get()=="" or self.year_var.get()=="":
                messagebox.showerror("Error","Employee ID / Month / Year required")
            elif not self.emp_s_code_var.get().isdigit()  or not  self.year_var.get().isdigit():
                messagebox.showerror("Error","Enter valid Employee ID / Month / Year required")
            else:
                sal_re = self.emp_s_code_var.get() + self.month_var.get() + self.year_var.get() + ".txt"
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("select * from sal_record where salary_reciept=%s", sal_re)
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID / Month / Year")
                else:
                    self.emp_s_code_var.set(row[0])
                    self.month_var.set(row[1])
                    self.year_var.set(row[2])
                    self.salary_var.set(row[3])
                    self.days_var.set(row[4])
                    self.absent_var.set(row[5])
                    self.pf_var.set(row[6])
                    self.medical_var.set(row[7])
                    self.convence_var.set(row[8])
                    self.net_salary_var.set(row[9])
                    file_ = open('Salary_Reciept/' + str(row[10]), 'r')
                    self.txt_salary_reciept.delete('1.0', END)
                    for i in file_:
                        self.txt_salary_reciept.insert(END, i)
                    file_.close()

                    self.btn_print.config(state=NORMAL)

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")

    def update_sal_record(self):
        if self.emp_s_code_var.get()=="" or self.net_salary_var.get()=="" or self.month_var=="" or self.year_var.get()=="":
            messagebox.showerror("Error", "All details are required")
        elif not self.emp_s_code_var.get().isdigit() or not self.year_var.get().isdigit() or not  self.pf_var.get().isdigit() or not self.medical_var.get().isdigit() or not self.convence_var.get().isdigit():
            messagebox.showerror("Error", "Enter valid Data")
        else:
            sal_re = self.emp_s_code_var.get() + self.month_var.get() + self.year_var.get() + ".txt"
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from sal_record where salary_reciept=%s", sal_re)
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Employee ID / Month / Year")
            else:
                cur.execute("UPDATE sal_record SET `e_id`=%s, `month`=%s,`year`=%s,`salary`=%s,`total_days`=%s,`absent`=%s,`pf`=%s,`medical`=%s,`convence`=%s,`net_salary`=%s,`salary_reciept`=%s WHERE `salary_reciept`=%s",
                            (self.emp_s_code_var.get(),
                                self.month_var.get(),
                                self.year_var.get(),
                                self.salary_var.get(),
                                self.days_var.get(),
                                self.absent_var.get(),
                                self.pf_var.get(),
                                self.medical_var.get(),
                                self.convence_var.get(),
                                self.net_salary_var.get(),
                                sal_re,
                                sal_re
                                ))
                file_ = open('Salary_Reciept/' +sal_re, 'w')
                file_.write(self.txt_salary_reciept.get('1.0', END))
                file_.close()
                messagebox.showinfo("Success", "Record updated Successfully")
                con.commit()
                con.close()
                self.clear_emp()



    def delete_sal_record(self):
        if self.emp_s_code_var.get() == "" or self.month_var.get() == "" or self.year_var.get() == "":
            messagebox.showerror("Error", "Employee ID / Month / Year required")
        elif not self.emp_s_code_var.get().isdigit() or not self.year_var.get().isdigit():
            messagebox.showerror("Error", "Enter valid Employee ID / Month / Year required")
        else:
            sal_re = self.emp_s_code_var.get() + self.month_var.get() + self.year_var.get() + ".txt"
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from sal_record where `salary_reciept`=%s", sal_re)
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Employee ID / Month / Year")
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete ?")
                if op == True:
                    cur.execute("delete from sal_record where salary_reciept=%s", sal_re)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Delete", "Employee record Successfully Deleted")
                    self.clear_sal_record()


    def load_emp_data(self,ev):
        cursor_row = self.emp_table.focus()
        contents = self.emp_table.item(cursor_row)
        row = contents["values"]
        self.emp_code_var.set(row[0])
        self.designation_var.set(row[1])
        self.name_var.set(row[2])
        self.age_var.set(row[3])
        self.gender_var.set(row[4])
        self.email_var.set(row[5])
        self.doj_var.set(row[6])
        self.salaryemp_var.set(row[7])
        self.contact_var.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])

    def email_validation(self,x):
        a=0
        y=len(x)
        dot=x.find(".")
        at = x.find("@")
        for i in range (0,at):
            if((x[i]>='a' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')):
                a=a+1
        if not (a>0 and at>0 and (dot-at)>0 and (dot+1)<y):
            return True

    def add_emp(self):
        try:
            if self.emp_code_var.get() == "" or self.designation_var.get() == "" or self.name_var.get() == "" or self.age_var.get() == "" or self.gender_var.get() == "" or self.email_var.get() == "" or self.doj_var.get() == "" or self.salaryemp_var.get() == "" or self.contact_var.get() == "":
                messagebox.showerror("Error", "All details are required")
            elif self.email_validation(self.email_var.get()):
                messagebox.showerror("Error","Enter valid Email")
            elif not len(self.contact_var.get())==10 or not self.contact_var.get().isdigit():
                messagebox.showerror("Error","Eneter valid Contact number")
            elif not self.salaryemp_var.get().isdigit() or not self.age_var.get().isdigit() :
                messagebox.showerror("Error","Enter valid Data")
            else:
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("select * from emp_management where e_id=%s", self.emp_code_var.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID is already present")
                else:
                    cur.execute(
                        "insert into emp_management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.emp_code_var.get(),
                         self.designation_var.get(),
                         self.name_var.get(),
                         self.age_var.get(),
                         self.gender_var.get(),
                         self.email_var.get(),
                         self.doj_var.get(),
                         self.salaryemp_var.get(),
                         self.contact_var.get(),
                         self.txt_address.get('1.0', END),
                         )
                    )
                    messagebox.showinfo("Success", "Record updated Successfully")
                    con.commit()
                    con.close()
                    self.clear_emp()
                    self.show_emp_data()

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")

    def search_emp(self):
        try:
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from emp_management where e_id=%s", self.emp_code_var.get())
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Employee ID")
            else:
                self.emp_code_var.set(row[0])
                self.designation_var.set(row[1])
                self.name_var.set(row[2])
                self.age_var.set(row[3])
                self.gender_var.set(row[4])
                self.email_var.set(row[5])
                self.doj_var.set(row[6])
                self.salaryemp_var.set(row[7])
                self.contact_var.set(row[8])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END, row[9])

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")



    def delete_emp(self):
        if self.emp_code_var.get() == "":
            messagebox.showerror("Error", "Employee ID required")
        else:
            try:
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("select * from emp_management where e_id=%s", self.emp_code_var.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID")
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete ?")
                    if op == True:
                        cur.execute("delete from emp_management where e_id=%s", self.emp_code_var.get())
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete", "Employee record Successfully Deleted")
                        self.clear_emp()
                        self.show_emp_data()


            except Exception as er:
                messagebox.showerror("Error", f"Error Due to:{str(er)}")

    def clear_emp(self):
        self.emp_code_var.set("")
        self.designation_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.doj_var.set("")
        self.salaryemp_var.set("")
        self.contact_var.set("")
        self.txt_address.delete('1.0', END)


    def update_emp(self):
        try:
            if self.email_validation(self.email_var.get()):
                messagebox.showerror("Error","Enter valid Email")
            elif self.emp_code_var.get() == ""  or self.name_var.get() == "":
                messagebox.showerror("Error", "All details are required")
            elif not len(self.contact_var.get())==10 or not self.contact_var.get().isdigit():
                messagebox.showerror("Error","Eneter valid Contact number")
            elif not self.salaryemp_var.get().isdigit() or not self.age_var.get().isdigit() :
                messagebox.showerror("Error","Enter valid Data")
            elif self.name_var.get().isdigit():
                messagebox.showerror("Error","Enter valid Employee Name")
            else:
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("select * from emp_management where e_id=%s", self.emp_code_var.get())
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Employee ID is already present")
                else:
                    cur.execute(
                            "UPDATE `emp_management` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`doj`=%s,`salary`=%s,`contact`=%s,`address`=%s WHERE `e_id`=%s",
                            (
                                self.designation_var.get(),
                                self.name_var.get(),
                                self.age_var.get(),
                                self.gender_var.get(),
                                self.email_var.get(),
                                self.doj_var.get(),
                                self.salaryemp_var.get(),
                                self.contact_var.get(),
                                self.txt_address.get('1.0', END),
                                self.emp_code_var.get())
                            )
                    file_ = open('Salary_Reciept/' + str(self.emp_code_var.get()) + '.txt', 'w')
                    file_.write(self.txt_salary_reciept.get('1.0', END))
                    file_.close()
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Record updated Successfully")
                    self.clear_emp()
                    self.show_emp_data()


        except Exception as er:
                messagebox.showerror("Error", f"Error Due to:{str(er)}")


    def salary_record(self):
        self.sal_table = Toplevel()
        self.sal_table.title("Hotel Management System")
        self.sal_table.geometry("1000x500+300+180")
        self.sal_table.focus_force()
        title = Label(self.sal_table, text="Salary Record", bd=5, relief=GROOVE,bg="#cacaff", fg="#722620", font=("times new roman", 25, "bold")
                      ).pack(fill=X)

        scroll_x = Scrollbar(self.sal_table, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.sal_table, orient=VERTICAL)

        self.sal_record = ttk.Treeview(self.sal_table, columns=(
            "e_id", "month", "year", "salary", "total_days", "absent", "pf", "medical", "convence", "net_salary",
            "salary_reciept"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.sal_record.xview)
        scroll_y.config(command=self.sal_record.yview)
        self.sal_record.heading("e_id", text="Emp ID")
        self.sal_record.heading("month", text="Month")
        self.sal_record.heading("year", text="Year")
        self.sal_record.heading("salary", text="Salary")
        self.sal_record.heading("total_days", text="Total Days")
        self.sal_record.heading("absent", text="Absent")
        self.sal_record.heading("pf", text="PF")
        self.sal_record.heading("medical", text="Medical")
        self.sal_record.heading("convence", text="Convence")
        self.sal_record.heading("net_salary", text="Net Salary")
        self.sal_record.heading("salary_reciept", text="Salary Reciept")
        self.sal_record["show"] = "headings"

        self.sal_record.column("e_id",width=50, anchor=CENTER)
        self.sal_record.column("month",width=50, anchor=CENTER)
        self.sal_record.column("year", width=50, anchor=CENTER)
        self.sal_record.column("salary",width=100, anchor=CENTER)
        self.sal_record.column("total_days",width=50, anchor=CENTER)
        self.sal_record.column("absent",width=50, anchor=CENTER)
        self.sal_record.column("pf",width=50, anchor=CENTER)
        self.sal_record.column("medical",width=50, anchor=CENTER)
        self.sal_record.column("convence",width=50, anchor=CENTER)
        self.sal_record.column("net_salary",width=100, anchor=CENTER)
        self.sal_record.column("salary_reciept",width=100, anchor=CENTER)
        self.sal_record.pack(fill=BOTH, expand=1)

        self.show_sal_record()

    def show_sal_record(self):
        try:
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from sal_record")
            rows = cur.fetchall()
            self.sal_record.delete(*self.sal_record.get_children())
            for row in rows:
                self.sal_record.insert('', END, values=row)
            con.close()
        except Exception as er:
            messagebox.showerror("Error", f"Error due to: {str(er)}")

    def show_emp_data(self):
        try:
            con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
            cur = con.cursor()
            cur.execute("select * from emp_management")
            rows = cur.fetchall()
            self.emp_table.delete(*self.emp_table.get_children())
            for row in rows:
                self.emp_table.insert('', END, values=row)
            con.close()
        except Exception as er:
            messagebox.showerror("Error", f"Error due to: {str(er)}")

    def print_emp_sal(self):
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(self.txt_salary_reciept.get('1.0', END))
        os.startfile(file)
    def show_pass(self):
        self.ent_passwd.config(show=NORMAL)

    def add_usr(self):
        try:
            if self.CUsername.get()=="" or self.CPassword.get()=="":
                messagebox.showerror("Error", "Username or Password can't be blank")
            else:
                self.a=datetime.datetime.today()
                time = self.a.strftime("%Y-%m-%d %H:%M:%S")
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("select * from login where Username=%s", self.CUsername.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This User is already present")
                else:
                    con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                    cur = con.cursor()
                    cur.execute("insert into login values (%s,%s,%s)", (self.CUsername.get(),self.CPassword.get(),time))
                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success", "User successfully added")

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")

    def clear_user(self):
        self.CUsername.set("")
        self.CPassword.set("")

    def update_user(self):
        try:
            if self.CUsername.get() == "" or self.CPassword.get() == "":
                messagebox.showerror("Error", "Username or Password can't be blank")
            else:
                self.a = datetime.datetime.today()
                time = self.a.strftime("%Y-%m-%d %H:%M:%S")
                con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
                cur = con.cursor()
                cur.execute("update login set Passwd=%s,Created_At=%s where Username=%s",
                            (self.CPassword.get(),
                             time,
                             self.CUsername.get()
                             ))
                con.commit()
                messagebox.showinfo("Update","Successfully Updated")
                self.clear_user()
                con.close()

        except Exception as er:
            messagebox.showerror("Error", f"Error Due to:{str(er)}")

    def delete_user(self):
        con = pymysql.connect(host="localhost", user="hms", password="Hotel@123", database="hms")
        cur = con.cursor()
        cur.execute("delete from login where Username=%s", self.CUsername.get())
        con.commit()
        messagebox.showinfo("Successfull","User deleted successfully")
        self.clear_user()
        con.close()




    def logout(self):
        self.master.destroy()
        self.master=Toplevel()
        app = SystemLogin(self.master)

if __name__ == '__main__':
    splash_win()