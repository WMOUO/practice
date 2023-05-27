while True:
    try:
        n = int(input())
        a,b = 0,1
        h = 1
        if n == 0:
            print(0)
            continue
        while h < n :
            a,b = b,a+b
            h += 1
        print(b)
    except:
        break