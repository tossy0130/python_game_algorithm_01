import random
hand = ["グー", "チョキ", "パー"]
you_win = 0
com_win = 0
print("コンピュータとじゃんけんをします。")
print("3回じゃんけんをして勝敗を決めます。")

for i in range(3):
    print("\n", i+1, "回目のじゃんけん")
    y = ""
    while True:
        y = input("あなたは何を出す？\n0=グー 1=チョキ 2=パー ")
        if y=="0" or y=="1" or y=="2":
            break
    y = int(y)
    c = random.randint(0, 2)
    print("コンピュータの手は"+hand[c])
    if y==c:
        print("あいこです")
    if y == 0:
        if c == 1:
            print("あなたの勝ち")
            you_win = you_win+1
        if c == 2:
            print("コンピュータの勝ち")
            com_win = com_win+1
    if y == 1:
        if c == 0:
            print("コンピュータの勝ち")
            com_win = com_win+1
        if c == 2:
            print("あなたの勝ち")
            you_win = you_win+1
    if y == 2:
        if c == 0:
            print("あなたの勝ち")
            you_win = you_win+1
        if c == 1:
            print("コンピュータの勝ち")
            com_win = com_win+1

print("--------------------")
print("あなたが勝った回数", you_win)
print("コンピュータが勝った回数", com_win)
if you_win>com_win:
    print("あなたの勝利！")
elif com_win>you_win:
    print("コンピュータの勝利！")
else:
    print("引き分け")
