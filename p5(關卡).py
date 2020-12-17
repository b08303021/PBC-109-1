import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk

class Level(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)
        
 
    def createWidgets(self):
        f1 = tkFont.Font(size = 32, family = "Courier New")
        f2 = tkFont.Font(size = 20, family = "Courier New")

        self.lbl1 = tk.Label(self, text = "水源阿伯", height = 1, width = 7, font = f2)
        self.lbl2 = tk.Label(self, text = "馬保國", height = 1, width = 7, font = f2)
        self.lbl3 = tk.Label(self, text = "傑哥", height = 1, width = 7, font = f2)
        self.lbl4 = tk.Label(self, text = "柯P", height = 1, width = 7, font = f2)
        self.lbl5 = tk.Label(self, text = "鋼鐵韓粉", height = 1, width = 7, font = f2)
        self.lbl6 = tk.Label(self, text = "國動", height = 1, width = 7, font = f2)
        self.lbl7 = tk.Label(self, text = "統神", height = 1, width = 7, font = f2)
        self.lbl8 = tk.Label(self, text = "小熊維尼", height = 1, width = 7, font = f2)
        self.lbl9 = tk.Label(self, text = "鍾家播", height = 1, width = 7, font = f2)
        self.lbl10 = tk.Label(self, text = "王希銘", height = 1, width = 7, font = f2)
        self.level = tk.Label(self, text="選擇關卡", height = 1, width = 7, font = f1)
        
        self.image1 = ImageTk.PhotoImage(file = "1.jpg")
        self.image2 = ImageTk.PhotoImage(file = "2.jpg")
        self.image3 = ImageTk.PhotoImage(file = "3.jpg")
        self.image4 = ImageTk.PhotoImage(file = "4.jpg")
        self.image5 = ImageTk.PhotoImage(file = "5.jpg")
        self.image6 = ImageTk.PhotoImage(file = "6.jpg")
        self.image7 = ImageTk.PhotoImage(file = "7.jpg")
        self.image8 = ImageTk.PhotoImage(file = "8.jpg")
        self.image9 = ImageTk.PhotoImage(file = "9.jpg")
        self.image10 = ImageTk.PhotoImage(file = "10.jpg")
        
        self.back = tk.Button(self, text = "返回", height = 1, width = 4, font = f2, command = self.toGame)
        self.btn1 = tk.Button(self, image = self.image1, command = self.check, font = f2, height = 200, width = 150)
        self.btn2 = tk.Button(self, image = self.image2, command = self.check, font = f2, height = 200, width = 150)
        self.btn3 = tk.Button(self, image = self.image3, command = self.check, font = f2, height = 200, width = 150)
        self.btn4 = tk.Button(self, image = self.image4, command = self.check, font = f2, height = 200, width = 150)
        self.btn5 = tk.Button(self, image = self.image5, command = self.check, font = f2, height = 200, width = 150)
        self.btn6 = tk.Button(self, image = self.image6, command = self.check, font = f2, height = 200, width = 150)
        self.btn7 = tk.Button(self, image = self.image7, command = self.check, font = f2, height = 200, width = 150)
        self.btn8 = tk.Button(self, image = self.image8, command = self.check, font = f2, height = 200, width = 150)
        self.btn9 = tk.Button(self, image = self.image9, command = self.check, font = f2, height = 200, width = 150)
        self.btn10 = tk.Button(self, image = self.image10, command = self.check, font = f2, height = 200, width = 150)
        
        self.back.grid(ipadx=10, ipady=30, sticky = tk.NE + tk.SW)
        self.level.grid(row = 0, column = 3, columnspan=2, sticky = tk.NE + tk.SW, ipady=30)
        self.lbl1.grid(row = 2, column = 0, sticky = tk.NE + tk.SW)
        self.lbl2.grid(row = 2, column = 1, sticky = tk.NE + tk.SW)
        self.lbl3.grid(row = 2, column = 2, sticky = tk.NE + tk.SW)
        self.lbl4.grid(row = 2, column = 3, sticky = tk.NE + tk.SW)
        self.lbl5.grid(row = 2, column = 4, sticky = tk.NE + tk.SW)
        self.lbl6.grid(row = 4, column = 0, sticky = tk.NE + tk.SW)
        self.lbl7.grid(row = 4, column = 1, sticky = tk.NE + tk.SW)
        self.lbl8.grid(row = 4, column = 2, sticky = tk.NE + tk.SW)
        self.lbl9.grid(row = 4, column = 3, sticky = tk.NE + tk.SW)
        self.lbl10.grid(row = 4, column = 4, sticky = tk.NE + tk.SW)
        
        self.btn1.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.btn2.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.btn3.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        self.btn4.grid(row = 1, column = 3, sticky = tk.NE + tk.SW)
        self.btn5.grid(row = 1, column = 4, sticky = tk.NE + tk.SW)
        self.btn6.grid(row = 3, column = 0, sticky = tk.NE + tk.SW)
        self.btn7.grid(row = 3, column = 1, sticky = tk.NE + tk.SW)
        self.btn8.grid(row = 3, column = 2, sticky = tk.NE + tk.SW)
        self.btn9.grid(row = 3, column = 3, sticky = tk.NE + tk.SW)
        self.btn10.grid(row = 3, column = 4, sticky = tk.NE + tk.SW)

    def check(self):
        response = messagebox.askokcancel("進入關卡", "即將進入關卡？")
        if response == True:
            pass
        elif response == False:
            pass
        
    def toGame(self):
        pass

        
Level = Level()
Level.mainloop()