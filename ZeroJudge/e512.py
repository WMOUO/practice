from decimal import Decimal
while True:
    try:
        n = [Decimal(_) for _ in input().split(' ') if _]
        z = []
        for i in range(0,8,2):
            z.append((n[i],n[i+1]))
        r = set(z)
        a = 0
        b = 0
        for i in r:
            if z.count(i) == 2:
                a -= i[0]
                b -= i[1]
            else:
                a += i[0]
                b += i[1]
        print(a,b)
    except:
        break