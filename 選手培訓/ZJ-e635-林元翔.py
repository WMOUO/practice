while True:
    try:
        n = int(input())
        if n == 0:break
        a = n*2
        b = int(a**0.5)
        if b*(b+1) <= a:
            b += 1
        Sn = int(b*(b+1)/2)
        print(f'{Sn-n} {b}')
    except:
        break