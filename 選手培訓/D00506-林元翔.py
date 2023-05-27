m = int(input())
for i in range(m):
    d = dict()
    b = dict()
    z = []
    x = []
    n = input().split(" ")
    c = n[0][0]
    if n == []:break
    for i in n:
        if i == "":continue 
        i = str(i).split(",")
        if d.get(i[0],'None') != 'None' :
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
        if d.get(i[1],'None') != 'None' :
            d[i[1]].append(i[0])
        else:
            d[i[1]] = [i[0]]    #建立字典的建及值
    b[c] = 0
    z.append(c)
    x.append(c)
    while len(z) != 0: #"仿"DFS  5
        if len(d[c])-1 < b[c]:
            b[c] = len(d[c])-1
        a = d[c][b[c]]
        b[c] += 1
        if a not in x:
            c = a
            b[c] = 0
            z.append(c)
            x.append(str(c))
        if b[c] == len(d[c]):
            z = z[:-1]
            if len(z) == 0:
                break
            c = z[-1]
    print(' '.join(x))