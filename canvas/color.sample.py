import tkinter

root = tkinter.Tk()
root.title("色を指定する英単語")
cvs = tkinter.Canvas(width=360, height=480, bg="black")

COL = [
    "maroon", "brown", "red", "orange", "gold",
    "yellow", "lime", "limegreen", "green",
    "skyblue","cyan", "blue", "navy", "indigo", "purple",
    "magenta", "white", "lightgray", "silver", "gray", 
    "olive", "pink"
]

### フォント
FON = ('Times, New Roman', 24)
x = 120
y = 40

for item in COL:
    cvs.create_text(x, y, text=item, fill=item, font=FON)
    y += 40
    ### ========= 縦　480px で　右側へ配置する。 =========
    if y >= 480:
        x += 120
        y = 40
    
    
cvs.pack()
root.mainloop()