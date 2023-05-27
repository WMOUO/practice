while True:
    try:
        n = int(input())
        r = n
        i = 2
        ans = 0
        while i <= n:
            if n % i == 0:
                n //= i
                ans += i
            else:
                i += 1
        print(ans)
    except:
        break
