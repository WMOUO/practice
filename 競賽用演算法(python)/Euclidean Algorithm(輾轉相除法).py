#用於計算最大公因數
while True:
    try:
        a,b = map(int,input().strip().split(' '))
        while True:
            a,b = b,a%b
            if b == 0:
                break
        print(a)
    except:
        break