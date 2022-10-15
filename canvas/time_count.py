import tkinter

# フォント
f = ("Times New Roman", 100)
n = 0

def counter() :
    global n
    n = n + 1
    cvs.delete("all")
    cvs.create_text(300, 200, text=n, font=f, fill="blue")
    root.after(1000, counter)
    
root = tkinter.Tk()
root.title("リアルタイム処理１")
cvs = tkinter.Canvas(width=600, height=400, bg="white")
cvs.pack()
counter()
root.mainloop()

