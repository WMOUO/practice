from math import ceil
z = [0,0]+[1]*9999
for i in range(2,10001):
    for u in range(i+i,10001,i):
        z[u] = 0
while True:
    try:
        a,b = map(int,input().split(' '))
        if a == 1:r = [0]+[1]*(b-a)
        else:r = [1]*(b-a+1)
        w = int(b**0.5)+1
        for i in range(2,w):
            if z[i] == 1:
                p = ceil(a/i)
                for u in range(i*p-a,len(r),i):
                    if i == (u+a):continue
                    r[u] = 0
        print(sum(r))
    except:
        break