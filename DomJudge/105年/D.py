for _ in range(int(input())):
    n = [int(_) for _ in input().split(',') if _]
    for i in range(max(n)+1,0,-1):
        t = 1
        for u in n:
            if u % i == 0:
                if t == 0:
                    t = 2
                    break
                t = 0
        if t == 2:break
    if t == 2:print(i)