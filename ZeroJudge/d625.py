a = int(input())
z = [['-']*a for _ in range(a)]
for i in range(a):
    n = input()
    r = []
    for u in range(len(n)):
        if n[u] == '*':
            z[i][u] = '*'
            if i >= 1 and u >= 1:#左上
                r.append([i-1,u-1])
            if i >= 1:#上
                r.append([i-1,u])
            if u >= 1:#左
                r.append([i,u-1])
            if i < (a-1) and u >= 1 :#左下
                r.append([i+1,u-1])
            if i >= 1 and u < (a-1):#右上
                r.append([i-1,u+1])
            if i < (a-1):#下
                r.append([i+1,u])
            if u < (a-1):#右
                r.append([i,u+1])
            if i < (a-1) and u < (a-1):#右下
                r.append([i+1,u+1])
    for i in r:
        if z[i[0]][i[1]] == '-':
            z[i[0]][i[1]] = 1
        elif z[i[0]][i[1]] == '*':
            continue
        else:
            z[i[0]][i[1]] += 1
for i in z:
    i = map(str,i)
    print(''.join(i))