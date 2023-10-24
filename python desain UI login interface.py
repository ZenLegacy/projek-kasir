from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Kasir')
app.geometry('750x600')  # membuat ukuran
app.configure(bg='#31c6d4')  # membuat backgroung warna

login_id = StringVar()
login_pass = StringVar()

def login():
    entered_id = login_id.get()
    entered_pass = login_pass.get()

    if entered_id == "admin" and entered_pass == "dhaniganteng":
        messagebox.showinfo(message="User Benar")

    else:
        messagebox.showerror(message="User Salah")

#program login user
Label(app, text='Login User', bg='#31c6d4', foreground='#fef5ac', font='arial 18 bold').place(x=280, y=30)

#tekslogin user
Label(app, text='Masukkan User ID', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=275, y=100)
Label(app, text='Masukkan User Password', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=240, y=160)

# dinggo login id pass
Entry(app, textvariable=login_id, width=28).place(x=260, y=130)
Entry(app, textvariable=login_pass, show='*', width=28).place(x=260, y=190)  # menggunakan show='*' untuk menyembunyikan karakter

#membuat tombol
Button(app, text='Login', foreground='white', bg='#36ae7c', width=10, command=login).place(x=230, y=240)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=lambda: login_id.set("") or login_pass.set("")).place(x=380, y=240)

#teks suara hatiku
Label(app, text='Mamahhhh tolong akuuuu', bg='#31c6d4', foreground='#fef5ac', font='arial 40 ').place(x=65, y=500)

app.mainloop()