import tkinter as tk
from tkinter import *

window=tk.Tk()
window.title("Saldo")
window.configure(bg="#171a30")
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

sisa_saldo=tk.StringVar()
kode_valid=tk.StringVar()
saldo=0
sisa_saldo.set(saldo)

def isValid_50rb():
    if kode_valid.get()=="050112233":
        global saldo
        saldo=saldo+50000
        sisa_saldo.set(saldo)
        label=tk.Label(frame1,text="Pembayaran berhasil!").place(x=450,y=540)
    else:
        label=tk.Label(frame1,text="Pembayaran gagal!").place(x=450,y=540)

def isValid_100rb():
    if kode_valid.get()=="100112233":
        global saldo
        saldo=saldo+100000
        sisa_saldo.set(saldo)
        label=tk.Label(frame1,text="Pembayaran berhasil!").place(x=450,y=540)
    else:
        label=tk.Label(frame1,text="Pembayaran gagal!").place(x=450,y=540)

def isValid_150rb():
    if kode_valid.get()=="150112233":
        global saldo
        saldo=saldo+150000
        sisa_saldo.set(saldo)
        label=tk.Label(frame1,text="Pembayaran berhasil!").place(x=450,y=540)
    else:
        label=tk.Label(frame1,text="Pembayaran gagal!").place(x=450,y=540)

def isValid_200rb():
    if kode_valid.get()=="200112233":
        global saldo
        saldo=saldo+200000
        sisa_saldo.set(saldo)
        label=tk.Label(frame1,text="Pembayaran berhasil!").place(x=450,y=540)
    else:
        label=tk.Label(frame1,text="Pembayaran gagal!").place(x=450,y=540)
        

def topup():
    label_nominal_topup=tk.Label(frame1,text="Pilih nominal top up",font=("Roboto",16,"bold"),fg="white",bg="#171a30").place(x=410,y=160)
    tombol_50ribu=tk.Button(frame1,text="Rp50.000,00",font=("Roboto",16),bg="#fc094c",command=top_50rb).place(x=150,y=215)
    tombol_100ribu=tk.Button(frame1,text="Rp100.000,00",font=("Roboto",16),bg="#fc094c",command=top_100rb).place(x=350,y=215)
    tombol_150ribu=tk.Button(frame1,text="Rp150.000,00",font=("Roboto",16),bg="#fc094c",command=top_150rb).place(x=550,y=215)
    tombol_200ribu=tk.Button(frame1,text="Rp200.000,00",font=("Roboto",16),bg="#fc094c",command=top_200rb).place(x=750,y=215)

def validasi_50rb():
    label_kode=tk.Label(frame1,text="Masukkan kode validasi: ",font=("Roboto",14,"bold"),fg="white",bg="#171a30").place(x=245,y=420)
    entry_kode=tk.Entry(frame1,width=20,font=("Roboto",14,"bold"),textvariable=kode_valid).place(x=500,y=420)
    tombol_bayar=tk.Button(frame1,text="Bayar",font=("Roboto",16,"bold"),command=isValid_50rb,bg="#fc094c").place(x=470,y=480)

def validasi_100rb():
    label_kode=tk.Label(frame1,text="Masukkan kode validasi: ",font=("Roboto",14,"bold"),fg="white",bg="#171a30").place(x=245,y=420)
    entry_kode=tk.Entry(frame1,width=20,font=("Roboto",14,"bold"),textvariable=kode_valid).place(x=500,y=420)
    tombol_bayar=tk.Button(frame1,text="Bayar",font=("Roboto",16,"bold"),command=isValid_100rb,bg="#fc094c").place(x=470,y=480)

def validasi_150rb():
    label_kode=tk.Label(frame1,text="Masukkan kode validasi: ",font=("Roboto",14,"bold"),fg="white",bg="#171a30").place(x=245,y=420)
    entry_kode=tk.Entry(frame1,width=20,font=("Roboto",14,"bold"),textvariable=kode_valid).place(x=500,y=420)
    tombol_bayar=tk.Button(frame1,text="Bayar",font=("Roboto",16,"bold"),command=isValid_150rb,bg="#fc094c").place(x=470,y=480)

def validasi_200rb():
    label_kode=tk.Label(frame1,text="Masukkan kode validasi: ",font=("Roboto",14,"bold"),fg="white",bg="#171a30").place(x=245,y=420)
    entry_kode=tk.Entry(frame1,width=20,font=("Roboto",14,"bold"),textvariable=kode_valid).place(x=500,y=420)
    tombol_bayar=tk.Button(frame1,text="Bayar",font=("Roboto",16,"bold"),command=isValid_200rb,bg="#fc094c").place(x=470,y=480)

def top_50rb():
    label_metode_pembayaran=tk.Label(frame1,text="Metode pembayaran",font=("Roboto",16,"bold"),fg="white",bg="#171a30").place(x=410,y=270)

    global logo_gopay
    global logo_ovo
    global logo_bca
    global logo_mandiri
    global logo_bni
    global logo_bri

    logo_gopay=tk.PhotoImage(file="logo gopay.png")
    tombol_gopay=tk.Button(frame1,image=logo_gopay,command=validasi_50rb).place(x=10,y=320)

    logo_ovo=tk.PhotoImage(file="logo ovo(1).png")
    tombol_ovo=tk.Button(frame1,image=logo_ovo,command=validasi_50rb).place(x=130,y=320)

    logo_bca=tk.PhotoImage(file="logo bca(1).png")
    tombol_bca=tk.Button(frame1,image=logo_bca,command=validasi_50rb).place(x=270,y=320)

    logo_mandiri=tk.PhotoImage(file="logo mandiri(1).png")
    tombol_mandiri=tk.Button(frame1,image=logo_mandiri,command=validasi_50rb).place(x=450,y=320)

    logo_bni=tk.PhotoImage(file="logo bni(1).png")
    tombol_bni=tk.Button(frame1,image=logo_bni,command=validasi_50rb).place(x=640,y=320)

    logo_bri=tk.PhotoImage(file="logo bri(1).png")
    tombol_bri=tk.Button(frame1,image=logo_bri,command=validasi_50rb).place(x=777,y=320)

