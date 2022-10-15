import tkinter
root = tkinter.Tk()
root.title("キャンバスに画像を表示")
cvs = tkinter.Canvas(width=540, height=720)
dog = tkinter.PhotoImage(file="shepherd.png")
cvs.create_image(270, 360, image=dog)
cvs.pack()
root.mainloop()
