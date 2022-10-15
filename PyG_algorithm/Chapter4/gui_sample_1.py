import tkinter

def btn_on():
    la["bg"] = "magenta"
    la["text"] = "ボタンを押しました"

root = tkinter.Tk()
root.geometry("300x200")
root.title("GUIの主な部品 -1-")
root["bg"]="black"
la = tkinter.Label(text="これがラベルという部品です", bg="cyan")
la.place(x=10, y=10)
bu = tkinter.Button(text="ボタン", command=btn_on)
bu.place(x=10, y=60, width=100, height=40)
root.mainloop()
