while True:
    try:
        n = input()
        if len(n) == 0:break
        n = int(n)
        z={}
        for i in range(n): 
            m = input().split(' ')
            z[m[0]] = m[1]
        for i in range(2):
            m = input()
            y = 0
            x = False
            while x != True:
                y += 1
                if z[str(m)] == '-':
                    x = True
                else:
                    m = z[str(m)]
            print(y)
    except :
        break