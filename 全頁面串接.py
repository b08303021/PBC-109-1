import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import pickle
from tkinter import messagebox
from PIL import Image, ImageTk
from functools import partial
import threading
import math

class B():
    exp = 0

class Charaters():
    def __init__(self, use, atk, level):
        self.use = use
        self.atk = atk
        self.level = level

a = Charaters(1, 100, 1)

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('我的大學')
        self.master.geometry("800x600")
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)

    def usr_login(self):
    # 獲取使用者輸入的usr_name和
        usr_name = self.var_usr_name.get()
        StartPage.name = usr_name
        yy = tkFont.families()
        if usr_name != '':
            self.destroy()
            self.master.switch_frame(Game)
        else:
            tkinter.messagebox.showinfo('你真的不幫角色取名嗎?', '叫你不設你還真不設啊!\n你這個好傢伙，不幫角色取名，那你也別想玩!')

    def createWidgets(self):
        self.background = tk.Label(self, text='背景', font=('KaiTi', 40)).pack(ipadx=340, ipady=10)
        self.introduction = tk.Label(self, text=('這是發生在2018年的秘辛，你任職台灣的\n某間大學，但因為雙標黨的操作，你被迫從大\n學驅離，你重新奪回大學時，卻發現人事已經被\n雙標黨給滲透，還有被奇怪的勢力占領，所以\n你要打走那些搶走你大學的人，好好加油吧!'), 
                        font=('KaiTi', 20)).pack(side='top')
        self.name = tk.Label(self, text='角色名稱:', font=('KaiTi', 26)).pack(padx=110, pady=25)
        self.hit = tk.Label(self, text='(你可以不輸入角色名稱看看)', font=('KaiTi', 20)).pack()
        self.var_usr_name = tk.StringVar()
        self.entry_usr_name = tk.Entry(self, textvariable=self.var_usr_name, font=('KaiTi', 20)).pack(pady=10)
        self.btn_login = tk.Button(self, text='登入', bg='#ffcc69', font=('KaiTi', 20), command=self.usr_login)
        self.btn_login.pack(padx=10, pady=10)


class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.master.geometry('800x600')
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "Courier New")
        f2 = tkFont.Font(size = 25, family = "Courier New")
        f3 = tkFont.Font(size = 20, family = "Courier New")
        f4 = tkFont.Font(size = 10, family = "Courier New")
        # 背景和圖片
        self.background = tk.Canvas(self, height = 600, width = 800, bg = 'white').pack()
        self.picture = tk.Canvas(self, height = 240, width = 240, bg = 'blue').place(x = 60, y = 60)
        # 經驗值
        self.exp = tk.Label(self, text = (str(B.exp) + '/' + str(100)), height = 1, width = 12, bg = 'white', font = f3).place(x = 450, y = 290)
        # 首頁基礎數值
        self.level = tk.Button(self, text = "等級：" + str(a.level), height = 1, width = 15, bg='#ccdd69', font = f3, anchor='w').place(x = 60, y = 360)
        self.blood = tk.Button(self, text = "血量：231", height = 1, width = 15, bg='#ccdd69', font = f3, anchor='w').place(x = 60, y = 420)
        self.attack = tk.Button(self, text = "攻擊：" + str(a.atk), height = 1, width = 15, bg='#ccdd69', font =f3, anchor='w').place(x = 60, y = 480)
        self.defend = tk.Button(self, text = "防禦：234", height = 1, width = 15, bg='#ccdd69', font =f3, anchor='w').place(x = 400, y = 360)
        self.skill = tk.Button(self, text = "技能：5%攻擊加倍", height = 1, width = 15, bg='#ccdd69', font =f3, anchor='w').place(x = 400, y = 420)
        self.dodge = tk.Button(self, text = "閃避：34%", height = 1, width = 15, font =f3, bg='#ccdd69', anchor='w').place(x = 400, y = 480)
        # 角色名和自己的名稱
        self.charater_name = tk.Label(self, text = "桐人", height = 1, width = 10, bg = 'white', font =f1).place(x = 420 , y = 100)
        self.name = tk. Label(self, text = StartPage.name, height = 1, width = 10, bg = 'white', font =f2).place(x = 80 , y = 310)
        self.word = '桐谷和人（桐ヶ谷きりがや 和人かずと，Kirigaya Kazuto），虛擬世界的用戶名為「桐人（キリト，Kirito）」，是日本小說家川原礫輕小說《刀劍神域》及其改編動、漫畫作品的主角。在以《刀劍神域》為主的諸多系列作裡作為主角或重要角色登場。'
        self.intro = tk.Message(self, text = self.word, font = f4, bg = 'white', width = 270).place(x = 400, y = 150)
        # 按鈕
        self.boss = tk.Button(self, text = "關\n卡", height = 2, width = 2, font = f3, bg='#bbaa69', command= self.toLevel).place(x = 760 , y = 60)
        self.character = tk.Button(self, text = "角\n色", height = 2, width = 2, bg='#bbaa69', font = f3, command=self.toCharacter).place(x = 760 , y = 180)
        self.action  = tk.Button(self, text = "行\n動", height = 2, width = 2, font = f3, bg='#bbaa69', command= self.toAction).place(x = 760 , y = 300)
    
    def toAction(self):
        self.destroy()
        self.master.switch_frame(Action)
        
    def toLevel(self):
        self.destroy()
        self.master.switch_frame(Level)

    def toCharacter(self):
        self.destroy()
        self.master.switch_frame(ChooseCharacter)


