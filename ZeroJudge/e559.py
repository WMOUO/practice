for _ in range(int(input())):
    n = [int(_) for _  in input().split(' ') if _]
    r = sum(n)
    if r % 2 != 0:
        print('NO')
    else:
        z = [0]*(r // 2 + 1)
        for i in n:
            for u in range(r//2,i-1,-1):
                z[u] = max(z[u],z[u-i]+i)
        if z[-1] == r//2:print('YES')
        else:print("NO")