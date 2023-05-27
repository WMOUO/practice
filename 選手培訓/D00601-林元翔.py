while True:
    try:
        n = input().split(" ")
        if len(n) == 0:break
        n = n[::-1]
        u = int(input())
        for i in range(u):
            c = int(input())
            m = 0
            for t in n :
                r = int(t)
                if c // r != 0:
                    z = c // r
                    c = c % r
                    m += z
            print(m)
    except:
        break