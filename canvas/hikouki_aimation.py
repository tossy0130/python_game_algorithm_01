import tkinter

x = 300
y = 100
xp = 25
yp = 1

def animation() :
    global x,y, xp,yp
    x = x + xp
    y = y + yp
    if x <= 30 : xp = 5
    if x >= 770: xp = -5
    
    if y >= 105: yp = -1
    if y <= 100: yp = 1
    cvs.delete("all") # キャンバスに描いたものを全て削除
    cvs.create_image(400, 200, image=bg)
    if xp < 0:
        ### 左向きの飛行機
        cvs.create_image(x, y, image=ap1)
    if xp > 0:
        cvs.create_image(x, y, image=ap2)
    root.after(50, animation)
    
root = tkinter.Tk()
root.title("リアルタイム処理２：飛行機アニメーション")
cvs = tkinter.Canvas(width=800, height=400)
cvs.pack()

### 画像読み込み
ap1 = tkinter.PhotoImage(file="airplane1.png")
ap2 = tkinter.PhotoImage(file="airplane2.png")
bg = tkinter.PhotoImage(file="bg.png")

animation()
root.mainloop()