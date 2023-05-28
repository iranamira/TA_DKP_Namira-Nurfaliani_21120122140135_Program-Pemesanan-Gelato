from tkinter import *
from tkinter.messagebox import *
from tkinter.messagebox import showerror
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.resizable(width = 0, height = 0)
        self.config(bg="light yellow")
        self.title("Gelato Lezato")

        self.judul = Label (self, text = "Gelato Lezato ", 
                            font=('Berlin Sans FB Demi', 50), 
                            foreground="black")
        self.judul.place(x = 300, y = 0)
        
        self.judul = Label (self, text = "Daftar Menu Gelato Lezato ", 
                            font=('Berlin Sans FB', 25), 
                            background = 'light pink', 
                            foreground="black")
        self.judul.place(x = 325, y = 85)
        
        self.text4 = Text(self, font=('script MT bold', 30, ), 
                          width = 23, 
                          background="light pink", 
                          foreground="black")
        self.text4.insert(INSERT, 'Menu Gelato')
        self.text4.place(y = 140)
        

        food = ["1. Chocolate",
                "2. Cashew Nut",
                "3. Vanilla",
                "4. Choco Mint",
                "5. Red Velvet",
                "6. Kitkat",
                "7. Salted Caramel",
                "8. Nutella",
                "9. Lotus Biscoff",
                "10. Hazelnut Chocolate"]
        
        
        self.text1 = Text(self, font=('century', 20),
                          pady=10,
                          background="light pink", 
                          foreground="black")
        for i in food:
            self.text1.insert(INSERT, i + '\n')
            self.text1.place(y = 195)


        self.button = Button(self, text = 'Kembali ke Pemesanan', 
                             font=('Times', 20, 'bold'),
                             bg='#dd429d', 
                             fg='white', 
                             activebackground='pink', 
                             activeforeground='white',)
        self.button['command'] = self.destroy
        self.button.place(x = 330, y = 600)
       
    def destroy(self):
        super().destroy() 
         
if __name__ == "__main__":
    app = App()
    app.mainloop()