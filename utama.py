from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.messagebox import showerror
import tkinter as tk
from harga import App


top = Tk()
top.geometry("1000x800")
top.resizable(width = 0, height = 0)
top.config(bg="light yellow")
top.title("Gelato Lezato") 

judul = Label (top, text = "Gelato Lezato ",
font=('Berlin Sans FB Demi', 50), foreground="black")
judul.place(x = 190, y = 0)

def on_click():
    print(askquestion("DKP", "Terimakasih Telah Memesan di Gelato Lezato"))


pembuka = Label (top, text = "Silahkan Pesan Gelato yang Tersedia", 
font=('Berlin Sans FB', 20), background="pink", foreground="white")
pembuka.place(x = 190, y = 120)

gelato = ["1. Chocolate ", 
        "2. Cashew Nut", 
        "3. Vanilla"]
gelato.append("4. Choco mint")

size = ["1. Small : 20.000", 
         "2. Medium : 35.000", 
         "3. Big : 50.000"]
gelato.append("4. Cone : 25.000")

text = Text(top, font=('Century', 15, 'bold'), 
            width = 800, 
            background="#dd429d", 
            foreground="black",
            )

text.insert(INSERT, 'Menu Unggulan Gelato Lezato')
text.edit = False
text.configure(state="disabled")
text.place(y = 170)

text1 = Text(top, font=('Kristen ITC', 13), 
             width = 800, 
             background="light yellow", 
             foreground="black")
for i in gelato:
    text1.insert(INSERT, i + '\n')
text1.configure(state="disabled")
text1.place(y = 200)


text2 = Text(top, font=('Century', 15, 'bold'), 
             width = 800, 
             background="#dd429d", 
             foreground="black"
             )
text2.insert(INSERT, 'Ukuran Gelato Lezato')
text2.configure(state="disabled")
text2.place(y = 300)

text3 = Text(top, font= ('Kristen ITC', 13), 
             width = 800, 
             background="light yellow", 
             foreground="black")
for i in size:
    text3.insert(INSERT, i + '\n')
text3.configure(state="disabled")
text3.place(y = 330)

pesan_apa = Label (top, text = "Pilih Gelato yang ingin dipesan :                ", 
                   font=('Algerian', 15), 
                   background="#dd429d", 
                   foreground="black")
pesan_apa.place(y = 440)

strgelato = StringVar(value='...')
combobox1 = ttk.Combobox(top, 
                        width = 20,
                        font = ('Algerian', 15), 
                        textvariable = strgelato, 
                        state ="readonly")
combobox1.place(x=480, y=440)
combobox1["values"] = ("Chocolate", 
                        "Cashew Nut", 
                        "KitKat",
                        "Choco Mint",
                        "Vanilla",
                        "Red Velvet",
                        "Nutella",
                        "Lotus Biscoff",
                        "Hazelnut Chocolate",
                        "Salted Caramel")

pesan_ukuran = Label (top, text = "Pilih ukuran Gelato yang ingin dipesan :                  ", 
                     font=('Algerian', 15), 
                     background="#dd429d", 
                     foreground="black")
pesan_ukuran.place(y = 500)

strukuran = StringVar(value='...')
combobox2 = ttk.Combobox(top, 
                        width = 20,
                        font = ('Algerian', 15), 
                        textvariable = strukuran, 
                        state ="readonly")

combobox2.place(x=480, y=500)
combobox2["values"] = ("Small", 
                 "Medium", 
                 "Big",
                 "cone")
            

pesan_berapa_gelato = Label (top, text = "Berapa Gelato yang ingin anda pesan : ",
                      font=('Algerian', 15), 
                      background="#dd429d", 
                      foreground="black")
pesan_berapa_gelato.place(y = 470)

jmlglt = IntVar()
jumlah_gelato = Entry (top, 
                font=('century', 10),
                width = 36,
                textvariable= jmlglt, 
                bd = 5)

jumlah_gelato.place(x = 480, y = 470)



def display():
    pesan_gelato = jumlah_gelato.get()
    try:
        pesan_gelato = int(pesan_gelato)
        if pesan_gelato < 1 or pesan_gelato > 10:
            raise ValueError
    except ValueError:
        messagebox.showerror('Warning!!!', 'Masukkan angka 1-10 pada jumlah yang ingin dipesan!!')
    else:
        messagebox.showinfo("Terima kasih sudah mampir ke Gelato Lezato", "Silahkan duduk dan Gelato akan segera disajikan...")

def on_click():
    if strgelato.get() == '...' or strukuran.get() == '...' or jumlah_gelato.get() == '':
        showerror('Warning!!!', 'Pilih gelato, ukuran, dan masukkan jumlah pesanan!')
    else:
        display()

button = Button(top, text = "Pesan Sekarang", 
font=('Times', 20, 'bold'),
    padx=1,
    pady=1,
    bg='#dd429d',
    fg='black',
    activebackground='pink',
    activeforeground='white', 
    command = on_click)
button.place(x = 250, y = 600)

button = Button(top, text = "Lihat Menu", 
font=('Times', 20, 'bold'),
    padx=1,
    pady=1,
    bg='#dd429d',
    fg='black',
    activebackground='pink',
    activeforeground='white', 
    command = App)
button.place(x = 470, y = 600)


top.mainloop()