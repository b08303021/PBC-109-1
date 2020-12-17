from PIL import ImageTk
import tkinter as tk
import math
import tkinter.font as tkFont


class ChooseCharacter(tk.Frame):
    haveCharacter2 = False  # 是否擁有該角色
    haveCharacter3 = False
    haveCharacter4 = False
    haveCharacter5 = False
    haveCharacter6 = False
    haveCharacter7 = False
    haveCharacter8 = False
    haveCharacter9 = False
    haveCharacter10 = False

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.geometry('800x600')
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)

    def createWidgets(self):
        #  設定字體
        f = tkFont.Font(size=20, family="Courier New")
        self.background = tk.Canvas(self, height=600, width=800, bg='white').pack()
        #  設定標題及角色名字
        self.lblChooseChr = tk.Label(self, text="選擇角色", height=1, width=8, bg='white', font=f)
        self.lblChr1 = tk.Label(self, text="  Chr1", height=1, width=7, bg='white', font=f)
        self.lblChr2 = tk.Label(self, text="  Chr2", height=1, width=7, bg='white', font=f)
        self.lblChr3 = tk.Label(self, text="  Chr3", height=1, width=7, bg='white', font=f)
        self.lblChr4 = tk.Label(self, text="  Chr4", height=1, width=7, bg='white', font=f)
        self.lblChr5 = tk.Label(self, text="  Chr5", height=1, width=7, bg='white', font=f)
        self.lblChr6 = tk.Label(self, text="  Chr6", height=1, width=7, bg='white', font=f)
        self.lblChr7 = tk.Label(self, text="  Chr7", height=1, width=7, bg='white', font=f)
        self.lblChr8 = tk.Label(self, text="  Chr8", height=1, width=7, bg='white', font=f)
        self.lblChr9 = tk.Label(self, text="  Chr9", height=1, width=7, bg='white', font=f)
        self.lblChr10 = tk.Label(self, text="  Chr10", height=1, width=7, bg='white', font=f)

        #  建立按鈕
        self.btnBack = tk.Button(self, text="返回", command=self.clickBtnBack, height=2, width=6, bg='gray', font=f)
        self.imageChr1 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr1.png")
        self.btnChr1 = tk.Button(self, image=self.imageChr1, command=self.clickBtnChr1, height=140, width=148)
        self.imageChr2 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr2.png")
        self.btnChr2 = tk.Button(self, image=self.imageChr2, command=self.clickBtnChr2, height=140, width=148)
        self.imageChr3 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr3.png")
        self.btnChr3 = tk.Button(self, image=self.imageChr3, command=self.clickBtnChr3, height=140, width=148)
        self.imageChr4 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr4.png")
        self.btnChr4 = tk.Button(self, image=self.imageChr4, command=self.clickBtnChr4, height=140, width=148)
        self.imageChr5 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr5.png")
        self.btnChr5 = tk.Button(self, image=self.imageChr5, command=self.clickBtnChr5, height=140, width=148)
        self.imageChr6 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr6.png")
        self.btnChr6 = tk.Button(self, image=self.imageChr6, command=self.clickBtnChr6, height=140, width=148)
        self.imageChr7 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr7.png")
        self.btnChr7 = tk.Button(self, image=self.imageChr7, command=self.clickBtnChr7, height=140, width=148)
        self.imageChr8 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr8.png")
        self.btnChr8 = tk.Button(self, image=self.imageChr8, command=self.clickBtnChr8, height=140, width=148)
        self.imageChr9 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr9.png")
        self.btnChr9 = tk.Button(self, image=self.imageChr9, command=self.clickBtnChr9, height=140, width=148)
        self.imageChr10 = ImageTk.PhotoImage(file="C:\\Users\\黃柏誌\\Desktop\\大二上\\PBC\\Chr10.png")
        self.btnChr10 = tk.Button(self, image=self.imageChr10, command=self.clickBtnChr10, height=140, width=148)

        self.lblChooseChr.place(x=320, y=35)
        self.btnBack.place(x=10, y=10)

        self.btnChr1.place(x=10, y=130)
        self.btnChr2.place(x=168, y=130)
        self.btnChr3.place(x=326, y=130)
        self.btnChr4.place(x=484, y=130)
        self.btnChr5.place(x=642, y=130)
        self.btnChr6.place(x=10, y=370)
        self.btnChr7.place(x=168, y=370)
        self.btnChr8.place(x=326, y=370)
        self.btnChr9.place(x=484, y=370)
        self.btnChr10.place(x=642, y=370)

        self.lblChr1.place(x=10, y=280)
        self.lblChr2.place(x=168, y=280)
        self.lblChr3.place(x=326, y=280)
        self.lblChr4.place(x=484, y=280)
        self.lblChr5.place(x=642, y=280)
        self.lblChr6.place(x=10, y=520)
        self.lblChr7.place(x=168, y=520)
        self.lblChr8.place(x=326, y=520)
        self.lblChr9.place(x=484, y=520)
        self.lblChr10.place(x=642, y=520)

    #  設定按鈕觸發事件
    def clickBtnBack(self):
        pass

    def clickBtnChr1(self):
        ### 切換至角色一
        pass

    def clickBtnChr2(self):
        """
        if self.haveCharacter2 == True:
            則切換至角色二
        else:
            跳出對話框說:您尚未擁有該角色
        """
        pass

    def clickBtnChr3(self):
        pass

    def clickBtnChr4(self):
        pass

    def clickBtnChr5(self):
        pass

    def clickBtnChr6(self):
        pass

    def clickBtnChr7(self):
        pass

    def clickBtnChr8(self):
        pass

    def clickBtnChr9(self):
        pass

    def clickBtnChr10(self):
        pass


ChooseChr = ChooseCharacter()
ChooseChr.master.title("選擇角色")
ChooseChr.mainloop()