import tkinter as tk
from database import list_movie

# Root Window
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title("Tubes Pengkom K16 Kelompok 5")
root.configure()

# Frame untuk List Movie Minggu Ini
movielist_frame = tk.Frame(root, highlightbackground="blue", highlightthickness=2)
movielist_frame.rowconfigure(3, weight=1)
movielist_frame.columnconfigure(4, weight=1)

# Title Movie List
movielist_title = tk.Label(movielist_frame, text="Film Sedang Tayang di XX5", background="green", font=("Arial, 30"))
movielist_title.grid(row=0, column=0, columnspan=5)

# Inisialisasi Array Image Label
img = ["" for i in range(len(list_movie))]

# Mencetak 4 Movie
for i in range(len(list_movie)):
    movie_frame = tk.Frame(movielist_frame, highlightbackground="blue", highlightthickness=2)
    img[i] = tk.PhotoImage(file=list_movie[i]["file"])
    movie_img = tk.Button(movie_frame, image=img[i], cursor="hand2", relief="flat").pack()
    movie_title = tk.Label(movie_frame, text=list_movie[i]["title"], background="red", font=("Arial, 18")).pack(fill="x")
    movie_age = tk.Label(movie_frame, text=list_movie[i]["age"], background="red", font=("Arial, 15")).pack(fill="x")
    movie_frame.grid(row=1, column=i, padx=10, pady=10)

movielist_frame.pack()

root.mainloop()