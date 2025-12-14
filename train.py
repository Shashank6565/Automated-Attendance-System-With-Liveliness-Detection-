import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Data")
        self.root.geometry("950x600+280+80")
        self.root.resizable(False, False)

        # ===== Top Title Bar ===== #
        title_lbl = tk.Label(self.root, text="TRAIN DATA SET",
                             font=("Segoe UI", 28, "bold"),
                             bg="#2a3d66", fg="white")
        title_lbl.pack(fill=tk.X)

        # ===== Top Image ===== #
        img_top = Image.open(r"C:\Users\933si\Downloads\Train Data 1.png")
        img_top = img_top.resize((900, 250), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        lbl_top_img = tk.Label(self.root, image=self.photoimg_top, bg="white")
        lbl_top_img.place(x=25, y=70)

        # ===== Bottom Image ===== #
        img_bottom = Image.open(r"C:\Users\933si\Downloads\Train Data 2.jpg")
        img_bottom = img_bottom.resize((900, 230), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        lbl_bottom_img = tk.Label(self.root, image=self.photoimg_bottom, bg="white")
        lbl_bottom_img.place(x=25, y=350)

        # ===== Train Button ===== #
        train_btn = tk.Button(self.root, text="START TRAINING",
                              command=self.train_classifier,
                              cursor="hand2",
                              font=("Segoe UI", 18, "bold"),
                              bg="#0078d4", fg="white",
                              activebackground="#005a9e",
                              activeforeground="white")
        train_btn.place(x=300, y=305, width=330, height=45)


    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "No Dataset Found!\nPlease Generate Face Samples First.", parent=self.root)
            return

        # Progress UI Window
        progress_win = tk.Toplevel(self.root)
        progress_win.title("Training in Progress")
        progress_win.geometry("450x150+600+350")
        progress_win.resizable(False, False)
        progress_win.configure(bg="white")

        lbl_status = tk.Label(progress_win, text="Training in Progress...", font=("Segoe UI", 14),
                              bg="white", fg="black")
        lbl_status.pack(pady=10)

        # Progress Bar
        progress = ttk.Progressbar(progress_win, orient="horizontal",
                                   length=380, mode="determinate")
        progress.pack(pady=10)

        # Spinner for animation
        spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        spinner_index = 0

        progress.update_idletasks()

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]

        faces = []
        ids = []

        total = len(path)
        progress["maximum"] = total

        for idx, image in enumerate(path):
            img = Image.open(image).convert('L')
            image_np = np.array(img, 'uint8')

            id_str = os.path.basename(image).split('.')[1]
            try:
                id_int = int(id_str)
            except ValueError:
                continue

            faces.append(image_np)
            ids.append(id_int)

            # Update Progress Bar
            progress["value"] = idx + 1

            # Spinner animation update
            spinner_index = (spinner_index + 1) % len(spinner)
            lbl_status.config(text=f"Training {spinner[spinner_index]}   {int((idx+1)/total * 100)}% Completed")

            progress_win.update_idletasks()

            cv2.waitKey(1)

        # Destroy popup if no valid images
        if len(ids) == 0:
            progress_win.destroy()
            messagebox.showerror("Error", "No valid training images found!", parent=self.root)
            return

        ids = np.array(ids)
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("classifier.xml")

        progress_win.destroy()
        cv2.destroyAllWindows()

        messagebox.showinfo("Success", "Training Complete!")
        self.root.destroy()  # Auto-close Training Portal


if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()
