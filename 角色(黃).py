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
        
    def createWidgets(self):
        #  設定字體
        f = tkFont.Font(size = 22, family = "Courier New")
        
        #  設定標題及角色名字
        self.lblChooseChr = tk.Label(self, text = "選擇角色", height = 3, width = 15, font = f)
        self.lblChr1 = tk.Label(self, text = "Chr1", height = 2, width = 10, font = f)
        self.lblChr2 = tk.Label(self, text = "Chr2", height = 2, width = 10, font = f)
        self.lblChr3 = tk.Label(self, text = "Chr3", height = 2, width = 10, font = f)
        self.lblChr4 = tk.Label(self, text = "Chr4", height = 2, width = 10, font = f)
        self.lblChr5 = tk.Label(self, text = "Chr5", height = 2, width = 10, font = f)
        self.lblChr6 = tk.Label(self, text = "Chr6", height = 2, width = 10, font = f)
        self.lblChr7 = tk.Label(self, text = "Chr7", height = 2, width = 10, font = f)
        self.lblChr8 = tk.Label(self, text = "Chr8", height = 2, width = 10, font = f)
        self.lblChr9 = tk.Label(self, text = "Chr9", height = 2, width = 10, font = f)
        self.lblChr10 = tk.Label(self, text = "Chr10", height = 2, width = 10, font = f)
        
        #  建立按鈕
        self.btnBack = tk.Button(self, text = "返回", command = self.clickBtnBack,  height = 5, width = 25)
        self.imageChr1 = ImageTk.PhotoImage(file = "Chr1.png")
        self.btnChr1 = tk.Button(self, image = self.imageChr1, command = self.clickBtnChr1, height = 210, width = 280)
        self.imageChr2 = ImageTk.PhotoImage(file = "Chr2.png")
        self.btnChr2 = tk.Button(self, image = self.imageChr2, command = self.clickBtnChr2, height = 210, width = 280)
        self.imageChr3 = ImageTk.PhotoImage(file = "Chr3.png")
        self.btnChr3 = tk.Button(self, image = self.imageChr3, command = self.clickBtnChr3, height = 210, width = 280)
        self.imageChr4 = ImageTk.PhotoImage(file = "Chr4.png")
        self.btnChr4 = tk.Button(self, image = self.imageChr4, command = self.clickBtnChr4, height = 210, width = 280)
        self.imageChr5 = ImageTk.PhotoImage(file = "Chr5.png")
        self.btnChr5 = tk.Button(self, image = self.imageChr5, command = self.clickBtnChr5, height = 210, width = 280)
        self.imageChr6 = ImageTk.PhotoImage(file = "Chr6.png")
        self.btnChr6 = tk.Button(self, image = self.imageChr6, command = self.clickBtnChr6, height = 210, width = 280)
        self.imageChr7 = ImageTk.PhotoImage(file = "Chr7.png")
        self.btnChr7 = tk.Button(self, image = self.imageChr7, command = self.clickBtnChr7, height = 210, width = 280)
        self.imageChr8 = ImageTk.PhotoImage(file = "Chr8.png")
        self.btnChr8 = tk.Button(self, image = self.imageChr8, command = self.clickBtnChr8, height = 210, width = 280)
        self.imageChr9 = ImageTk.PhotoImage(file = "Chr9.png")
        self.btnChr9 = tk.Button(self, image = self.imageChr9, command = self.clickBtnChr9, height = 210, width = 280)
        self.imageChr10 = ImageTk.PhotoImage(file = "Chr10.png")
        self.btnChr10 = tk.Button(self, image = self.imageChr10, command = self.clickBtnChr10, height = 210, width = 280)
        
        #  設定標題及角色名字位置
        self.lblChooseChr.grid(row = 0, column = 1, columnspan = 8)
        self.lblChr1.grid(row = 2, column = 0, columnspan = 2)
        self.lblChr2.grid(row = 2, column = 2, columnspan = 2)
        self.lblChr3.grid(row = 2, column = 4, columnspan = 2)
        self.lblChr4.grid(row = 2, column = 6, columnspan = 2)
        self.lblChr5.grid(row = 2, column = 8, columnspan = 2)
        self.lblChr6.grid(row = 4, column = 0, columnspan = 2)
        self.lblChr7.grid(row = 4, column = 2, columnspan = 2)
        self.lblChr8.grid(row = 4, column = 4, columnspan = 2)
        self.lblChr9.grid(row = 4, column = 6, columnspan = 2)
        self.lblChr10.grid(row = 4, column = 8, columnspan = 2)
        
        #  設定按鈕位置
        self.btnBack.grid(row=0, column=0, columnspan=2)
        self.btnChr1.grid(row = 1, column = 0, columnspan = 2)
        self.btnChr2.grid(row = 1, column = 2, columnspan = 2)
        self.btnChr3.grid(row = 1, column = 4, columnspan = 2)
        self.btnChr4.grid(row = 1, column = 6, columnspan = 2)
        self.btnChr5.grid(row = 1, column = 8, columnspan = 2)
        self.btnChr6.grid(row = 3, column = 0, columnspan = 2)
        self.btnChr7.grid(row = 3, column = 2, columnspan = 2)
        self.btnChr8.grid(row = 3, column = 4, columnspan = 2)
        self.btnChr9.grid(row = 3, column = 6, columnspan = 2)
        self.btnChr10.grid(row = 3, column = 8, columnspan = 2)
        
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