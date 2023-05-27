#701
import time
while True:
    try:
        m = [int(a) for a in input().split(' ') if a]
        if len(m) == 0:
            break
        n = int(input())
        start = time.perf_counter()
        z = [1]*1000001
        z[0] = 0
        #m = m[::-1]
        for i in range(2,1000001):
            if i not in m:
                lower = 0
                for u in range(len(m)):#Q1
                    if m[u] < i:
                        if i % m[u] == 0 and m[u] != 1 and i // m[u] < lower:
                            lower = i//m[u]
                        else:
                            a = i - m[u]
                        if lower == 0 or z[a]+1 < lower:    
                            lower = z[a]+1
                    else:
                        break
                    z[i] = lower
        end = time.perf_counter()
        print(end-start)
        for _ in range(n):
            k = eval(input())
            print(z[k])
    except:
        break