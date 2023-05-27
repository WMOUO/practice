for _ in range(int(input())):
    a,b = map(int,input().split(' '))
    n = sorted([int(_) for _ in input().split(' ')])
    z = [0]*(b+1)
    for i in range(1,b+1):
        for u in n:
            if u > i:
                break
            z[i] = z[i-u]+1
    print(z[-1])