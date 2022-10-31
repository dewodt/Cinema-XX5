# Program: Aplikasi Cinema
# 1. Dewantoro Triatmojo / 19622152
# 2. Randy Verdian / 19622202
# 3. Aira Ardistya Akbarsyah/ 16522062
# 4. Berto Togatorop/ 19622192

# Algoritma:
from itertools import count
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askyesno
from PIL import Image, ImageTk
import ast
import locale
import datetime
from database import *

# Define Date
today = datetime.date.today().strftime("%d-%m-%Y")
tomorrow =  (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")

# Define Time (Now)
time_now = datetime.datetime.now()
hour_minute_now = time_now.strftime("%H:%M")

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
center_x = (screen_width - 980) * 0.5

# Logo XX5
xx5_img = tk.PhotoImage(file="images/xx5.png")
img_xx5_heading = tk.PhotoImage(file="images/xx5heading.png")

# Array Image Movie
img = [tk.PhotoImage(file=list_movie[i]["img"]) for i in range(4)]
upcoming_img = [tk.PhotoImage(file=upcoming_movie[i]["img"]) for i in range(4)]

# Image Beberapa Pembayaran
logo_gopay = tk.PhotoImage(file="images/gopay.png")
logo_ovo = tk.PhotoImage(file="images/ovo.png")
logo_bca = tk.PhotoImage(file="images/bca.png")
logo_mandiri = tk.PhotoImage(file="images/mandiri.png")
logo_bni = tk.PhotoImage(file="images/bni.png")
logo_bri = tk.PhotoImage(file="images/bri.png")

# Image Kursi
seat_free = tk.PhotoImage(file="images/seat_free.png")
seat_own = tk.PhotoImage(file="images/seat_own.png")
seat_sold = tk.PhotoImage(file="images/seat_sold.png")

# Image Screen
screen_img = tk.PhotoImage(file="images/screen.png")

# Buttons On Hover
button1 = tk.PhotoImage(file="images/button1.png")
button2 = tk.PhotoImage(file="images/button2.png")

# Callback function bila box kosong
def onclick_entry(event, word):
    if event.widget.get() == f"{word}" and (event.widget.get() == "Password" or event.widget.get() == "Konfirmasi Password"):
        event.widget.delete(0, "end")
        event.widget.config(show="*")
    elif event.widget.get() == f"{word}":
        event.widget.delete(0, "end")

def onleave_entry(event, word):
    if (event.widget.get() == ""):
        event.widget.insert(0, f"{word}")
        event.widget.config(show="")

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


# FRAME LOGIN
def LoginFrame():
    global login_frame
    login_frame = tk.Frame(root, bg="#171a30")
    login_frame.pack()
    label_gambar = tk.Label(login_frame, image=xx5_img, border=0).pack()
    heading = tk.Label(login_frame, text="Login", fg="#eaebf1", bg="#171a30", font=("Roboto", 23, "bold")).pack(pady=10)

    # Email
    email = tk.Entry(login_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Roboto", 11))
    email.pack()
    email_border = tk.Frame(login_frame,width=295,height=2,bg="#eaebf1").pack(pady=(5, 20))
    email.insert(0, "Email")
    email.bind("<FocusIn>", lambda event: onclick_entry(event, "Email"))
    email.bind("<FocusOut>", lambda event: onleave_entry(event, "Email"))

    # Password
    pasw = tk.Entry(login_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Roboto", 11))
    pasw.pack()
    pasword_border = tk.Frame(login_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))
    pasw.insert(0, "Password")
    pasw.bind("<FocusIn>", lambda event: onclick_entry(event, "Password"))
    pasw.bind("<FocusOut>", lambda event: onleave_entry(event, "Password"))

    # Call Back FUnction Bila Klik Login
    def login():
        akun_email = email.get()
        akun_password = pasw.get()
        user_found = False
        for i in range(len(list_user)):
            if akun_email == list_user[i]['nama'] and akun_password == list_user[i]['password']:
                user_found = True
                global user_ke
                user_ke = i
                break
        if user_found:
            showinfo("Berhasil login", f"Selamat datang, {akun_email}!")
            LoginToList()
        else:
            showerror("Invalid", "Email atau password salah")
    
    # Register & Login Button
    tombol_login = tk.Button(login_frame, width=32, pady=7, activebackground="#fc094c", activeforeground="#eaebf1", text="Login", fg="#eaebf1", bg="#fc094c", cursor="hand2", command=login, font=("Roboto", 12)).pack(pady=(0, 5))
    noacc_frame = tk.Frame(login_frame, bg="#171a30")
    label_register = tk.Label(noacc_frame, text="Belum punya akun?", fg="#eaebf1", bg="#171a30", font=("Roboto", 9)).pack(side="left")
    tombol_register = tk.Button(noacc_frame, width=6, text="Register", border=0, cursor="hand2", bg="#171a30", fg="#b70e43", activebackground="#171a30", activeforeground="#b70e43", command=LoginToRegister).pack()
    noacc_frame.pack()


# REGISTER FRAME
def RegisterFrame():
    global register_frame
    register_frame = tk.Frame(root, bg="#171a30")
    register_frame.pack()

    def klik_register():
        nama_lengkap = nama.get()
        akun_email = email.get()
        akun_password = pasw.get()
        confirm = conf_pasw.get()
        if akun_password == confirm:
            dict = {
                "nama": nama_lengkap,
                "email": akun_email,
                "password": akun_password,
                "saldo": 0,
                "riwayat": []
            }
            read_file = open('database.py', 'r')
            content = read_file.read()
            old_list_user = str(list_user)
            list_user.append(dict)
            new_list_user = str(list_user)

            content = content.replace(old_list_user, new_list_user)
            read_file.close()

            write_file = open('database.py', 'w')
            write_file.write(content)
            write_file.close()

            showinfo("Register", "Registrasi berhasil!")
            RegisterToLogin()
        else:
            showerror("Invalid", "Password tidak cocok")

    label_gambar = tk.Label(register_frame, image=xx5_img, border=0).pack()
    heading = tk.Label(register_frame, text="Register", fg="#eaebf1", bg="#171a30", font=("Roboto", 23, "bold")).pack(pady=10)

    # Input nama lengkap
    nama = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Roboto", 11))
    nama.pack()
    nama.insert(0, "Nama Lengkap")
    nama.bind("<FocusIn>", lambda event: onclick_entry(event, "Nama Lengkap"))
    nama.bind("<FocusOut>", lambda event: onleave_entry(event, "Nama Lengkap"))
    frame2 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))

    # Input email
    email = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Roboto", 11))
    email.pack()
    email.insert(0, "Email")
    email.bind("<FocusIn>", lambda event: onclick_entry(event, "Email"))
    email.bind("<FocusOut>", lambda event: onleave_entry(event, "Email"))
    frame2 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))

    pasw = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Roboto", 11))
    pasw.pack()
    pasw.insert(0, "Password")
    pasw.bind("<FocusIn>", lambda event: onclick_entry(event, "Password"))
    pasw.bind("<FocusOut>", lambda event: onleave_entry(event, "Password"))
    frame3 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))

    conf_pasw = tk.Entry(register_frame, width=36, fg="#eaebf1", border=0, bg="#171a30", font=("Roboto", 11))
    conf_pasw.pack()
    conf_pasw.insert(0, "Konfirmasi Password")
    conf_pasw.bind("<FocusIn>", lambda event: onclick_entry(event, "Konfirmasi Password"))
    conf_pasw.bind("<FocusOut>", lambda event: onleave_entry(event, "Konfirmasi Password"))
    frame3 = tk.Frame(register_frame, width=295, height=2, bg="#eaebf1").pack(pady=(5, 20))

    tombol_register = tk.Button(register_frame, width=32, pady=7, text="Register", activebackground="#fc094c", activeforeground="#eaebf1", bg="#fc094c", fg="#eaebf1", cursor="hand2", command=klik_register, font=("Roboto", 12)).pack(pady=(0, 5))
    sudah_akun = tk.Frame(register_frame, bg="#171a30")
    ada_akun = tk.Label(sudah_akun, text="Saya sudah punya akun?", fg="#eaebf1", bg="#171a30", font=("Roboto", 9)).pack(side="left")
    tombol_login = tk.Button(sudah_akun, width=6, text="Login", border=0, bg="#171a30", cursor="hand2", fg="#b70e43", activebackground="#171a30", activeforeground="#b70e43", font=("Roboto", 9), command=RegisterToLogin).pack()
    sudah_akun.pack()


