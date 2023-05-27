while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        n = n[1:]
        n.sort()
        u = (n[0]+n[-1])*(n[-1]-n[0]+1)//2
        if sum(n) == (n[0]+n[-1])*(n[-1]-n[0]+1)//2:print(f'{n[0]} {n[-1]} yes')
        else:print(f'{n[0]} {n[-1]} no')
    except:
        break