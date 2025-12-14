import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import os
import cv2
import numpy as np
import mysql.connector

class face_recognition: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Portal")
        self.root.configure(bg="#101522")

        # Title
        title_lbl = tk.Label(self.root, text="FACE RECOGNITION",
                             font=("Segoe UI", 32, "bold"),
                             bg="#1f2c45", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        # Left image
        img_top = Image.open(r"C:\Users\933si\Downloads\Gemini_Generated_Image_xmbmqmxmbmqmxmbm.png")
        img_top = img_top.resize((650, 730), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = tk.Label(self.root, image=self.photoimg_top, bg="#101522")
        f_lbl.place(x=0, y=60, width=650, height=730)

        # Right section background
        right_panel = tk.Frame(self.root, bg="#162039")
        right_panel.place(x=650, y=60, width=880, height=730)

        # Bottom image inside panel
        img_bottom = Image.open(r"C:\Users\933si\Downloads\Gemini_Generated_Image_nam6aynam6aynam6.png")
        img_bottom = img_bottom.resize((880, 530), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        b_lbl = tk.Label(right_panel, image=self.photoimg_bottom, bg="#162039")
        b_lbl.place(x=0, y=0, width=880, height=530)

        # Face Recognition Button
        tk.Button(right_panel,
                  text="START FACE RECOGNITION",
                  command=self.face_recog,
                  font=("Segoe UI", 22, "bold"),
                  bg="#00a86b", fg="white",
                  bd=0, cursor="hand2").place(x=225, y=560, width=420, height=55)

        # Exit Button
        tk.Button(right_panel,
                  text="EXIT",
                  command=self.root.destroy,
                  font=("Segoe UI", 20, "bold"),
                  bg="#d7263d", fg="white",
                  bd=0, cursor="hand2").place(x=310, y=640, width=250, height=50)

    

    #===================== Attendance ========================
    def mark_attendance(self, n, r, d, c):
        file_path = os.path.join(os.path.dirname(__file__), "attendance.csv")

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("Name,Roll,Department,StudentID,Time,Date,Status\n")

        with open(file_path, "r", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

        if ((c not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            with open(file_path, "a", newline="\n") as f:
                f.write(f"{n},{r},{d},{c},{dtString},{d1},Present\n")


    # Face Recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            
            coord = []

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict/300))

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="GEUshashanksingh6565",
                    database="college"
                )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE `Student ID`=%s", (id,))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT `University Roll No.` FROM student WHERE `Student ID`=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "N/A"

                my_cursor.execute("SELECT Department FROM student WHERE `Student ID`=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "N/A"

                my_cursor.execute("SELECT `Student ID` FROM student WHERE `Student ID`=%s", (id,))
                c = my_cursor.fetchone()
                c = "+".join(c) if c else "N/A"

                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {c}", (x, y-95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name: {n}", (x, y-70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Roll: {r}", (x, y-45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Dept: {d}", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                    self.mark_attendance(n, r, d, c)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # 📌 PHONE CAMERA STREAM
        ip_url = "http://192.168.0.105:8080//video"
        video_cap = cv2.VideoCapture(ip_url)

        if not video_cap.isOpened():
            messagebox.showerror("Camera Error", "Failed to access Phone Camera.\nCheck WiFi or change IP URL.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = tk.Tk()
    obj = face_recognition(root)
    root.mainloop()
