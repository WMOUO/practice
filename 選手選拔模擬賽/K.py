while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        if n[0] % 2 != 0:
            n[0] += 1
        if n[1] % 2 != 0:
            n[1] -= 1
        ans = 0
        for i in range(n[0],n[1]+1,2):
            ans += i
        print(ans)
    except:
        break