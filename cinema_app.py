# Program: Aplikasi Cinema
# 1. Dewantoro Triatmojo / 19622152
# 2. Randy Verdian / 19622202
# 3. Aira Ardistya Akbarsyah/ 16522062
# 4. Berto Togatorop/ 19622192

# Algoritma:
import tkinter as tk
from tkinter import ttk
import locale
import datetime
from database import *

# Define Date
today = datetime.date.today().strftime("%d-%m-%Y")
tomorrow =  (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")

# Define Time (Now)
time_now = datetime.datetime.now()

# Set Locale (For Currency)
locale.setlocale( locale.LC_ALL, 'id-ID')

# Root Window
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Tubes Pengkom K16 Kelompok 5")
root.iconbitmap("images/xx5.ico")
root.state('zoomed')
root.configure(background="#171a30")

# Mencari Posisi Center sb x
center_x = (screen_width - 800) * 0.5

# Array Image Movie
img = [tk.PhotoImage(file=list_movie[i]["img"]) for i in range(4)]

# Image Back Button
back_img = tk.PhotoImage(file="images/back.png")

# Image Kursi
seat_free = tk.PhotoImage(file="images/seat_free.png")
seat_own = tk.PhotoImage(file="images/seat_own.png")
seat_sold = tk.PhotoImage(file="images/seat_sold.png")

# Image Screen
screen_img = tk.PhotoImage(file="images/screen.png")

# Buttons On Hover
button1 = tk.PhotoImage(file="images/button1.png")
button2 = tk.PhotoImage(file="images/button2.png")

# Fungsi Mengganti Image Saat Ditunjuk Mouse
def onHoverImage(event, img):
    event.widget.config(image=img)

def onLeaveImage(event, img):
    event.widget.config(image=img)

# Fungsi Mengganti Warna Border Saat Ditunjuk Mouse
def onHoverBorder(event):
        event.widget.config(background="#fc094c")

def onLeaveBorder(event):
        event.widget.config(background="#171a30")

# FRAME LIST MOVIE
def MovieListFrame():
    # Frame Utama
    global movielist_frame
    movielist_frame = tk.Frame(root, background="#171a30", highlightbackground="red", highlightthickness=2)
    movielist_frame.rowconfigure(3, weight=1)
    movielist_frame.columnconfigure(4, weight=1)

    # Title Movie List
    movielist_title = tk.Label(movielist_frame, text="Film Sedang Tayang di XX5", background="#171a30", font=("Roboto", "30", "bold"), fg="#eaebf1").grid(row=0, column=0, columnspan=5, ipadx=10, ipady=10, pady=10)

    # Mencetak 4 Movie
    for i in range(len(list_movie)):
        movie_frame = tk.Frame(movielist_frame, background="#171a30")
        movie_img = tk.Button(movie_frame, image=img[i], cursor="hand2", background="#171a30", bd=0, command=lambda i=i: ListToInfo(i), fg="#eaebf1")
        movie_img.bind("<Enter>", onHoverBorder)
        movie_img.bind("<Leave>", onLeaveBorder)
        movie_img.pack(ipadx=5, ipady=5)
        title_age_frame = tk.Frame(movie_frame, background="#fc094c")
        movie_title = tk.Label(title_age_frame, text=list_movie[i]["title"], background="#fc094c", font=("Helvatica", "18", "bold"), fg="#eaebf1").pack(pady=(5, 0))
        movie_age = tk.Label(title_age_frame, text=list_movie[i]["age"], background="#fc094c", font=("Helvatica", "15"), fg="#eaebf1").pack(pady=(0, 5))
        title_age_frame.pack(pady=15, fill="x", ipadx=10)
        movie_frame.grid(row=1, column=i, padx=20, pady=10)

    movielist_frame.pack()


# FRAME INFORMASI MOVIE
def MovieInformationFrame(k):
    # Membuat Scrollbar
    global movieinfo_frame
    movieinfo_frame = tk.Frame(root)
    movieinfo_frame.pack(fill="both", expand=1)

    my_canvas = tk.Canvas(movieinfo_frame, background="#171a30")
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(movieinfo_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Membuat Frame
    moviedesc_frame = tk.Frame(my_canvas, background="#171a30", highlightbackground="red", highlightthickness=2)
    moviedesc_frame.rowconfigure(9, weight=1)
    moviedesc_frame.columnconfigure(2, weight=1)

    my_canvas.create_window((center_x, 0), window=moviedesc_frame, anchor="nw")

    # Back Button
    back_button = tk.Button(moviedesc_frame, image=back_img, command=InfoToList, activebackground="#171a30", background="#171a30", relief="flat").grid(row=0, column=0, columnspan=2, sticky="nw")

    # Title, Genre, Duration
    titlegenre_frame = tk.Frame(moviedesc_frame, background="#171a30")
    moviedesc_title = tk.Label(titlegenre_frame, font=("Helvetica 18 bold"), text=list_movie[k]["title"], background="#171a30", fg="#eaebf1").pack()
    moviedesc_genre = tk.Label(titlegenre_frame, font=("Helvetica 14 bold"), text=list_movie[k]["genre"], background="#171a30", fg="#b70e43").pack()
    moviedesc_duration = tk.Label(titlegenre_frame, font=("Helvetica 14 bold"), text=list_movie[k]["duration"], background="#171a30", fg="#b70e43").pack()
    titlegenre_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Image
    img_and_buy_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_img = tk.Label(img_and_buy_frame, image=img[k], relief="flat", highlightthickness = 0, bd = 0).pack(side="left")

    # Buy Frame
    buy_frame = tk.Frame(img_and_buy_frame, background="#171a30")
    buy_frame.rowconfigure(9, weight=1)
    buy_frame.columnconfigure(5, weight=1)
    
    # Cek jika pemesanan tiket melebihi waktu tayang
    def CekDisabled(hour, minute):
        time = time_now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if time_now >= time:
            
            return "disabled"
        else:
            return "normal"
    
    # Looping 3 Lokasi
    for i in range(3):
        loc_title = tk.Label(buy_frame, text=location[i], background="#171a30", font=("Helvetica", "12", "bold"), fg="#b70e43").grid(row=0+3*i, column=0, columnspan=5, sticky="w", pady=(10, 0))
        today_label = tk.Label(buy_frame, text=today, background="#171a30", font=("Helvetica", "11", "bold"), fg="#eaebf1").grid(row=1+3*i, column=0, padx=(0, 5))
        for j in range(4):
            today_time = tk.Button(buy_frame, text=time_str[j], image=button2, state=CekDisabled(time_int[j]["hour"], time_int[j]["minute"]), command=lambda i=i, j=j: InfoToBooking(k, location[i], "today", time_str[j]), fg="#eaebf1", background="#171a30", activebackground="#171a30", activeforeground="#eaebf1", font=("Helvetica", "11", "bold"), relief="flat", cursor="hand2", compound="center")
            today_time.bind('<Enter>', lambda event, imgs=button1: onHoverImage(event, imgs))
            today_time.bind('<Leave>', lambda event, imgs=button2: onLeaveImage(event, imgs))
            today_time.grid(row=1+3*i, column=j+1, padx=5, pady= 4)

        tomorrow_label = tk.Label(buy_frame, text=tomorrow, background="#171a30", font=("Helvetica", "11", "bold"), fg="#eaebf1").grid(row=2+3*i, column=0, padx=(0, 5))
        for j in range(4):
            tomorrow_time = tk.Button(buy_frame, text=time_str[j], image=button2, command=lambda i=i, j=j: InfoToBooking(k, location[i], "tomorrow", time_str[j]), fg="#eaebf1", background="#171a30", activebackground="#171a30", activeforeground="#eaebf1", font=("Helvetica", "11", "bold"), relief="flat", cursor="hand2", compound="center")
            tomorrow_time.bind('<Enter>', lambda event, imgs=button1: onHoverImage(event, imgs))
            tomorrow_time.bind('<Leave>', lambda event, imgs=button2: onLeaveImage(event, imgs))
            tomorrow_time.grid(row=2+3*i, column=j+1, padx=5, pady= 4)

    buy_frame.pack(side="right", padx=15)

    img_and_buy_frame.grid(row=2, column=0, sticky="w", padx=10)

    # Movie Plot
    movie_plot_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_plot_title = tk.Label(movie_plot_frame, text="Plot", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_plot = tk.Label(movie_plot_frame, wraplength=800, justify="left", text=list_movie[k]["plot"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_plot_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

    # Movie Producer
    movie_prod_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_prod_title = tk.Label(movie_prod_frame, text="Producer", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_prod = tk.Label(movie_prod_frame, text=list_movie[k]["producer"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_prod_frame.grid(row=4, column=0, sticky="we", padx=10, pady=10)

    # Movie Director
    movie_director_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_director_title = tk.Label(movie_director_frame, text="Director", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_director = tk.Label(movie_director_frame, text=list_movie[k]["director"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_director_frame.grid(row=5, column=0, sticky="we", padx=10, pady=10)

    # Movie Writer
    movie_writer_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_writer_title = tk.Label(movie_writer_frame, text="Writer", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_writer = tk.Label(movie_writer_frame, text=list_movie[k]["writer"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_writer_frame.grid(row=6, column=0, sticky="we", padx=10, pady=10)

    # Movie Cast
    movie_cast_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_cast_title = tk.Label(movie_cast_frame, text="Cast", font=("Helvetica 13 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_cast = tk.Label(movie_cast_frame, wraplength=800, justify="left",text=list_movie[k]["cast"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_cast_frame.grid(row=7, column=0, sticky="we", padx=10, pady=10)


# FRAME SEAT BOOKING
def SeatBookingFrame(k, place, day, time):
    global count_seat, list_seat, str_seat, booking_frame
    # Main Frame
    booking_frame = tk.Frame(root, background="#171a30",highlightbackground="red", highlightthickness=2)

    # Information Frame
    information_frame = tk.Frame(booking_frame, background="#171a30")

    # Seat Icons
    icon_frame = tk.Frame(information_frame, background="#171a30")
    seat_free_img = tk.Label(icon_frame, image=seat_free, background="#171a30").pack(side="left")
    seat_fre_label = tk.Label(icon_frame, text="Available", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(side="left", padx=(0, 15))
    seat_own_img = tk.Label(icon_frame, image=seat_own, background="#171a30").pack(side="left")
    seat_own_label = tk.Label(icon_frame, text="Picked Seat", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(side="left", padx=(0, 15))
    seat_sold_img = tk.Label(icon_frame, image=seat_sold, background="#171a30").pack(side="left")
    seat_sold_label = tk.Label(icon_frame, text="Sold", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(padx=(0, 10))
    icon_frame.pack(anchor="w")

    # Seperator
    separator = ttk.Separator(information_frame, orient='horizontal').pack(fill='x', pady=10)

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
    data_frame = tk.Frame(information_frame, background="#171a30")
    book_title = tk.Label(data_frame, text=list_movie[k]["title"], background="#171a30", fg="#b70e43", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    seat_list = tk.Label(data_frame, textvariable=text_var_seat, wraplength=510, justify="left", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    num_ticket = tk.Label(data_frame, textvariable=text_var_ticket, background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    location = tk.Label(data_frame, text=place, background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    studio = tk.Label(data_frame, text=f"Studio: {k+1}", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    if day == "today":
        date = tk.Label(data_frame, text=f"{today}, Time: {time}", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    elif day == "tomorrow":
        date = tk.Label(data_frame, text=f"{tomorrow}, Time: {time}", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    total = tk.Label(data_frame, textvariable=str_total, background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    data_frame.pack(anchor=tk.W)

    information_frame.pack(anchor="w", fill="x")

    # Seperator
    separator = ttk.Separator(booking_frame, orient='horizontal').pack(fill='x', pady=10)

    # Seats Frame
    seat_frame = tk.Frame(booking_frame, background="#171a30")
    seat_frame.rowconfigure((9), weight=1)
    seat_frame.columnconfigure(15, weight=1)

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
                    item = tk.Label(seat_frame, text=f"{j+1}", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).grid(row=i, column=j)
                elif j > 7:
                    item = tk.Label(seat_frame, text=f"{j}", background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).grid(row=i, column=j)
            elif j == 7: # Cetak Huruf
                item = tk.Label(seat_frame, text=f"{chr(ord('A')+i-1)}", background="#171a30", fg="#eaebf1", font=("Helvetica", "13", "bold")).grid(row=i, column=j)
            else: # Cetak Kursi
                if list_movie[k]["sold_seat"][place][day][time][i][j]: # Jika Sold
                    item = tk.Label(seat_frame, image=seat_sold, background="#171a30").grid(row=i, column=j)
                else: # Jika Available
                    # Penentu Kode Seat
                    if j < 7:
                        x_seat = str(j+1)
                    elif j > 7:
                        x_seat = str(j)
                    y_seat = f"{chr(ord('A')+i-1)}"
                    seat_var = tk.IntVar()
                    
                    # Check Button Seat
                    item = tk.Checkbutton(seat_frame, variable=seat_var, onvalue=1, offvalue=0, command=lambda num=seat_var, i=y_seat, j=x_seat: clicked_seat(num, i, j), indicatoron=False, image=seat_free, selectimage=seat_own, cursor="hand2", background="#171a30", selectcolor="#171a30", activebackground="#171a30")
                    item.bind('<Enter>', lambda event, imgs=seat_own: onHoverImage(event, imgs))
                    item.bind('<Leave>', lambda event, imgs=seat_free: onLeaveImage(event, imgs))
                    item.grid(row=i, column=j, padx=3, pady=3)

    screen = tk.Label(seat_frame, image=screen_img, background="#171a30").grid(row=11, column=0, columnspan=15)

    seat_frame.pack()

    # Separator
    separator = ttk.Separator(booking_frame, orient='horizontal').pack(fill='x', pady=10)

    # Confirm and Cancel Button Frame
    button_frame = tk.Frame(booking_frame, background="#171a30")
    button_frame.rowconfigure(1)
    button_frame.columnconfigure(2)
    confirm_button = tk.Button(button_frame, text="Confirm Order", command="", font=("Helvetica", "13", "bold"), bg="green", fg="#eaebf1", state=tk.DISABLED)
    confirm_button.grid(row=0, column=0, padx=5, ipadx=28, ipady=8)
    cancel_button = tk.Button(button_frame, text="Cancel", command=lambda: BookingToInfo(k), font=("Helvetica", "13", "bold"), bg="red", fg="#eaebf1", cursor="hand2").grid(row=0, column=1, padx=5, ipadx=55, ipady=8)
    button_frame.pack()

    booking_frame.pack()


# TRANSISI DARI LIST MOVIE KE INFORMASI MOVIE
def ListToInfo(k):
    movielist_frame.forget()
    MovieInformationFrame(k)


# TRANSISI DARI INFORMASI MOVIE KE LIST MOVIE
def InfoToList():
    movieinfo_frame.forget()
    MovieListFrame()


# TRANSISI DARI INFORMASI MOVIE KE BOOKING MOVIE
def InfoToBooking(k, place, day, time):
    movieinfo_frame.forget()
    SeatBookingFrame(k, place, day, time)


# TRANSISI DARI BOOKING MOVIE KE INFORMASI MOVIE
def BookingToInfo(k):
    booking_frame.forget()
    MovieInformationFrame(k)


MovieListFrame()

root.mainloop()
