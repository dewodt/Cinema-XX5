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

# Define Today and Tomorrow
today = datetime.date.today().strftime("%d-%m-%Y")
tomorrow =  (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")

# Set Locale (For Currency)
locale.setlocale( locale.LC_ALL, 'id-ID')

# Root Window
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Tubes Pengkom K16 Kelompok 5")
root.state('zoomed')

# Array Image
img = [tk.PhotoImage(file=list_movie[i]["img"]) for i in range(4)]
back_img = tk.PhotoImage(file="C:/Users/Dewo/Desktop/back.png")

# FRAME LIST MOVIE MINGGU INI
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
    # Mencari Posisi Center x
    root_width = root.winfo_screenwidth()
    pos_x = (root_width - 800) * 0.5

    # Membuat Scrollbar
    global main_frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side="left", fill="both", expand=1)

    scroll_bar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
    scroll_bar.pack(side="right", fill="y")

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Membuat Frame
    moviedesc_frame = tk.Frame(my_canvas, highlightbackground="blue", highlightthickness=2)
    moviedesc_frame.rowconfigure(9, weight=1)
    moviedesc_frame.columnconfigure(2, weight=1)

    my_canvas.create_window((pos_x, 0), window=moviedesc_frame, anchor="nw")

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

    # Buy Button
    buy_frame = tk.Frame(img_and_buy_frame, highlightbackground="blue", highlightthickness=2)
    buy_frame.rowconfigure(10, weight=1)
    buy_frame.columnconfigure(5, weight=1)

    buy_title = tk.Label(buy_frame, text="Buy Ticket", font="Helvetica 13 bold", background="red").grid(row=0, column=0, columnspan=5, sticky="w")
    for i in range(3):
        loc1_title = tk.Label(buy_frame, text=location[i], font="Helvetica 11 bold", background="red").grid(row=1+3*i, column=0, columnspan=5, sticky="w", pady=(10, 0))
        loc_1_date1 = tk.Label(buy_frame, text=today, font="Helvetica 10 bold").grid(row=2+3*i, column=0)
        loc1_date1_time1 = tk.Button(buy_frame, text="13:30", cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=1, ipadx=5, padx=5, pady= 2)
        loc1_date1_time2 = tk.Button(buy_frame, text="16:00", cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=2, ipadx=5, padx=5, pady= 2)
        loc1_date1_time3 = tk.Button(buy_frame, text="18:30", cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=3, ipadx=5, padx=5, pady= 2)
        loc1_date1_time4 = tk.Button(buy_frame, text="21:00", cursor="hand2", font="Helvetica 11 bold").grid(row=2+3*i, column=4, ipadx=5)

        loc_1_date1 = tk.Label(buy_frame, text=tomorrow, font="Helvetica 10 bold").grid(row=3+3*i, column=0)
        loc1_date2_time1 = tk.Button(buy_frame, text="13:30", cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=1, ipadx=5, padx=5, pady= 2)
        loc1_date2_time2 = tk.Button(buy_frame, text="16:00", cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=2, ipadx=5, padx=5, pady= 2)
        loc1_date2_time3 = tk.Button(buy_frame, text="18:30", cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=3, ipadx=5, padx=5, pady= 2)
        loc1_date2_time4 = tk.Button(buy_frame, text="21:00", cursor="hand2", font="Helvetica 11 bold").grid(row=3+3*i, column=4, ipadx=5)

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

def ListToInfo(k):
    movielist_frame.forget()
    MovieInformationFrame(k)

def InfoToList():
    main_frame.forget()
    movielist_frame.pack()


root.mainloop()
