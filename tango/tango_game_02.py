q = ["リンゴの英単語？", "本の英単語？","猫の英単語？", "犬の英単語"]
ans = ["apple", "book", "cat", "dog"]

q_len = len(q)
ten = 0 # 点数
seikai_num = 0 # 正解数
for i in range(q_len) :
    kaitou_arr = input(q[i])
    if kaitou_arr == ans[i]:
        print("正解")
        ten = ten + 100
        seikai_num = seikai_num + 1
    else:
        print("残念。不正解") 
    
    
print("正解数:" + str(seikai_num))
print("得点:" + str(ten))

    
    
    