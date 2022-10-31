import tkinter as tk
from tkinter import ttk
import locale

locale.setlocale( locale.LC_ALL, 'id-ID')

# Main Window
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title("Tubes Pengkom K16 Kelompok 5")
root.state('zoomed')

# Main Frame
booking_frame = tk.Frame(root, highlightbackground="blue", highlightthickness=2)

# Information Frame
information_frame = tk.Frame(booking_frame, highlightbackground="blue", highlightthickness=2)

# Seat Icons
icon_frame = tk.Frame(information_frame)
seat_free = tk.PhotoImage(file="C:/Users/Dewo/Desktop/seat_free.png")
seat_own = tk.PhotoImage(file="C:/Users/Dewo/Desktop/seat_own.png")
seat_sold = tk.PhotoImage(file="C:/Users/Dewo/Desktop/seat_sold.png")
seat_free_img = tk.Label(icon_frame, image=seat_free).pack(side="left")
seat_fre_label = tk.Label(icon_frame, text="Available").pack(side="left")
seat_own_img = tk.Label(icon_frame, image=seat_own).pack(side="left")
seat_own_label = tk.Label(icon_frame, text="Picked Seat").pack(side="left")
seat_sold_img = tk.Label(icon_frame, image=seat_sold).pack(side="left")
seat_sold_label = tk.Label(icon_frame, text="Sold").pack()
icon_frame.pack(anchor="w")

# Seperator
separator = ttk.Separator(information_frame, orient='horizontal')
separator.pack(fill='x')

# Initialization
count_seat = 0
text_var_ticket = tk.StringVar()
text_var_ticket.set("Tickets: 0")

price = 50000
str_total = tk.StringVar()
str_total.set("Total Payment: Rp0")

list_seat = []
str_seat = ""
text_var_seat = tk.StringVar()
text_var_seat.set("Seats: -")

# Datas Frame
data_frame = tk.Frame(information_frame)
book_title = tk.Label(data_frame, text="Black Adam").pack(anchor=tk.W)
seat_list = tk.Label(data_frame, textvariable=text_var_seat, wraplength=510, justify="left").pack(anchor=tk.W)
num_ticket = tk.Label(data_frame, textvariable=text_var_ticket).pack(anchor=tk.W)
location = tk.Label(data_frame, text="Cinema: XX5 Bandung").pack(anchor=tk.W)
studio = tk.Label(data_frame, text="Studio: 1").pack(anchor=tk.W)
date = tk.Label(data_frame, text="22-10-2022, Time: 15:30").pack(anchor=tk.W)
total = tk.Label(data_frame, textvariable=str_total).pack(anchor=tk.W)
data_frame.pack(anchor=tk.W)

information_frame.pack(anchor="w", fill="x")

# Seats Frame
seat_frame = tk.Frame(booking_frame, highlightbackground="blue", highlightthickness=2)
seat_frame.rowconfigure((9), weight=1)
seat_frame.columnconfigure(15, weight=1)

# temporary array
sold_seat = [[False for j in range(15)] for i in range(9)]
sold_seat[1][1] = True

# Fungsi bila seat diklik
def clicked_seat(par, i, j):
    global count_seat, list_seat, str_seat
    # Menambah Count Seat
    if par.get() == 1:
        count_seat += 1
    elif par.get() == 0:
        count_seat -= 1
    text_var_ticket.set(f"Tickets: {count_seat}")

    # Menambah Total Belanja
    str_total.set(f"Total Payment: {locale.currency(price*count_seat, grouping=True)}")

    # Mencetak Tempat Duduk Dipilih
    picked_seat = i+j
    if par.get() == 1:
        list_seat.append(picked_seat)
    elif par.get() == 0:
        list_seat.remove(picked_seat)
    list_seat.sort()
    str_seat = "Seats: "+str(list_seat).replace("[", "").replace("]", "").replace("'", "")
    text_var_seat.set(str_seat)

    # Mengubah State & Cursor
    if count_seat > 0:
        confirm_button['state'] =  tk.NORMAL
        confirm_button['cursor'] = "hand2"
    else:
        confirm_button['state'] = tk.DISABLED
        confirm_button['cursor'] = ""
        str_seat = "Seats: -"
        text_var_seat.set(str_seat)

# Create Seat Items
for i in range(9):
    for j in range(15):
        if i == 0: # Cetak Angka
            if j < 7:
                item = tk.Label(seat_frame, text=f"{j+1}").grid(row=i, column=j)
            elif j > 7:
                item = tk.Label(seat_frame, text=f"{j}").grid(row=i, column=j)
        elif j == 7: # Cetak Huruf
            item = tk.Label(seat_frame, text=f"{chr(ord('A')+i-1)}").grid(row=i, column=j)
        else: # Cetak Kursi
            if sold_seat[i][j]: # Jika Sold
                item = tk.Label(seat_frame, image=seat_sold).grid(row=i, column=j)
            else: # Jika Available
                # Penentu Kode Seat
                x_seat = ""
                if j < 7:
                    x_seat = str(j+1)
                elif j > 7:
                    x_seat = str(j)
                y_seat = f"{chr(ord('A')+i-1)}"
                seat_var = tk.IntVar()
                # Check Button Seat
                item = tk.Checkbutton(seat_frame, variable=seat_var, onvalue=1, offvalue=0, command=lambda num=seat_var, i=y_seat, j=x_seat: clicked_seat(num, i, j), indicatoron=False, image=seat_free, selectimage=seat_own, cursor="hand2").grid(row=i, column=j, padx=3, pady=3)

screen = tk.Label(seat_frame, text="SCREEN", font=("Arial, 18")).grid(row=11, column=0, columnspan=15, pady=(10,0))

seat_frame.pack()

# Seperator
separator = ttk.Separator(booking_frame, orient='horizontal').pack(fill='x', pady=5)

# Fungsi Bila confirm button diklik
def clicked_confirm():
    ...

# Fungsi bila cancel button diklik
def clicked_cancel():
    ...

# Confirm and Cancel Button Frame
button_frame = tk.Frame(booking_frame, highlightbackground="blue", highlightthickness=2)
button_frame.rowconfigure(1)
button_frame.columnconfigure(2)
confirm_button = tk.Button(button_frame, text="Confirm Order", command="", font=("Arial, 13"), bg="green", state=tk.DISABLED)
confirm_button.grid(row=0, column=0, padx=5, ipadx=28, ipady=12)
cancel_button = tk.Button(button_frame, text="Cancel", command="", font=("Arial, 13"), bg="red", cursor="hand2").grid(row=0, column=1, padx=5, ipadx=55, ipady=12)
button_frame.pack()

booking_frame.pack()
root.mainloop()