# FRAME HEADER
def HeaderFrame(frame):
    header_frame = tk.Frame(frame, bg="#171a30")
    header_frame.pack()

    # Left Frame (Logo, Now Playing, Upcoming)
    left_frame = tk.Frame(header_frame, bg="#171a30")
    left_frame.pack(side="left", padx=(0, 80))
    label_gambar = tk.Label(left_frame, image=img_xx5_heading, bg="#171a30").pack(side="left", padx=10)
    now_playing = tk.Button(left_frame, text="Now Playing", font=("arial", 14), command=lambda frame=frame: ToNowPlaying(frame)).pack(side="left", anchor="center", padx=10)
    up_coming = tk.Button(left_frame, text="Upcoming", font=("arial", 14), command=lambda frame=frame: ToUpcoming(frame)).pack(side="right",anchor="center", padx=10)

    # Right Frame (Saldo, Loglout, Name)
    right_frame = tk.Frame(header_frame, bg="#171a30")
    right_frame.pack(side="right", padx=(80, 0))
    topup = tk.Button(right_frame, text="Top Up", command=lambda frame=frame: ToSaldo(frame), font=("arial", 14)).pack(side="left", padx=10)
    riwayat = tk.Button(right_frame, text="Riwayat Pemesanan", font=("arial", 14), command=lambda frame=frame: ToRiwayat(frame)).pack(side="left", padx=10)
    logout = tk.Button(right_frame, text="Log Out", font=("arial", 14), command=lambda frame=frame: ClickLogOut(frame)).pack(side="left", padx=10)
    akun = tk.Label(right_frame, text=f"Halo {list_user[user_ke]['nama']}!", font=("arial", 14)).pack(side="right", padx=10)


