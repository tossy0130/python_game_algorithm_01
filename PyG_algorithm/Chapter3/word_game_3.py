japanese = ["リンゴ", "本", "猫", "犬", "卵", "魚", "女の子"]
english = ["apple", "book", "cat", "dog", "egg", "fish", "girl"]
n = len(japanese)
right = 0
for i in range(n):
    a = input(japanese[i]+"の英単語は？ ")
    if a==english[i]:
        print("正解です")
        right = right + 1
    else:
        print("違います")
        print("正しくは"+english[i])
print("終了です")
print("正解数", right)
print("間違い", n-right)
