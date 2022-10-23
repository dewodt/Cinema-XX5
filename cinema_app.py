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

# FRAME LIST MOVIE
def MovieListFrame():
    # Frame Utama
    global movielist_frame
    movielist_frame = tk.Frame(root, highlightbackground="blue", highlightthickness=2)
    movielist_frame.rowconfigure(3, weight=1)
    movielist_frame.columnconfigure(4, weight=1)

    # Title Movie List
    movielist_title = tk.Label(movielist_frame, text="Film Sedang Tayang di XX5", background="green", font=("Arial, 30"))
    movielist_title.grid(row=0, column=0, columnspan=5)

    # Mencetak 4 Movie
    for i in range(len(list_movie)):
        movie_frame = tk.Frame(movielist_frame, highlightbackground="blue", highlightthickness=2)
        movie_img = tk.Button(movie_frame, image=img[i], cursor="hand2", relief="flat", command=lambda i=i: ListToInfo(i)).pack()
        movie_title = tk.Label(movie_frame, text=list_movie[i]["title"], background="red", font=("Arial, 18")).pack(fill="x")
        movie_age = tk.Label(movie_frame, text=list_movie[i]["age"], background="red", font=("Arial, 15")).pack(fill="x")
        movie_frame.grid(row=1, column=i, padx=10, pady=10)

    movielist_frame.pack()


