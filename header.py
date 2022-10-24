import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

window=tk.Tk()
window.title("Cinema XX5")
window.configure(bg="white")
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

frame1=tk.Frame(window,highlightbackground="orange",bg="white",highlightthickness=3)
frame1.rowconfigure(1,weight=1)
frame1.columnconfigure(5,weight=1)



image = Image.open("logo xx5.png")
resize_image = image.resize((180,100))
img = ImageTk.PhotoImage(resize_image)
label_gambar=tk.Label(frame1,image=img).grid(row=0,column=0,padx=10)
now_playing=tk.Button(frame1,text="Now Playing",font=("arial",16)).grid(row=0,column=1,padx=10)
up_coming=tk.Button(frame1,text="Up Coming",font=("arial",16)).grid(row=0,column=2,padx=10)
label_empty=tk.Label(frame1,text="",bg="white").grid(row=0,column=3,padx=250)
saldo=tk.Button(frame1,text="Rp100.000,00",font=("arial",16)).grid(row=0,column=4,padx=10)
akun=tk.Label(frame1,text="Erling Haaland",font=("arial",16),fg="blue",bg="yellow").grid(row=0,column=5,padx=10)







frame1.place(x=0,y=0)

window.mainloop()