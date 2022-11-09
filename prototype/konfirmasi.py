import tkinter as tk
from tkinter.messagebox import showinfo, showerror

window = tk.Tk()
window.title("Tiket")
window.configure(bg = "#171a30")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

confirm_frame2 = tk.Frame(window,width = 500,height = 600,bg = "#171a30")
confirm_frame2.pack(anchor = tk.CENTER)


label_1 = tk.Label(confirm_frame2,fg="#fc094c",bg="#171a30",text = "Booking Confirmation",font = ("Roboto",18,"bold")).pack(anchor = tk.CENTER,pady = 10)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Name                          : Dudung",font = ("Roboto",14,"bold")).pack(anchor = tk.W)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Movie                         : Black Adam",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady=10)
label_3 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Tickets                       : 2",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady = 10)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Cinema                      : XX5 Plaza Indonesia",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady = 10)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Studio                        : 3",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady = 10)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Seats                         : C12,C13",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady = 10)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Date                           : 03-11-2022",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady = 10)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Time                          : 16:00",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady = 10)
label_2 = tk.Label(confirm_frame2,fg="white",bg="#171a30",text = "Total payment         : Rp90.000,00",font = ("Roboto",14,"bold")).pack(anchor = tk.W,pady = 10)

# Button image
button_price_on = tk.PhotoImage(file="images/price_on.png")
button_price_off = tk.PhotoImage(file="images/price_off.png")

# Fungsi Mengganti Image Saat Ditunjuk Mouse
def onHoverImage(event, img):
    event.widget.config(image=img)

def onLeaveImage(event, img):
    event.widget.config(image=img)

# Tombol konfirmasi
tombol_konfirm = tk.Button(confirm_frame2, text="Book Tickets", image=button_price_on, font=("Roboto", 13, "bold"), activebackground="#171a30", activeforeground="#eaebf1", fg="#eaebf1", bg="#171a30", cursor="hand2", borderwidth=0, compound="center")
tombol_konfirm.pack(pady=(0, 5))
tombol_konfirm.bind('<Enter>', lambda event, imgs=button_price_on: onHoverImage(event, imgs))
tombol_konfirm.bind('<Leave>', lambda event, imgs=button_price_off: onLeaveImage(event, imgs))



confirm_frame2.pack()






window.mainloop()
