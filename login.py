from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json, hashlib, os

from main import attendence__System   # Keep your main project link

# ---------------- HELPER FUNCTIONS ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

def center_window(win, width, height):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# Load existing users
users = load_users()


# ---------------- MAIN CLASS ----------------
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Portal")
        self.root.geometry("1550x880+0+0")
        self.root.configure(bg="#0d1b2a")
        self.root.resizable(False, False)

        # Background Image
        self.bg_img = Image.open(r"C:\Users\933si\Downloads\Login bg.jpg")
        self.bg_img = self.bg_img.resize((1550, 880), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_img)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Glass Card Frame
        frame = Frame(self.root, bg="#ffffff", highlightthickness=2, highlightbackground="black")
        frame.place(x=600, y=200, width=380, height=500)

        # Login Icon
        img_login = Image.open(r"C:\Users\933si\Downloads\Login Logo.jpg")
        img_login = img_login.resize((110, 110), Image.Resampling.LANCZOS)
        self.photoimage_login = ImageTk.PhotoImage(img_login)
        lbl2 = Label(frame, image=self.photoimage_login, bg="white")
        lbl2.place(x=135, y=20)

        # Title Text
        get_str = Label(frame, text="Welcome Back!",
                        font=("Segoe UI", 20, "bold"), bg="white", fg="#0d1b2a")
        get_str.place(x=100, y=140)

        # Username
        username = Label(frame, text="Username",
                         font=("Segoe UI", 12, "bold"), bg="white", fg="#0d1b2a")
        username.place(x=45, y=200)
        self.txtuser = ttk.Entry(frame, font=("Segoe UI", 12))
        self.txtuser.place(x=45, y=225, width=290, height=30)

        # Password
        password = Label(frame, text="Password",
                         font=("Segoe UI", 12, "bold"), bg="white", fg="#0d1b2a")
        password.place(x=45, y=270)
        self.txtpass = ttk.Entry(frame, font=("Segoe UI", 12), show="*")
        self.txtpass.place(x=45, y=295, width=290, height=30)

        # Show Password
        self.show_pass_var = IntVar()
        show_pass = Checkbutton(frame, text="Show Password",
                                variable=self.show_pass_var,
                                command=self.toggle_password,
                                bg="white", fg="#0d1b2a", font=("Segoe UI", 10))
        show_pass.place(x=45, y=330)

        # Login Button
        loginbtn = Button(frame, text="LOGIN", command=self.login,
                          font=("Segoe UI", 13, "bold"), bg="#1d4ed8",
                          fg="white", activebackground="#1e3a8a", bd=0)
        loginbtn.place(x=45, y=370, width=290, height=40)

        # Forget + Register
        forgetbtn = Button(frame, text="Forgot Password?",
                           command=self.forget_password_window,
                           font=("Segoe UI", 10, "bold"), fg="#1d4ed8",
                           bg="white", bd=0)
        forgetbtn.place(x=45, y=420)

        registerbtn = Button(frame, text="New here? Create account",
                             command=self.register_window,
                             font=("Segoe UI", 10, "bold"), fg="#1d4ed8",
                             bg="white", bd=0)
        registerbtn.place(x=45, y=445)

    # ---------------- TOGGLE PASSWORD ----------------
    def toggle_password(self):
        if self.show_pass_var.get():
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    # ---------------- LOGIN FUNCTION ----------------
    def login(self):
        user = self.txtuser.get().strip()
        password = self.txtpass.get().strip()

        if user == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        if user in users and users[user] == hash_password(password):
            messagebox.showinfo("Success", f"Welcome {user}!")
            self.open_attendance_window()
        else:
            messagebox.showerror("Invalid", "Incorrect username or password")

    def open_attendance_window(self):
        self.new_window = Toplevel(self.root)
        self.app = attendence__System(self.new_window)

    # ---------------- REGISTER ----------------
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Register")
        center_window(self.new_window, 400, 400)

        Label(self.new_window, text="Register New User",
              font=("Segoe UI", 20, "bold")).pack(pady=10)
        Label(self.new_window, text="Username",
              font=("Segoe UI", 15)).pack(pady=5)
        self.reg_username = Entry(self.new_window, font=("Segoe UI", 15))
        self.reg_username.pack(pady=5)

        Label(self.new_window, text="Password",
              font=("Segoe UI", 15)).pack(pady=5)
        self.reg_password = Entry(self.new_window, font=("Segoe UI", 15), show="*")
        self.reg_password.pack(pady=5)

        Button(self.new_window, text="Register",
               font=("Segoe UI", 15, "bold"), bg="green",
               fg="white", command=self.register_user).pack(pady=20)

    def register_user(self):
        new_user = self.reg_username.get().strip()
        new_pass = self.reg_password.get().strip()

        if new_user == "" or new_pass == "":
            messagebox.showerror("Error", "All fields are required", parent=self.new_window)
        elif new_user in users:
            messagebox.showerror("Error", "Username already exists", parent=self.new_window)
        else:
            users[new_user] = hash_password(new_pass)
            save_users()
            messagebox.showinfo("Success", "Registration Successful!", parent=self.new_window)
            self.new_window.destroy()

    # ---------------- RESET PASSWORD ----------------
    def forget_password_window(self):
        self.forget_win = Toplevel(self.root)
        self.forget_win.title("Reset Password")
        center_window(self.forget_win, 400, 300)

        Label(self.forget_win, text="Reset Your Password",
              font=("Segoe UI", 20, "bold")).pack(pady=10)

        Label(self.forget_win, text="Username", font=("Segoe UI", 15)).pack(pady=5)
        self.forget_username = Entry(self.forget_win, font=("Segoe UI", 15))
        self.forget_username.pack(pady=5)

        Label(self.forget_win, text="New Password", font=("Segoe UI", 15)).pack(pady=5)
        self.forget_newpass = Entry(self.forget_win, font=("Segoe UI", 15), show="*")
        self.forget_newpass.pack(pady=5)

        Button(self.forget_win, text="Reset",
               font=("Segoe UI", 15, "bold"), bg="orange",
               fg="white", command=self.reset_password).pack(pady=20)

    def reset_password(self):
        user = self.forget_username.get().strip()
        new_pass = self.forget_newpass.get().strip()

        if user == "" or new_pass == "":
            messagebox.showerror("Error", "All fields are required", parent=self.forget_win)
        elif user not in users:
            messagebox.showerror("Error", "Username not found", parent=self.forget_win)
        else:
            users[user] = hash_password(new_pass)
            save_users()
            messagebox.showinfo("Success", "Password reset successfully!", parent=self.forget_win)
            self.forget_win.destroy()


# ---------------- RUN MAIN APP ----------------
if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
