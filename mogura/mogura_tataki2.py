def mogura(r):
    m = ''
    n = ''
    for i in range(8):
        ana = '.'
        if i == r:
            ana = '○'
        n = '_' + ana + '_'
        m = '[' + str(i) + ']'
        print(n,end="")
        print(m,end="")
    
### 関数実行
mogura(3)
print("")
mogura(6)
            