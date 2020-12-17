pm = float(input())
temp = float(input())
point = float(input())
crit = float(input())

# 計算Wa
if pm <= 35.0:
    Wa = 0.5 + (100 - pm)*0.005
else:
    Wa = 0.5 + (45 - pm)*0.02

wet = 100 - 5*(temp - point)  # 計算濕度

# 計算Wh
if wet <= 30.0:
    Wh = (0.5/60)*(110 - wet)
else:
    Wh = (0.5/45)*(90 - wet)
    
# 取最低意願為最終意願    
if Wh <= Wa:
    final = Wh
else:
    final = Wa

# 去除負數
if final < 0:
    final = 0
    
# 印出最終意願及文字
print('{:.2f}'.format(final))
if final >= crit:
    print("Let's go together.")
else:
    print("I wouldn't go out with you.")