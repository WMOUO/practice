while True:
    try:
        n = int(input())
        a = 1
        r = int(n)
        while True:
            if a % 2 != 0:
                print(' '.join([str(_) for _ in range(n-r+1,n+1)]))
                n += r
            else:
                print(' '.join([str(_) for _ in range(n,n-r,-1)]))
                n += r
            a += 1
            if a == r+1:break
    except:
        break