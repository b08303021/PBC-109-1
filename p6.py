import tkinter as tk
import tkinter.font as tkFont


class Boss(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.geometry('800x600')
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)
        self.background()
        self.createWidgets()
        self.master.configure(bg='white')
        self.configure(bg='white')

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
        self.btnBack = tk.Button(self, text="BACK", height=2, width=8, font=fSize3)  # 暫定返回鍵
        self.btnBack.grid(row=0, column=0, sticky=tk.NW)

        self.btnFight = tk.Button(self, text="戰  鬥", height=2, width=10, font=fSize1)  # 暫定戰鬥鍵
        self.btnFight.grid(row=6, column=1, columnspan=2)


boss = Boss()
boss.mainloop()