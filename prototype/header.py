import tkinter as tk

window = tk.Tk()
window.title("Cinema XX5")

img_xx5_heading = tk.PhotoImage(file="images/xx5heading.png")

def HeaderFrame():
    header_frame = tk.Frame(window, width=1200, bg="#171a30")
    header_frame.pack(fill="x")
    # Left Frame (Logo, Now Playing, Upcoming)
    left_frame = tk.Frame(header_frame, bg="#171a30")
    left_frame.pack(side="left")
    label_gambar = tk.Label(left_frame, image=img_xx5_heading, bg="#171a30").pack(side="left", padx=10)
    now_playing = tk.Button(left_frame, text="Now Playing", font=("arial", 16)).pack(side="left", anchor="center", padx=10)
    up_coming = tk.Button(left_frame, text="Up Coming", font=("arial", 16)).pack(side="right",anchor="center", padx=10)

    # Right Frame (Saldo, Loglout, Name)
    right_frame = tk.Frame(header_frame, bg="#171a30")
    right_frame.pack(side="right")
    saldo = tk.Button(right_frame, text="Rp100.000,00", font=("arial", 16)).pack(side="left", padx=10)
    logout = tk.Button(right_frame, text="Log Out", font=("arial", 16)).pack(side="left", padx=10)
    akun = tk.Label(right_frame, text="Erling Haaland", font=("arial", 16)).pack(side="right", padx=10)

HeaderFrame()

window.mainloop()
