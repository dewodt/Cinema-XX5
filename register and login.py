import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast


root=tk.Tk()
root.title("Portal Login")
root.configure(bg="white")
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


#fungsi
def login():
    akun_email=email.get()
    akun_password=pasw.get()

    file=open("database.txt","r")
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    #print(r.keys())
    #print(r.values())

    if akun_email in r.keys() and akun_password==r[akun_email]:
        messagebox.showinfo("Berhasil login",f"Selamat datang, {akun_email}!")
    else:
        messagebox.showerror("Invalid","Email atau password salah")

####################################### menu register
def mau_register():
    window=Toplevel(root)
    window.title("Register")
    window.configure(bg="white")
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")

    #fungsi
    def register():
        akun_email=email.get()
        akun_password=pasw.get()
        confirm=conf_pasw.get()
        if akun_password==confirm:
            try:
                file=open("database.txt","r+")
                d=file.read()
                r=ast.literal_eval(d)

                dict2={akun_email:akun_password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open("database.txt","w")
                w=file.write(str(r))

                messagebox.showinfo("Register","Registrasi berhasil!")
                window.destroy()

            except:
                file=open("database.txt","w")
                pp=str({"email":"password"})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror("Invalid","Password tidak cocok")


    frame1=tk.Frame(window,width=400,height=430,bg="white")
    frame1.place(x=520,y=190)

    image = Image.open("images/logo xx5.png")
    resize_image = image.resize((346,150))
    img = ImageTk.PhotoImage(resize_image)
    label_gambar=tk.Label(window,image=img,border=0).place(x=500,y=40)

    heading=tk.Label(frame1,text="Register",fg="#8BBCCC",bg="white",font=("Roboto",23,"bold"))
    heading.place(x=120,y=5)

    #input nama lengkap
    def on_enter(x):
        nama.delete(0,"end")

    def on_leave(x):
        if (nama.get()==""):
            nama.insert(0,"Nama Lengkap")

    nama=tk.Entry(frame1,width=25,fg="black",border=0,bg="white",font=("Roboto",11))
    nama.place(x=30,y=80)
    nama.insert(0,"Nama Lengkap")
    nama.bind("<FocusIn>",on_enter)
    nama.bind("<FocusOut>",on_leave)
    frame2=tk.Frame(frame1,width=295,height=2,bg="black").place(x=25,y=107)

    #input email
    def on_enter(x):
        email.delete(0,"end")

    def on_leave(x):
        if (email.get()==""):
            email.insert(0,"Email")

    email=tk.Entry(frame1,width=25,fg="black",border=0,bg="white",font=("Roboto",11))
    email.place(x=30,y=150)
    email.insert(0,"Email")
    email.bind("<FocusIn>",on_enter)
    email.bind("<FocusOut>",on_leave)
    frame2=tk.Frame(frame1,width=295,height=2,bg="black").place(x=25,y=177)

    def login_ok():
        window.destroy()


    #input password
    def on_enter(x):
        pasw.delete(0,"end")

    def on_leave(x):
        if (pasw.get()==""):
            pasw.insert(0,"Password")

    pasw=tk.Entry(frame1,width=25,fg="black",border=0,bg="white",font=("Roboto",11))
    pasw.place(x=30,y=220)
    pasw.insert(0,"Password")
    pasw.bind("<FocusIn>",on_enter)
    pasw.bind("<FocusOut>",on_leave)
    frame3=tk.Frame(frame1,width=295,height=2,bg="black").place(x=25,y=247)

    #input confirm password
    def on_enter(x):
        conf_pasw.delete(0,"end")

    def on_leave(x):
        if (conf_pasw.get()==""):
            conf_pasw.insert(0,"Konfirmasi Password")

    conf_pasw=tk.Entry(frame1,width=25,fg="black",border=0,bg="white",font=("Roboto",11))
    conf_pasw.place(x=30,y=290)
    conf_pasw.insert(0,"Konfirmasi Password")
    conf_pasw.bind("<FocusIn>",on_enter)
    conf_pasw.bind("<FocusOut>",on_leave)
    frame3=tk.Frame(frame1,width=295,height=2,bg="black").place(x=25,y=317)

    tombol_register=tk.Button(frame1,width=41,pady=7,text="Register",bg="#F96666",cursor="hand2",fg="white",border=0,command=register).place(x=25,y=350)
    ada_akun=tk.Label(frame1,text="Saya sudah punya akun.",fg="black",bg="white",font=("Roboto",9))
    ada_akun.place(x=90,y=400)

    tombol_login=tk.Button(frame1,width=6,text="Login",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=login_ok).place(x=228,y=400)

    window.mainloop()
 

#######################################


image = Image.open("images/xx5.png")
resize_image = image.resize((346,150))
img = ImageTk.PhotoImage(resize_image)
label_gambar=tk.Label(root,image=img,border=0).place(x=500,y=40)

frame1=tk.Frame(root,width=350,height=350,bg="white")
frame1.place(x=520,y=250)

heading=tk.Label(frame1,text="Login",fg="#8BBCCC",bg="white",font=("Roboto",23,"bold"))
heading.place(x=130,y=5)

#input email
def on_enter(x):
    email.delete(0,"end")

def on_leave(x):
    if (email.get()==""):
        email.insert(0,"Email")

email=tk.Entry(frame1,width=25,fg="black",border=0,bg="white",font=("Roboto",11))
email.place(x=30,y=80)
email.insert(0,"Email")
email.bind("<FocusIn>",on_enter)
email.bind("<FocusOut>",on_leave)
frame2=tk.Frame(frame1,width=295,height=2,bg="black").place(x=25,y=107)

#input password
def on_enter(x):
    pasw.delete(0,"end")

def on_leave(x):
    if (pasw.get()==""):
        pasw.insert(0,"Password")

pasw=tk.Entry(frame1,width=25,fg="black",border=0,bg="white",font=("Roboto",11))
pasw.place(x=30,y=150)
pasw.insert(0,"Password")
pasw.bind("<FocusIn>",on_enter)
pasw.bind("<FocusOut>",on_leave)
frame3=tk.Frame(frame1,width=295,height=2,bg="black").place(x=25,y=177)

tombol_login=tk.Button(frame1,width=41,pady=7,text="Login",bg="#F96666",cursor="hand2",fg="white",border=0,command=login).place(x=25,y=204)
label_register=tk.Label(frame1,text="Belum punya akun?",fg="black",bg="white",font=("Roboto",9))
label_register.place(x=84,y=270)

#tombol register
register=tk.Button(frame1,width=6,text="Register",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=mau_register)
register.place(x=200,y=270)



root.mainloop()