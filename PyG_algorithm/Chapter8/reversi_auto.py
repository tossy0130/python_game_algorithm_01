import tkinter
import tkinter.messagebox
import random

score = [0]*3 # 対戦結果
match = 0 # 対戦回数

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 60)
BLACK = 1
WHITE = 2
proc = 0
turn = 0
msg = ""
space = 0
color = [0]*2
board = []
back = []
for y in range(8):
    board.append([0]*8)
    back.append([0]*8)

def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x*80
            Y = y*80
            cvs.create_rectangle(X, Y, X+80, Y+80, outline="black")
            if board[y][x]==BLACK:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="black", width=0)
            if board[y][x]==WHITE:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="white", width=0)
    cvs.update()

def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE

# 石を打ち、相手の石をひっくり返す
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break

# そこに打つといくつ返せるか数える
def kaeseru(x, y, iro):
    if board[y][x]>0:
        return -1 # 置けないマス
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    total += k
                    break
    return total

# 打てるマスがあるか調べる
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0:
                return True
    return False

# 黒い石、白い石、いくつかあるか数える
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x]==BLACK: b += 1
            if board[y][x]==WHITE: w += 1
    return b, w

#コンピュータの思考ルーチン
def computer_0(iro): # ランダムに打つ
    while True:
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        if kaeseru(rx, ry, iro)>0:
            return rx, ry

point = [
    [6,2,5,4,4,5,2,6],
    [2,1,3,3,3,3,1,2],
    [5,3,3,3,3,3,3,5],
    [4,3,3,0,0,3,3,4],
    [4,3,3,0,0,3,3,4],
    [5,3,3,3,3,3,3,5],
    [2,1,3,3,3,3,1,2],
    [6,2,5,4,4,5,2,6]
]
def computer_1(iro): # 優先的に打つべきマスを選ぶ
    sx = 0
    sy = 0
    p = 0
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0 and point[y][x]>p:
                    p = point[y][x]
                    sx = x
                    sy = y
    return sx, sy

# モンテカルロ法による思考ルーチン
def save():
    for y in range(8):
        for x in range(8):
            back[y][x] = board[y][x]

def load():
    for y in range(8):
        for x in range(8):
            board[y][x] = back[y][x]

def uchiau(iro):
    while True:
        if uteru_masu(BLACK)==False and uteru_masu(WHITE)==False:
            break
        iro = 3-iro
        if uteru_masu(iro)==True:
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if kaeseru(x, y, iro)>0:
                    ishi_utsu(x, y, iro)
                    break

def computer_2(iro, loops):
    global msg
    win = [0]*64
    save()
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0:
                msg += "."
                banmen()
                win[x+y*8] = 1
                for i in range(loops):
                    ishi_utsu(x, y, iro)
                    uchiau(iro)
                    b, w = ishino_kazu()
                    if iro==BLACK and b>w:
                        win[x+y*8] += 1
                    if iro==WHITE and w>b:
                        win[x+y*8] += 1
                    load()
    m = 0
    n = 0
    for i in range(64):
        if win[i]>m:
            m = win[i]
            n = i
    x = n%8
    y = int(n/8)
    return x, y

def main():
    global proc, turn, msg, space, match
    banmen()
    if proc==0: # タイトル画面
        cvs.create_text(320, 200, text="Reversi AUTO", fill="gold", font=FL)
        ban_syokika()
        color[0] = BLACK
        color[1] = WHITE
        turn = 0
        proc = 1
    elif proc==1: # どちらの番か表示
        msg = "アルゴリズム "+str(turn)+" 思考中"
        proc = 2
    elif proc==2: # 石を打つマスを決める
        if turn==0: # アルゴリズム 先手
            cx, cy = computer_1(color[turn])
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
        else: # アルゴリズム 後手
            cx, cy = computer_2(color[turn], 30)
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
    elif proc==3: # 打つ番を交代
        msg = ""
        turn = 1-turn
        proc = 4
    elif proc==4: # 打てるマスがあるか
        if space==0:
            proc = 5
        elif uteru_masu(BLACK)==False and uteru_masu(WHITE)==False:
            msg = "どちらも打てないので終了"
            proc = 5
        elif uteru_masu(color[turn])==False:
            msg = "COM"+str(turn)+"は打てるマスがないのでパス"
            proc = 3
        else:
            proc = 1
    elif proc==5: # 勝敗判定
        b, w = ishino_kazu()
        if (color[0]==BLACK and b>w) or (color[0]==WHITE and w>b):
            score[0] += 1
        elif (color[1]==BLACK and b>w) or (color[1]==WHITE and w>b):
            score[1] += 1
        else:
            score[2] += 1

        # 結果を表示する
        match += 1
        print("--------------------")
        print("対戦回数", match)
        print("黒", b, "　白", w)
        print("COM(先手) WIN", score[0])
        print("COM(後手) WIN", score[1])
        print("DRAW", score[2]) 
        if match%100==0:
            tkinter.messagebox.showinfo("", "100試合ごとに一時停止します")
        proc = 0
    root.after(1, main) # アルゴリズムの対戦 100msecを1msec

root = tkinter.Tk()
root.title("リバーシ")
root.resizable(False, False)
cvs = tkinter.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()
