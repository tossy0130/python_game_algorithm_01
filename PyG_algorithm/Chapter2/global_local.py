total = 0
def kasan():
    global total
    loops = 11
    for i in range(loops):
        total += i

print("totalの初期値", total)
kasan()
print("関数実行後のtotalの値", total)
