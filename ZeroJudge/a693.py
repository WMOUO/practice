while True:
    try:
        a,b = map(int,input().split(' '))
        n = [int(_) for _ in input().split(' ')]
        z = [0]*(len(n)+1)
        for i in range(0,len(n)):
            z[i+1] = z[i]+n[i]
        for _ in range(b):
            j,k = map(int,input().split(' '))
            print(z[k]-z[j-1])
    except:
        break