class Level(tk.Frame):
    def __init__(self, master):
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
        
        self.back = tk.Button(self, text = "返回", width = 3, bg='#00E3E3', bd=1, font = ('KaiTi', 25), command = self.toGame)
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
        
        self.back.grid(ipady=30, sticky = tk.NE + tk.SW)
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
            self.toBoss()  
        elif response == False:
            pass
        
    def toGame(self):
        self.destroy()
        self.master.switch_frame(Game)
    
    def toBoss(self):
        self.destroy()
        self.master.switch_frame(Boss)


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

    def __init__(self, master):
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
        self.lblChooseChr = tk.Label(self, text="選擇角色", height=1, width=8, bg='white', font=('KaiTi', 30))
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
        self.btnBack = tk.Button(self, text="返回", height=1, width=6, font=('KaiTi', 30), bg='#00E3E3', command=self.toGame)
        self.imageChr1 = ImageTk.PhotoImage(file="Chr1.png")
        self.btnChr1 = tk.Button(self, image=self.imageChr1, command=self.clickBtnChr1, height=140, width=148)
        self.imageChr2 = ImageTk.PhotoImage(file="Chr2.png")
        self.btnChr2 = tk.Button(self, image=self.imageChr2, command=self.clickBtnChr2, height=140, width=148)
        self.imageChr3 = ImageTk.PhotoImage(file="Chr3.png")
        self.btnChr3 = tk.Button(self, image=self.imageChr3, command=self.clickBtnChr3, height=140, width=148)
        self.imageChr4 = ImageTk.PhotoImage(file="Chr4.png")
        self.btnChr4 = tk.Button(self, image=self.imageChr4, command=self.clickBtnChr4, height=140, width=148)
        self.imageChr5 = ImageTk.PhotoImage(file="Chr5.png")
        self.btnChr5 = tk.Button(self, image=self.imageChr5, command=self.clickBtnChr5, height=140, width=148)
        self.imageChr6 = ImageTk.PhotoImage(file="Chr6.png")
        self.btnChr6 = tk.Button(self, image=self.imageChr6, command=self.clickBtnChr6, height=140, width=148)
        self.imageChr7 = ImageTk.PhotoImage(file="Chr7.png")
        self.btnChr7 = tk.Button(self, image=self.imageChr7, command=self.clickBtnChr7, height=140, width=148)
        self.imageChr8 = ImageTk.PhotoImage(file="Chr8.png")
        self.btnChr8 = tk.Button(self, image=self.imageChr8, command=self.clickBtnChr8, height=140, width=148)
        self.imageChr9 = ImageTk.PhotoImage(file="Chr9.png")
        self.btnChr9 = tk.Button(self, image=self.imageChr9, command=self.clickBtnChr9, height=140, width=148)
        self.imageChr10 = ImageTk.PhotoImage(file="Chr10.png")
        self.btnChr10 = tk.Button(self, image=self.imageChr10, command=self.clickBtnChr10, height=140, width=148)

        # 設定位置
        self.lblChooseChr.place(x=320, y=35)
        self.btnBack.place(x=10, y=0)

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

    def toGame(self):
        self.destroy()
        self.master.switch_frame(Game)


