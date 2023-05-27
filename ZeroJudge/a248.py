while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        a = str(n[0]*(10**n[2])//n[1])
        if len(a) <= n[2]:
            a = '0.'+'0'*(n[2]-len(a))+a
            print(a)
        elif len(a) == n[1]:print('0.'+a)
        else:print(a[:n[2]*(-1)]+'.'+a[n[2]*(-1):])
    except:
        break