a = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    z = {}
    n = input().lower()
    for i in n:
        if i in a:
            if z.get(i,None) == None:
                z[i] = 1
            else:
                z[i] += 1
    b = list(z.values())
    b = max(b)
    ans = []
    for i in z.keys():
        if z[i] == b:
            ans.append(i)
    print(''.join(sorted(ans)))