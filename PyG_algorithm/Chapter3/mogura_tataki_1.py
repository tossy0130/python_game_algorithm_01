import time
print("========== 計測開始 ==========")
ts = time.time()
print("エポック秒", ts)
input("Enterキーを押すまでの時間を計測します")
te = time.time()
print("エポック秒", te)
print("========== 計測終了 ==========")
print("経過秒数", int(te-ts))