# FRAME SALDO
def SaldoFrame():   
    # Fungsi Pengecek Validasi Pembayaran
    def isValid(price, method):
        if selected_method.get() == "N/A" or selected_price.get() == 0:
            showerror("Pilih Saldo/Metode!", f"Pilih saldo atau metode pembayaran yang benar!")
        else:
            if kode_valid.get() == list_validasi[price][method]:
                read_file = open('database.py', 'r')
                content = read_file.read()
                old_dict_user = str(list_user[user_ke])
                list_user[user_ke]['saldo'] += price
                new_dict_user = str(list_user[user_ke])
                content = content.replace(old_dict_user, new_dict_user)
                read_file.close()

                write_file = open('database.py', 'w')
                write_file.write(content)
                write_file.close()

                sisa_saldo.set(locale.currency(list_user[user_ke]['saldo'], grouping=True))
                showinfo("Top Up Berhasil!", f"Top up Anda sebesar {price} berhasil!")
                kode_valid.set("")
                selected_price.set(0)
                selected_method.set("N/A")
            else:
                showerror("Top Up Gagal!", f"Top up Anda gagal! Coba masukkan kode yang benar!")

    kode_valid = tk.StringVar()
    sisa_saldo = tk.StringVar()
    sisa_saldo.set(locale.currency(list_user[user_ke]['saldo'], grouping=True))

    global saldo_frame
    saldo_frame = tk.Frame(root, bg="#171a30")
    saldo_frame.pack()

    HeaderFrame(saldo_frame)

    # Saldo dan Nominal
    frame_nomimal = tk.Frame(saldo_frame, bg="#171a30", width=1000, height=600)
    frame_nomimal.pack()
    label_saldo = tk.Label(frame_nomimal, text="Saldo Anda: ", font=("Roboto", 20, "bold"), fg="white", bg="#171a30").pack(side="left")
    label_sisa_saldo = tk.Label(frame_nomimal, textvariable=sisa_saldo, font=("Roboto", 20, "bold"), fg="orange", bg="#171a30").pack()

    # Separator
    separator = ttk.Separator(saldo_frame, orient='horizontal').pack(fill='x', pady=10)

    # Tombol Memilih Nominal
    frame_pilih_nominal = tk.Frame(saldo_frame, background="#171a30")
    frame_pilih_nominal.pack(pady=15)
    selected_price = tk.IntVar(value=0)
    label_nominal_topup = tk.Label(frame_pilih_nominal, text="Pilih nominal top up", font=("Roboto", 16, "bold"), fg="white", bg="#171a30").pack()
    tombol_50ribu = tk.Radiobutton(frame_pilih_nominal, value=50000, variable=selected_price, text="Rp50.000,00", font=("Roboto", 16)).pack(side="left", padx=20)
    tombol_100ribu = tk.Radiobutton(frame_pilih_nominal, value=100000, variable=selected_price, text="Rp100.000,00", font=("Roboto", 16)).pack(side="left", padx=20)
    tombol_150ribu = tk.Radiobutton(frame_pilih_nominal, value=150000, variable=selected_price, text="Rp150.000,00", font=("Roboto", 16)).pack(side="left", padx=20)
    tombol_200ribu = tk.Radiobutton(frame_pilih_nominal, value=200000, variable=selected_price, text="Rp200.000,00", font=("Roboto", 16)).pack(padx=20)

    # Pilih Metode Pembayaran
    frame_pilih_pembayaran = tk.Frame(saldo_frame, background="#171a30")
    frame_pilih_pembayaran.pack(pady=15)
    selected_method = tk.StringVar(value="N/A")
    label_metode_pembayaran = tk.Label(frame_pilih_pembayaran, text="Metode pembayaran", font=("Roboto", 16, "bold"), fg="white", bg="#171a30").pack()
    tombol_gopay = tk.Radiobutton(frame_pilih_pembayaran, value="gopay", variable=selected_method, image=logo_gopay).pack(side="left", padx=15)
    tombol_ovo = tk.Radiobutton(frame_pilih_pembayaran, value="ovo", variable=selected_method, image=logo_ovo).pack(side="left", padx=15)
    tombol_bca = tk.Radiobutton(frame_pilih_pembayaran, value="bca", variable=selected_method, image=logo_bca).pack(side="left", padx=15)
    tombol_mandiri = tk.Radiobutton(frame_pilih_pembayaran, value="mandiri", variable=selected_method, image=logo_mandiri).pack(side="left", padx=15)
    tombol_bni = tk.Radiobutton(frame_pilih_pembayaran, value="bni", variable=selected_method, image=logo_bni).pack(side="left", padx=15)
    tombol_bri = tk.Radiobutton(frame_pilih_pembayaran, value="bri", variable=selected_method, image=logo_bri).pack(padx=15)

    # Masukkan Kode Validasi
    frame_validasi = tk.Frame(saldo_frame, background="#171a30")
    frame_validasi.pack(pady=15)
    label_kode = tk.Label(frame_validasi, text="Masukkan kode validasi: ", font=("Roboto", 14, "bold"), fg="white", bg="#171a30").pack()
    entry_kode = tk.Entry(frame_validasi, width=20, font=("Roboto", 14, "bold"), textvariable=kode_valid, show="*").pack()
    tombol_bayar = tk.Button(frame_validasi, text="Bayar", font=("Roboto", 16, "bold"), bg="#fc094c", command=lambda: isValid(selected_price.get(), selected_method.get())).pack()


