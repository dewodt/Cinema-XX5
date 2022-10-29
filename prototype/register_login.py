import tkinter as tk
from tkinter import messagebox
import ast

# Main Window
root = tk.Tk()
root.title("Portal Login")
root.configure(bg="#171a30")

# Logo XX5
xx5_img = tk.PhotoImage(file="images/xx5.png")

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

# Frame Login
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

        file = open("database.txt", "r")
        d = file.read()
        r = ast.literal_eval(d)
        file.close()

        if akun_email in r.keys() and akun_password == r[akun_email]:
            messagebox.showinfo("Berhasil login", f"Selamat datang, {akun_email}!")
        else:
            messagebox.showerror("Invalid", "Email atau password salah")
    
    # Register & Login Button
    tombol_login = tk.Button(login_frame, width=32, pady=7, activebackground="#fc094c", activeforeground="#eaebf1", text="Login", fg="#eaebf1", bg="#fc094c", cursor="hand2", command=login, font=("Roboto", 12)).pack(pady=(0, 5))
    noacc_frame = tk.Frame(login_frame, bg="#171a30")
    label_register = tk.Label(noacc_frame, text="Belum punya akun?", fg="#eaebf1", bg="#171a30", font=("Roboto", 9)).pack(side="left")
    tombol_register = tk.Button(noacc_frame, width=6, text="Register", border=0, cursor="hand2", bg="#171a30", fg="#b70e43", activebackground="#171a30", activeforeground="#b70e43", command=LoginToRegister).pack()
    noacc_frame.pack()

# Frame Register
def RegisterFrame():
    global register_frame
    register_frame = tk.Frame(root, bg="#171a30")
    register_frame.pack()

    def klik_register():
        akun_email = email.get()
        akun_password = pasw.get()
        confirm = conf_pasw.get()
        if akun_password == confirm:
            try:
                file = open("database.txt", "r+")
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {akun_email:akun_password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open("database.txt", "w")
                w = file.write(str(r))

                messagebox.showinfo("Register", "Registrasi berhasil!")
                RegisterToLogin()
                # window.destroy()

            except:
                file = open("database.txt", "w")
                pp = str({"email":"password"})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror("Invalid", "Password tidak cocok")

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

def LoginToRegister():
    login_frame.forget()
    RegisterFrame()

def RegisterToLogin():
    register_frame.forget()
    LoginFrame()

LoginFrame()

root.mainloop()