def top_100rb():
    label_metode_pembayaran=tk.Label(frame1,text="Metode pembayaran",font=("Roboto",16,"bold"),fg="white",bg="#171a30").place(x=410,y=270)

    global logo_gopay
    global logo_ovo
    global logo_bca
    global logo_mandiri
    global logo_bni
    global logo_bri

    logo_gopay=tk.PhotoImage(file="logo gopay.png")
    tombol_gopay=tk.Button(frame1,image=logo_gopay,command=validasi_100rb).place(x=10,y=320)

    logo_ovo=tk.PhotoImage(file="logo ovo(1).png")
    tombol_ovo=tk.Button(frame1,image=logo_ovo,command=validasi_100rb).place(x=130,y=320)

    logo_bca=tk.PhotoImage(file="logo bca(1).png")
    tombol_bca=tk.Button(frame1,image=logo_bca,command=validasi_100rb).place(x=270,y=320)

    logo_mandiri=tk.PhotoImage(file="logo mandiri(1).png")
    tombol_mandiri=tk.Button(frame1,image=logo_mandiri,command=validasi_100rb).place(x=450,y=320)

    logo_bni=tk.PhotoImage(file="logo bni(1).png")
    tombol_bni=tk.Button(frame1,image=logo_bni,command=validasi_100rb).place(x=640,y=320)

    logo_bri=tk.PhotoImage(file="logo bri(1).png")
    tombol_bri=tk.Button(frame1,image=logo_bri,command=validasi_100rb).place(x=777,y=320)

def top_150rb():
    label_metode_pembayaran=tk.Label(frame1,text="Metode pembayaran",font=("Roboto",16,"bold"),fg="white",bg="#171a30").place(x=410,y=270)

    global logo_gopay
    global logo_ovo
    global logo_bca
    global logo_mandiri
    global logo_bni
    global logo_bri

    logo_gopay=tk.PhotoImage(file="logo gopay.png")
    tombol_gopay=tk.Button(frame1,image=logo_gopay,command=validasi_150rb).place(x=10,y=320)

    logo_ovo=tk.PhotoImage(file="logo ovo(1).png")
    tombol_ovo=tk.Button(frame1,image=logo_ovo,command=validasi_150rb).place(x=130,y=320)

    logo_bca=tk.PhotoImage(file="logo bca(1).png")
    tombol_bca=tk.Button(frame1,image=logo_bca,command=validasi_150rb).place(x=270,y=320)

    logo_mandiri=tk.PhotoImage(file="logo mandiri(1).png")
    tombol_mandiri=tk.Button(frame1,image=logo_mandiri,command=validasi_150rb).place(x=450,y=320)

    logo_bni=tk.PhotoImage(file="logo bni(1).png")
    tombol_bni=tk.Button(frame1,image=logo_bni,command=validasi_150rb).place(x=640,y=320)

    logo_bri=tk.PhotoImage(file="logo bri(1).png")
    tombol_bri=tk.Button(frame1,image=logo_bri,command=validasi_150rb).place(x=777,y=320)

def top_200rb():
    label_metode_pembayaran=tk.Label(frame1,text="Metode pembayaran",font=("Roboto",16,"bold"),fg="white",bg="#171a30").place(x=410,y=270)

    global logo_gopay
    global logo_ovo
    global logo_bca
    global logo_mandiri
    global logo_bni
    global logo_bri

    logo_gopay=tk.PhotoImage(file="logo gopay.png")
    tombol_gopay=tk.Button(frame1,image=logo_gopay,command=validasi_200rb).place(x=10,y=320)

    logo_ovo=tk.PhotoImage(file="logo ovo(1).png")
    tombol_ovo=tk.Button(frame1,image=logo_ovo,command=validasi_200rb).place(x=130,y=320)

    logo_bca=tk.PhotoImage(file="logo bca(1).png")
    tombol_bca=tk.Button(frame1,image=logo_bca,command=validasi_200rb).place(x=270,y=320)

    logo_mandiri=tk.PhotoImage(file="logo mandiri(1).png")
    tombol_mandiri=tk.Button(frame1,image=logo_mandiri,command=validasi_200rb).place(x=450,y=320)

    logo_bni=tk.PhotoImage(file="logo bni(1).png")
    tombol_bni=tk.Button(frame1,image=logo_bni,command=validasi_200rb).place(x=640,y=320)

    logo_bri=tk.PhotoImage(file="logo bri(1).png")
    tombol_bri=tk.Button(frame1,image=logo_bri,command=validasi_200rb).place(x=777,y=320)

frame1=tk.Frame(window,bg="#171a30",width=1000,height=600)
label_saldo=tk.Label(frame1,text="Saldo Anda: ",font=("Roboto",20,"bold"),fg="white",bg="#171a30").place(x=400,y=10)
label_sisa_saldo=tk.Label(frame1,textvariable=sisa_saldo,font=("Roboto",20,"bold"),fg="orange",bg="#171a30").place(x=600,y=10)
tombol_topup=tk.Button(frame1,text="Top Up",font=("Roboto",20,"bold"),bg="#fc094c",command=topup).place(x=450,y=90)



frame1.place(x=180,y=40)







window.mainloop()