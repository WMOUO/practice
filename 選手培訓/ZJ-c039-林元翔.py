d = {1:1}
while True:
    try:
        n = [int(n) for n in input().split(' ') if n]
        if len(n) == 0 :break
        if n[0] == n[1] == 1:
            print("1 1 1")
            continue
        ans = []
        for r in range(max(n),min(n)-1,-1):
            i = r
            z = [i]
            
            while i != 1:
                if  i % 2 == 0:
                    i = i//2
                    z.append(i)
                else:
                    i = i*3+1
                    z.append(i)
                if d.get(i,"None") != "None":
                    w = len(z)-1
                    for u in z[:-1]:
                        d[u]  = d[i] + w
                        w -= 1
                    ans.append(d[r])
                    break
        print(f'{n[0]} {n[1]} {max(ans)}')
    except:
        break