# FRAME RIWAYAT
def FrameRiwayat():
    riwayat_frame = tk.Frame(root, bg="#171a30")
    riwayat_frame.pack()

    HeaderFrame(riwayat_frame)

    tabel_frame = tk.Frame(riwayat_frame, bg="#171a30")
    tabel_frame.pack()

    row_riwayat = len(list_user[user_ke]['riwayat'])
    tabel_frame.columnconfigure(6)
    tabel_frame.rowconfigure(row_riwayat+1)

    header = ["Tanggal Beli", "Lokasi", "Judul", "Jadwal", "Ticket", "Total"]
    for i in range(row_riwayat+1):
        if i == 0:
            for j in range(6):
                label = tk.Label(tabel_frame, text=header[j]).grid(row=i, column=j)
        else:
            for j in range(6):
                label = tk.Label(tabel_frame, text=list_user[user_ke]['riwayat'][i-1][header[j]]).grid(row=i, column=j) 


# FRAME LIST MOVIE
def MovieListFrame(list, image, func, title):
    # Frame Utama
    global movielist_frame
    movielist_frame = tk.Frame(root, background="#171a30", highlightbackground="red", highlightthickness=2)
    movielist_frame.pack()

    # Header
    HeaderFrame(movielist_frame)

    # Title Movie List
    movielist_title = tk.Label(movielist_frame, text=title, background="#171a30", font=("Roboto", "30", "bold"), fg="#eaebf1").pack(ipadx=10, ipady=10, pady=10)

    # Mencetak 4 Movie
    fourmovie_frame = tk.Frame(movielist_frame, bg="#171a30")
    fourmovie_frame.pack()
    
    for i in range(len(list)):
        movie_frame = tk.Frame(fourmovie_frame, background="#171a30")
        movie_img = tk.Button(movie_frame, image=image[i], cursor="hand2", background="#171a30", bd=0, command=lambda i=i: func(i), fg="#eaebf1")
        movie_img.bind("<Enter>", onHoverBorder)
        movie_img.bind("<Leave>", onLeaveBorder)
        movie_img.pack(ipadx=5, ipady=5)
        title_age_frame = tk.Frame(movie_frame, background="#fc094c")
        movie_title = tk.Label(title_age_frame, text=list[i]["title"], background="#fc094c", wraplength=190, font=("Helvatica", "18", "bold"), fg="#eaebf1").pack(pady=(5, 0))
        movie_age = tk.Label(title_age_frame, text=list[i]["age"], background="#fc094c", font=("Helvatica", "15"), fg="#eaebf1").pack(pady=(0, 5))
        title_age_frame.pack(pady=15, fill="x", ipadx=10)
        movie_frame.pack(padx=20, pady=10, side="left")


