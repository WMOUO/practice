while True:
    try:
        n = input()
        if len(n) == 0:break
        n = int(n)
        z = []
        for i in range(n): 
            m = input().split(' ')
            if m[1] != "-":
                z.append(m[0])
                z = sorted(z)
        for i in range(n):
            print(z[i])
    except :
        break