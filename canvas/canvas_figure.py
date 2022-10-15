import tkinter

root = tkinter.Tk()
root.title("canvas 図形を描く")
cvs = tkinter.Canvas(width=720, height=400, bg="black")

### 線
cvs.create_line(20, 40, 120, 360, fill="red", width=8)

### 長方形
cvs.create_rectangle(160, 60, 260, 340, fill="orange", width=0)

### 円
cvs.create_oval(300, 100, 500, 300, outline="yellow", width=12)

### 三角
cvs.create_polygon(600, 100, 500, 300, 700, 300, fill="green", outline="lime", width=3)

cvs.pack()
root.mainloop()