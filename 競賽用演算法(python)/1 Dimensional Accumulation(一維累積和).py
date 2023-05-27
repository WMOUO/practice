#曾經APCS第三題的類題
a = int(input())
z = [0]*a
while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        for i in range(n[0],n[1]):
            z[i] += 1
    except:
        print(' '.join(list(map(str,z))))
        break