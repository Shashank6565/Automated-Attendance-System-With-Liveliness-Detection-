import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser

class HelpPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Help & Support")
        self.root.geometry("900x600+350+100")
        self.root.resizable(False, False)
        self.root.configure(bg="#0b0f1d")

        # Title
        header = tk.Label(self.root, text="HELP & SUPPORT",
                          font=("Segoe UI", 28, "bold"),
                          bg="#1f3557", fg="white")
        header.pack(fill=tk.X, pady=10)

        container = tk.Frame(self.root, bg="#102030")
        container.place(x=30, y=80, width=840, height=500)

        # Contact Information
        info_frame = tk.LabelFrame(container, text=" Contact Us ",
                                   font=("Segoe UI", 14, "bold"),
                                   bg="#102030", fg="white",
                                   labelanchor="n")
        info_frame.place(x=20, y=20, width=380, height=200)

        tk.Label(info_frame, text="📧 Email: 933singhshashank@gmail.com",
                 font=("Segoe UI", 12), bg="#102030", fg="lightgray").pack(anchor="w", padx=10, pady=5)

        tk.Label(info_frame, text="📞 Phone: +91 9935026933",
                 font=("Segoe UI", 12), bg="#102030", fg="lightgray").pack(anchor="w", padx=10, pady=5)

        tk.Label(info_frame, text="🏫 Address: GEU Campus, Dehradun",
                 font=("Segoe UI", 12), bg="#102030", fg="lightgray").pack(anchor="w", padx=10, pady=5)

        tk.Button(info_frame, text="Send Email",
                  font=("Segoe UI", 11, "bold"), bg="#1cb27d", fg="white",
                  command=lambda: webbrowser.open("mailto:support@attendance.com")).pack(pady=10)

        # Quick Help Topics
        help_frame = tk.LabelFrame(container, text=" Help Topics ",
                                   font=("Segoe UI", 14, "bold"),
                                   bg="#102030", fg="white",
                                   labelanchor="n")
        help_frame.place(x=420, y=20, width=390, height=205)

        topics = [
            "• How to mark attendance?",
            "• Fix camera connection issues",
            "• IP Webcam setup guide",
            "• Face not recognized troubleshooting",
            "• Update student database"
        ]

        for topic in topics:
            tk.Label(help_frame, text=topic,
                     font=("Segoe UI", 11),
                     bg="#102030", fg="lightgray").pack(anchor="w", padx=10, pady=3)

        # Feedback Section
        feedback_frame = tk.LabelFrame(container, text=" Send Feedback ",
                                       font=("Segoe UI", 14, "bold"),
                                       bg="#102030", fg="white",
                                       labelanchor="n")
        feedback_frame.place(x=20, y=230, width=785, height=245)

        tk.Label(feedback_frame, text="Write your query/issue:",
                 font=("Segoe UI", 12), bg="#102030", fg="white").place(x=10, y=10)

        self.feedback_entry = tk.Text(feedback_frame, height=5, width=90,
                                      font=("Segoe UI", 11), bg="#1b2b3a", fg="white")
        self.feedback_entry.place(x=10, y=40)

        send_btn = tk.Button(feedback_frame, text="Submit",
                             font=("Segoe UI", 12, "bold"),
                             bg="#e63946", fg="white",
                             command=self.submit_feedback)
        send_btn.place(x=660, y=180, width=100, height=30)

    def submit_feedback(self):
        feedback = self.feedback_entry.get("1.0", "end").strip()
        if feedback == "":
            messagebox.showerror("Error", "Feedback cannot be empty")
        else:
            messagebox.showinfo("Thank You", "Your feedback has been submitted!")
            self.feedback_entry.delete("1.0", "end")


if __name__ == "__main__":
    root = tk.Tk()
    obj = HelpPortal(root)
    root.mainloop()
