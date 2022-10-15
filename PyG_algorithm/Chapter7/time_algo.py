import time
st = time.time()
n = 0
for i in range(1000000):
    n = n + 1
et = time.time()
print("計測開始エポック秒", st)
print("計測終了エポック秒", et)
print("処理時間", et-st)
