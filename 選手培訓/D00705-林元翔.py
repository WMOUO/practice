while True:
    try:
        n = [n for n in input().split(' ') if n]
        a = int(n[0])
        b = int(n[1])
        z = [0]*(a+1)
        for i in range(1,a+1):
            z[i] = (z[i-1]+b)%i
        print(z[a])
    except:
        break