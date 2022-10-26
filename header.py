import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Cinema XX5")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

header_frame = tk.Frame(window, highlightbackground="orange", highlightthickness=3)

image = Image.open("images/xx5.png")
resize_image = image.resize((180, 100))
img = ImageTk.PhotoImage(resize_image)
left_frame = tk.Frame(header_frame)
label_gambar = tk.Label(left_frame, image=img).pack(side="left")
now_playing = tk.Button(left_frame, text="Now Playing", font=("arial", 16)).pack(side="left", anchor="center")
up_coming = tk.Button(left_frame, text="Up Coming", font=("arial", 16)).pack(side="right",anchor="center")
left_frame.pack(side="left")
right_frame = tk.Frame(header_frame)
saldo = tk.Button(right_frame, text="Rp100.000,00", font=("arial", 16)).pack(side="left")
akun = tk.Label(right_frame, text="Erling Haaland", font=("arial", 16)).pack(side="right")
right_frame.pack(side="right", anchor="center")

header_frame.pack(fill="x")

window.mainloop()
