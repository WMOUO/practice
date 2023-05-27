d = int(input())
for i in range(d):
    n = input().split('/') 
    n[0] = n[0].split('.')
    n[1] = n[1].split('.')
    o = 0
    p = 0
    z = ''
    while p < 4:
        n1 = int(n[0][o])
        n2 = 255-int(n[1][p])
        g =  n1|n2
        z += str(g)
        if p != 3 :z += '.'
        o += 1
        p += 1 
    print(z)