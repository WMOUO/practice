#法一 (柱列)
import time
while True :
    L = input()
    a = time.perf_counter()
    if len(L) == 0 :break
    L = int(L)
    z = []
    f = -1
    for i in range(1,L+1):
        i = str(i)
        z.append(i)
    while len(z) != 1:
        if len(z) == 2:
            z = z[1:]
        else:    
            for i in range(6) :
                z.append(z[i])
            z=z[7:]
    print(z[0])
    b = time.perf_counter()
    print(b-a)
    
#法二 (動態)
import time
while True:
    try:
        n = int(input())
        a = time.perf_counter()
        high = 2
        z = [0,0]
        if high > n :
            print(z[n])
            b = time.time_counter()
            print(b-a)
            continue
        else:
            for i in range(high,n+1):
                z.append((z[i-1]+7)%i)
            print(z[n])
            b = time.perf_counter()
            print(b-a)
            continue
    except:
        break