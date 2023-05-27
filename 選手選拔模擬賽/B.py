for _ in range(int(input())):
    n = input().replace(' ','')
    while True:
        z = []
        r = ''
        for i in range(len(n)):
            r += n[i]
            if i % 2 != 0:
                z.append(int(r))
                r = ''
        if i % 2 == 0:
            z.append(int(r))
        w = 1
        for i in z:
            if i != 0:
                w *= i
        n = str(w)
        if len(n) == 1:
            break
    print(n)