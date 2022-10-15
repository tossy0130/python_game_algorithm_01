import random
hand = ["グー", "チョキ", "パー"]

for i in range(3):
    print("\n", i+1, "回目")
    c = random.randint(0, 2)
    print("コンピュータの手は"+hand[c])
