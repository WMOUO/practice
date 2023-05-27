while True:
    z = {}
    u = {}
    a = int(input())
    if a == 0:
        break
    for _ in range(a):
        n = [int(_) for _ in input().split(' ') if _]
        r = n[0]
        if len(n) == 1:
            break
        if z.get(n[0],None) == None:
            z[n[0]] = set(n[1:])
            u[n[0]] = 0
        else:
            z[n[0]] = z[n[0]] | set(n[1:])
        for i in n[1:]:
            if z.get(i,None) == None:
                z[i] = {n[0]}
                u[i] = 0
            else:
                z[i] = z[i] | {n[0]}
    w = [r]
    road = [0]*a
    r = [0]*a
    while True:
        if u[w[-1]] <= z[w[-1]]:
            if z[w[-1]][u[w[-1]]] not in w:
                
#1 2 4 6
#2 1 3 5
#3 2 4
#4 1 3
#5 2 6
#6 5 1
#0
#5
#5 1 2 3 4
#0
#6
#2 1 3
#5 4 6 2
#0
#5
#1 2
#2 3
#3 4
#4 5
#5 1
#0
#5
#1 2
#2 3
#3 4
#4 5
#0
#9
#1 3 6
#2 7 9
#3 5 7 9
#4 7
#5 6 9
#7 8
#0
#0