from distutils import bcppcompiler
import tkinter

### 風船の色 リストで管理
COL = ["red", "orange", "yellow", "lime", "cyan", "blue", "violet"]

bc = 0 # 風船をどの色で描くかを管理する
bx = 0 # 風船の x 座標
by = 0 # 風船の y 座標
mx = 0 # マウスポインタの x 座標
my = 0 # マウスポインタの y 座標

### クリック時の処理
def click(e):
    global bc
    bc = bc + 1
    if bc == 7: bc=0
    
### マウス移動時の関数
def move(e):
    global mx, my
    mx = e.x # マウスポインターの x 座標を入れる
    my = e.y # マウスポインターの y 座標を入れる

def main():
    global bx, by 
    if bx < mx: bx += 5
    if mx < bx: bx -= 5
    if by < my: by += 5
    if my < by: by -= 5
    cvs.delete("all")
    cvs.create_oval(bx-40, by-60, bx+40, by+60, fill=COL[bc])
    cvs.create_oval(bx-30, by-45, bx-5, by-20, fill="white", width=0)
    cvs.create_line(bx, by+60, bx-10, by+100, bx+10, by+140, bx, bx+180, smooth=True)
    
    root.after(50, main) ### 50ミリ秒後にmain() を呼ぶ
    
root = tkinter.Tk()

root.title("マウスポインター、風船")
root.bind("<Button>", click) ### クリックイベントに関数を紐づけ
root.bind("<Motion>", move)  ### マウスを動かした時の関数を紐づけ

cvs = tkinter.Canvas(width=900, height=600, bg="skyblue")
cvs.pack()    
main()
root.mainloop()
