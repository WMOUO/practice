while True:
    try:
        ans = 0
        n = int(input())
        if n == 0:
            print(1)
            continue
        ans += (n-1)*2
        if n >= 3:
            r = 1+(n-3)
            ans+=(1+r)*(n-2)
        print(ans+2)
    except:
        break