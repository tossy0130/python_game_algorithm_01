import tkinter

fnt = ("Times New Roman", 40)

### マウスポインターの動きを取得する
def move(e):
    cvs.delete("all") # キャンバスに描いたものを全て削除
    s = "({}, {})".format(e.x, e.y)
    cvs.create_text(300, 200., text=s, font=fnt)
    
root = tkinter.Tk()
root.title("マウスポインタの座標")
root.bind("<Motion>", move) # イベント時に実行する関数指定
cvs = tkinter.Canvas(width=600, height=400)
cvs.create_text(300, 200, text="ウィンドウ内でマウスポインタを動かす")

cvs.pack()
root.mainloop()