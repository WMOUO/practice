while True:
    try:
        n,c = map(int,input().split(' '))
        z = [0]+[1]*n
        r = [1]
        k = 1
        for i in range(2,n+1):
            if z[i] != 0:
                k += 1
                r.append(i)
                for u in range(i+i,n+1,i):
                    z[u] = 0
        if k % 2 == 0:
            if k >= 2*c:
                while k != 2*c:
                    r.pop(0)
                    r.pop(-1)
                    k -= 2
            r = map(str,r)
            print(str(n)+' '+str(c)+": "+' '.join(r))
        else:
            if k >= 2*c-1:
                while k != 2*c-1:
                    r.pop(0)
                    r.pop(-1)
                    k -= 2
            r = map(str,r)
            print(str(n)+' '+str(c)+": "+' '.join(r))
    except:
        break