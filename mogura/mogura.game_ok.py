import random 
import time

### モグラたたき　出現関数
def mogura(r):
    m = ""
    n = ""
    for i in range(8):
        ana = "."
        if r == i :
            ana = "○"
        m = "_" + ana + "_"
        n = "[" + str(i) + "]"
        print(m, end="")
        print(n, end="")
        
######### ゲーム開始
print("====================== ゲーム開始 ======================")

hit = 0
ts = time.time()
for i in range(10):
    ### 0 - 7 の乱数
    r = random.randint(0, 7)
    mogura(r)
    p = input("もぐらはどこ？")
    if str(r) == p:
        print("HIT !!!")
        hit = hit + 1
    else:
        print("MISS")
now_t = int(time.time() - ts) # ゲーム開始からの、経過時間
bouns = 0
### ボーナス計算
if now_t < 60:
    bouns = 60 - now_t
    
print("====================== ゲーム終了 ======================")
print("TIME ",now_t," sec")
print("HIT ",hit,"×" + " BONUS ",bouns)
print("SCORE ",hit * bouns)

        