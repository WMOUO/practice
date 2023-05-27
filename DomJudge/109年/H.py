for ___ in range(int(input())):
    w = int(input())
    z = [0]*(w+1)
    u = [0]*(w+1)
    ans = 0
    h = 0
    for __ in range(w):
        n = [int(_) for _ in input().split(' ') if _]
        z[n[0]] = n[1]
    for i in range(1,len(u)):
        if u[i] == 1:continue
        r = 0
        e = i
        y = [0]*(w+1)
        while y[e] != 1:
            y[e] = 1
            r += 1
            e = z[e]
            # if u[e] != 0:
            #     r += u[e]
            #     break
        # for j in range(len(y)):
        #     if y[j] != 0:u[j] = max(u[j],r)
        if r > h:
            h = r
            ans = i
    print(ans)