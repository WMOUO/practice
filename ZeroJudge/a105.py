a = [int(_) for _ in input().split(" ") if _]
z = [[0]*(a[0]+1) for _ in range(a[1]+1)]
ans = 0
for _ in range(int(input())):
    n = [int(_) for _ in input().split(" ") if _]
    if n[0] == n[2]:
        for i in range(min(n[1],n[3]),max(n[1],n[3])+1):
            z[i][n[0]] = 1
    elif n[1] == n[3]:
        for i in range(min(n[0],n[2]),max(n[0],n[2])+1):
            z[n[1]][i] = 1
    else:
        if n[0] > n[2]:t = 'l'#左
        else:t = 'r'#右
        if n[1] > n[3]:y = 'u'#上
        else:y = 'o'#下
        b = 0
        if t == 'l' and y == "o":#左上 x- y+
            while True:
                z[n[1]+b][n[0]-b] = 1
                if n[0]-b == n[2] and n[1]+b == n[3]:break
                b += 1
        elif t == 'l' and y == "u":#左下 x- y-
            while True:
                z[n[1]-b][n[0]-b] = 1
                if n[0]-b == n[2] and n[1]-b == n[3]:break
                b += 1
        elif t == 'r' and y == "o":#右上 x+ y+
            while True:
                z[n[1]+b][n[0]+b] = 1
                if n[0]+b == n[2] and n[1]+b == n[3]:break
                b += 1
        elif t == 'r' and y == "u":#右下 x+ y-
            while True:
                z[n[1]-b][n[0]+b] = 1
                if n[0]+b == n[2] and n[1]-b == n[3]:break
                b += 1
for i in z:
    ans += sum(i)
print(ans)