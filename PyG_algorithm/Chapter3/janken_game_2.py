import random
hand = ["グー", "チョキ", "パー"]
print("コンピュータとじゃんけんをします。")

for i in range(3):
    print("\n", i+1, "回目のじゃんけん")
    y = input("あなたは何を出す？\n0=グー 1=チョキ 2=パー ")
    y = int(y)
    c = random.randint(0, 2)
    print("コンピュータの手は"+hand[c])
    if y==c:
        print("あいこです")
    if y == 0:
        if c == 1:
            print("あなたの勝ち")
        if c == 2:
            print("コンピュータの勝ち")
    if y == 1:
        if c == 0:
            print("コンピュータの勝ち")
        if c == 2:
            print("あなたの勝ち")
    if y == 2:
        if c == 0:
            print("あなたの勝ち")
        if c == 1:
            print("コンピュータの勝ち")
