for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    a = n[1]-n[0]
    b = n[2]-n[1]
    c = n[3]-n[2]
    if b == a:
        n.append(n[-1]+c)
    else:
        n.append(n[-1]*(c//b))
    n = map(str,n)
    print(' '.join(n))