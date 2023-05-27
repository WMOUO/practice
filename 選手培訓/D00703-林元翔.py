k = int(input())
for _ in range(k):
    n = input()#x
    m = input()#y
    z = [[(0,None) for i in range(len(n)+1)] for u in range(len(m)+1)]
    for i in range(1,len(n)+1):
        for u in range(1,len(m)+1):
            if n[i-1] == m[u-1]:
                a = z[u-1][i-1][0]
                z[u][i] = (a+1,"↖")
            elif n[i-1] != m[u-1]:
                if z[u-1][i][0] > z[u][i-1][0] :
                    a = z[u-1][i][0]
                    z[u][i] = (a,"←")
                else:
                    a = z[u][i-1][0]
                    z[u][i] = (a,"↑")
    a = len(n)
    b = len(m)
    print(z[len(m)][len(n)][0])