while True:
    n = [_ for _ in input().split(' ') if _]
    if len(n) == 1:
        break
    w = len(n[1])//int(n[0])
    z = ''
    r = ''
    a = 0
    for i in n[1]:
        a += 1
        r += i
        if a == w :
            z += r[::-1]
            a = 0
            r = ''
    print(z)