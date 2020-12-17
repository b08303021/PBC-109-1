import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import pickle

from functools import partial  # raw 109
import threading

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

    def usr_login(self):
    # 獲取使用者輸入的usr_name和
        usr_name = self.var_usr_name.get()
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
        self.btn_login = tk.Button(self, text='登入', bg='#A877BA', font=('KaiTi', 20), command=self.usr_login)
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
        # 背景和圖片
        self.background = tk.Canvas(self, height = 600, width = 800, bg = 'white').pack()
        self.picture = tk.Canvas(self, height = 240, width = 240, bg = 'blue').place(x = 60, y = 60)
        # 經驗值
        self.exp = tk.Label(self, text = "經驗：100", height = 1, width = 12, bg = 'white', font = f3).place(x = 445, y = 260)
        # 首頁基礎數值
        self.level = tk.Button(self, text = "等級：12", height = 1, width = 15, font = f3, anchor='w').place(x = 60, y = 360)
        self.blood = tk.Button(self, text = "血量：231", height = 1, width = 15, font = f3, anchor='w').place(x = 60, y = 420)
        self.attack = tk.Button(self, text = "攻擊：243", height = 1, width = 15, font =f3, anchor='w').place(x = 60, y = 480)
        self.defend = tk.Button(self, text = "防禦：234", height = 1, width = 15, font =f3, anchor='w').place(x = 400, y = 360)
        self.skill = tk.Button(self, text = "技能：5%攻擊加倍", height = 1, width = 15, font =f3, anchor='w').place(x = 400, y = 420)
        self.dodge = tk.Button(self, text = "閃避：34%", height = 1, width = 15, font =f3, anchor='w').place(x = 400, y = 480)
        # 角色名和自己的名稱
        self.charater_name = tk.Label(self, text = "桐人", height = 1, width = 10, bg = 'white', font =f1).place(x = 420 , y = 100)
        self.name = tk. Label(self, text = "亞斯娜", height = 1, width = 10, bg = 'white', font =f2).place(x = 440 , y = 200)
        # 按鈕
        self.boss = tk.Button(self, text = "關\n卡", height = 2, width = 2, font = f3, command= self.toBoss).place(x = 760 , y = 60)
        self.character = tk.Button(self, text = "角\n色", height = 2, width = 2, font = f3).place(x = 760 , y = 180)
        self.action  = tk.Button(self, text = "行\n動", height = 2, width = 2, font = f3, command= self.toAction).place(x = 760 , y = 300)
    
    def toAction(self):
        self.destroy()
        self.master.switch_frame(Action)
    def toBoss(self):
        self.destroy()
        self.master.switch_frame(Boss)

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
        self.output = tk.Text(self, width=100, height=15, font = f4)
        self.output.place(x = 30, y = 300)
        # 按鈕
        self.back = tk.Button(self, text = "返回", height = 1, width = 4, font = f3, anchor='w', command= self.toGame).place(x = 30, y = 30)
        self.a = tk.Button(self, text = "A", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext, 'a')).place(x = 35, y = 120)
        self.b = tk.Button(self, text = "B", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'b')).place(x = 220, y = 120)
        self.c = tk.Button(self, text = "C", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'c')).place(x = 405, y = 120)
        self.d = tk.Button(self, text = "D", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'d')).place(x = 590, y = 120)
        self.e = tk.Button(self, text = "E", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'e')).place(x = 35, y = 220)
        self.f = tk.Button(self, text = "F", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'f')).place(x = 220, y = 220)
        self.g = tk.Button(self, text = "G", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'g')).place(x = 405, y = 220)
        self.h = tk.Button(self, text = "H", height = 1, width = 10, font = f3, anchor='w', command=partial(self.actiontext,'h')).place(x = 590, y = 220)
        # 標題
        self.title = tk.Label(self, text = "行動", height = 1, width = 10, bg = 'white', font = f1).place(x = 600 , y = 25)
        # CD
        self.text = tk.StringVar()
        self.text.set('')
        self.cd = tk.Label(self, text = "冷卻時間:", height = 1, width = 10, bg = 'white', font = f2).place(x = 200 , y = 32)
        self.cdnumber = tk.Label(self, textvariable=self.text, height = 1, width = 2, bg = 'white', font = f2, fg="red")
        self.cdnumber.place(x = 390 , y = 32)
        self.cantrigger = True  # 為防止透過切頁重置CD這邊要做調整
        
    def actiontext(self, act):
        if self.cantrigger == True:
            self.write('已成功行動'+ str(act) + '\n')
            self.cooldown(10)

    def write(self, txt):
        self.output.insert('1.0',str(txt))
        self.update_idletasks()
    
    def cooldown(self, cdnum):
        if cdnum > 0:
            self.cantrigger = False
            self.text.set(str(cdnum))
            cdnum -= 1
            t = threading.Timer(1, self.cooldown, args = (cdnum,))
            t.start()
        else:
            self.cantrigger = True
            self.text.set('')
    
    def toGame(self):
        self.destroy()
        self.master.switch_frame(Game)
