from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class attendance:

    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management Portal")
        self.root.geometry("1530x790+0+0")
        self.root.title("Automated Attendance System")

        #=================== Variables ===================
        self.var_name = StringVar()
        self.var_university_id = StringVar()
        self.var_department = StringVar()
        self.var_student_id = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance_status = StringVar()


        # Images 1.
        img1 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU png.png")
        img1 = img1.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        title_lbl = Label(self.root, image=self.photoimg1)
        title_lbl.place(x=500, y=0, width=500, height=130)

        # Images 2.
        img2 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU5.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        title_lbl = Label(self.root, image=self.photoimg2)
        title_lbl.place(x=0, y=0, width=500, height=130) 

        # Images 3.
        img3 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU5.jpeg")
        img3 = img3.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        title_lbl = Label(self.root, image=self.photoimg3)
        title_lbl.place(x=1000, y=0, width=550, height=130) 

        # Background Image
        img4 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\bg.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.BICUBIC)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="Attendance Management Portal", font=("times new roman", 35, "bold"), bg="yellow", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Frame (Main Frame)
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=30, y=10, width=700, height=580)

        # Image
        left_img = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\bg.jpg")
        left_img = left_img.resize((1530, 710), Image.Resampling.BICUBIC)
        self.photoleft_img = ImageTk.PhotoImage(left_img)

        f_img = Label(self.root, image=self.photoleft_img)
        f_img.place(x=60, y=220, width=690, height=120)

        #  left Inside Frame

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=3, y=125, width=690, height=423)

        #===== Labels and Entries =====#

        # Name
        attendance_id_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendance_id_entry = ttk.Entry(left_inside_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # University ID
        name_label = Label(left_inside_frame, text="University Roll ID:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_university_id, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Department
        roll_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        roll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_department, width=20, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Student ID
        class_label = Label(left_inside_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        class_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        class_entry = ttk.Entry(left_inside_frame, textvariable=self.var_student_id, width=20, font=("times new roman", 12, "bold"))
        class_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_time, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_date, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        attendance_status_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        attendance_status_entry = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance_status, width=18,
                                            font=("times new roman", 12, "bold"), state="readonly")
        attendance_status_entry['values'] = ("Present", "Absent")
        attendance_status_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)



        # Buttons

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=300, width=660, height=90)


        save_btn = Button(btn_frame, text="Import CSV", command=self.load_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=0, pady=5, sticky=W)

        update_btn = Button(btn_frame, text="Export CSV", command=self.export_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=0, pady=5, sticky=W)

        delete_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=0, pady=5, sticky=W)
        
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=0, pady=5, sticky=W)

        exit_btn = Button(btn_frame, text="Exit", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white", command=self.root.destroy)
        exit_btn.grid(row=1, column=0, padx=0, pady=5, sticky=W)


        # Right Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=740, y=10, width=700, height=580)

        # table frame
        table_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=685, height=540)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(table_frame, column=("Name", "University ID", "Department", "Student ID", "Time", "Date", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        self.attendance_table.heading("Name", text="Name")
        self.attendance_table.heading("University ID", text="University ID")
        self.attendance_table.heading("Department", text="Department")
        self.attendance_table.heading("Student ID", text="Student ID")
        self.attendance_table.heading("Time", text="Time")
        self.attendance_table.heading("Date", text="Date")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"
        self.attendance_table.column("Name", width=100)
        self.attendance_table.column("University ID", width=100)
        self.attendance_table.column("Department", width=100)
        self.attendance_table.column("Student ID", width=100)
        self.attendance_table.column("Time", width=100)
        self.attendance_table.column("Date", width=100)
        self.attendance_table.column("status", width=100)


        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease-1>", self.get_cursor)


        

    #===================== Fetch Data ========================
    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)
    
    def load_data(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #===================== Export Data ========================
    def export_data(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Your data has been exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        row = content["values"]
        self.var_name.set(row[0])
        self.var_university_id.set(row[1])
        self.var_department.set(row[2])
        self.var_student_id.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attendance_status.set(row[6])


    def reset_data(self):
        self.var_name.set("")
        self.var_university_id.set("")
        self.var_department.set("")
        self.var_student_id.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("")
        

    # ===================== Update Data =======================
    def update_data(self):
        try:
            selected = self.attendance_table.focus()
            if not selected:
                messagebox.showerror("Selection Error", "No record selected!" , parent=self.root)
                return

            # Get selected row index
            row_id = self.attendance_table.index(selected)

            # Update table view
            self.attendance_table.item(selected, values=(
                self.var_name.get(),
                self.var_university_id.get(),
                self.var_department.get(),
                self.var_student_id.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attendance_status.get()
            ))

            # Update in global mydata list
            mydata[row_id] = [
                self.var_name.get(),
                self.var_university_id.get(),
                self.var_department.get(),
                self.var_student_id.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attendance_status.get()
            ]

            messagebox.showinfo("Success", "Record Updated Successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()