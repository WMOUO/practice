z = [1,1,2,6,24,120]
for _ in range(int(input())):
    x = ''
    y = ''
    n = [int(_) for _ in input().split(',')]
    for i in range(1,3):
        a = str(n[0])
        a = ' '.join(a)
        a = a.split(' ')
        for u in range(len(a)-1,-1,-1):
            p = 1
            while True:
                if z[u] * p >= n[i]:
                    break
                p += 1
            n[i] -= z[u]*(p-1)
            if i == 1:
                x += a.pop(p-1)
            else:
                y += a.pop(p-1)
    a = 0
    b = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            a += 1
        else:
            b += 1
    print(str(a)+"A"+str(b)+"B")