#原版
z = [1,2,6,24,120,720]
for _ in range(int(input())):
    n = [int(_) for _ in input().split(',') if _]
    n[0] = str(n[0])
    i = len(n[0])
    ans = [0,0]
    while i != 0:
        a = 1
        b = 1
        while True:
            if z[i-2] * a < n[1]:
                a += 1
            if z[i-2] * b < n[2]:
                b += 1
            if z[i-2] * a >= n[1] and z[i-2] * b >= n[2]:
                a -= 1
                b -= 1
                break
        if a == b:
            ans[0] += 1
        else:
            ans[1] += 1
        n[1] = n[1] - (z[i-2]*a)
        n[2] = n[2] - (z[i-2]*b)
        n[0] = n[0][1:]
    print(str(ans[0])+"A"+str(ans[1])+"B")