# FRAME INFORMASI MOVIE
def NowMovieInfoFrame(k):
    # Membuat Scrollbar
    global movieinfo_frame
    movieinfo_frame = tk.Frame(root, background="#171a30")
    movieinfo_frame.pack(fill="both", expand=1)

    # Header
    HeaderFrame(movieinfo_frame)

    my_canvas = tk.Canvas(movieinfo_frame, background="#171a30")
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(movieinfo_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Membuat Frame
    moviedesc_frame = tk.Frame(my_canvas, background="#171a30", highlightbackground="red", highlightthickness=2)

    my_canvas.create_window((center_x, 0), window=moviedesc_frame, anchor="nw")

    # Title, Genre, Duration
    titlegenre_frame = tk.Frame(moviedesc_frame, background="#171a30")
    titlegenre_frame.pack()
    moviedesc_title = tk.Label(titlegenre_frame, font=("Helvetica 18 bold"), text=list_movie[k]["title"], background="#171a30", fg="#eaebf1").pack()
    moviedesc_genre = tk.Label(titlegenre_frame, font=("Helvetica 14 bold"), text=list_movie[k]["genre"], background="#171a30", fg="#b70e43").pack()
    moviedesc_duration = tk.Label(titlegenre_frame, font=("Helvetica 14 bold"), text=list_movie[k]["duration"], background="#171a30", fg="#b70e43").pack()

    # Image
    img_and_buy_frame = tk.Frame(moviedesc_frame, background="#171a30")
    img_and_buy_frame.pack(anchor="w", padx=10, pady=10)
    movie_img = tk.Label(img_and_buy_frame, image=img[k], relief="flat", highlightthickness = 0, bd = 0).pack(side="left")

    # Buy Frame
    buy_frame = tk.Frame(img_and_buy_frame, background="#171a30")
    buy_frame.pack(side="right", padx=15)
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


    # Movie Plot
    movie_plot_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_plot_title = tk.Label(movie_plot_frame, text="Plot", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_plot = tk.Label(movie_plot_frame, wraplength=980, justify="left", text=list_movie[k]["plot"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_plot_frame.pack(anchor="w", padx=10, pady=10)

    # Movie Producer
    movie_prod_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_prod_title = tk.Label(movie_prod_frame, text="Producer", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_prod = tk.Label(movie_prod_frame, text=list_movie[k]["producer"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_prod_frame.pack(anchor="w", padx=10, pady=10)

    # Movie Director
    movie_director_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_director_title = tk.Label(movie_director_frame, text="Director", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_director = tk.Label(movie_director_frame, text=list_movie[k]["director"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_director_frame.pack(anchor="w", padx=10, pady=10)

    # Movie Writer
    movie_writer_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_writer_title = tk.Label(movie_writer_frame, text="Writer", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_writer = tk.Label(movie_writer_frame, text=list_movie[k]["writer"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_writer_frame.pack(anchor="w", padx=10, pady=10)
    # Movie Cast
    movie_cast_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_cast_title = tk.Label(movie_cast_frame, text="Cast", font=("Helvetica 13 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_cast = tk.Label(movie_cast_frame, wraplength=980, justify="left",text=list_movie[k]["cast"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_cast_frame.pack(anchor="w", padx=10, pady=10)


# FRAME UPCOMING MOVIE
def UpcomingMovieInfoFrame(k):
    # Membuat Scrollbar
    global upcoming_movie_frame
    upcoming_movie_frame = tk.Frame(root, background="#171a30")
    upcoming_movie_frame.pack(fill="both", expand=1)

    # Header
    HeaderFrame(upcoming_movie_frame)

    my_canvas = tk.Canvas(upcoming_movie_frame, background="#171a30")
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(upcoming_movie_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Membuat Frame
    moviedesc_frame = tk.Frame(my_canvas, background="#171a30", highlightbackground="red", highlightthickness=2)

    my_canvas.create_window((center_x, 0), window=moviedesc_frame, anchor="nw")

    # Title, Genre, Duration
    titlegenre_frame = tk.Frame(moviedesc_frame, background="#171a30")
    titlegenre_frame.pack()
    moviedesc_title = tk.Label(titlegenre_frame, font=("Helvetica 18 bold"), text=upcoming_movie[k]["title"], background="#171a30", fg="#eaebf1").pack()
    moviedesc_genre = tk.Label(titlegenre_frame, font=("Helvetica 14 bold"), text=upcoming_movie[k]["genre"], background="#171a30", fg="#b70e43").pack()
    moviedesc_duration = tk.Label(titlegenre_frame, font=("Helvetica 14 bold"), text=upcoming_movie[k]["duration"], background="#171a30", fg="#b70e43").pack()

    # Image
    img_and_buy_frame = tk.Frame(moviedesc_frame, background="#171a30")
    img_and_buy_frame.pack(anchor="w", padx=10, pady=10)
    movie_img = tk.Label(img_and_buy_frame, image=upcoming_img[k], relief="flat", highlightthickness = 0, bd = 0).pack(side="left")

    # Movie Plot
    movie_plot_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_plot_title = tk.Label(movie_plot_frame, text="Plot", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_plot = tk.Label(movie_plot_frame, wraplength=980, justify="left", text=upcoming_movie[k]["plot"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_plot_frame.pack(anchor="w", padx=10, pady=10)

    # Movie Producer
    movie_prod_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_prod_title = tk.Label(movie_prod_frame, text="Producer", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_prod = tk.Label(movie_prod_frame, text=upcoming_movie[k]["producer"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_prod_frame.pack(anchor="w", padx=10, pady=10)

    # Movie Director
    movie_director_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_director_title = tk.Label(movie_director_frame, text="Director", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_director = tk.Label(movie_director_frame, text=upcoming_movie[k]["director"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_director_frame.pack(anchor="w", padx=10, pady=10)

    # Movie Writer
    movie_writer_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_writer_title = tk.Label(movie_writer_frame, text="Writer", font=("Helvetica 12 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_writer = tk.Label(movie_writer_frame, text=upcoming_movie[k]["writer"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_writer_frame.pack(anchor="w", padx=10, pady=10)
    # Movie Cast
    movie_cast_frame = tk.Frame(moviedesc_frame, background="#171a30")
    movie_cast_title = tk.Label(movie_cast_frame, text="Cast", font=("Helvetica 13 bold"), background="#171a30", fg="#b70e43").pack(anchor=tk.W)
    movie_cast = tk.Label(movie_cast_frame, wraplength=980, justify="left",text=upcoming_movie[k]["cast"], background="#171a30", fg="#eaebf1", font=("Helvetica", "11", "bold")).pack(anchor=tk.W)
    movie_cast_frame.pack(anchor="w", padx=10, pady=10)


# FRAME SEAT BOOKING
def SeatBookingFrame(k, place, day, time):
    global booking_frame, count_seat
    booking_frame = tk.Frame(root, background="#171a30",highlightbackground="red", highlightthickness=2)

    # Header
    HeaderFrame(booking_frame)    

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

    price = list_movie[k]['price']
    str_total = tk.StringVar()
    str_total.set("Total Payment: Rp0")

    list_seat = []
    str_seat = "Seats: -"
    text_var_seat = tk.StringVar()
    text_var_seat.set(str_seat)

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

    picked_seat_ij = [[0 for j in range(15)] for i in range(9)]

    # Fungsi bila seat diklik
    def clicked_seat(par, i, j, x, y):
        global count_seat
        # Menambah Count Seat
        picked_seat = x + y
        if par.get() == 1:
            count_seat += 1
            list_seat.append(picked_seat)
            picked_seat_ij[i][j] = True
        elif par.get() == 0:
            count_seat -= 1
            list_seat.remove(picked_seat)
            picked_seat_ij[i][j] = False
        text_var_ticket.set(f"Tickets: {count_seat}")

        # Menambah Total Belanja
        str_total.set(f"Total Payment: {locale.currency(price*count_seat, grouping=True)}")

        # Mengolah list_seat agar menjadi string
        list_seat.sort()
        str_seat = "Seats: "+str(list_seat).replace("[", "").replace("]", "").replace("'", "")
        text_var_seat.set(str_seat)

        # Mengubah State & Cursor
        if count_seat > 0:
            confirm_button['state'] =  "normal"
            confirm_button['cursor'] = "hand2"
        else:
            confirm_button['state'] = "disabled"
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
                    x_seat = ""
                    if j < 7:
                        x_seat = str(j+1)
                    elif j > 7:
                        x_seat = str(j)
                    y_seat = f"{chr(ord('A')+i-1)}"
                    seat_var = tk.IntVar()
                    
                    # Check Button Seat
                    item = tk.Checkbutton(seat_frame, variable=seat_var, onvalue=1, offvalue=0, command=lambda num=seat_var, i=i, j=j, y=y_seat, x=x_seat: clicked_seat(num, i, j, y, x), indicatoron=False, image=seat_free, selectimage=seat_own, cursor="hand2", background="#171a30", selectcolor="#171a30", activebackground="#171a30")
                    item.bind('<Enter>', lambda event, imgs=seat_own: onHoverImage(event, imgs))
                    item.bind('<Leave>', lambda event, imgs=seat_free: onLeaveImage(event, imgs))
                    item.grid(row=i, column=j, padx=3, pady=3)

    screen = tk.Label(seat_frame, image=screen_img, background="#171a30").grid(row=11, column=0, columnspan=15)

    seat_frame.pack()

    # Separator
    separator = ttk.Separator(booking_frame, orient='horizontal').pack(fill='x', pady=10)

    def click_confirm():
        confirmation = askyesno(title='Confirmation', message='Are you sure of your purchase?')
        if confirmation:
            if list_user[user_ke]['saldo'] >= price*count_seat:
                # Edit Database User
                read_file = open('database.py', 'r')
                content = read_file.read()
                old_dict_user = str(list_user[user_ke])
                dict_riwayat = {
                    'Tanggal Beli': f"{hour_minute_now} {today}",
                    'Lokasi': place,
                    'Judul': list_movie[k]['title'],
                    'Jadwal': f"{time} {day}",
                    'Ticket': text_var_seat.get().replace("Seats: ", ""),
                    'Total': locale.currency(price*count_seat, grouping=True)
                }
                list_user[user_ke]['riwayat'].append(dict_riwayat)
                list_user[user_ke]['saldo'] -= price*count_seat
                new_dict_user = str(list_user[user_ke])
                content = content.replace(old_dict_user, new_dict_user)
                read_file.close()

                write_file = open('database.py', 'w')
                write_file.write(content)
                write_file.close()

                # Edit Database Seat
                for i in range(9):
                    for j in range(15):
                        append_file = open('database.py', 'a')
                        if picked_seat_ij[i][j] == True:
                            list_movie[k]['sold_seat'][place][day][time][i][j] = True
                            append_file.write(f"\nlist_movie[{k}]['sold_seat']['{place}']['{day}']['{time}'][{i}][{j}] = True")
                        append_file.close()

                # Transisi
                booking_frame.forget()
                MovieListFrame(list_movie, img, ListToNowMovieInfo, "Film Yang Sedang Tayang Di XX5")
            else:
                showerror("Kurang Saldo", "Anda kekurangan saldo! Silahkan toup terlebih dahulu")

    def click_cancel():
        booking_frame.forget()
        NowMovieInfoFrame(k)
        

    # Confirm and Cancel Button Frame
    button_frame = tk.Frame(booking_frame, background="#171a30")
    button_frame.rowconfigure(1)
    button_frame.columnconfigure(2)
    confirm_button = tk.Button(button_frame, text="Confirm Order", command=click_confirm, font=("Helvetica", "13", "bold"), bg="green", fg="#eaebf1", state="disabled")
    confirm_button.grid(row=0, column=0, padx=5, ipadx=28, ipady=8)
    cancel_button = tk.Button(button_frame, text="Cancel", command= click_cancel, font=("Helvetica", "13", "bold"), bg="red", fg="#eaebf1", cursor="hand2").grid(row=0, column=1, padx=5, ipadx=55, ipady=8)
    button_frame.pack()

    booking_frame.pack()


# TRANSISI LOGIN KE REGISTER
def LoginToRegister():
    login_frame.forget()
    RegisterFrame()

# TRANSISI REGISTER KE LOGIN
def RegisterToLogin():
    register_frame.forget()
    LoginFrame()

# TRANSISI LOGIN KE LIST MOVIE
def LoginToList():
    login_frame.forget()
    MovieListFrame(list_movie, img, ListToNowMovieInfo, "Film Yang Sedang Tayang Di XX5")


# HEADING NOW PLAYING
def ToNowPlaying(frame):
    frame.forget()
    MovieListFrame(list_movie, img, ListToNowMovieInfo, "Film Yang Sedang Tayang Di XX5")

# HEADING UPCOMING
def ToUpcoming(frame):
    frame.forget()
    MovieListFrame(upcoming_movie, upcoming_img, ListToUpcomingMovieInfo, "Film Akan Tayang Di XX5")

# HEADING SALDO
def ToSaldo(frame):
    frame.forget()
    SaldoFrame()

# HEADING RIWAYAT
def ToRiwayat(frame):
    frame.forget()
    FrameRiwayat()

# HEADING LOGOUT
def ClickLogOut(frame):
    confirmation = askyesno(title='Confirmation', message='Are you sure that you want to logout?')
    if confirmation:
        frame.forget()
        LoginFrame()


# TRANSISI DARI NOW LIST MOVIE KE INFORMASI MOVIE
def ListToNowMovieInfo(k):
    movielist_frame.forget()
    NowMovieInfoFrame(k)

# TRANSISI DARI LIST MOVIE UPCOMING KE INFORMASI MOVE
def ListToUpcomingMovieInfo(k):
    movielist_frame.forget()
    UpcomingMovieInfoFrame(k)

# TRANSISI DARI INFORMASI MOVIE KE BOOKING MOVIE
def InfoToBooking(k, place, day, time):
    movieinfo_frame.forget()
    SeatBookingFrame(k, place, day, time)


LoginFrame()

root.mainloop()
