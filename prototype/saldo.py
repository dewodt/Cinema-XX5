import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

# Root Window
window = tk.Tk()
window.title("Saldo")
window.configure(bg="#171a30")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

# Variable String
sisa_saldo = tk.StringVar()
kode_valid = tk.StringVar()
saldo = 0
sisa_saldo.set(saldo)


# Logo Beberapa Pembayaran
logo_gopay = tk.PhotoImage(file="images/gopay.png")
logo_ovo = tk.PhotoImage(file="images/ovo.png")
logo_bca = tk.PhotoImage(file="images/bca.png")
logo_mandiri = tk.PhotoImage(file="images/mandiri.png")
logo_bni = tk.PhotoImage(file="images/bni.png")
logo_bri = tk.PhotoImage(file="images/bri.png")


# Data Token & Uang
list_validasi = {
    50000: {
            "gopay": "50gopay",
            "ovo": "050ovo",
            "bca": "050bca",
            "mandiri": "050mandiri",
            "bni": "050bni",
            "bri": "050bri",
        },
    100000: {
        "gopay": "100gopay",
        "ovo": "100ovo",
        "bca": "100bca",
        "mandiri": "100mandiri",
        "bni": "100bni",
        "bri": "100bri",
    },
    150000: {
        "gopay": "150gopay",
        "ovo": "150ovo",
        "bca": "150bca",
        "mandiri": "150mandiri",
        "bni": "150bni",
        "bri": "150bri",
    },
    200000: {
        "gopay": "200gopay",
        "ovo": "200ovo",
        "bca": "200bca",
        "mandiri": "200mandiri",
        "bni": "200bni",
        "bri": "200bri",
    }
}


# Fungsi Pengecek Validasi Pembayaran
def isValid(price, method):
    if kode_valid.get() == list_validasi[price][method]:
        global saldo
        saldo = saldo + price
        sisa_saldo.set(saldo)
        showinfo("Top Up Berhasil!", f"Top up Anda sebesar {price} berhasil!")
        kode_valid.set("")
        selected_price.set(0)
        selected_method.set("N/A")
    else:
        showerror("Top Up Gagal!", f"Top up Anda gagal! Coba masukkan kode yang benar!")


# Frmae atas
frame1 = tk.Frame(window, bg="#171a30", width=1000, height=600)
frame_saldo = tk.Frame(frame1)
label_saldo = tk.Label(frame_saldo, text="Saldo Anda: ", font=("Roboto", 20, "bold"), fg="white", bg="#171a30").pack(side="left")
label_sisa_saldo = tk.Label(frame_saldo, textvariable=sisa_saldo, font=("Roboto", 20, "bold"), fg="orange", bg="#171a30").pack()
frame_saldo.pack()
frame1.pack(pady=5)

# Separator
separator = ttk.Separator(window, orient='horizontal').pack(fill='x', pady=10)

# Fungsi Tombol Memilih Nominal
frame_pilih_nominal = tk.Frame(window, background="#171a30")
selected_price = tk.IntVar(value=0)
tombol_topup = tk.Label(frame_pilih_nominal, text="Top Up Saldo", font=("Roboto", 20, "bold"), bg="#fc094c").pack()
label_nominal_topup = tk.Label(frame_pilih_nominal, text="Pilih nominal top up", font=("Roboto", 16, "bold"), fg="white", bg="#171a30").pack()
tombol_50ribu = tk.Radiobutton(frame_pilih_nominal, value=50000, variable=selected_price, text="Rp50.000,00", font=("Roboto", 16)).pack(side="left", padx=20)
tombol_100ribu = tk.Radiobutton(frame_pilih_nominal, value=100000, variable=selected_price, text="Rp100.000,00", font=("Roboto", 16)).pack(side="left", padx=20)
tombol_150ribu = tk.Radiobutton(frame_pilih_nominal, value=150000, variable=selected_price, text="Rp150.000,00", font=("Roboto", 16)).pack(side="left", padx=20)
tombol_200ribu = tk.Radiobutton(frame_pilih_nominal, value=200000, variable=selected_price, text="Rp200.000,00", font=("Roboto", 16)).pack(padx=20)
frame_pilih_nominal.pack(pady=15)


# Pilih Metode Pembayaran
frame_pilih_pembayaran = tk.Frame(window, background="#171a30")
selected_method = tk.StringVar(value="N/A")
label_metode_pembayaran = tk.Label(frame_pilih_pembayaran, text="Metode pembayaran", font=("Roboto", 16, "bold"), fg="white", bg="#171a30").pack()
tombol_gopay = tk.Radiobutton(frame_pilih_pembayaran, value="gopay", variable=selected_method, image=logo_gopay).pack(side="left", padx=15)
tombol_ovo = tk.Radiobutton(frame_pilih_pembayaran, value="ovo", variable=selected_method, image=logo_ovo).pack(side="left", padx=15)
tombol_bca = tk.Radiobutton(frame_pilih_pembayaran, value="bca", variable=selected_method, image=logo_bca).pack(side="left", padx=15)
tombol_mandiri = tk.Radiobutton(frame_pilih_pembayaran, value="mandiri", variable=selected_method, image=logo_mandiri).pack(side="left", padx=15)
tombol_bni = tk.Radiobutton(frame_pilih_pembayaran, value="bni", variable=selected_method, image=logo_bni).pack(side="left", padx=15)
tombol_bri = tk.Radiobutton(frame_pilih_pembayaran, value="bri", variable=selected_method, image=logo_bri).pack(padx=15)
frame_pilih_pembayaran.pack(pady=15)


# Masukkan Kode Validasi
frame_validasi = tk.Frame(window, background="#171a30")
label_kode = tk.Label(frame_validasi, text="Masukkan kode validasi: ", font=("Roboto", 14, "bold"), fg="white", bg="#171a30").pack()
entry_kode = tk.Entry(frame_validasi, width=20, font=("Roboto", 14, "bold"), textvariable=kode_valid, show="*").pack()
tombol_bayar = tk.Button(frame_validasi, text="Bayar", font=("Roboto", 16, "bold"), bg="#fc094c", command=lambda: isValid(selected_price.get(), selected_method.get())).pack()
frame_validasi.pack(pady=15)

window.mainloop()
