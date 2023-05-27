import time
while True :
    n = input()
    if len(n) == 0 :break
    n = int(n)
    z = []
    t = n
    for i in range(n+1):
        z.append(i)
    for c in range(4,n+1,2):
        z[c] = 0
        t -= 1
    for i in range(3,n+1,2):
        for p in range(2*i,n+1,i):
            if z[p] != 0:t -= 1 
            z[p] = 0
            
    print(t-1)