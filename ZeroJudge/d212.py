while True:
    try:
        a = 1
        b = 1
        n = int(input())
        for _ in range(2,n+1):
            a,b = b,a+b
        print(b)
    except:
        break