class Boss(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.master.geometry('800x600')
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)
        self.createWidgets()

    def background(self):  # 暫定背景圖
        self.imageBG = tk.PhotoImage(file='p6BG.gif')  # 注意檔案路徑
        self.bg = tk.Label(self, image=self.imageBG)
        self.bg.grid(row=0, column=0, columnspan=4)

    def createWidgets(self):
        pFile = 'p6P.gif'  # 注意檔案路徑，會隨上場角色更動所以分開寫
        self.imageP = tk.PhotoImage(file=pFile)  # 注意檔案路徑
        self.pImage = tk.Label(self, image=self.imageP)  # 玩家角色圖
        self.pImage.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        bFile = 'p6P.gif'  # 注意檔案路徑，會隨上場角色更動所以分開寫
        self.imageB = tk.PhotoImage(file=bFile)  # 注意檔案路徑
        self.bImage = tk.Label(self, image=self.imageB)  # Boss角色名
        self.bImage.grid(row=0, column=3, columnspan=2, sticky=tk.E)

        fSize1 = tkFont.Font(size=20)
        pName = "玩家角色名"  # 會隨上場角色更動所以分開寫
        self.nameP = tk.Label(self, text=pName, font=fSize1)
        self.nameP.grid(row=0, column=0, sticky=tk.S)
        bName = "Boss角色名"  # 會隨上場角色更動所以分開寫
        self.nameB = tk.Label(self, text=bName, font=fSize1)
        self.nameB.grid(row=0, column=3, sticky=tk.S)

        fSize2 = tkFont.Font(size=14)
        pLevel = 0  # 會隨上場角色更動所以分開寫
        self.level = tk.Label(self, text=("Lv.", pLevel), font=fSize2)  # 角色等級
        self.level.grid(row=0, column=1, sticky=tk.SW)

        pInfo = [0, 1, 2, 3, 4]  # 玩家角色資訊[血量,攻擊,防禦,技能,閃避]
        bInfo = [0.0, 0.1, 0.2, 0.3, 0.4]  # Boss角色資訊[血量,攻擊,防禦,技能,閃避]

        self.hp = tk.Label(self, text="－ －血量－ －", height=2, font=fSize2, bg='white')
        self.hp.grid(row=1, column=1, columnspan=2)
        self.p_hp = tk.Label(self, text=str(pInfo[0]), height=2, font=fSize2, bg='white')
        self.p_hp.grid(row=1, column=0)
        self.b_hp = tk.Label(self, text=str(bInfo[0]), height=2, font=fSize2, bg='white')
        self.b_hp.grid(row=1, column=3)

        self.atk = tk.Label(self, text="－ －攻擊－ －", height=2, font=fSize2, bg='white')
        self.atk.grid(row=2, column=1, columnspan=2)
        self.p_atk = tk.Label(self, text=str(pInfo[1]), height=2, font=fSize2, bg='white')
        self.p_atk.grid(row=2, column=0)
        self.b_atk = tk.Label(self, text=str(bInfo[1]), height=2, font=fSize2, bg='white')
        self.b_atk.grid(row=2, column=3)

        self.defend = tk.Label(self, text="－ －防禦－ －", height=2, font=fSize2, bg='white')
        self.defend.grid(row=3, column=1, columnspan=2)
        self.p_defend = tk.Label(self, text=str(pInfo[2]), height=2, font=fSize2, bg='white')
        self.p_defend.grid(row=3, column=0)
        self.b_defend = tk.Label(self, text=str(bInfo[2]), height=2, font=fSize2, bg='white')
        self.b_defend.grid(row=3, column=3)

        self.skill = tk.Label(self, text="－ －技能－ －", height=2, font=fSize2, bg='white')
        self.skill.grid(row=4, column=1, columnspan=2)
        self.p_skill = tk.Label(self, text=str(pInfo[3]), height=2, font=fSize2, bg='white')
        self.p_skill.grid(row=4, column=0)
        self.b_skill = tk.Label(self, text=str(bInfo[3]), height=2, font=fSize2, bg='white')
        self.b_skill.grid(row=4, column=3)

        self.miss = tk.Label(self, text="－ －閃避－ －", height=2, font=fSize2, bg='white')
        self.miss.grid(row=5, column=1, columnspan=2)
        self.p_miss = tk.Label(self, text=str(pInfo[4]), height=2, font=fSize2, bg='white')
        self.p_miss.grid(row=5, column=0)
        self.b_miss = tk.Label(self, text=str(bInfo[4]), height=2, font=fSize2, bg='white')
        self.b_miss.grid(row=5, column=3)

        fSize3 = tkFont.Font(size=12)
        self.btnBack = tk.Button(self, text="BACK", height=2, width=8, font=fSize3, command= self.toGame)  # 暫定返回鍵
        self.btnBack.grid(row=0, column=0, sticky=tk.NW)

        self.btnFight = tk.Button(self, text="戰  鬥", height=2, width=10, font=fSize1)  # 暫定戰鬥鍵
        self.btnFight.grid(row=6, column=1, columnspan=2)
    def toGame(self):
        self.destroy()
        self.master.switch_frame(Game)
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()