# FRAME INFORMASI MOVIE
def MovieInformationFrame(k):
    # Membuat Scrollbar
    global movieinfo_frame
    movieinfo_frame = tk.Frame(root)
    movieinfo_frame.pack(fill="both", expand=1)

    my_canvas = tk.Canvas(movieinfo_frame)
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(movieinfo_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Membuat Frame
    moviedesc_frame = tk.Frame(my_canvas, highlightbackground="blue", highlightthickness=2)
    moviedesc_frame.rowconfigure(9, weight=1)
    moviedesc_frame.columnconfigure(2, weight=1)

    my_canvas.create_window((center_x, 0), window=moviedesc_frame, anchor="nw")

    # Back Button
    back_button = tk.Button(moviedesc_frame, image=back_img, command=InfoToList).grid(row=0, column=0, columnspan=2, sticky="nw")

    # Title, Genre, Duration
    titlegenre_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
    moviedesc_title = tk.Label(titlegenre_frame, font=("Helvetica 15 bold"),  text=list_movie[k]["title"]).pack()
    moviedesc_genre = tk.Label(titlegenre_frame, font=("Helvetica 13 bold"), text=list_movie[k]["genre"]).pack()
    moviedesc_duration = tk.Label(titlegenre_frame, font=("Helvetica 13 bold"), text=list_movie[k]["duration"]).pack()
    titlegenre_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Image
    img_and_buy_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
    movie_img = tk.Label(img_and_buy_frame, image=img[k], relief="flat", highlightbackground="blue", highlightthickness=2).pack(side="left")

    # Buy Frame
    buy_frame = tk.Frame(img_and_buy_frame, highlightbackground="blue", highlightthickness=2)
    buy_frame.rowconfigure(10, weight=1)
    buy_frame.columnconfigure(5, weight=1)
    
    buy_title = tk.Label(buy_frame, text="Buy Ticket", font="Helvetica 13 bold", background="red").grid(row=0, column=0, columnspan=5, sticky="w")
    
    # Cek jika pemesanan tiket melebihi waktu tayang
    def CekDisabled(hour, minute):
        time = time_now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if time_now >= time:
            return "disabled"
        else:
            return "normal"        
    
    # Looping 3 Lokasi
    for i in range(3):
        loc_title = tk.Label(buy_frame, text=location[i], font="Helvetica 11 bold", background="red").grid(row=1+3*i, column=0, columnspan=5, sticky="w", pady=(10, 0))
        today_label = tk.Label(buy_frame, text=today, font="Helvetica 10 bold").grid(row=2+3*i, column=0)
        today_time1 = tk.Button(buy_frame, text="13:30", state=CekDisabled(13, 30), command=lambda i=i: InfoToBooking(k, location[i], "today", "13:30"), cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=1, ipadx=5, padx=5, pady= 2)
        today_time2 = tk.Button(buy_frame, text="16:00", state=CekDisabled(16, 0), command=lambda i=i: InfoToBooking(k, location[i], "today", "16:00"), cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=2, ipadx=5, padx=5, pady= 2)
        today_time3 = tk.Button(buy_frame, text="18:30", state=CekDisabled(18, 30), command=lambda i=i: InfoToBooking(k, location[i], "today", "18:30"), cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=3, ipadx=5, padx=5, pady= 2)
        today_time4 = tk.Button(buy_frame, text="21:00", state=CekDisabled(21, 0), command=lambda i=i: InfoToBooking(k, location[i], "today", "21:00"), cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=4, ipadx=5)

        tomorrow_label = tk.Label(buy_frame, text=tomorrow, font="Helvetica 10 bold").grid(row=3+3*i, column=0)
        tomorrow_time1 = tk.Button(buy_frame, text="13:30", command=lambda i=i: InfoToBooking(k, location[i], "tomorrow", "13:30"), cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=1, ipadx=5, padx=5, pady= 2)
        tomorrow_time2 = tk.Button(buy_frame, text="16:00", command=lambda i=i: InfoToBooking(k, location[i], "tomorrow", "16:00"), cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=2, ipadx=5, padx=5, pady= 2)
        tomorrow_time3 = tk.Button(buy_frame, text="18:30", command=lambda i=i: InfoToBooking(k, location[i], "tomorrow", "18:30"), cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=3, ipadx=5, padx=5, pady= 2)
        tomorrow_time4 = tk.Button(buy_frame, text="21:00", command=lambda i=i: InfoToBooking(k, location[i], "tomorrow", "21:00"), cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=4, ipadx=5)

    buy_frame.pack(side="right", padx=15)

    img_and_buy_frame.grid(row=2, column=0, sticky="w", padx=10)

    # Movie Plot
    movie_plot_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
    movie_plot_title = tk.Label(movie_plot_frame, text="Plot", font=("Helvetica 12 bold")).pack(anchor=tk.W)
    movie_plot = tk.Label(movie_plot_frame, wraplength=800, justify="left", text=list_movie[k]["plot"]).pack(anchor=tk.W)
    movie_plot_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

    # Movie Producer
    movie_prod_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
    movie_prod_title = tk.Label(movie_prod_frame, text="Producer", font=("Helvetica 12 bold")).pack(anchor=tk.W)
    movie_prod = tk.Label(movie_prod_frame, text=list_movie[k]["producer"]).pack(anchor=tk.W)
    movie_prod_frame.grid(row=4, column=0, sticky="we", padx=10, pady=10)

    # Movie Director
    movie_director_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
    movie_director_title = tk.Label(movie_director_frame, text="Director", font=("Helvetica 12 bold")).pack(anchor=tk.W)
    movie_director = tk.Label(movie_director_frame, text=list_movie[k]["director"]).pack(anchor=tk.W)
    movie_director_frame.grid(row=5, column=0, sticky="we", padx=10, pady=10)

    # Movie Writer
    movie_writer_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
    movie_writer_title = tk.Label(movie_writer_frame, text="Writer", font=("Helvetica 12 bold")).pack(anchor=tk.W)
    movie_writer = tk.Label(movie_writer_frame, text=list_movie[k]["writer"]).pack(anchor=tk.W)
    movie_writer_frame.grid(row=6, column=0, sticky="we", padx=10, pady=10)

    # Movie Cast
    movie_cast_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
    movie_cast_title = tk.Label(movie_cast_frame, text="Cast", font=("Helvetica 12 bold")).pack(anchor=tk.W)
    movie_cast = tk.Label(movie_cast_frame, wraplength=800, justify="left",text=list_movie[k]["cast"]).pack(anchor=tk.W)
    movie_cast_frame.grid(row=7, column=0, sticky="we", padx=10, pady=10)


# FRAME SEAT BOOKING
def SeatBookingFrame(k, place, day, time):
    global count_seat, list_seat, str_seat, booking_frame
    # Main Frame
    booking_frame = tk.Frame(root, highlightbackground="blue", highlightthickness=2)

    # Information Frame
    information_frame = tk.Frame(booking_frame, highlightbackground="blue", highlightthickness=2)

    # Seat Icons
    icon_frame = tk.Frame(information_frame)
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
    book_title = tk.Label(data_frame, text=list_movie[k]["title"]).pack(anchor=tk.W)
    seat_list = tk.Label(data_frame, textvariable=text_var_seat, wraplength=510, justify="left").pack(anchor=tk.W)
    num_ticket = tk.Label(data_frame, textvariable=text_var_ticket).pack(anchor=tk.W)
    location = tk.Label(data_frame, text=place).pack(anchor=tk.W)
    studio = tk.Label(data_frame, text=f"Studio: {k+1}").pack(anchor=tk.W)
    if day == "today":
        date = tk.Label(data_frame, text=f"{today}, Time: {time}").pack(anchor=tk.W)
    elif day == "tomorrow":
        date = tk.Label(data_frame, text=f"{tomorrow}, Time: {time}").pack(anchor=tk.W)
    total = tk.Label(data_frame, textvariable=str_total).pack(anchor=tk.W)
    data_frame.pack(anchor=tk.W)

    information_frame.pack(anchor="w", fill="x")

    # Seats Frame
    seat_frame = tk.Frame(booking_frame, highlightbackground="blue", highlightthickness=2)
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
                    item = tk.Label(seat_frame, text=f"{j+1}").grid(row=i, column=j)
                elif j > 7:
                    item = tk.Label(seat_frame, text=f"{j}").grid(row=i, column=j)
            elif j == 7: # Cetak Huruf
                item = tk.Label(seat_frame, text=f"{chr(ord('A')+i-1)}").grid(row=i, column=j)
            else: # Cetak Kursi
                if list_movie[k]["sold_seat"][place][day][time][i][j]: # Jika Sold
                    item = tk.Label(seat_frame, image=seat_sold).grid(row=i, column=j)
                else: # Jika Available
                    # Penentu Kode Seat
                    if j < 7:
                        x_seat = str(j+1)
                    elif j > 7:
                        x_seat = str(j)
                    y_seat = f"{chr(ord('A')+i-1)}"
                    seat_var = tk.IntVar()
                    
                    # Check Button Seat
                    item = tk.Checkbutton(seat_frame, variable=seat_var, onvalue=1, offvalue=0, command=lambda num=seat_var, i=y_seat, j=x_seat: clicked_seat(num, i, j), indicatoron=False, image=seat_free, selectimage=seat_own, cursor="hand2")
                    item.grid(row=i, column=j, padx=3, pady=3)

    screen = tk.Label(seat_frame, text="SCREEN", font=("Arial, 18")).grid(row=11, column=0, columnspan=15, pady=(10,0))

    seat_frame.pack()

    # Seperator
    separator = ttk.Separator(booking_frame, orient='horizontal').pack(fill='x', pady=5)

    # Confirm and Cancel Button Frame
    button_frame = tk.Frame(booking_frame, highlightbackground="blue", highlightthickness=2)
    button_frame.rowconfigure(1)
    button_frame.columnconfigure(2)
    confirm_button = tk.Button(button_frame, text="Confirm Order", command="", font=("Arial, 13"), bg="green", state=tk.DISABLED)
    confirm_button.grid(row=0, column=0, padx=5, ipadx=28, ipady=12)
    cancel_button = tk.Button(button_frame, text="Cancel", command=lambda: BookingToInfo(k), font=("Arial, 13"), bg="red", cursor="hand2").grid(row=0, column=1, padx=5, ipadx=55, ipady=12)
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