class Action(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.master.geometry('800x600')
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "Courier New")
        f2 = tkFont.Font(size = 25, family = "Courier New")
        f3 = tkFont.Font(size = 20, family = "Courier New")
        f4 = tkFont.Font(size = 15, family = "Courier New")
        # 背景
        self.background = tk.Canvas(self, height = 600, width = 800, bg = 'white').pack()
        # 文字
        self.output = tk.Text(self, width=60, height=14, font = f4, bg='#D3A4FF')
        self.output.place(x = 30, y = 300)
        # 按鈕
        self.back = tk.Button(self, text = "返回", height = 1, width = 5, bg='#00E3E3', font = ('KaiTi', 30), command= self.toGame).place(x = 10, y = 0)
        self.a = tk.Button(self, text = "A", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext, 'a')).place(x = 35, y = 120)
        self.b = tk.Button(self, text = "B", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext,'b')).place(x = 220, y = 120)
        self.c = tk.Button(self, text = "C", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext,'c')).place(x = 405, y = 120)
        self.d = tk.Button(self, text = "D", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext,'d')).place(x = 590, y = 120)
        self.e = tk.Button(self, text = "E", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext,'e')).place(x = 35, y = 220)
        self.f = tk.Button(self, text = "F", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext,'f')).place(x = 220, y = 220)
        self.g = tk.Button(self, text = "G", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext,'g')).place(x = 405, y = 220)
        self.h = tk.Button(self, text = "H", height = 1, width = 10, font = f3, bg='#228922', anchor='w', command=partial(self.actiontext,'h')).place(x = 590, y = 220)
        # 標題
        self.title = tk.Label(self, text = "行動", height = 1, width = 10, bg = 'white', font = f1).place(x = 600 , y = 25)
        # CD
        self.text = tk.StringVar()
        self.text.set('')
        self.cd = tk.Label(self, text = "冷卻時間:", height = 1, width = 10, bg = 'white', font = f2).place(x = 200 , y = 32)
        self.cdnumber = tk.Label(self, textvariable=self.text, height = 1, width = 2, bg = 'white', font = f2, fg="red")
        self.cdnumber.place(x = 390 , y = 32)
        Action.cantrigger = True  # 為防止透過切頁重置CD這邊要做調整
        
    def actiontext(self, act):
        if Action.cantrigger == True:
            self.write('已成功行動'+ str(act) + '\n')
            self.cooldown(0)
            B.exp += 11
            if B.exp > 10:
                a.level += 1
                a.atk += 10
        else:
            tkinter.messagebox.showinfo('還在冷卻哦!', '就算沒有秒數，還是在冷卻喔!')

    def write(self, txt):
        self.output.insert('1.0',str(txt))
        self.update_idletasks()

    def cooldown(self, cdnum):
        if cdnum > 0:
            Action.cantrigger = False
            self.text.set(str(cdnum))
            cdnum -= 1
            t = threading.Timer(1, self.cooldown, args = (cdnum,))
            t.start()
        else:
            Action.cantrigger = True
            self.text.set('')
    
    def toGame(self):
        self.destroy()
        self.master.switch_frame(Game)


