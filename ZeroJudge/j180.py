while True:
    n = [int(_) for _ in input().split(' ') if _]
    if len(n) == 1:
        break
    ans = 0
    n[0] = n[0]*n[1]
    while True:
        if n[0] == 0 or n[1] == 0:
            break
        if n[0] % n[1] != 0:
            n[0] -= (n[0]//n[1])+1
        else:
            n[0] -= (n[0]//n[1])
        ans += 1
    print(ans)