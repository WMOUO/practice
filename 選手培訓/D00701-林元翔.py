import time
while True:
    try:
        m = [int(a) for a in input().split(' ') if a]
        if len(m) == 0:
            break
        n = int(input())
        start = time.perf_counter()
        z = [1]*1000001
        for i in range(2,1000001):
            if i in m:
                z[i] = 1
                continue
            lower = 0
            for u in m:
                if u < i:
                    if i % m[-1] == 0:
                        z[i] = i // m[-1]
                        break
                    a = i - u
                    if lower == 0 or lower > z[a]+1:
                        lower = z[a]+1
                else:
                    break
                z[i] = lower
        end = time.perf_counter()
        print(end-start)
        for _ in range(n):
            k = eval(input())
            if z[k] != 0:
                print(z[k])
                continue
    except:
        break