class Boss(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.background()
        self.createWidgets()
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)


    def background(self):  # 暫定背景圖
        self.imageBG = tk.PhotoImage(file='p6BG1.GIF')  # 注意檔案路徑
        self.bg = tk.Label(self, image=self.imageBG)
        self.bg.grid(row=1, column=0, columnspan=4)

    def createWidgets(self):
        pFile = 'p6P.gif'  # 注意檔案路徑，會隨上場角色更動所以分開寫
        self.imageP = tk.PhotoImage(file=pFile)  # 注意檔案路徑
        self.pImage = tk.Label(self, image=self.imageP)  # 玩家角色圖
        self.pImage.grid(row=1, column=0, columnspan=2, sticky=tk.W)

        bFile = 'p6P.gif'  # 注意檔案路徑，會隨上場角色更動所以分開寫
        self.imageB = tk.PhotoImage(file=bFile)  # 注意檔案路徑
        self.bImage = tk.Label(self, image=self.imageB)  # Boss角色名
        self.bImage.grid(row=1, column=2, columnspan=2, sticky=tk.E)

        fSize1 = tkFont.Font(size=20)
        pName = "玩家角色名"  # 會隨上場角色更動所以分開寫
        self.nameP = tk.Label(self, text=pName, font=fSize1)
        self.nameP.grid(row=2, column=0, sticky=tk.S)
        bName = "Boss角色名"  # 會隨上場角色更動所以分開寫
        self.nameB = tk.Label(self, text=bName, font=fSize1)
        self.nameB.grid(row=2, column=3, sticky=tk.S)

        fSize2 = tkFont.Font(size=14)
        pLevel = 0  # 會隨上場角色更動所以分開寫
        self.level = tk.Label(self, text=("Lv.", pLevel), font=fSize2)  # 角色等級
        self.level.grid(row=2, column=1, sticky=tk.SW)

        pInfo = [0, 1, 2, 3, 4]  # 玩家角色資訊[血量,攻擊,防禦,技能,閃避]
        bInfo = [0.0, 0.1, 0.2, 0.3, 0.4]  # Boss角色資訊[血量,攻擊,防禦,技能,閃避]

        self.hp = tk.Label(self, text="－ －血量－ －", height=2, font=fSize2, bg='yellow')
        self.hp.grid(row=4, column=1, columnspan=2)
        self.p_hp = tk.Label(self, text=str(pInfo[0]), height=2, font=fSize2, bg='yellow')
        self.p_hp.grid(row=4, column=0)
        self.b_hp = tk.Label(self, text=str(bInfo[0]), height=2, font=fSize2, bg='yellow')
        self.b_hp.grid(row=4, column=3)

        self.atk = tk.Label(self, text="－ －攻擊－ －", height=2, font=fSize2, bg='yellow')
        self.atk.grid(row=5, column=1, columnspan=2)
        self.p_atk = tk.Label(self, text=str(pInfo[1]), height=2, font=fSize2, bg='yellow')
        self.p_atk.grid(row=5, column=0)
        self.b_atk = tk.Label(self, text=str(bInfo[1]), height=2, font=fSize2, bg='yellow')
        self.b_atk.grid(row=5, column=3)

        self.defend = tk.Label(self, text="－ －防禦－ －", height=2, font=fSize2, bg='yellow')
        self.defend.grid(row=6, column=1, columnspan=2)
        self.p_defend = tk.Label(self, text=str(pInfo[2]), height=2, font=fSize2, bg='yellow')
        self.p_defend.grid(row=6, column=0)
        self.b_defend = tk.Label(self, text=str(bInfo[2]), height=2, font=fSize2, bg='yellow')
        self.b_defend.grid(row=6, column=3)

        self.skill = tk.Label(self, text="－ －技能－ －", height=2, font=fSize2, bg='yellow')
        self.skill.grid(row=7, column=1, columnspan=2)
        self.p_skill = tk.Label(self, text=str(pInfo[3]), height=2, font=fSize2, bg='yellow')
        self.p_skill.grid(row=7, column=0)
        self.b_skill = tk.Label(self, text=str(bInfo[3]), height=2, font=fSize2, bg='yellow')
        self.b_skill.grid(row=7, column=3)

        self.miss = tk.Label(self, text="－ －閃避－ －", height=2, font=fSize2, bg='yellow')
        self.miss.grid(row=8, column=1, columnspan=2)
        self.p_miss = tk.Label(self, text=str(pInfo[4]), height=2, font=fSize2, bg='yellow')
        self.p_miss.grid(row=8, column=0)
        self.b_miss = tk.Label(self, text=str(bInfo[4]), height=2, font=fSize2, bg='yellow')
        self.b_miss.grid(row=8, column=3)

        fSize3 = tkFont.Font(size=20)
        self.btnBack = tk.Button(self, text="返回", height=2, width=8, bg='#00E3E3', font=fSize3, command=self.toLevel)  # 暫定返回鍵
        self.btnBack.grid(row=0, column=0, sticky=tk.NW)

        self.btnFight = tk.Button(self, text="戰  鬥", height=1, width=10, font=fSize1, bg='#FF5151', command=self.toFight)  # 暫定戰鬥鍵
        self.btnFight.grid(row=9, column=1, columnspan=2)

    def toLevel(self):
        self.destroy()
        self.master.switch_frame(Level)

    def toFight(self):
        self.destroy()
        self.master.switch_frame(Fight)


class Fight(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)

    def createWidgets(self):
        fSize1 = tkFont.Font(size=32, family="Courier New")
        self.title = tk.Label(self, text='－ 戰鬥結果 －', font=fSize1)
        self.title.grid(row=0, column=0)

        fSize2 = tkFont.Font(size=20, family="Courier New")
        self.btnEnd = tk.Button(self, text="結束", height=2, width=8, bg='#aa1169', font=fSize2, command=self.toLevel)  # 暫定結束鍵
        self.btnEnd.grid(row=1, column=0, sticky=tk.S)

    def toLevel(self):
        self.destroy()
        self.master.switch_frame(Level)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()