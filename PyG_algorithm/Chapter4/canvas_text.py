import tkinter
root = tkinter.Tk()
root.title("キャンバスに文字列を表示")
cvs = tkinter.Canvas(width=600, height=400, bg="white")
cvs.create_text(300, 200, text="Python", font=("Times New Roman", 40))
cvs.pack()
root.mainloop()
