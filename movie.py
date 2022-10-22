import tkinter as tk
from tkinter import ttk
import datetime

# Format Todays and Tomorrows Date
today = datetime.date.today().strftime("%d-%m-%Y")
tomorrow =  (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")

# Root Window
root = tk.Tk()
root.title("Tubes Pengkom K16 Kelompok 5")
root.state('zoomed')

# Mencari Posisi Center x
root_width = root.winfo_screenwidth()
pos_x = (root_width - 800) * 0.5

# Membuat Scrollbar
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
moviedesc_frame.rowconfigure(8, weight=1)
moviedesc_frame.columnconfigure(2, weight=1)

my_canvas.create_window((pos_x, 0), window=moviedesc_frame, anchor="nw")

# Title, Genre, Duration
titlegenre_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
moviedesc_title = tk.Label(titlegenre_frame, font=("Helvetica 15 bold"),  text="Black Adam").pack()
moviedesc_genre = tk.Label(titlegenre_frame, font=("Helvetica 13 bold"), text="Action, Fantasy, Sci-fi").pack()
moviedesc_duration = tk.Label(titlegenre_frame, font=("Helvetica 13 bold"), text="125 Minutes").pack()
titlegenre_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Image
img_and_buy_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
img11 = tk.PhotoImage(file="C:/Users/Dewo/Desktop/22BADM.png")
movie11_img = tk.Label(img_and_buy_frame, image=img11, relief="flat", highlightbackground="blue", highlightthickness=2).pack(side="left")

# Buy Button
buy_frame = tk.Frame(img_and_buy_frame, highlightbackground="blue", highlightthickness=2)
buy_frame.rowconfigure(10, weight=1)
buy_frame.columnconfigure(5, weight=1)

# temporary array
location =  ["XX5 Aeon Mall BSD", "XX5 Ciwalk Bandung", "Plaza Indonesia"]

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

img_and_buy_frame.grid(row=1, column=0, sticky="w", padx=10)

# Movie Plot
movie_plot_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
movie_plot_title = tk.Label(movie_plot_frame, text="Plot", font=("Helvetica 12 bold")).pack(anchor=tk.W)
movie_plot = tk.Label(movie_plot_frame, wraplength=800, justify="left", text="Berkisah tentang sosok antihero yang mendapatkan kekuatan dari dewa mesir bernama Adam. Ia datang untuk menciptakan keadilan di dunia saat ini.").pack(anchor=tk.W)
movie_plot_frame.grid(row=2, column=0, sticky="we", padx=10, pady=10)

# Movie Producer
movie_prod_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
movie_prod_title = tk.Label(movie_prod_frame, text="Ploducer", font=("Helvetica 12 bold")).pack(anchor=tk.W)
movie_prod = tk.Label(movie_prod_frame, text="Beau Flynn, Dany Garcia, Hiram Garcia").pack(anchor=tk.W)
movie_prod_frame.grid(row=3, column=0, sticky="we", padx=10, pady=10)

# Movie Director
movie_director_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
movie_director_title = tk.Label(movie_director_frame, text="Director", font=("Helvetica 12 bold")).pack(anchor=tk.W)
movie_director = tk.Label(movie_director_frame, text="Jaume Collet-Serra").pack(anchor=tk.W)
movie_director_frame.grid(row=4, column=0, sticky="we", padx=10, pady=10)

# Movie Writer
movie_writer_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
movie_writer_title = tk.Label(movie_writer_frame, text="Writer", font=("Helvetica 12 bold")).pack(anchor=tk.W)
movie_writer = tk.Label(movie_writer_frame, text="Adam Sztykiel, Rory Haines, Sohrab Noshirvani").pack(anchor=tk.W)
movie_writer_frame.grid(row=5, column=0, sticky="we", padx=10, pady=10)

# Movie Cast
movie_cast_frame = tk.Frame(moviedesc_frame, highlightbackground="blue", highlightthickness=2)
movie_cast_title = tk.Label(movie_cast_frame, text="Cast", font=("Helvetica 12 bold")).pack(anchor=tk.W)
movie_cast = tk.Label(movie_cast_frame, wraplength=800, justify="left",text="Dwayne Johnson, Viola Davis, Sarah Shahi, Pierce Brosnan, Noah Centineo, Aldis Hodge, Angel Rosario Jr., Joseph Gatt, Mohammed Amer, Quintessa Swindell").pack(anchor=tk.W)
movie_cast_frame.grid(row=6, column=0, sticky="we", padx=10, pady=10)

root.mainloop()