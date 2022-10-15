import time

print("=== 計測開始 ===")
ts = time.time()
print("ts::" , ts)

input("Enter キーを押すまでの時間を計測")
te = time.time()

print("=== 計測終了 ===")
print("経過時間:::", int(te - ts))
