import tkinter

root = tkinter.Tk()
root.title("画像読み込み")

cvs = tkinter.Canvas(width=540, height=720)
img = tkinter.PhotoImage(file="image_01.png")
cvs.create_image(270, 360, image=img)

cvs.pack()
root.mainloop()