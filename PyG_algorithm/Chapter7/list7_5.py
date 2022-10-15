import tkinter
import random

BLACK = 1
WHITE = 2
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
board = [
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 1, 0, 0, 0],
 [0, 0, 0, 1, 2, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
]

def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x/80)
    my = int(e.y/80)
    if mx>7: mx = 7
    if my>7: my = 7

def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver")
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

#コンピュータの思考ルーチン
def computer_0(iro): # ランダムに打つ
    while True:
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        if kaeseru(rx, ry, iro)>0:
            return rx, ry

def main():
    global mc, proc, turn, msg
    banmen()
    if proc==0: # スタート待ち
        msg = "クリックして開始します"
        if mc==1: # ウィンドウをクリック
            mc = 0
            turn = 0
            proc = 1
    elif proc==1: # どちらの番か表示
        msg = "あなたの番です"
        if turn==1:
            msg = "コンピュータ 考え中."
        proc = 2
    elif proc==2: # 石を打つマスを決める
        if turn==0: # プレイヤー
            if mc==1:
                mc = 0
                if kaeseru(mx, my, BLACK)>0:
                    ishi_utsu(mx, my, BLACK)
                    proc = 3
        else: # コンピュータ
            cx, cy = computer_0(WHITE)
            ishi_utsu(cx, cy, WHITE)
            proc = 3
    elif proc==3: # 打つ番を交代
        turn = 1-turn
        proc = 4
    elif proc==4: # 打てるマスがあるか
        if uteru_masu(BLACK)==False and uteru_masu(WHITE)==False:
            msg = "どちらも打てないので終了です"
        elif turn==0 and uteru_masu(BLACK)==False:
            msg = "あなたは打てないのでパス"
            proc = 3
        elif turn==1 and uteru_masu(WHITE)==False:
            msg = "コンピュータは打てないのでパス"
            proc = 3
        else:
            proc = 1
    root.after(100, main)

root = tkinter.Tk()
root.title("リバーシ")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()
