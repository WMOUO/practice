from math import gcd
while True:
    try:
        a = int(input())
        if a == 0:break
        n = [int(_) for _ in input().split(' ') if _]
        while len(n) >= 2:
            a = n.pop()
            b = n.pop()
            n.append(a*b//gcd(a,b))
        print(n[-1])
    except:
        break